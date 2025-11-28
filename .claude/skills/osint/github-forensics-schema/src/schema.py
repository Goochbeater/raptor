"""
GitHub Forensics Verifiable Evidence Schema

Two evidence types:

1. Event - Something that happened (from GH Archive, git)
   when, who, what

2. Observation - Something we observed (from GitHub, Wayback, security vendors)
   Original: when, who, what (if known)
   Observer: when observed, who observed, what they found
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Literal

from pydantic import BaseModel, Field, HttpUrl


# =============================================================================
# ENUMS
# =============================================================================


class EvidenceSource(str, Enum):
    """Where evidence was obtained."""

    GHARCHIVE = "gharchive"
    GIT = "git"
    GITHUB = "github"
    WAYBACK = "wayback"
    SECURITY_VENDOR = "security_vendor"


class EventType(str, Enum):
    """GitHub event types from GH Archive."""

    PUSH = "PushEvent"
    PULL_REQUEST = "PullRequestEvent"
    ISSUES = "IssuesEvent"
    ISSUE_COMMENT = "IssueCommentEvent"
    CREATE = "CreateEvent"
    DELETE = "DeleteEvent"
    FORK = "ForkEvent"
    WATCH = "WatchEvent"
    RELEASE = "ReleaseEvent"
    MEMBER = "MemberEvent"
    PUBLIC = "PublicEvent"
    WORKFLOW_RUN = "WorkflowRunEvent"


class RefType(str, Enum):
    BRANCH = "branch"
    TAG = "tag"
    REPOSITORY = "repository"


class PRAction(str, Enum):
    OPENED = "opened"
    CLOSED = "closed"
    REOPENED = "reopened"
    MERGED = "merged"


class IssueAction(str, Enum):
    OPENED = "opened"
    CLOSED = "closed"
    REOPENED = "reopened"
    DELETED = "deleted"


class WorkflowConclusion(str, Enum):
    SUCCESS = "success"
    FAILURE = "failure"
    CANCELLED = "cancelled"


class IOCType(str, Enum):
    """Indicator types."""

    COMMIT_SHA = "commit_sha"
    FILE_PATH = "file_path"
    FILE_HASH = "file_hash"
    CODE_SNIPPET = "code_snippet"
    EMAIL = "email"
    USERNAME = "username"
    REPOSITORY = "repository"
    TAG_NAME = "tag_name"
    BRANCH_NAME = "branch_name"
    WORKFLOW_NAME = "workflow_name"
    IP_ADDRESS = "ip_address"
    DOMAIN = "domain"
    URL = "url"
    API_KEY = "api_key"
    SECRET = "secret"


# =============================================================================
# COMMON MODELS
# =============================================================================


class GitHubActor(BaseModel):
    """GitHub user/actor."""

    login: str
    id: int | None = None
    is_bot: bool = False


class GitHubRepository(BaseModel):
    """GitHub repository."""

    owner: str
    name: str
    full_name: str
    id: int | None = None


class VerificationInfo(BaseModel):
    """How to verify this evidence."""

    source: EvidenceSource
    url: HttpUrl | None = None
    bigquery_table: str | None = None
    query: str | None = None


# =============================================================================
# EVENT - Something that happened
#
# when, who, what
# Sources: GH Archive, git
# =============================================================================


class Event(BaseModel):
    """Something that happened."""

    evidence_id: str
    when: datetime
    who: GitHubActor
    what: str
    repository: GitHubRepository
    verification: VerificationInfo


class CommitInPush(BaseModel):
    """Commit embedded in PushEvent."""

    sha: str
    message: str
    author_name: str
    author_email: str


class PushEvent(Event):
    """Someone pushed commits."""

    event_type: Literal["push"] = "push"
    ref: str
    before_sha: str
    after_sha: str
    size: int
    commits: list[CommitInPush] = Field(default_factory=list)
    is_force_push: bool = False


class PullRequestEvent(Event):
    """PR action."""

    event_type: Literal["pull_request"] = "pull_request"
    action: PRAction
    pr_number: int
    pr_title: str
    pr_body: str | None = None
    head_sha: str | None = None
    merged: bool = False


class IssueEvent(Event):
    """Issue action."""

    event_type: Literal["issue"] = "issue"
    action: IssueAction
    issue_number: int
    issue_title: str
    issue_body: str | None = None


class IssueCommentEvent(Event):
    """Comment on issue/PR."""

    event_type: Literal["issue_comment"] = "issue_comment"
    action: Literal["created", "edited", "deleted"]
    issue_number: int
    comment_id: int
    comment_body: str


class CreateEvent(Event):
    """Branch/tag/repo created."""

    event_type: Literal["create"] = "create"
    ref_type: RefType
    ref_name: str


class DeleteEvent(Event):
    """Branch/tag deleted."""

    event_type: Literal["delete"] = "delete"
    ref_type: RefType
    ref_name: str


class ForkEvent(Event):
    """Repository forked."""

    event_type: Literal["fork"] = "fork"
    fork_full_name: str


class WorkflowRunEvent(Event):
    """GitHub Actions. Absence during commit = API attack."""

    event_type: Literal["workflow_run"] = "workflow_run"
    action: Literal["requested", "completed", "in_progress"]
    workflow_name: str
    head_sha: str
    conclusion: WorkflowConclusion | None = None


class ReleaseEvent(Event):
    """Release published."""

    event_type: Literal["release"] = "release"
    action: Literal["published", "created", "deleted"]
    tag_name: str
    release_name: str | None = None
    release_body: str | None = None


class WatchEvent(Event):
    """Repo starred."""

    event_type: Literal["watch"] = "watch"


class MemberEvent(Event):
    """Collaborator changed."""

    event_type: Literal["member"] = "member"
    action: Literal["added", "removed"]
    member: GitHubActor


class PublicEvent(Event):
    """Repo made public."""

    event_type: Literal["public"] = "public"


AnyEvent = (
    PushEvent
    | PullRequestEvent
    | IssueEvent
    | IssueCommentEvent
    | CreateEvent
    | DeleteEvent
    | ForkEvent
    | WorkflowRunEvent
    | ReleaseEvent
    | WatchEvent
    | MemberEvent
    | PublicEvent
)


# =============================================================================
# OBSERVATION - Something we observed
#
# Two perspectives:
# - Original event (if known): when, who, what
# - Observer: when observed, by whom, what found
#
# Sources: GitHub, Wayback, security vendors
# =============================================================================


class Observation(BaseModel):
    """Something we observed."""

    evidence_id: str

    # Original event (if known)
    original_when: datetime | None = None
    original_who: GitHubActor | None = None
    original_what: str | None = None

    # Observer
    observed_when: datetime
    observed_by: EvidenceSource
    observed_what: str

    # Context
    repository: GitHubRepository | None = None
    verification: VerificationInfo

    # State
    is_deleted: bool = False  # No longer exists at source


# -----------------------------------------------------------------------------
# Atomic observations
# -----------------------------------------------------------------------------


class CommitAuthor(BaseModel):
    name: str
    email: str
    date: datetime


class FileChange(BaseModel):
    filename: str
    status: Literal["added", "modified", "removed", "renamed"]
    additions: int = 0
    deletions: int = 0
    patch: str | None = None


class CommitObservation(Observation):
    """Commit."""

    observation_type: Literal["commit"] = "commit"
    sha: Annotated[str, Field(min_length=40, max_length=40)]
    message: str
    author: CommitAuthor
    committer: CommitAuthor
    parents: list[str] = Field(default_factory=list)
    files: list[FileChange] = Field(default_factory=list)
    is_dangling: bool = False  # Not on any branch


class IssueObservation(Observation):
    """Issue or PR."""

    observation_type: Literal["issue"] = "issue"
    issue_number: int
    is_pull_request: bool = False
    title: str | None = None
    body: str | None = None
    state: Literal["open", "closed", "merged"] | None = None


class FileObservation(Observation):
    """File content."""

    observation_type: Literal["file"] = "file"
    file_path: str
    branch: str | None = None
    content: str
    content_hash: str | None = None  # SHA256


class WikiObservation(Observation):
    """Wiki page."""

    observation_type: Literal["wiki"] = "wiki"
    page_name: str
    content: str


class ForkObservation(Observation):
    """Fork relationship."""

    observation_type: Literal["fork"] = "fork"
    fork_full_name: str
    parent_full_name: str


class BranchObservation(Observation):
    """Branch."""

    observation_type: Literal["branch"] = "branch"
    branch_name: str
    head_sha: str | None = None


class TagObservation(Observation):
    """Tag."""

    observation_type: Literal["tag"] = "tag"
    tag_name: str
    target_sha: str | None = None


class ReleaseObservation(Observation):
    """Release."""

    observation_type: Literal["release"] = "release"
    tag_name: str
    release_name: str | None = None
    release_body: str | None = None


class WaybackSnapshot(BaseModel):
    """Single Wayback capture."""

    timestamp: str
    captured_at: datetime
    archive_url: HttpUrl
    original_url: HttpUrl
    status_code: int = 200


class SnapshotObservation(Observation):
    """Wayback snapshots for a URL."""

    observation_type: Literal["snapshot"] = "snapshot"
    original_url: HttpUrl
    snapshots: list[WaybackSnapshot]
    total_snapshots: int


# -----------------------------------------------------------------------------
# IOC - Indicator of Compromise
# -----------------------------------------------------------------------------


class IOC(Observation):
    """Indicator of Compromise."""

    observation_type: Literal["ioc"] = "ioc"
    ioc_type: IOCType
    value: str
    confidence: Literal["confirmed", "high", "medium", "low"] = "medium"
    first_seen: datetime | None = None
    last_seen: datetime | None = None
    extracted_from: str | None = None  # Evidence ID


AnyObservation = (
    CommitObservation
    | IssueObservation
    | FileObservation
    | WikiObservation
    | ForkObservation
    | BranchObservation
    | TagObservation
    | ReleaseObservation
    | SnapshotObservation
    | IOC
)


# =============================================================================
# TYPE ALIASES
# =============================================================================


AnyEvidence = AnyEvent | AnyObservation

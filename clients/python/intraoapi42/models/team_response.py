from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scale_team_response import ScaleTeamResponse
    from ..models.team_user_response import TeamUserResponse


T = TypeVar("T", bound="TeamResponse")


@_attrs_define
class TeamResponse:
    """
    Example:
        {'id': 1000001, 'name': 'example-team', 'url': 'https://api.example.com/v2/teams/1000001', 'final_mark': 80,
            'project_id': 2000001, 'created_at': '2024-01-10T10:00:00.000Z', 'updated_at': '2024-01-10T12:00:00.000Z',
            'status': 'finished', 'terminating_at': '2024-01-11T12:00:00.000Z', 'users': [{'id': 1000002, 'login': 'example-
            user', 'url': 'https://api.example.com/v2/users/example-user', 'leader': True, 'occurrence': 0, 'validated':
            True, 'projects_user_id': 3000001}], 'locked?': True, 'validated?': True, 'closed?': True, 'repo_url':
            'git@example.com:example/project.git', 'repo_uuid': 'example-repository-uuid', 'locked_at':
            '2024-01-10T10:00:00.000Z', 'closed_at': '2024-01-11T12:00:00.000Z', 'project_session_id': 4000001,
            'project_gitlab_path': 'example/project', 'scale_teams': [{'id': 5000001, 'scale_id': 6000001, 'comment':
            'Example evaluation comment.', 'created_at': '2024-01-10T10:05:00.000Z', 'updated_at':
            '2024-01-10T11:00:00.000Z', 'feedback': 'Example feedback.', 'final_mark': 75, 'flag': {'id': 1, 'name':
            'Approved', 'positive': True, 'icon': 'check', 'created_at': '2024-01-01T00:00:00.000Z', 'updated_at':
            '2024-01-01T00:00:00.000Z'}, 'begin_at': '2024-01-10T10:30:00.000Z', 'correcteds': [{'id': 1000002, 'login':
            'example-user', 'url': 'https://api.example.com/v2/users/example-user'}], 'corrector': {'id': 1000003, 'login':
            'evaluator', 'url': 'https://api.example.com/v2/users/evaluator'}, 'truant': {}, 'filled_at':
            '2024-01-10T11:00:00.000Z', 'questions_with_answers': []}, {'id': 5000002, 'scale_id': 6000001, 'comment':
            'Another example evaluation comment.', 'created_at': '2024-01-10T10:05:00.000Z', 'updated_at':
            '2024-01-10T11:05:00.000Z', 'feedback': 'Another example feedback.', 'final_mark': 85, 'flag': {'id': 1, 'name':
            'Approved', 'positive': True, 'icon': 'check', 'created_at': '2024-01-01T00:00:00.000Z', 'updated_at':
            '2024-01-01T00:00:00.000Z'}, 'begin_at': '2024-01-10T11:00:00.000Z', 'correcteds': [{'id': 1000002, 'login':
            'example-user', 'url': 'https://api.example.com/v2/users/example-user'}], 'corrector': {'id': 1000004, 'login':
            'second-evaluator', 'url': 'https://api.example.com/v2/users/second-evaluator'}, 'truant': {}, 'filled_at':
            '2024-01-10T11:05:00.000Z', 'questions_with_answers': []}]}

    Attributes:
        id (int):
        name (str):
        url (str):
        project_id (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        status (str):
        terminating_at (datetime.datetime | None):
        users (list[TeamUserResponse]):
        locked (bool):
        validated (bool):
        closed (bool):
        repo_url (None | str):
        repo_uuid (str):
        locked_at (datetime.datetime | None):
        closed_at (datetime.datetime | None):
        project_session_id (int):
        project_gitlab_path (None | str):
        scale_teams (list[ScaleTeamResponse]):
        final_mark (int | None | Unset):
    """

    id: int
    name: str
    url: str
    project_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    status: str
    terminating_at: datetime.datetime | None
    users: list[TeamUserResponse]
    locked: bool
    validated: bool
    closed: bool
    repo_url: None | str
    repo_uuid: str
    locked_at: datetime.datetime | None
    closed_at: datetime.datetime | None
    project_session_id: int
    project_gitlab_path: None | str
    scale_teams: list[ScaleTeamResponse]
    final_mark: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        url = self.url

        project_id = self.project_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        status = self.status

        terminating_at: None | str
        if isinstance(self.terminating_at, datetime.datetime):
            terminating_at = self.terminating_at.isoformat()
        else:
            terminating_at = self.terminating_at

        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()
            users.append(users_item)

        locked = self.locked

        validated = self.validated

        closed = self.closed

        repo_url: None | str
        repo_url = self.repo_url

        repo_uuid = self.repo_uuid

        locked_at: None | str
        if isinstance(self.locked_at, datetime.datetime):
            locked_at = self.locked_at.isoformat()
        else:
            locked_at = self.locked_at

        closed_at: None | str
        if isinstance(self.closed_at, datetime.datetime):
            closed_at = self.closed_at.isoformat()
        else:
            closed_at = self.closed_at

        project_session_id = self.project_session_id

        project_gitlab_path: None | str
        project_gitlab_path = self.project_gitlab_path

        scale_teams = []
        for scale_teams_item_data in self.scale_teams:
            scale_teams_item = scale_teams_item_data.to_dict()
            scale_teams.append(scale_teams_item)

        final_mark: int | None | Unset
        if isinstance(self.final_mark, Unset):
            final_mark = UNSET
        else:
            final_mark = self.final_mark

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "url": url,
                "project_id": project_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "status": status,
                "terminating_at": terminating_at,
                "users": users,
                "locked?": locked,
                "validated?": validated,
                "closed?": closed,
                "repo_url": repo_url,
                "repo_uuid": repo_uuid,
                "locked_at": locked_at,
                "closed_at": closed_at,
                "project_session_id": project_session_id,
                "project_gitlab_path": project_gitlab_path,
                "scale_teams": scale_teams,
            }
        )
        if final_mark is not UNSET:
            field_dict["final_mark"] = final_mark

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scale_team_response import ScaleTeamResponse
        from ..models.team_user_response import TeamUserResponse

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        url = d.pop("url")

        project_id = d.pop("project_id")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        status = d.pop("status")

        def _parse_terminating_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                terminating_at_type_0 = datetime.datetime.fromisoformat(data)

                return terminating_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        terminating_at = _parse_terminating_at(d.pop("terminating_at"))

        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = TeamUserResponse.from_dict(users_item_data)

            users.append(users_item)

        locked = d.pop("locked?")

        validated = d.pop("validated?")

        closed = d.pop("closed?")

        def _parse_repo_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        repo_url = _parse_repo_url(d.pop("repo_url"))

        repo_uuid = d.pop("repo_uuid")

        def _parse_locked_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                locked_at_type_0 = datetime.datetime.fromisoformat(data)

                return locked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        locked_at = _parse_locked_at(d.pop("locked_at"))

        def _parse_closed_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closed_at_type_0 = datetime.datetime.fromisoformat(data)

                return closed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        closed_at = _parse_closed_at(d.pop("closed_at"))

        project_session_id = d.pop("project_session_id")

        def _parse_project_gitlab_path(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        project_gitlab_path = _parse_project_gitlab_path(d.pop("project_gitlab_path"))

        scale_teams = []
        _scale_teams = d.pop("scale_teams")
        for scale_teams_item_data in _scale_teams:
            scale_teams_item = ScaleTeamResponse.from_dict(scale_teams_item_data)

            scale_teams.append(scale_teams_item)

        def _parse_final_mark(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        final_mark = _parse_final_mark(d.pop("final_mark", UNSET))

        team_response = cls(
            id=id,
            name=name,
            url=url,
            project_id=project_id,
            created_at=created_at,
            updated_at=updated_at,
            status=status,
            terminating_at=terminating_at,
            users=users,
            locked=locked,
            validated=validated,
            closed=closed,
            repo_url=repo_url,
            repo_uuid=repo_uuid,
            locked_at=locked_at,
            closed_at=closed_at,
            project_session_id=project_session_id,
            project_gitlab_path=project_gitlab_path,
            scale_teams=scale_teams,
            final_mark=final_mark,
        )

        team_response.additional_properties = d
        return team_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

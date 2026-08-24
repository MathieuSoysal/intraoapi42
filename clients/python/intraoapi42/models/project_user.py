from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.light_project import LightProject
    from ..models.light_team import LightTeam
    from ..models.light_user import LightUser


T = TypeVar("T", bound="ProjectUser")


@_attrs_define
class ProjectUser:
    """
    Attributes:
        id (int):
        occurrence (int):
        status (str):
        validated (bool | None):
        current_team_id (int):
        project (LightProject):
        cursus_ids (list[int]):
        user (LightUser):
        teams (list[LightTeam]):
        final_mark (int | None | Unset):
        marked_at (datetime.datetime | None | Unset):
        marked (bool | None | Unset):
        retriable_at (datetime.datetime | None | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    id: int
    occurrence: int
    status: str
    validated: bool | None
    current_team_id: int
    project: LightProject
    cursus_ids: list[int]
    user: LightUser
    teams: list[LightTeam]
    final_mark: int | None | Unset = UNSET
    marked_at: datetime.datetime | None | Unset = UNSET
    marked: bool | None | Unset = UNSET
    retriable_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        occurrence = self.occurrence

        status = self.status

        validated: bool | None
        validated = self.validated

        current_team_id = self.current_team_id

        project = self.project.to_dict()

        cursus_ids = self.cursus_ids

        user = self.user.to_dict()

        teams = []
        for teams_item_data in self.teams:
            teams_item = teams_item_data.to_dict()
            teams.append(teams_item)

        final_mark: int | None | Unset
        if isinstance(self.final_mark, Unset):
            final_mark = UNSET
        else:
            final_mark = self.final_mark

        marked_at: None | str | Unset
        if isinstance(self.marked_at, Unset):
            marked_at = UNSET
        elif isinstance(self.marked_at, datetime.datetime):
            marked_at = self.marked_at.isoformat()
        else:
            marked_at = self.marked_at

        marked: bool | None | Unset
        if isinstance(self.marked, Unset):
            marked = UNSET
        else:
            marked = self.marked

        retriable_at: None | str | Unset
        if isinstance(self.retriable_at, Unset):
            retriable_at = UNSET
        elif isinstance(self.retriable_at, datetime.datetime):
            retriable_at = self.retriable_at.isoformat()
        else:
            retriable_at = self.retriable_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "occurrence": occurrence,
                "status": status,
                "validated?": validated,
                "current_team_id": current_team_id,
                "project": project,
                "cursus_ids": cursus_ids,
                "user": user,
                "teams": teams,
            }
        )
        if final_mark is not UNSET:
            field_dict["final_mark"] = final_mark
        if marked_at is not UNSET:
            field_dict["marked_at"] = marked_at
        if marked is not UNSET:
            field_dict["marked"] = marked
        if retriable_at is not UNSET:
            field_dict["retriable_at"] = retriable_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.light_project import LightProject
        from ..models.light_team import LightTeam
        from ..models.light_user import LightUser

        d = dict(src_dict)
        id = d.pop("id")

        occurrence = d.pop("occurrence")

        status = d.pop("status")

        def _parse_validated(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        validated = _parse_validated(d.pop("validated?"))

        current_team_id = d.pop("current_team_id")

        project = LightProject.from_dict(d.pop("project"))

        cursus_ids = cast(list[int], d.pop("cursus_ids"))

        user = LightUser.from_dict(d.pop("user"))

        teams = []
        _teams = d.pop("teams")
        for teams_item_data in _teams:
            teams_item = LightTeam.from_dict(teams_item_data)

            teams.append(teams_item)

        def _parse_final_mark(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        final_mark = _parse_final_mark(d.pop("final_mark", UNSET))

        def _parse_marked_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                marked_at_type_0 = datetime.datetime.fromisoformat(data)

                return marked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        marked_at = _parse_marked_at(d.pop("marked_at", UNSET))

        def _parse_marked(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        marked = _parse_marked(d.pop("marked", UNSET))

        def _parse_retriable_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                retriable_at_type_0 = datetime.datetime.fromisoformat(data)

                return retriable_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        retriable_at = _parse_retriable_at(d.pop("retriable_at", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        project_user = cls(
            id=id,
            occurrence=occurrence,
            status=status,
            validated=validated,
            current_team_id=current_team_id,
            project=project,
            cursus_ids=cursus_ids,
            user=user,
            teams=teams,
            final_mark=final_mark,
            marked_at=marked_at,
            marked=marked,
            retriable_at=retriable_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        project_user.additional_properties = d
        return project_user

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

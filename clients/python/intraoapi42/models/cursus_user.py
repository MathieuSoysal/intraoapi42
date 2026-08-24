from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cursus import Cursus
    from ..models.skill import Skill


T = TypeVar("T", bound="CursusUser")


@_attrs_define
class CursusUser:
    """
    Attributes:
        id (int):
        begin_at (datetime.datetime):
        grade (str):
        level (float):
        skills (list[Skill]):
        cursus_id (int):
        cursus (Cursus):
        has_coalition (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        end_at (datetime.datetime | Unset):
        blackholed_at (datetime.datetime | None | Unset):
    """

    id: int
    begin_at: datetime.datetime
    grade: str
    level: float
    skills: list[Skill]
    cursus_id: int
    cursus: Cursus
    has_coalition: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    end_at: datetime.datetime | Unset = UNSET
    blackholed_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        begin_at = self.begin_at.isoformat()

        grade = self.grade

        level = self.level

        skills = []
        for skills_item_data in self.skills:
            skills_item = skills_item_data.to_dict()
            skills.append(skills_item)

        cursus_id = self.cursus_id

        cursus = self.cursus.to_dict()

        has_coalition = self.has_coalition

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        end_at: str | Unset = UNSET
        if not isinstance(self.end_at, Unset):
            end_at = self.end_at.isoformat()

        blackholed_at: None | str | Unset
        if isinstance(self.blackholed_at, Unset):
            blackholed_at = UNSET
        elif isinstance(self.blackholed_at, datetime.datetime):
            blackholed_at = self.blackholed_at.isoformat()
        else:
            blackholed_at = self.blackholed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "begin_at": begin_at,
                "grade": grade,
                "level": level,
                "skills": skills,
                "cursus_id": cursus_id,
                "cursus": cursus,
                "has_coalition": has_coalition,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if end_at is not UNSET:
            field_dict["end_at"] = end_at
        if blackholed_at is not UNSET:
            field_dict["blackholed_at"] = blackholed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cursus import Cursus
        from ..models.skill import Skill

        d = dict(src_dict)
        id = d.pop("id")

        begin_at = datetime.datetime.fromisoformat(d.pop("begin_at"))

        grade = d.pop("grade")

        level = d.pop("level")

        skills = []
        _skills = d.pop("skills")
        for skills_item_data in _skills:
            skills_item = Skill.from_dict(skills_item_data)

            skills.append(skills_item)

        cursus_id = d.pop("cursus_id")

        cursus = Cursus.from_dict(d.pop("cursus"))

        has_coalition = d.pop("has_coalition")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _end_at = d.pop("end_at", UNSET)
        end_at: datetime.datetime | Unset
        if isinstance(_end_at, Unset):
            end_at = UNSET
        else:
            end_at = datetime.datetime.fromisoformat(_end_at)

        def _parse_blackholed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                blackholed_at_type_0 = datetime.datetime.fromisoformat(data)

                return blackholed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        blackholed_at = _parse_blackholed_at(d.pop("blackholed_at", UNSET))

        cursus_user = cls(
            id=id,
            begin_at=begin_at,
            grade=grade,
            level=level,
            skills=skills,
            cursus_id=cursus_id,
            cursus=cursus,
            has_coalition=has_coalition,
            created_at=created_at,
            updated_at=updated_at,
            end_at=end_at,
            blackholed_at=blackholed_at,
        )

        cursus_user.additional_properties = d
        return cursus_user

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

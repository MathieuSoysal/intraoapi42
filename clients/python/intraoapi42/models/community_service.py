from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.light_close import LightClose


T = TypeVar("T", bound="CommunityService")


@_attrs_define
class CommunityService:
    """
    Attributes:
        id (int):
        duration (int):
        schedule_at (datetime.datetime):
        occupation (str):
        state (str):
        created_at (datetime.datetime):
        updated_at (str):
        close (LightClose | Unset):
    """

    id: int
    duration: int
    schedule_at: datetime.datetime
    occupation: str
    state: str
    created_at: datetime.datetime
    updated_at: str
    close: LightClose | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        duration = self.duration

        schedule_at = self.schedule_at.isoformat()

        occupation = self.occupation

        state = self.state

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at

        close: dict[str, Any] | Unset = UNSET
        if not isinstance(self.close, Unset):
            close = self.close.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "duration": duration,
                "schedule_at": schedule_at,
                "occupation": occupation,
                "state": state,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if close is not UNSET:
            field_dict["close"] = close

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.light_close import LightClose

        d = dict(src_dict)
        id = d.pop("id")

        duration = d.pop("duration")

        schedule_at = datetime.datetime.fromisoformat(d.pop("schedule_at"))

        occupation = d.pop("occupation")

        state = d.pop("state")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = d.pop("updated_at")

        _close = d.pop("close", UNSET)
        close: LightClose | Unset
        if isinstance(_close, Unset):
            close = UNSET
        else:
            close = LightClose.from_dict(_close)

        community_service = cls(
            id=id,
            duration=duration,
            schedule_at=schedule_at,
            occupation=occupation,
            state=state,
            created_at=created_at,
            updated_at=updated_at,
            close=close,
        )

        community_service.additional_properties = d
        return community_service

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

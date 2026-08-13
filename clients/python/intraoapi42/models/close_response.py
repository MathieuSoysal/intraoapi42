from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.close_response_kind import CloseResponseKind, check_close_response_kind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.community_service_response import CommunityServiceResponse
    from ..models.light_user_response import LightUserResponse


T = TypeVar("T", bound="CloseResponse")


@_attrs_define
class CloseResponse:
    """
    Attributes:
        id (int):
        reason (str):
        state (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        community_services (list[CommunityServiceResponse]):
        kind (CloseResponseKind):
        user (LightUserResponse):
        closer (LightUserResponse):
        end_at (datetime.datetime | None | Unset):
    """

    id: int
    reason: str
    state: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    community_services: list[CommunityServiceResponse]
    kind: CloseResponseKind
    user: LightUserResponse
    closer: LightUserResponse
    end_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        reason = self.reason

        state = self.state

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        community_services = []
        for community_services_item_data in self.community_services:
            community_services_item = community_services_item_data.to_dict()
            community_services.append(community_services_item)

        kind: str = self.kind

        user = self.user.to_dict()

        closer = self.closer.to_dict()

        end_at: None | str | Unset
        if isinstance(self.end_at, Unset):
            end_at = UNSET
        elif isinstance(self.end_at, datetime.datetime):
            end_at = self.end_at.isoformat()
        else:
            end_at = self.end_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "reason": reason,
                "state": state,
                "created_at": created_at,
                "updated_at": updated_at,
                "community_services": community_services,
                "kind": kind,
                "user": user,
                "closer": closer,
            }
        )
        if end_at is not UNSET:
            field_dict["end_at"] = end_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.community_service_response import CommunityServiceResponse
        from ..models.light_user_response import LightUserResponse

        d = dict(src_dict)
        id = d.pop("id")

        reason = d.pop("reason")

        state = d.pop("state")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        community_services = []
        _community_services = d.pop("community_services")
        for community_services_item_data in _community_services:
            community_services_item = CommunityServiceResponse.from_dict(community_services_item_data)

            community_services.append(community_services_item)

        kind = check_close_response_kind(d.pop("kind"))

        user = LightUserResponse.from_dict(d.pop("user"))

        closer = LightUserResponse.from_dict(d.pop("closer"))

        def _parse_end_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_at_type_0 = datetime.datetime.fromisoformat(data)

                return end_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_at = _parse_end_at(d.pop("end_at", UNSET))

        close_response = cls(
            id=id,
            reason=reason,
            state=state,
            created_at=created_at,
            updated_at=updated_at,
            community_services=community_services,
            kind=kind,
            user=user,
            closer=closer,
            end_at=end_at,
        )

        close_response.additional_properties = d
        return close_response

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

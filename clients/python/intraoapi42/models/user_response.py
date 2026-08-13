from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.light_user_response_kind import LightUserResponseKind, check_light_user_response_kind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.achievement_response import AchievementResponse
    from ..models.campus_response import CampusResponse
    from ..models.campus_user_response import CampusUserResponse
    from ..models.cursus_user_response import CursusUserResponse
    from ..models.group_response import GroupResponse
    from ..models.language_user_response import LanguageUserResponse
    from ..models.patronage_response import PatronageResponse
    from ..models.project_user_response import ProjectUserResponse
    from ..models.role_response import RoleResponse
    from ..models.title_response import TitleResponse
    from ..models.title_user_response import TitleUserResponse
    from ..models.user_image_response import UserImageResponse


T = TypeVar("T", bound="UserResponse")


@_attrs_define
class UserResponse:
    """
    Attributes:
        id (int): The unique identifier of the user.
        login (str): The login name of the user.
        first_name (str): The first name of the user.
        usual_full_name (str): The usual full name of the user, usually usual_first_name or first_name + last_name.
        last_name (str): The last name of the user.
        email (str): The email address of the user.
        url (str): The URL to the user's resource.
        displayname (str): The display name of the user.
        kind (LightUserResponseKind): The kind of user (e.g., student, admin, external).
        image (UserImageResponse):
        staff (bool): Indicates if the user is staff.
        correction_point (int): The user's correction points.
        pool_month (str): The month of the user's pool.
        pool_year (str): The year of the user's pool.
        wallet (int): The user's wallet balance.
        anonymize_date (datetime.datetime | None): The date when user data will be anonymized.
        data_erasure_date (datetime.datetime): The date when user data will be erased.
        created_at (datetime.datetime): The user creation timestamp.
        updated_at (datetime.datetime): The last user update timestamp.
        alumnized_at (datetime.datetime): The date when the user became an alumnus.
        alumni (bool): Indicates if the user is an alumnus.
        active (bool): Indicates if the user is active.
        groups (list[GroupResponse]):
        cursus_users (list[CursusUserResponse]):
        projects_users (list[ProjectUserResponse]):
        languages_users (list[LanguageUserResponse]):
        achievements (list[AchievementResponse]):
        titles (list[TitleResponse]):
        titles_users (list[TitleUserResponse]):
        patroned (list[PatronageResponse]):
        patroning (list[PatronageResponse]):
        roles (list[RoleResponse]):
        campus (list[CampusResponse]):
        campus_users (list[CampusUserResponse]):
        usual_first_name (None | str | Unset): The usual first name of the user, first_name if none.
        phone (str | Unset): The phone number of the user (always hidden).
        location (None | str | Unset): The location of the user.
    """

    id: int
    login: str
    first_name: str
    usual_full_name: str
    last_name: str
    email: str
    url: str
    displayname: str
    kind: LightUserResponseKind
    image: UserImageResponse
    staff: bool
    correction_point: int
    pool_month: str
    pool_year: str
    wallet: int
    anonymize_date: datetime.datetime | None
    data_erasure_date: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime
    alumnized_at: datetime.datetime
    alumni: bool
    active: bool
    groups: list[GroupResponse]
    cursus_users: list[CursusUserResponse]
    projects_users: list[ProjectUserResponse]
    languages_users: list[LanguageUserResponse]
    achievements: list[AchievementResponse]
    titles: list[TitleResponse]
    titles_users: list[TitleUserResponse]
    patroned: list[PatronageResponse]
    patroning: list[PatronageResponse]
    roles: list[RoleResponse]
    campus: list[CampusResponse]
    campus_users: list[CampusUserResponse]
    usual_first_name: None | str | Unset = UNSET
    phone: str | Unset = UNSET
    location: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        login = self.login

        first_name = self.first_name

        usual_full_name = self.usual_full_name

        last_name = self.last_name

        email = self.email

        url = self.url

        displayname = self.displayname

        kind: str = self.kind

        image = self.image.to_dict()

        staff = self.staff

        correction_point = self.correction_point

        pool_month = self.pool_month

        pool_year = self.pool_year

        wallet = self.wallet

        anonymize_date: None | str
        if isinstance(self.anonymize_date, datetime.datetime):
            anonymize_date = self.anonymize_date.isoformat()
        else:
            anonymize_date = self.anonymize_date

        data_erasure_date = self.data_erasure_date.isoformat()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        alumnized_at = self.alumnized_at.isoformat()

        alumni = self.alumni

        active = self.active

        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.to_dict()
            groups.append(groups_item)

        cursus_users = []
        for cursus_users_item_data in self.cursus_users:
            cursus_users_item = cursus_users_item_data.to_dict()
            cursus_users.append(cursus_users_item)

        projects_users = []
        for projects_users_item_data in self.projects_users:
            projects_users_item = projects_users_item_data.to_dict()
            projects_users.append(projects_users_item)

        languages_users = []
        for languages_users_item_data in self.languages_users:
            languages_users_item = languages_users_item_data.to_dict()
            languages_users.append(languages_users_item)

        achievements = []
        for achievements_item_data in self.achievements:
            achievements_item = achievements_item_data.to_dict()
            achievements.append(achievements_item)

        titles = []
        for titles_item_data in self.titles:
            titles_item = titles_item_data.to_dict()
            titles.append(titles_item)

        titles_users = []
        for titles_users_item_data in self.titles_users:
            titles_users_item = titles_users_item_data.to_dict()
            titles_users.append(titles_users_item)

        patroned = []
        for patroned_item_data in self.patroned:
            patroned_item = patroned_item_data.to_dict()
            patroned.append(patroned_item)

        patroning = []
        for patroning_item_data in self.patroning:
            patroning_item = patroning_item_data.to_dict()
            patroning.append(patroning_item)

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.to_dict()
            roles.append(roles_item)

        campus = []
        for campus_item_data in self.campus:
            campus_item = campus_item_data.to_dict()
            campus.append(campus_item)

        campus_users = []
        for campus_users_item_data in self.campus_users:
            campus_users_item = campus_users_item_data.to_dict()
            campus_users.append(campus_users_item)

        usual_first_name: None | str | Unset
        if isinstance(self.usual_first_name, Unset):
            usual_first_name = UNSET
        else:
            usual_first_name = self.usual_first_name

        phone = self.phone

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "login": login,
                "first_name": first_name,
                "usual_full_name": usual_full_name,
                "last_name": last_name,
                "email": email,
                "url": url,
                "displayname": displayname,
                "kind": kind,
                "image": image,
                "staff?": staff,
                "correction_point": correction_point,
                "pool_month": pool_month,
                "pool_year": pool_year,
                "wallet": wallet,
                "anonymize_date": anonymize_date,
                "data_erasure_date": data_erasure_date,
                "created_at": created_at,
                "updated_at": updated_at,
                "alumnized_at": alumnized_at,
                "alumni?": alumni,
                "active?": active,
                "groups": groups,
                "cursus_users": cursus_users,
                "projects_users": projects_users,
                "languages_users": languages_users,
                "achievements": achievements,
                "titles": titles,
                "titles_users": titles_users,
                "patroned": patroned,
                "patroning": patroning,
                "roles": roles,
                "campus": campus,
                "campus_users": campus_users,
            }
        )
        if usual_first_name is not UNSET:
            field_dict["usual_first_name"] = usual_first_name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.achievement_response import AchievementResponse
        from ..models.campus_response import CampusResponse
        from ..models.campus_user_response import CampusUserResponse
        from ..models.cursus_user_response import CursusUserResponse
        from ..models.group_response import GroupResponse
        from ..models.language_user_response import LanguageUserResponse
        from ..models.patronage_response import PatronageResponse
        from ..models.project_user_response import ProjectUserResponse
        from ..models.role_response import RoleResponse
        from ..models.title_response import TitleResponse
        from ..models.title_user_response import TitleUserResponse
        from ..models.user_image_response import UserImageResponse

        d = dict(src_dict)
        id = d.pop("id")

        login = d.pop("login")

        first_name = d.pop("first_name")

        usual_full_name = d.pop("usual_full_name")

        last_name = d.pop("last_name")

        email = d.pop("email")

        url = d.pop("url")

        displayname = d.pop("displayname")

        kind = check_light_user_response_kind(d.pop("kind"))

        image = UserImageResponse.from_dict(d.pop("image"))

        staff = d.pop("staff?")

        correction_point = d.pop("correction_point")

        pool_month = d.pop("pool_month")

        pool_year = d.pop("pool_year")

        wallet = d.pop("wallet")

        def _parse_anonymize_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                anonymize_date_type_0 = datetime.datetime.fromisoformat(data)

                return anonymize_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        anonymize_date = _parse_anonymize_date(d.pop("anonymize_date"))

        data_erasure_date = datetime.datetime.fromisoformat(d.pop("data_erasure_date"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        alumnized_at = datetime.datetime.fromisoformat(d.pop("alumnized_at"))

        alumni = d.pop("alumni?")

        active = d.pop("active?")

        groups = []
        _groups = d.pop("groups")
        for groups_item_data in _groups:
            groups_item = GroupResponse.from_dict(groups_item_data)

            groups.append(groups_item)

        cursus_users = []
        _cursus_users = d.pop("cursus_users")
        for cursus_users_item_data in _cursus_users:
            cursus_users_item = CursusUserResponse.from_dict(cursus_users_item_data)

            cursus_users.append(cursus_users_item)

        projects_users = []
        _projects_users = d.pop("projects_users")
        for projects_users_item_data in _projects_users:
            projects_users_item = ProjectUserResponse.from_dict(projects_users_item_data)

            projects_users.append(projects_users_item)

        languages_users = []
        _languages_users = d.pop("languages_users")
        for languages_users_item_data in _languages_users:
            languages_users_item = LanguageUserResponse.from_dict(languages_users_item_data)

            languages_users.append(languages_users_item)

        achievements = []
        _achievements = d.pop("achievements")
        for achievements_item_data in _achievements:
            achievements_item = AchievementResponse.from_dict(achievements_item_data)

            achievements.append(achievements_item)

        titles = []
        _titles = d.pop("titles")
        for titles_item_data in _titles:
            titles_item = TitleResponse.from_dict(titles_item_data)

            titles.append(titles_item)

        titles_users = []
        _titles_users = d.pop("titles_users")
        for titles_users_item_data in _titles_users:
            titles_users_item = TitleUserResponse.from_dict(titles_users_item_data)

            titles_users.append(titles_users_item)

        patroned = []
        _patroned = d.pop("patroned")
        for patroned_item_data in _patroned:
            patroned_item = PatronageResponse.from_dict(patroned_item_data)

            patroned.append(patroned_item)

        patroning = []
        _patroning = d.pop("patroning")
        for patroning_item_data in _patroning:
            patroning_item = PatronageResponse.from_dict(patroning_item_data)

            patroning.append(patroning_item)

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = RoleResponse.from_dict(roles_item_data)

            roles.append(roles_item)

        campus = []
        _campus = d.pop("campus")
        for campus_item_data in _campus:
            campus_item = CampusResponse.from_dict(campus_item_data)

            campus.append(campus_item)

        campus_users = []
        _campus_users = d.pop("campus_users")
        for campus_users_item_data in _campus_users:
            campus_users_item = CampusUserResponse.from_dict(campus_users_item_data)

            campus_users.append(campus_users_item)

        def _parse_usual_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        usual_first_name = _parse_usual_first_name(d.pop("usual_first_name", UNSET))

        phone = d.pop("phone", UNSET)

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        user_response = cls(
            id=id,
            login=login,
            first_name=first_name,
            usual_full_name=usual_full_name,
            last_name=last_name,
            email=email,
            url=url,
            displayname=displayname,
            kind=kind,
            image=image,
            staff=staff,
            correction_point=correction_point,
            pool_month=pool_month,
            pool_year=pool_year,
            wallet=wallet,
            anonymize_date=anonymize_date,
            data_erasure_date=data_erasure_date,
            created_at=created_at,
            updated_at=updated_at,
            alumnized_at=alumnized_at,
            alumni=alumni,
            active=active,
            groups=groups,
            cursus_users=cursus_users,
            projects_users=projects_users,
            languages_users=languages_users,
            achievements=achievements,
            titles=titles,
            titles_users=titles_users,
            patroned=patroned,
            patroning=patroning,
            roles=roles,
            campus=campus,
            campus_users=campus_users,
            usual_first_name=usual_first_name,
            phone=phone,
            location=location,
        )

        user_response.additional_properties = d
        return user_response

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

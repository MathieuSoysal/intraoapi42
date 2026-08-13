from typing import Literal

LightUserResponseKind = Literal["admin", "external", "student"]

LIGHT_USER_RESPONSE_KIND_VALUES: set[LightUserResponseKind] = {
    "admin",
    "external",
    "student",
}


def check_light_user_response_kind(value: str) -> LightUserResponseKind:
    if value in LIGHT_USER_RESPONSE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIGHT_USER_RESPONSE_KIND_VALUES!r}")

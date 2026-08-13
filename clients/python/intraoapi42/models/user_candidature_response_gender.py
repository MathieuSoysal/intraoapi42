from typing import Literal

UserCandidatureResponseGender = Literal["female", "male", "other"]

USER_CANDIDATURE_RESPONSE_GENDER_VALUES: set[UserCandidatureResponseGender] = {
    "female",
    "male",
    "other",
}


def check_user_candidature_response_gender(value: str) -> UserCandidatureResponseGender:
    if value in USER_CANDIDATURE_RESPONSE_GENDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_CANDIDATURE_RESPONSE_GENDER_VALUES!r}")

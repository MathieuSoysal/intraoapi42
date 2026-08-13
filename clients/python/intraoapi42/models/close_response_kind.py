from typing import Literal

CloseResponseKind = Literal[
    "agu", "black_hole", "deserter", "non_admitted", "other", "pace_unknown", "serious_misconduct", "social_security"
]

CLOSE_RESPONSE_KIND_VALUES: set[CloseResponseKind] = {
    "agu",
    "black_hole",
    "deserter",
    "non_admitted",
    "other",
    "pace_unknown",
    "serious_misconduct",
    "social_security",
}


def check_close_response_kind(value: str) -> CloseResponseKind:
    if value in CLOSE_RESPONSE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CLOSE_RESPONSE_KIND_VALUES!r}")

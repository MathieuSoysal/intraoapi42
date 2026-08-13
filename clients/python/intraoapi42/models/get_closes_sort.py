from typing import Literal

GetClosesSort = Literal[
    "closer_id", "created_at", "end_at", "id", "jid", "kind", "reason", "state", "updated_at", "user_id"
]

GET_CLOSES_SORT_VALUES: set[GetClosesSort] = {
    "closer_id",
    "created_at",
    "end_at",
    "id",
    "jid",
    "kind",
    "reason",
    "state",
    "updated_at",
    "user_id",
}


def check_get_closes_sort(value: str) -> GetClosesSort:
    if value in GET_CLOSES_SORT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_CLOSES_SORT_VALUES!r}")

from typing import Literal

GetClosesByUserIdSort = Literal[
    "closer_id", "created_at", "end_at", "id", "jid", "kind", "reason", "state", "updated_at", "user_id"
]

GET_CLOSES_BY_USER_ID_SORT_VALUES: set[GetClosesByUserIdSort] = {
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


def check_get_closes_by_user_id_sort(value: str) -> GetClosesByUserIdSort:
    if value in GET_CLOSES_BY_USER_ID_SORT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_CLOSES_BY_USER_ID_SORT_VALUES!r}")

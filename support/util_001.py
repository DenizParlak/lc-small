"""Support helpers for util_001."""


def helper_1_a(value):
    return str(value).upper()


def helper_1_b(items):
    return [item for item in items if item]


def helper_1_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}

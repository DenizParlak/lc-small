"""Support helpers for util_000."""


def helper_0_a(value):
    return str(value).upper()


def helper_0_b(items):
    return [item for item in items if item]


def helper_0_c(mapping):
    return {key: value for key, value in mapping.items() if value is not None}

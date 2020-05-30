from uuid import UUID

from jsonschema import draft4_format_checker


# register custom parameter validators
# you will use it probably for validating more complex objects
# there where you can, use pattern or other properties describing items in OpenAPI spec
# such as, min max values, min max items, between etc
@draft4_format_checker.checks('uuid')
def uuid_validator(uuid_str):
    """
    Custom validator for strings declared in openapi spec as uuid format strings.
    :param uuid_str: uuid param in request
    :return: True if valid uuid, False otherwise
    """
    try:
        UUID(uuid_str)
        return True
    except (TypeError, ValueError):
        return False

import pytest

from json_operations import get_nested, set_nested, update_field_name


@pytest.fixture
def nested_json():
    return {
        "user": {
            "profile": {
                "name": "John Doe",
                "email": "john@example.com",
                "preferences": {"notifications": True, "theme": "dark"},
            }
        }
    }


def test_get_nested(nested_json):
    # Test getting a value from nested JSON
    email = get_nested(nested_json, "user.profile.email")
    assert email == "john@example.com"


def test_set_nested(nested_json):
    # Test setting a value in nested JSON
    set_nested(nested_json, "user.profile.preferences.theme", "light")
    assert nested_json["user"]["profile"]["preferences"]["theme"] == "light"


def test_update_field_name(nested_json):
    # Test renaming a field in nested JSON
    update_field_name(nested_json, "user.profile.preferences.notifications", "alerts")
    assert "alerts" in nested_json["user"]["profile"]["preferences"]
    assert nested_json["user"]["profile"]["preferences"]["alerts"] == True
    assert "notifications" not in nested_json["user"]["profile"]["preferences"]

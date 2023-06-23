import pytest
from src.app.app import App


def test_main_instance_application_correctly():
    assert App() is not None


def test_main_catch_an_exception():
    with pytest.raises(Exception):
        raise Exception("An exception was raised for test")


if __name__ == "__main__":
    pytest.main([__file__])

import pytest


@pytest.fixture()
def set_up():
    print("\nSTART TEST")
    yield
    print("\nFINISH TEST")

import pytest
from Factory import Factory
from InitWindow import InitWindow
from Storage import Storage


@pytest.fixture(scope="module")
def app():
    app = Factory.create(InitWindow)
    yield app


@pytest.fixture(scope="module")
def storage():
    storage = Storage()
    yield storage


def test_storage_get_version(storage):
    result = storage.get_version()
    type(result) == str


def test_storage_get_help(storage):
    result = storage.get_help()
    type(result) == str
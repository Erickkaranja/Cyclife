import pytest

from api.v1.app import create_app


@pytest.fixture()
def app():
    yield create_app()


@pytest.fixture()
def client(app):
    return app.test_client()


# @pytest.fixture()
# def runner(app):
#     return app.test_cli_runner()

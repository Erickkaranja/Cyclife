import uuid

import cmd2_ext_test
import pytest
from cmd2 import CommandResult

import console

user1_id = None
bicycle1_id = None


class CyclifeTester(cmd2_ext_test.ExternalTestMixin, console.CyclifeCommand):
    def __init__(self, *args, **kwargs):
        # gotta have this or neither the plugin or cmd2 will initialize
        super().__init__(*args, **kwargs)


@pytest.fixture
def cyclife_app():
    app = CyclifeTester(console.CyclifeCommand())
    app.fixture_setup()
    yield app
    app.fixture_teardown()


def test_help(cyclife_app):
    # execute a command
    out = cyclife_app.app_cmd("help")

    # validate the command output and result data
    assert isinstance(out, CommandResult)
    assert "create" in str(out.stdout).strip()
    assert "show" in str(out.stdout).strip()
    assert "update" in str(out.stdout).strip()
    assert "delete" in str(out.stdout).strip()


def is_uuid(string):
    try:
        uuid_obj = uuid.UUID(string, version=4)
        return str(uuid_obj) == string
    except ValueError:
        return False


def test_create_user(cyclife_app):
    global user1_id
    out = cyclife_app.app_cmd(
        "create user -f testname -l testlname -e testemail -p testpassword"
    )
    user1_id = str(out.stdout).strip()
    assert is_uuid(user1_id) is True


def test_show_users(cyclife_app):
    global user1_id
    out = cyclife_app.app_cmd("show users")
    assert "testname" in str(out.stdout).strip()
    assert "testemail" in str(out.stdout).strip()
    assert user1_id in str(out.stdout).strip()


def test_show_user(cyclife_app):
    global user1_id
    out = cyclife_app.app_cmd(f"show user -u {user1_id} ")
    assert "testname" in str(out.stdout).strip()
    assert "testemail" in str(out.stdout).strip()


def test_create_bicycle(cyclife_app):
    global bicycle1_id
    out = cyclife_app.app_cmd(
        "create bicycle -m model1 -b brand1 -d description1 -p 200 -i image_url"
    )
    bicycle1_id = str(out.stdout).strip()
    assert is_uuid(bicycle1_id) is True


def test_show_bicycle(cyclife_app):
    global bicycle1_id
    out = cyclife_app.app_cmd("show bicycles")
    assert bicycle1_id in str(out.stdout).strip()
    assert "model1" in str(out.stdout).strip()
    assert "brand1" in str(out.stdout).strip()
    assert "description1" in str(out.stdout).strip()


def test_create_cart(cyclife_app):
    global user1_id
    global bicycle1_id

    out = cyclife_app.app_cmd(
        f"create cart -u {user1_id} -b {bicycle1_id} -q 10"
    )
    cart1_id = str(out.stdout).strip()
    assert is_uuid(cart1_id) is True


def test_create_order(cyclife_app):
    global user1_id
    global bicycle1_id

    out = cyclife_app.app_cmd(
        f"create order -s Pending -p 400 -u {user1_id} -b {bicycle1_id}"
    )
    order1_id = str(out.stdout).strip()
    assert is_uuid(order1_id) is True


def test_create_review(cyclife_app):
    global user1_id
    global bicycle1_id

    out = cyclife_app.app_cmd(
        f"create review -r 4 -t 'Good bicycle' -u {user1_id} -b {bicycle1_id}"
    )
    review1_id = str(out.stdout).strip()
    assert is_uuid(review1_id) is True


def test_update_user(cyclife_app):
    global user1_id
    cyclife_app.app_cmd(
        f"update user -u {user1_id} -f updatefname -e updateemail"
    )
    out = cyclife_app.app_cmd(f"show user -u {user1_id}")
    assert "updatefname" in str(out.stdout).strip()
    assert "updateemail" in str(out.stdout).strip()
    assert "testname" not in str(out.stdout).strip()
    assert "testemail" not in str(out.stdout).strip()


def test_update_bicycle(cyclife_app):
    global bicycle1_id
    out = cyclife_app.app_cmd(
        f"update bicycle -i {bicycle1_id} -m updatedmodel -p 400"
    )

    assert bicycle1_id in str(out.stdout).strip()
    out = cyclife_app.app_cmd("show bicycles")
    assert "updatedmodel" in str(out.stdout).strip()
    assert "400" in str(out.stdout).strip()


def test_delete_user(cyclife_app):
    global user1_id
    cyclife_app.app_cmd(f"delete  user -u {user1_id}")
    out = cyclife_app.app_cmd(f"show user -u {user1_id}")
    assert user1_id not in str(out.stdout).strip()


def test_delete_bicycle(cyclife_app):
    global bicycle1_id
    cyclife_app.app_cmd(f"delete  bicycle -b {bicycle1_id}")
    out = cyclife_app.app_cmd(f"show bicycle -b {bicycle1_id}")
    assert bicycle1_id not in str(out.stdout).strip()

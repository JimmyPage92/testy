from typing import Dict
import pytest

def __fake_config(param: str):
    fake_config: Dict[str, str] = {
        "DB_URL": "db_fake_url",
        "DB_USERNAME": "fake_user_name",
        "DB_PASSWORD": "fake_password",
        "OK_MSG": "fake_ok_msg",
        "NOK_MSG": "fake_not_ok_msg",
    }

    return fake_config[param]


def test_connect_to_database(mocker):
    mocker.patch("decouple.config", side_effect=__fake_config)

    from functionality.zadania import DbHandler
    db_handler: DbHandler = DbHandler()

    results: str = db_handler.connect_to_database()
    assert results == f"I am connecting to db_fake_url as fake_user_name with pass: fake_password..."

def test_show_msg_when_connected(mocker):
    mocker.patch("decouple.config", side_effect=__fake_config)

    from functionality.zadania import DbHandler
    db_handler: DbHandler = DbHandler()

    results: str = db_handler.show_msg_when_connected()
    assert results == "fake_ok_msg"

def test_show_msg_when_interrputed(mocker):
    mocker.patch("decouple.config", side_effect=__fake_config)

    from functionality.zadania import DbHandler
    db_handler: DbHandler = DbHandler()

    result: str = db_handler.show_msg_when_interrputed()
    assert result == "fake_not_ok_msg"




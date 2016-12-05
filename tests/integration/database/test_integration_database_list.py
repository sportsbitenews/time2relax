# -*- coding: utf-8 -*-

FIXTURE = ['database', 'list']


def test_list(server, db_name):
    """Should list the correct databases."""

    json = server.list().json()

    assert db_name in json
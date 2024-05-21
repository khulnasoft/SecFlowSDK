#!/usr/bin/env -S python3 -OO
# coding:utf8

from secflow.apis.dashboard import SecflowApi
import pytest
import os


api = SecflowApi(
    url=os.environ['URL'],
    auth_token=os.environ['TOKEN']
)


@pytest.mark.run('first')
def test_first():
    api.get_orgs()
    # Create test teams
    pytest.organisation1 = api.create_org('test-team-1', 'test-team-1', True)
    pytest.organisation2 = api.create_org('test-team-2', 'test-team-2', True)


def test_delete():
    api.delete_org(pytest.organisation1["id"])
    api.delete_org(pytest.organisation2["id"])

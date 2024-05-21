#!/usr/bin/env -S python3 -OO
# coding:utf8

from secflow.apis.dashboard import SecflowApi
import json
import pytest
import os


api = SecflowApi(
    url=os.environ['URL'],
    auth_token=os.environ['TOKEN']
)


@pytest.mark.run('first')
def test_first():
    """Get orgs."""
    orgs = json.loads(api.get_orgs())
    assert len(orgs['results']) >= 0


def test_org_details():
    """Get org details."""
    orgs = json.loads(api.get_orgs())
    org_id = orgs['results'][0]['id']
    assert str(org_id).isnumeric()
    org = json.loads(api.get_org(org_id))
    assert org['name'] != ""
    org_users = json.loads(api.get_org_users(org_id))
    assert len(org_users['results']) >= 0
    org_not_users = json.loads(api.get_org_not_users(org_id))
    assert len(org_not_users['results']) >= 0

# org_settings = json.loads(api.get_org_settings(org_id))
# print(org_settings)
# print(api.get_org_setting(org_id, org_settings['results'][0]['id']))


# reset
# print(api.get_org_settings_reset(org_id))

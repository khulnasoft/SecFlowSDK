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

    # Retests
    # List all feeds
    print(api.get_feeds())
    # print(api.get_team_by_id(1))
    #
    # rand_name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    # new_team = api.add_team(name=rand_name, is_active=False)
    # print(new_team)
    # print(api.delete_team(new_team['id']))

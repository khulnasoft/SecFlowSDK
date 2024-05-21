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
    # Users
    # List all users
    users = json.loads(api.get_users())
    print(users)

    # Get user details
    user_id = users['results'][0]['id']
    print(api.get_user(user_id))
    print(api.get_user_totp(user_id))

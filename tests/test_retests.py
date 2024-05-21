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

    # Vulns
    # List all vulns
    retests = json.loads(api.get_retests())

    # Get retest details

    if len(retests) > 0 and len(retests['results']) > 0:
        retest_id = retests['results'][0]['id']
        print(api.get_retest(retest_id))

    # Sync retests
    print(api.sync_retests())

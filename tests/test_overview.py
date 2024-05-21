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
    # Stats
    print(api.get_overview_stats(1))

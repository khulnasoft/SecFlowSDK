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
    print(api.get_vulns())

    new_vuln = api.create_vuln(
        # arsenal_id=0,
        asset_id=1,
        severity=1,  # Low
        cvss_vector="AV:A/AC:H/PR:L/UI:R/S:C/C:H/I:H/A:H",
        title="title test",
        description="description test",
        solution_headline="solution_headline test",
        solution="solution test",
        solution_priority="urgent",
        solution_effort="medium",
        is_quickwin=True,
        comments=""
    )
    print(new_vuln)

    # Get vuln
    vuln = api.get_vuln(
        vuln_id=json.loads(new_vuln)['id']
    )
    print(vuln)

    # Delete the vuln
    deleted_vuln = api.delete_vuln(
        vuln_id=json.loads(new_vuln)['id']
    )
    print(deleted_vuln)

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
    # Assets
    # List all assets
    print(api.get_assets())
    print(api.get_assets(1))

    # Sync all assets
    r = json.loads(api.sync_assets(2))
    print(r['status'])
    assert r['status'] == "enqueued"

    # Create an asset
    new_asset = api.create_asset(
        value="coucou.com",
        criticality=1,  # Low
        type="domain",
        is_active=True,
        description="description test",
        exposure="external",
        is_monitored=True
    )
    print(new_asset)

    # Get asset
    asset = api.get_asset(
        asset_id=json.loads(new_asset)['id']
    )
    print(asset)

    # Update the asset
    updated_asset = api.update_asset(
        asset_id=json.loads(new_asset)['id'],
        kwargs={'exposure': 'internal'}
    )
    print(updated_asset)

    # Delete the asset
    deleted_asset = api.delete_asset(
        asset_id=json.loads(updated_asset)['id']
    )
    print(deleted_asset)

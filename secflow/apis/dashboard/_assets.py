#!/usr/bin/env -S python3 -OO
# coding:utf8

import requests
from secflow.exceptions import SecflowException
from . import constants


def get_assets(self, org_id: int = None, page: int = 1, limit: int = 10):
    """
    Get all assets.

    :param org_id: Organization ID
    :type org_id: int|str
    :param page: Page number of results (Opt.)
    :type page: int
    :param limit: Max results per page. Default is 10, Max is 100 (Opt.)
    :type limit: int
    :rtype: json
    """
    url_params = f'?format=json&page={str(page)}&limit={str(limit)}'
    if org_id is not None and str(org_id).isnumeric():
        url_params += f'&org={str(org_id)}'

    try:
        r = self.rs.get(f"{self.url}/api/auth/assets/{url_params}")
        return r.text
    except requests.exceptions.RequestException as e:
        raise SecflowException("Unable to list assets: {}".format(e))


def get_asset(self, asset_id: int):
    """
    Get asset details.

    :param asset_id: Asset ID
    :type asset_id: int
    :return: Asset details
    :rtype: json
    """
    try:
        r = self.rs.get(self.url+f"/api/auth/assets/{str(asset_id)}/?format=json")
        return r.text
    except requests.exceptions.RequestException as e:
        raise SecflowException("Unable to retrieve asset: {}".format(e))


def sync_assets(self, org_id: int = None):
    """
    Sync all assets from Arsenal.

    ** Administration Only **

    :param org_id: Organization ID
    :type org_id: int
    :rtype: json
    """
    url_params = f"{self.url}/api/auth/assets/sync?format=json"
    if org_id is not None and str(org_id).isnumeric():
        url_params += f'&org={str(org_id)}'

    try:
        r = self.rs.get(url_params)
        return r.text
    except requests.exceptions.RequestException as e:
        raise SecflowException("Unable to sync retests: {}".format(e))


def create_asset(
        self, value: str, criticality: int = 0, type: str = "", is_active: bool = False,
        description: str = "", exposure: str = "external", is_monitored: bool = False):
    """
    Create a new asset.

    :param value: Asset value
    :type value: str
    :param criticality: Criticality
    :type criticality: int
    :param type: Type
    :type type: str
    :param is_active: Is active ?
    :type is_active: bool
    :param description: Description
    :type description: str
    :param exposure: Exposure
    :type exposure: str
    :param is_monitored: Is monitored ?
    :type is_monitored: bool
    :rtype: json
    """
    if criticality not in constants.ASSET_CRITICALITIES:
        raise SecflowException("Bad 'criticality' parameter")
    if type not in constants.ASSET_TYPES:
        raise SecflowException("Bad 'type' parameter")
    if exposure not in constants.ASSET_EXPOSURES:
        raise SecflowException("Bad 'exposure' parameter")
    data = {
        'value': value,
        'criticality': criticality,
        'type': type,
        'is_active': is_active,
        'description': description,
        'exposure': exposure,
        'is_monitored': is_monitored
    }
    try:
        r = self.rs.post(self.url+"/api/auth/assets/?format=json", json=data)
        return r.text
    except requests.exceptions.RequestException as e:
        raise SecflowException("Unable to create asset: {}".format(e))


def update_asset(self, asset_id: int, kwargs):
    """
    Update an asset.

    :param asset_id: Asset ID
    :type asset_id: int
    :param kwargs: Parameters
    :type kwargs: dict
    :rtype: json
    """
    data = {}

    for attrib in kwargs.keys():
        if attrib not in ['value', 'criticality', 'type', 'is_active', 'description', 'exposure', 'is_monitored']:
            raise SecflowException(f"Bad parameter: {attrib}")
        if attrib == 'criticality' and kwargs['criticality'] not in constants.ASSET_CRITICALITIES:
            raise SecflowException("Bad 'criticality' parameter")
        if attrib == 'type' and kwargs['type'] not in constants.ASSET_TYPES:
            raise SecflowException("Bad 'type' parameter")
        if attrib == 'exposure' and kwargs['exposure'] not in constants.ASSET_EXPOSURES:
            raise SecflowException("Bad 'exposure' parameter")

        data.update({
            attrib: kwargs[attrib]
        })

    try:
        r = self.rs.patch(self.url+f"/api/auth/assets/{str(asset_id)}/?format=json", json=data)
        return r.text
    except requests.exceptions.RequestException as e:
        raise SecflowException("Unable to update asset: {}".format(e))


def delete_asset(self, asset_id: int):
    """
    Delete an asset.

    :param asset_id: Asset ID
    :type asset_id: int
    :rtype: json
    """
    try:
        r = self.rs.delete(self.url+f"/api/auth/assets/{str(asset_id)}/?format=json")
        return r.text
    except requests.exceptions.RequestException as e:
        raise SecflowException("Unable to delete an asset: {}".format(e))

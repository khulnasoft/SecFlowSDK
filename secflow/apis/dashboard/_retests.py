#!/usr/bin/env -S python3 -OO
# coding:utf8

import requests
from secflow.exceptions import SecflowException


def get_retests(self, org_id: int = None, page: int = 1, limit: int = 10):
    """
    Get all retests.

    :param org_id: Organization ID
    :param page: Page number of results (Opt.)
    :param limit: Max results per page. Default is 10, Max is 100 (Opt.)
    :rtype: json
    """
    url_params = f'?format=json&page={str(page)}&limit={str(limit)}'
    if org_id is not None and str(org_id).isnumeric():
        url_params += f'&org={str(org_id)}'

    try:
        r = self.rs.get(self.url+"/api/auth/retests/{}".format(url_params))
        return r.text
    except requests.exceptions.RequestException as e:
        raise SecflowException("Unable to list retests: {}".format(e))


def get_retest(self, retest_id: int):
    """
    Get retest details.

    :param retest_id: Retest ID
    :rtype: json
    """
    try:
        r = self.rs.get(self.url+f"/api/auth/retests/{str(retest_id)}/?format=json")
        return r.text
    except requests.exceptions.RequestException as e:
        raise SecflowException("Unable to retrieve retest: {}".format(e))


def cancel_retest(self, retest_id: int):
    """
    Cancel a retest.

    :param retest_id: Retest ID
    :rtype: json
    """
    try:
        r = self.rs.get(
            self.url+f"/api/auth/retests/{str(retest_id)}/cancel?format=json")
        return r.text
    except requests.exceptions.RequestException as e:
        raise SecflowException("Unable to cancel retest: {}".format(e))


def refresh_retest(self, retest_id: int):
    """
    Refresh a retest.

    :param retest_id: Retest ID
    :rtype: json
    """
    try:
        r = self.rs.get(
            self.url+f"/api/auth/retests/{str(retest_id)}/refresh?format=json")
        return r.text
    except requests.exceptions.RequestException as e:
        raise SecflowException("Unable to refresh retest: {}".format(e))


def sync_retests(self):
    """
    Sync all retests from Arsenal.

    ** Administration Only **

    :rtype: json
    """
    try:
        r = self.rs.get(self.url+"/api/auth/retests/sync?format=json")
        return r.text
    except requests.exceptions.RequestException as e:
        raise SecflowException("Unable to sync retests: {}".format(e))

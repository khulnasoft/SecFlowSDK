#!/usr/bin/env -S python3 -OO
# coding:utf8

import requests
from secflow.exceptions import SecflowException


def get_feeds(self, org_id: int = None, page: int = 1, limit: int = 10):
    """
    Get all feeds.

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
        r = self.rs.get(self.url+"/api/auth/feeds/{}".format(url_params))
        return r.text
    except requests.exceptions.RequestException as e:
        raise SecflowException("Unable to list feeds: {}".format(e))

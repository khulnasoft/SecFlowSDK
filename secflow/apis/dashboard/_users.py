#!/usr/bin/env -S python3 -OO
# coding:utf8

import requests
from secflow.exceptions import SecflowException


def get_users(self, page: int = 1, limit: int = 10):
    """
    Get all users.

    :param page: Page number of results (Opt.)
    :param limit: Max results per page. Default is 10, Max is 100 (Opt.)
    :rtype: json
    """
    url_params = f'?format=json&page={str(page)}&limit={str(limit)}'

    try:
        r = self.rs.get(self.url+"/api/auth/users/{}".format(url_params))
        return r.text
    except requests.exceptions.RequestException as e:
        raise SecflowException("Unable to list users: {}".format(e))


def get_user(self, user_id: int):
    """
    Get user details.

    :param user_id: User ID
    :rtype: json
    """
    try:
        r = self.rs.get(self.url+f"/api/auth/users/{str(user_id)}/?format=json")
        return r.text
    except requests.exceptions.RequestException as e:
        raise SecflowException("Unable to retrieve user: {}".format(e))


def get_user_totp(self, user_id: int):
    """
    Get user TOTP.

    :param user_id: User ID
    :rtype: json
    """
    try:
        r = self.rs.get(self.url+f"/api/auth/users/{str(user_id)}/totp?format=json")
        return r.text
    except requests.exceptions.RequestException as e:
        raise SecflowException("Unable to retrieve user TOTP: {}".format(e))

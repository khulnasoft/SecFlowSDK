#!/usr/bin/env -S python3 -OO
# coding:utf8

import requests
from secflow.exceptions import SecflowException
from . import constants


def get_vulns(self, org_id: int = None, page: int = 1, limit: int = 10):
    """
    Get all vulns.

    :param org_id: Organization ID
    :param page: Page number of results (Opt.)
    :param limit: Max results per page. Default is 10, Max is 100 (Opt.)
    :rtype: json
    """
    url_params = f'?format=json&page={str(page)}&limit={str(limit)}'
    if org_id is not None and str(org_id).isnumeric():
        url_params += f'&org={str(org_id)}'

    try:
        r = self.rs.get(self.url+"/api/auth/vulns/{}".format(url_params))
        return r.text
    except requests.exceptions.RequestException as e:
        raise SecflowException("Unable to list vulns: {}".format(e))


def get_vuln(self, vuln_id: int):
    """
    Get vuln details.

    :param vuln_id: Vulnerability ID
    :type vuln_id: int
    :return: Vulnerability details
    :rtype: json
    """
    try:
        r = self.rs.get(self.url+f"/api/auth/vulns/{str(vuln_id)}/?format=json")
        return r.text
    except requests.exceptions.RequestException as e:
        raise SecflowException("Unable to retrieve vuln: {}".format(e))


def create_vuln(
        self, asset_id: int, severity: int = 0, cvss_vector: str = "",
        title: str = "", description: str = "",
        category: str = "", solution_headline: str = "", solution: str = "",
        solution_priority: str = "hardening", solution_effort: str = "low",
        is_quickwin: bool = False, comments: str = ""):
    """
    Create a new vulnerability.

    :param asset_id: Asset ID
    :param severity: Severity
    :param cvss_vector: CVSSv3 vector
    :param title: Title
    :param description: Description
    :param category: Category
    :param solution_headline: Solution Headline
    :param solution: Solution details
    :param solution_priority: Solution priority
    :param solution_effort: Solution effort
    :param is_quickwin: Is quick-win ?
    :param comments: Comments
    :rtype: json
    """
    if severity not in constants.VULNERABILITY_SEVERITY:
        raise SecflowException("Bad 'severity' parameter")
    if solution_priority not in constants.VULNERABILITY_SOLUTION_PRIORITIES:
        raise SecflowException("Bad 'solution_priority' parameter")
    if solution_effort not in constants.VULNERABILITY_SOLUTION_EFFORTS:
        raise SecflowException("Bad 'solution_effort' parameter")
    data = {
        'asset': asset_id,
        'severity': severity,
        'cvss_vector': cvss_vector,
        'title': title,
        'description': description,
        'category': category,
        'solution_headline': solution_headline,
        'solution': solution,
        'solution_priority': solution_priority,
        'solution_effort': solution_effort,
        'is_quickwin': is_quickwin,
        'comments': comments
    }
    try:
        r = self.rs.post(self.url+"/api/auth/vulns/?format=json", json=data)
        return r.text
    except requests.exceptions.RequestException as e:
        raise SecflowException("Unable to create vuln: {}".format(e))


def delete_vuln(self, vuln_id: int):
    """
    Delete a vulnerability.

    :param vuln_id: Vuln ID
    :type vuln_id: int
    :rtype: json
    """
    try:
        r = self.rs.delete(self.url+f"/api/auth/vulns/{str(vuln_id)}/?format=json")
        return r.text
    except requests.exceptions.RequestException as e:
        raise SecflowException("Unable to delete a vuln: {}".format(e))

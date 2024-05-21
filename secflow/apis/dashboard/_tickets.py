#!/usr/bin/env -S python3 -OO
# coding:utf8

import requests
from secflow.exceptions import SecflowException


def get_tickets(self, org_id: int = None, page: int = 1, limit: int = 10):
    """
    Get all tickets.

    :param org_id: Organization ID
    :param page: Page number of results (Opt.)
    :param limit: Max results per page. Default is 10, Max is 100 (Opt.)
    :rtype: json
    """
    url_params = f'?format=json&page={str(page)}&limit={str(limit)}'
    if org_id is not None and str(org_id).isnumeric():
        url_params += f'&org={str(org_id)}'

    try:
        r = self.rs.get(self.url+"/api/auth/tickets/{}".format(url_params))
        return r.text
    except requests.exceptions.RequestException as e:
        raise SecflowException("Unable to list tickets: {}".format(e))


def get_ticket(self, ticket_id: int):
    """
    Get ticket details.

    :param ticket_id: Ticket ID
    :rtype: json
    """
    try:
        r = self.rs.get(self.url+f"/api/auth/tickets/{str(ticket_id)}/?format=json")
        return r.text
    except requests.exceptions.RequestException as e:
        raise SecflowException("Unable to retrieve ticket: {}".format(e))

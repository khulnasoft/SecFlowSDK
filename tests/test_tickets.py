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

    # Tickets
    # List all tickets
    tickets = json.loads(api.get_tickets())
    if len(tickets) > 0 and len(tickets['results']) > 0:
        # Get ticket details
        ticket_id = tickets['results'][0]['id']
        print(api.get_ticket(ticket_id))

#!/usr/bin/env -S python3 -OO
# coding:utf8

# Assets
ASSET_TYPES = [
    'ip',
    'ip-range',
    'ip-subnet',
    'fqdn',
    'domain',
    'url',
    'keyword'
]

ASSET_EXPOSURES = [
    'unknown', 'external', 'internal', 'restricted'
]

ASSET_CRITICALITIES = [
    1, 2, 3
]


# Vulnerability
VULNERABILITY_SEVERITY = [
    0, 1, 2, 3, 4
]

VULNERABILITY_STATUS = [
    'new', 'ack', 'assigned', 'patched', 'closed',
    'closed-benign', 'closed-fp', 'closed-duplicate', 'closed-workaround'
]

active_vulns_status = [
    'new', 'ack', 'assigned'
]

closed_vulns_status = [
    'patched', 'closed',
    'closed-benign', 'closed-fp', 'closed-duplicate', 'closed-workaround'
]

VULNERABILITY_SOLUTION_PRIORITIES = [
    'urgent', 'moderate', 'hardening'
]

VULNERABILITY_SOLUTION_EFFORTS = [
    'low', 'medium', 'high'
]

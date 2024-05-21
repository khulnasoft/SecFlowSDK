#!/usr/bin/env -S python3 -OO
# coding:utf8

"""Setup file."""


from setuptools import setup, find_packages

setup(
    name='secflow-sdk',
    version='1.0.1',
    description='Python API SDK for SecFlowDashboard',
    url='https://github.com/khulnasoft/SecFlowSDK',
    author='KhulnaSoft Ltd',
    author_email='security@khulnasoft.com',
    license='AGPLv3',
    packages=find_packages(),
)

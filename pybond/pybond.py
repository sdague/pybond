# -*- coding: utf-8 -*-

import requests

"""Main module."""

class Hub(object):

    def __init__(self, addr, token):
        self._addr = addr
        self._token = token
        self.client = requests.Session()
        self.client.headers.update({"BOND-Token": self._token})

    def _url(self, url):
        return "http://{}/v2{}".format(self._addr, url)

    def _get(self, path):
        return self.client.get(self._url(path))

    @property
    def devices(self):
        return self._get("/devices")

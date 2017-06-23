#!/usr/bin/env python
# -*- coding: utf-8 -*-


class client():

    def __init__(self, server, id_client):
        self.server = server
        self.id = id_client

    def get_time(self):

        print("I am client {i}, getting time {t}".format(i=self.id, t=self.server.get_time()))

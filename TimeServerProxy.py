#!/usr/bin/env python
# -*- coding: utf-8 -*-

from TimeServer import Server


class TimeServerProxy():

    def __init__(self):
        self.time_server = Server()

    def get_time(self):

        return self.time_server.get_time()

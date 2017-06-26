#!/usr/bin/env python
# -*- coding: utf-8 -*-

from TimeServer import TimeServer


class TimeServerProxy():

    def __init__(self):
        self.time_server = TimeServer()

    def get_time(self):

        return self.time_server.get_time()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from TimeServerProxyIPC import TimeServerProxyIPC
from main_time_server import *
import datetime as dt


def time_server_process():
    thread_server = TimeServerIPC()
    thread_server.start()


class TestStringMethods(unittest.TestCase):

    def test_IPC(self):
        client = TimeServerProxyIPC()
        time_server_process()
        result=client.get_time() - dt.datetime.today()
        #result= abs(dt.datetime.today()-client.get_time() )   # plus de 5ms
        self.assertEqual(result.microseconds < 5, True)

if __name__ == '__main__':
    unittest.main()
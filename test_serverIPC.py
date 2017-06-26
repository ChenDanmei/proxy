#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from TimeServerProxyIPC import TimeServerProxyIPC
from main_time_server import time_server_process
import threading
import datetime as dt


class TestStringMethods(unittest.TestCase):

    def test_IPC(self):
        server = threading.Thread(target=time_server_process, args=())
        server.start()
        client = TimeServerProxyIPC()
        result=client.get_time() - dt.datetime.today()
        #result= dt.datetime.today()-client.get_time()    # plus de 5ms
        self.assertEqual(result.microseconds < 5, True)

if __name__ == '__main__':
    unittest.main()
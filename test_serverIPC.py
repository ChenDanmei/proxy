#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from TimeServerProxyIPC import TimeServerProxyIPC
from TimeServerIPC import TimeServerIPC
import datetime as dt
import time


class TestIPCServer(unittest.TestCase):

    def test_IPC(self):
        socket_mode = 'zmq'
        client = TimeServerProxyIPC(socket_mode= socket_mode)
        server = TimeServerIPC(socket_mode=socket_mode)
        server.start()
        srv_time = client.get_time() 
        server.stop()
        while not server.stopped():
            time.sleep(0.1)
        print("try to join")
        server.join()
        print("joined")
        result= abs(dt.datetime.today()-srv_time)   # plus de 5ms
        print ("duration: "+str(result))
        self.assertEqual(result.microseconds < 200*1000, True)

if __name__ == '__main__':
    unittest.main()

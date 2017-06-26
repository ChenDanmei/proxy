#!/usr/bin/env python
# -*- coding: utf-8 -*-

from TimeServerProxyIPC import TimeServerProxyIPC
import time


def test_serverIPC():
    server = TimeServerProxyIPC()
    try:
        while True:
            tm = server.get_time()
            time.sleep(1)
    finally:
        pass

if __name__ == '__main__':
    test_serverIPC()
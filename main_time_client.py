#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zmq
import pickle


class TimeServerProxyIPC():

    def __init__(self):
        pass

    def get_time(self):

        context = zmq.Context()
        ask_time = context.socket(zmq.REQ)
        ask_time.connect("tcp://localhost:5558")
        try:
            while True:
                ask_time.send(b"time")
                time = pickle.loads(ask_time.recv())
        finally:
            ask_time.close()
            context.term()

        return time

if __name__ == '__main__':
    client = TimeServerProxyIPC()
    client.get_time()

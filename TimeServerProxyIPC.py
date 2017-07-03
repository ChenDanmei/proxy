#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zmq
import pickle
import socket

class TimeServerProxyIPC():
    def __init__(self, socket_mode):
        self.socket_mode = socket_mode

    def get_time(self):
        if self.socket_mode == 'zmq':
            context = zmq.Context()
            ask_time = context.socket(zmq.REQ)
            ask_time.connect("tcp://localhost:5558")
            ask_time.send(b"time")
            time = pickle.loads(ask_time.recv())
            ask_time.close()
            context.term()
        elif self.socket_mode == 'tcp':
            address = ('localhost', 5558)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(address)
            s.send(b'hihi')
            time = pickle.loads(s.recv(512))
            s.close()
        else:
            print("chose the socket_mode from 'zmq' and 'tcp' !")
            raise ValueError
        return time





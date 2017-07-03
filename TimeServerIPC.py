#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zmq
from TimeServer import TimeServer
import pickle
import time
import threading
import socket
TIMEOUT = 5



class TimeServerIPC(threading.Thread):
    def __init__(self, socket_mode):
        super(TimeServerIPC, self).__init__()
        self._stop_event = threading.Event()
        self._server_closed = threading.Event()
        self.socket_mode = socket_mode

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._server_closed.is_set()


    def run(self):
        server = TimeServer()
        if self.socket_mode == 'zmq':
            context = zmq.Context()
            answer_time = context.socket(zmq.REP)
            answer_time.bind("tcp://*:5558")

            try:
                while not self._stop_event.is_set():
                    msg = answer_time.recv()
                    answer_time.send(pickle.dumps(server.get_time()))
                    time.sleep(.001)
            finally:
                answer_time.close()
                self._server_closed.set()
        elif self.socket_mode == 'tcp':
            address = ('localhost', 5558)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # s = socket.socket()
            s.bind(address)
            s.listen(1)
            ss, addr = s.accept()
            try:
                while not self._stop_event.is_set():
                    ss.recv(512)
                    ss.send(pickle.dumps(server.get_time()))
                    time.sleep(0.001)
            finally:
                ss.close()
                s.close()
                self._server_closed.set()
        else:
            print("chose the socket_mode from 'zmq' and 'tcp' !")
            raise ValueError






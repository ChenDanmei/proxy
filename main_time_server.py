#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zmq
from TimeServer import TimeServer
import pickle
from threading import Thread
TIMEOUT = 5

class TimeServerIPC(Thread):
    def __init__(self):
        Thread.__init__(self, name="TimeServerIPC")
        self.stop = False

    def stop_ipc_server(self):
        self.stop = True

    def run(self):
        server = TimeServer()
        context = zmq.Context()
        answer_time = context.socket(zmq.REP)
        answer_time.bind("tcp://*:5558")
        poll = zmq.Poller()
        poll.register(answer_time, zmq.POLLIN)

        try:
            while not self.stop:
                msg = dict(poll.poll(TIMEOUT))
                if len(msg) > 0:
                    answer_time.recv()
                else:
                    print("Time out")
                    break
                answer_time.send(pickle.dumps(server.get_time()))


        finally:
            answer_time.close()






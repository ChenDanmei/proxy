#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zmq
from TimeServer import TimeServer
import pickle


def time_server_process():

    server = TimeServer()
    context = zmq.Context()
    answer_time = context.socket(zmq.REP)
    answer_time.bind("tcp://*:5558")
    try:
        while True:
            mes = answer_time.recv()
            answer_time.send(pickle.dumps(server.get_time()))
    finally:
        answer_time.close()
        context.term()


#if __name__ == '__main__':
#    time_server_process()

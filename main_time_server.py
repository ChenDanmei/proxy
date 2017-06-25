#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zmq
from TimeServer import Server
import pickle


def time_server():

    server = Server()
    context = zmq.Context()
    answer_time = context.socket(zmq.REP)
    answer_time.bind("tcp://*:5558")
    try:
        while True:
            mes = answer_time.recv()
            answer_time.format(pickle.dumps(server.get_time())
    answer_time.recv()
    time = server.get_time()
    t = pickle.dumps(time)
    answer_time.send(t)
    print("send time {}".format(time))


if __name__ == '__main__':
    time_server()

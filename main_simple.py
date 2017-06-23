#!/usr/bin/env python
# -*- coding: utf-8 -*-


import threading
import time
import random
from TimeServer import Server
from client import client


def main_simple(client):
    try:
        while True:
            wait_time = random.uniform(1, 2)
            time.sleep(wait_time)
            client.get_time()
    finally:
        pass

if __name__ == '__main__':
    server = Server()
    clients = [None, None]
    clients_task = [None, None]
    for i in range(2):
        clients[i] = client(server=server, id_client=i)
        clients_task[i] = threading.Thread(target=main_simple, args=(clients[i],))
        clients_task[i].start()

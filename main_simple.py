#!/usr/bin/env python
# -*- coding: utf-8 -*-


import threading
import time
import sys
import random
from main_time_server import time_server_process
from TimeServer import TimeServer
from TimeServerProxy import TimeServerProxy
from TimeServerProxyIPC import TimeServerProxyIPC
from client import client


def main_simple(client):
    try:
        while True:
            wait_time = random.uniform(1, 2)
            time.sleep(wait_time)
            client.get_time()
    finally:
        pass

def print_help():
    print("""
    use one of these options:
    -mode=direct        : runs the client-server as a function call
    -mode=simple_proxy  : uses a server proxy, in the same process
    -mode=client-IPC    : runs the client side when in interprocess (IPC) mode
    -mode=server-IPC    : runs the server side when using IPC
        """)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print_help()
        exit(-1)
    arg = sys.argv[1]
    server = None
    if arg=="-mode=direct":
        server = TimeServer()
    elif arg=="-mode=simple_proxy":
        server = TimeServerProxy()
    elif arg=="-mode=client-IPC":
        server = TimeServerProxyIPC()
    elif arg=="-mode=server-IPC":
        time_server_process()
    else:
        print_help()
        exit(-1)




    clients = [None, None]
    clients_task = [None, None]
    for i in range(2):
        clients[i] = client(server=server, id_client=i)
        clients_task[i] = threading.Thread(target=main_simple, args=(clients[i],))
        clients_task[i].start()

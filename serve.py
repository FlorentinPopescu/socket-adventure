"""
serve.py

Instantiates a socket-adventure `Server` and serves it on a specified
port.

You should not need to make any changes in this file.
"""
# imports
import sys

# import server class
from server import Server
#-----------------------------------

# get a port number from command line
try:
    port = int(sys.argv[1])
except IndexError:
    print("Please include a port number, eg: python serve.py 50000")
    exit(-1)
#-----------------------------------

# create an instance of the class
server = Server(port)

# invoke instance's serve method
server.serve()

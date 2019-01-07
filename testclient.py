#!/usr/bin/python
import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) < 2:
    print 'not enough args'
    sys.exit(1)

s_addr = (sys.argv[1], int(sys.argv[2]))
sock.connect(s_addr)

try:
    msg = 'test message'
    print >>sys.stderr, 'sending "%s"' % msg
    sock.sendall(msg)

    recv = 0
    expd = len(msg)

    while recv < expd:
        d = sock.recv(16)
        recv += len(d)
        print >>sys.stderr, 'recevied "%s"' % d

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()

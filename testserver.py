#!/usr/bin/python
import socket, sys

#instantiate tcp/ip socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) < 2:
    print "not enough args"
    sys.exit(1)

#define server address and port
s_addr = (sys.argv[1], int(sys.argv[2]))

print >>sys.stderr, 'initiating on %s port %s' % s_addr

#bind to server address
sock.bind(s_addr)
#listen on given address, with 1000 backlog tcp connections
sock.listen(1000)

while True:
    #waiting for connection
    print >>sys.stderr, 'ready to accept connection'
    conn, c_addr = sock.accept()
    
    try:
        print >>sys.stderr, 'conn src: ', c_addr

        while True:
            d = conn.recv(16)
            print >>sys.stderr, 'received "%s"' % d
            if d:
                print >>sys.stderr, 'sending buffer back to client'
                conn.sendall(d)
            else:
                print >>sys.stderr, 'buffer is empty, connection will now close'
                break
    finally:
        conn.close()

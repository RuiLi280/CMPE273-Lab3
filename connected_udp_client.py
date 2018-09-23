from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class Client(DatagramProtocol):

    def startProtocol(self):
        host = "127.0.0.1"
        port = 1234

        self.transport.connect(host, port)
        print("client connect to host %s port %d" % (host, port))
        self.transport.write(b"hi from client")  # no need for address

    def datagramReceived(self, data, address):
        host, port = address
        print("received %r from %s:%d" % (data.decode(), host, port))

    # Possibly invoked if there is no server listening on the
    # address to which we are sending.
    def connectionRefused(self):
        print("No one listening")


reactor.listenUDP(0, Client())
reactor.run()

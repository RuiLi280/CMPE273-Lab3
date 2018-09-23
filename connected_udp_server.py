from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class Helloer(DatagramProtocol):

    def datagramReceived(self, data, address):
        host, port = address
        print("received %r from %s:%d" % (data.decode(), host, port))
        # no need for address
        self.transport.write(b"hello from server", address)


# 0 means any port, we don't care in this case
reactor.listenUDP(1234, Helloer())
reactor.run()

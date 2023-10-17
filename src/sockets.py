import socket as s
from abc import abstractmethod


class PingSocket:

    def __init__(self, host, port, timeout, addr_family, protocol_desc):
        self.HOST = host
        self.PORT = port
        self.PROTOCOL: s.AddressFamily = addr_family
        self.protocol_desc = protocol_desc
        self.TIMEOUT = timeout
        self.socket: s.socket = None

    def __enter__(self):
        self.socket = s.socket(self.PROTOCOL, s.SOCK_STREAM)
        self.socket.settimeout(self.TIMEOUT)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.socket.close()
        self.socket = None

    @abstractmethod
    def connect(self):
        pass


class SocketIPV4(PingSocket):

    def __init__(self, host, port, timeout):
        super().__init__(host, port, timeout, s.AF_INET, 'IPV4')

    def connect(self):
        self.socket.connect((self.HOST, self.PORT))


class SocketIPV6(PingSocket):

    def __init__(self, host, port, flowinfo, scope_id, timeout):
        super().__init__(host, port, timeout, s.AF_INET6, 'IPV6')
        self.flowinfo = flowinfo
        self.scope_id = scope_id

    def connect(self):
        self.socket.connect((self.HOST, self.PORT,
                             self.flowinfo, self.scope_id))


def get_socket(args):
    ip_address_data = s.getaddrinfo(args.address, args.port)
    if args.is_force_ipv4:
        ip_address_data = filter(lambda x: x[0] == s.AF_INET, ip_address_data)
    elif args.is_force_ipv6:
        ip_address_data = filter(lambda x: x[0] == s.AF_INET6, ip_address_data)

    ip_address_data = list(ip_address_data)
    if len(ip_address_data) == 0:
        return None
    ip_address = ip_address_data[0]

    socket = None
    if ip_address[0] == s.AF_INET:
        socket = SocketIPV4(*ip_address[4], args.timeout)
    elif ip_address[0] == s.AF_INET6:
        socket = SocketIPV6(*ip_address[4], args.timeout)

    return socket

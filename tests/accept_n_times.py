import socket
import sys


def accept(n, family):
    with socket.socket(family, socket.SOCK_STREAM) as sock:
        sock.bind(('localhost', 9999))
        sock.listen()
        for _ in range(n):
            client, addr = sock.accept()


if __name__ == '__main__':
    n = int(sys.argv[1])
    family = sys.argv[2]
    if family == '4':
        family = socket.AF_INET
    else:
        family = socket.AF_INET6
    accept(n, family)

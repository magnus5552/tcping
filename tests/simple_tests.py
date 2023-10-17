import unittest

from src import *
from test_socket import TestSocket


class SimpleTests(unittest.TestCase):
    def setUp(self):
        self.fake_socket = TestSocket(0.01, 0.005, 'test', '80')
        self.ping = Ping(self.fake_socket, interval=0.01)

    def test_simple(self):
        self.ping.ping()
        self.assertTrue(all(r.is_success for r in self.ping.results))

    def test_handle_timeout(self):
        self.fake_socket.fake_timeout = 0.2
        self.ping.ping()
        self.assertTrue(all(r.is_timeout for r in self.ping.results))

    def test_handle_OSError(self):
        self.fake_socket.is_OSError = True
        self.ping.ping()
        self.assertTrue(all(not r.is_success and not r.is_timeout
                            for r in self.ping.results))


if __name__ == '__main__':
    unittest.main()

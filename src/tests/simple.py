import unittest

from src import *
from .test_socket import TestSocket


class SimpleTests(unittest.TestCase):
    def setUp(self):
        self.parser = configure_parser()
        self.args = self.parser.parse_args(
            ['-i', '0.01', '-w', '0.01', 'test', '80'])

    def test_simple(self):
        ping = Ping(self.args, lambda: TestSocket(0.005))
        ping.ping()
        self.assertTrue(all(r.is_success for r in ping.results))

    def test_handle_timeout(self):
        ping = Ping(self.args, lambda: TestSocket(0.02))
        ping.ping()
        self.assertTrue(all(r.is_timeout for r in ping.results))

    def test_handle_OSError(self):
        ping = Ping(self.args, lambda: TestSocket(0.005, True))
        ping.ping()
        self.assertTrue(all(not r.is_success and not r.is_timeout
                            for r in ping.results))


if __name__ == '__main__':
    unittest.main()

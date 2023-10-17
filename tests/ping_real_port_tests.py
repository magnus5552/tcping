from os.path import dirname, abspath, join
import unittest
from subprocess import Popen

from parameterized import parameterized

from src import parse_args, get_socket, Ping


class RealPing(unittest.TestCase):

    def setUp(self) -> None:
        dir_name = dirname(abspath(__file__))
        self.runner_file = join(dir_name, 'accept_n_times.py')
        self.python = join(dir_name, '../venv/Scripts/python.exe')


    @parameterized.expand(['4', '6'])
    def test_protocol(self, version):
        self.subprocess = Popen([self.python, self.runner_file, '4', version],
                                shell=False)
        args = parse_args(['-' + version, 'localhost', '9999'])
        socket = get_socket(args)
        ping = Ping(socket, interval=0.05, count=4, is_infinite=False)
        ping.ping()
        self.assertEqual(len(ping.results), 4)
        self.assertTrue(all(r.is_success for r in ping.results))

    def tearDown(self) -> None:
        self.subprocess.kill()
        self.subprocess.wait(1)


if __name__ == '__main__':
    unittest.main()

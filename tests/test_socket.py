from src.sockets import PingSocket


class TestSocket(PingSocket):
    __test__ = False

    def __init__(self, timeout, fake_timeout, host, port, is_OSError = False):
        super().__init__(host, port, timeout, None, 'fake')
        self.fake_timeout = fake_timeout
        self.is_OSError = is_OSError

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

    def connect(self):
        if self.is_OSError:
            raise OSError

        if self.TIMEOUT < self.fake_timeout:
            raise TimeoutError

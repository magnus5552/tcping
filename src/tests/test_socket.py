class TestSocket:
    __test__ = False

    def __init__(self, timeout, is_OSError = False):
        self.timeout = 1
        self.fake_timeout = timeout
        self.is_OSError = is_OSError

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

    def settimeout(self, timeout):
        self.timeout = timeout

    def connect(self, tuple):
        if self.is_OSError:
            raise OSError

        if self.timeout < self.fake_timeout:
            raise TimeoutError

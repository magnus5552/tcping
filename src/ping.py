import time

from .ping_statistic import PingResult, print_result, PingStatistic
from .sockets import PingSocket


def to_ms(time_in_seconds):
    return round(time_in_seconds * 1000, 2)


def ping_once(socket):
    result = PingResult(socket.ip, False, False, 0)
    with socket as sock:
        try:
            start_time = time.time()
            sock.connect()
            result.is_success = True
        except TimeoutError:
            result.is_success = False
            result.is_timeout = True
        except OSError:
            result.is_success = False
        result.elapsed = to_ms(time.time() - start_time)

    return result


class Ping:
    def __init__(self,
                 sockets: list[PingSocket],
                 interval=1.0,
                 count=4,
                 is_infinite=False):
        self.recieved_count = 0
        self.sent_count = 0
        self.is_infinite = is_infinite
        self.COUNT = count
        self.INTERVAL = interval
        self.SOCKETS = sockets

    def ping(self):
        ips = [s.ip for s in self.SOCKETS]
        print(f'Проверка TCP соединения с {" ".join(ips)}')
        while self.is_infinite or self.sent_count < self.COUNT:
            self.sent_count += 1
            for socket in self.SOCKETS:
                ping_result = ping_once(socket)

                socket.statistic.add_result(ping_result)
                print_result(ping_result)
            print()
            time.sleep(self.INTERVAL)
        print()

    def print_statistic(self):
        for socket in self.SOCKETS:
            socket.statistic.print_statistic()
            print()

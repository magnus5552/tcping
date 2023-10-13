import socket
import time
from dataclasses import dataclass
from statistics import mean


@dataclass
class PingResult:
    ip: str
    is_success: bool
    is_timeout: bool
    elapsed: float


def print_result(result: PingResult):
    if result.is_success:
        print(f'Подключение к {result.ip}: {result.elapsed}ms')
        return

    if result.is_timeout:
        print(f'Превышено время ожидания')
        return

    print('Возникла ошибка при подключении')


def to_ms(time_in_seconds):
    return round(time_in_seconds * 1000, 2)


class Ping:
    def __init__(self, args):
        self.results = []
        self.recieved_count = 0
        self.sent_count = 0
        self.count = args.count
        self.is_infinite = args.is_infinite
        self.interval = args.interval
        self.timeout = args.timeout
        self.address = args.address
        self.port = args.port

    @property
    def ip(self):
        return f'{self.address}:{self.port}'

    def ping(self):
        print(f'Проверка TCP соединения с {self.ip}')
        while self.is_infinite or self.sent_count < self.count:
            self.sent_count += 1
            ping_result = self.ping_once()

            if ping_result.is_success:
                self.recieved_count += 1

            self.results.append(ping_result)
            print_result(ping_result)

            time.sleep(self.interval)

    def ping_once(self):
        result = PingResult(self.ip, False, False, 0)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(self.timeout)
            try:
                start_time = time.time()
                sock.connect((self.address, self.port))
                result.is_success = True
            except TimeoutError:
                result.is_success = False
                result.is_timeout = True
            except OSError:
                result.is_success = False
            result.elapsed = to_ms(time.time() - start_time)

        return result

    def print_statistic(self):
        lost = self.sent_count - self.recieved_count
        loss = lost / self.sent_count * 100 if self.sent_count != 0 else 0.0
        elapsed_stats = [r.elapsed for r in self.results]
        min_elapsed = min(elapsed_stats)
        max_elapsed = max(elapsed_stats)
        mean_elapsed = round(mean(elapsed_stats), 2)

        print(f'Статистика TCP Ping для {self.ip}:')
        print(
            f'    Пакетов отправлено: {self.sent_count}, '
            f'получено: {self.recieved_count}, '
            f'потеряно: {lost} ({loss}% потерь)')
        print(f'Приблизительное время приема-передачи:')
        print(
            f'    Минимальное: {min_elapsed}ms, максимальное: {max_elapsed}ms,'
            f' среднее: {mean_elapsed}ms')

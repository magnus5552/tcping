from dataclasses import dataclass
from statistics import mean


@dataclass
class PingResult:
    ip: str
    is_success: bool
    is_timeout: bool
    elapsed: float


class PingStatistic:
    def __init__(self, ip):
        self.sent_count = 0
        self.recieved_count = 0
        self.results = []
        self.ip = ip

    def add_result(self, result: PingResult):
        self.sent_count += 1
        self.results.append(result)
        if result.is_success:
            self.recieved_count += 1

    def print_statistic(self):
        lost = self.sent_count - self.recieved_count
        loss = lost / self.sent_count * 100 if self.sent_count != 0 else 0.0
        print(f'Статистика TCP Ping для {self.ip}:')
        print(
            f'    Пакетов отправлено: {self.sent_count}, '
            f'получено: {self.recieved_count}, '
            f'потеряно: {lost} ({loss}% потерь)')

        if all(not r.is_success for r in self.results):
            return

        elapsed_stats = [r.elapsed for r in self.results if r.is_success]
        min_elapsed = min(elapsed_stats)
        max_elapsed = max(elapsed_stats)
        mean_elapsed = round(mean(elapsed_stats), 2)

        print(f'Приблизительное время приема-передачи:')
        print(
            f'    Минимальное: {min_elapsed}ms, максимальное: {max_elapsed}ms,'
            f' среднее: {mean_elapsed}ms')

    @property
    def is_all_success(self):
        return all(r.is_success for r in self.results)


def print_result(result: PingResult):
    if result.is_success:
        print(f'{result.ip}: {result.elapsed}ms', end=' ')
        return

    if result.is_timeout:
        print(f'Превышено время ожидания', end=' ')
        return

    print('Возникла ошибка при подключении', end=' ')

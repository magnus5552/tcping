# TCPing
Утилита для проверки TCP портов

## Usage

```shell
python tcping.py [-h] [-n COUNT] [-t] [-i INTERVAL] [-w TIMEOUT] ips [ips ...]

```

| Команда     | Описание                                           |
|-------------|----------------------------------------------------|
| ips         | IP-адрес (в формате: адрес,порт)                   |
| -h, --help  | Показать доступные команды                         |
| -n COUNT    | Число отправляемых запросов проверки связи.        |
 | -t          | Отправлять запросы до остановки с помощью CTRL + C |
| -i INTERVAL | Задержка между запросами                           |
| -w TIMEOUT  | Время ожидания одного запроса                      |

### Покрытие тестами
Проверить покрытие
```shell
 coverage run --include=src\*.* -m pytest .\tests\simple_tests.py .\tests\ping_real_port_tests.py
```
Результаты тестов
```shell
Name                    Stmts   Miss  Cover   Missing
-----------------------------------------------------
src\__init__.py             5      0   100%
src\cmd_parser.py          21      1    95%   41
src\ping.py                43      3    93%   56-58
src\ping_statistic.py      43     13    70%   27-44, 50
src\sockets.py             62      2    97%   29, 79
-----------------------------------------------------
TOTAL                     174     19    89%
```
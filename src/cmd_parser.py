import argparse


def configure_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='tcping',
        description='Утилита tcping')

    parser.add_argument('-n', default=4, type=int, dest='count',
                        help='Число отправляемых запросов проверки связи.')
    parser.add_argument('-t', action='store_true', dest='is_infinite',
                        help='Отправлять запросы до остановки с помощью CTRL '
                             '+ C')
    parser.add_argument('-i', default=1.0, type=float, dest='interval',
                        help='Задержка между запросами')
    parser.add_argument('-w', default=2.0, type=float, dest='timeout',
                        help='Время ожидания одного запроса')
    parser.add_argument('address', help='Конечный узел')
    parser.add_argument('port', nargs='?', default=80, type=int,
                        help='Порт')
    return parser

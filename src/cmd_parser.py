import argparse
import sys


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
    parser.add_argument('-4', action='store_true', dest='is_force_ipv4',
                        help='Задает принудительное использование протокола '
                             'IPv4')
    parser.add_argument('-6', action='store_true', dest='is_force_ipv6',
                        help='Задает принудительное использование протокола '
                             'IPv6')
    parser.add_argument('ips', nargs='+', default=('localhost', 80), type=ip,
                        help='IP-адрес (через запятую)')
    return parser


def ip(arg):
    args = arg.split(',')
    return args[0], int(args[1])


def parse_args(custom_args=None):
    parser = configure_parser()

    args = parser.parse_args(custom_args) if custom_args is not None \
        else parser.parse_args()
    if args.is_force_ipv4 and args.is_force_ipv6:
        raise ValueError('-4 and -6 parameters cannot be used together')

    return args

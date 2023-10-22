from src.cmd_parser import parse_args
from src.ping import Ping
from src.sockets import get_sockets


def main():
    args = parse_args()
    sockets = get_sockets(args)
    if sockets is None:
        print(f'При проверке связи не удалось обнаружить узел {args.ip}\n'
              f'Проверьте имя узла и повторите попытку.')

    ping = Ping(sockets,
                interval=args.interval,
                count=args.count,
                is_infinite=args.is_infinite)
    try:
        ping.ping()
    except KeyboardInterrupt:
        pass
    finally:
        ping.print_statistic()


if __name__ == '__main__':
    main()

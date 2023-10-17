from src.sockets import get_socket
from src.cmd_parser import parse_args
from src.ping import Ping


def main():
    args = parse_args()
    socket = get_socket(args)
    if socket is None:
        print(f'При проверке связи не удалось обнаружить узел {args.address}\n'
              f'Проверьте имя узла и повторите попытку.')

    ping = Ping(socket,
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

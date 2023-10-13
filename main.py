from parser import configure_parser
from ping import Ping


def main():
    parser = configure_parser()
    args = parser.parse_args()
    ping = Ping(args)
    try:
        ping.ping()
    except KeyboardInterrupt:
        pass
    finally:
        ping.print_statistic()


if __name__ == '__main__':
    main()

import sys

from src.cmd_parser import configure_parser
from src.ping import Ping


def main():
    parser = configure_parser()
    if len(sys.argv) == 1:
        parser.print_help()
        return

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

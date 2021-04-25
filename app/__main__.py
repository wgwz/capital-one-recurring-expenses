import argparse
from app.parse import parse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args()
    parse(args.file)


if __name__ == "__main__":
    main()

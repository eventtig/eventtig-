import argparse
import os

import eventtig.process


def main():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="subparser_name")

    build_parser = subparsers.add_parser("build")
    build_parser.add_argument("source")
    build_parser.add_argument("--sqlite", help="Location of SQLite file")
    build_parser.add_argument("--staticsite", help="Location of Static Site")

    check_parser = subparsers.add_parser("check")
    check_parser.add_argument("source")

    args = parser.parse_args()

    if args.subparser_name == "build":

        if not args.sqlite and not args.staticsite:
            print("You must specify one of the build options when running build.")
            exit(-1)

        eventtig.process.build(
            args.source, os.path.join(args.source, "eventtig.yaml"), args
        )

    elif args.subparser_name == "check":

        eventtig.process.check(args.source, os.path.join(args.source, "eventtig.yaml"))


if __name__ == "__main__":
    main()

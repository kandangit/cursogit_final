#!/usr/bin/env python3
import re
import sys


def main():
    regex = r"^\w+(\(.+\))*: .+"
    commit_msg_filepath = sys.argv[1]

    with open(commit_msg_filepath, "r") as file:
        content = file.read().strip()

    if not re.match(regex, content):
        print("ERROR: El missatge de commit no és convencional.")
        return 1

    print("El teu missatge de commit és convencional.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
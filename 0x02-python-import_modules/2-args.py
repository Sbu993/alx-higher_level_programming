#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    user = argv[1:]
    siz = len(user)
    print("{:d} {:s}{:s}".
          format(siz,
                 "arguments" if (siz) is not 1 else "argument",
                 "." if (siz) is 0 else ":"))
    for idx, arg in enumerate(user):
        print("{:d}: {:s}".format(idx + 1, arg))

#!/usr/bin/python3
def multiple_returns(sent):

    length = len(sent)
    char = sent[0] if length > 0 else None

    return (length, char)

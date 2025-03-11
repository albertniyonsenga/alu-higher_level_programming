#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        len = len(sentence)
    else:
        len = 0
    return tuple((len, None if not sentence else sentence[:1]))

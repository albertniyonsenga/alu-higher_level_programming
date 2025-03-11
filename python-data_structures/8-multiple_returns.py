#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        leng = len(sentence)
    else:
        leng = 0
    return tuple((leng, None if not sentence else sentence[:1]))

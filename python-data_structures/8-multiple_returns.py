#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = 0
    return tuple(len(sentence), None if not sentence else sentence[:1])

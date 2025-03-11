#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence="":
        return None
    return tuple(len(sentence), len(sentence[0]))

#!/usr/bin/python3


def best_score(a_dictionary):
    max_score = 0
    if a_dictionary is None:
        return None
    else:
        for i, j in a_dictionary.items():
            if a_dictionary[i] > max_score:
                max_score = a_dictionary[i]
                max_key = i
        return max_key

#!/usr/bin/python3


def no_c(my_string):
    c_list = ['c', 'C']
    my_list = list(my_string)
    noC_list = []
    for i in (my_list):
        if i not in c_list:
            noC_list.append(i)
    i = 0
    noC_string = ""

    while (i < len(noC_list)):
        noC_string += str(noC_list[i])
        i += 1
    return noC_string

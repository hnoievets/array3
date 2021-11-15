from math import sqrt


def list_sqrt(data_list):
    sqrt_list = []
    if len(data_list) > 0:
        for i in data_list:
            sqrt_list += [sqrt(i)]

        return sqrt_list

    else:
        return -1

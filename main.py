#!/user/bin/env/python
# -*- coding: utf-8 -*-
import importlib
import sys

from TK_1 import num_in_list
from TK_2 import list_in_tuple_min_max
from TK_3 import list_div_on_avg
from TK_4 import list_multi_on_avg
tk5 = importlib.import_module('TK-5')


def main():
    data = []
    t_data = ()
    data_2 = []

    count = int(input('Enter size of array: '))
    if count <= 0:
        print('ERROR')
        return 1

    data = num_in_list(count)
    print(data)

    t_data = list_in_tuple_min_max(data)
    print('Tuple : ' + str(t_data))

    data_2 = list_div_on_avg(data)
    print('List divided by avg : ' + str(data_2))

    data_2 = list_multi_on_avg(data)
    print('List multiplied by avg : ' + str(data_2))

    data_2 = tk5.list_sqrt(data)
    print('List with sqrt  : ' + str(data_2))

    return 0


if __name__ == '__main__':
    sys.exit(main())

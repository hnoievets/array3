def num_in_list(count):
    data = []
    if count > 0:
        print('Enter ' + str(count) + ' numbers')
        for i in range(count):
            data += [int(input(('Enter number ' + str(i+1) + ': ')))]
        return data

    else:
        return 0

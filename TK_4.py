def list_multi_on_avg(data_list):
    if len(data_list) > 0:
        avg_list = []
        avg = sum(data_list) / len(data_list)
        for i in data_list:
            avg_list += [i * avg]

        return avg_list
    else:
        return 0

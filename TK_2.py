def list_in_tuple_min_max(data_list):
    count = len(data_list)
    t_max = data_list[0]
    t_min = data_list[0]
    if count > 0:
        for i in data_list:
            if i > t_max:
                t_max = i
            if i <= t_min:
                t_min = i

        data_tuple = (t_min, t_max)
        return data_tuple
    else:
        return 0



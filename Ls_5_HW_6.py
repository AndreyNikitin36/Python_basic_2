subj_dict = {}
subj_list = []

with open(r"Text_6.txt", "r", encoding="UTF-8") as key_log:
    for line in key_log:
        subj_list = line.split(" ")
        integ = []
        for ind in subj_list:
            l = len(ind)
            i = 0
            while i < l:
                s_int = ''
                a = ind
                for symbol in a:
                    if '0' <= symbol <= '9':
                        s_int += symbol
                    i += 1
                if s_int != '':
                    integ.append(int(s_int))
        key_1 = subj_list[0][:-1]
        value_1 = str(sum(integ))
        new_dict = {key_1: value_1}
        subj_dict.update(new_dict)

    print(subj_dict)
    print(type(subj_dict))

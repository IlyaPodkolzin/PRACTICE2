def generate_groups():
    group_dict = {"В": 9, "К": 37, "М": 2, "Н": 12}
    for key in group_dict.keys():
        print('\n'.join([f'И{key}БО', " ".join([f'И{key}БО-0{val + 1}-22' if val < 9 else f'И{key}БО-{val + 1}-22' for val in range(group_dict[key])])]))


generate_groups()
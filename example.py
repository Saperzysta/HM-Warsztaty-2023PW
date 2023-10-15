def sweap_max(items: list) -> list:

    max_pos = items.index(max(items))
    items[0], items[max_pos] = items[max_pos], items[0]

    return items

print(sweap_max([5, 10, 1, 2, 3, 10 , 11 ,10]))
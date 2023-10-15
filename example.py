def sweap_max(items: list) -> list:
    max_item = items[0]
    max_pos = 0
    for i in range(len(items)):
        if max_item <= items[i]:
            max_item = items[i]
            max_pos = i
    items[max_pos] = items[0]
    items[0] = max_item
    return items

print(sweap_max([5, 10, 1, 2, 3, 10 , 11 ,10]))
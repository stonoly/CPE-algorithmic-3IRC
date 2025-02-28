def maxliste(list: list[int]) -> int:
    size_list = len(list)

    if size_list == 1:
        return list[0]

    if size_list == 2:
        return list[0] if list[0] > list[1] else list[1]

    first_slice = list[:size_list//2]
    last_slice = list[size_list//2:]

    a = maxliste(first_slice)
    b = maxliste(last_slice)

    return a if a > b else b


    


    

if __name__ == "__main__":

    list_test = [888, 990, 582, 458, 676, 778, 677, 185, 282, 634, 722, 41, 128, 787, 214, 767, 321, 481, 28, 941, 225, 86, 167, 627, 396, 583, 5, 970, 55, 1000, 521, 916, 337, 626, 195, 433, 194, 879, 6, 760, 129, 653, 500, 221, 938, 387, 167, 790, 979, 294, 140, 963, 412, 334, 840, 123, 691, 925, 19, 322, 285, 123, 108, 302, 84, 773, 562, 389, 657, 577, 34, 195, 175, 987, 104, 129, 788, 187, 965, 537, 639, 128, 386, 192, 329, 339, 950, 488, 39, 237, 492, 754, 977, 854, 457, 242, 927, 901, 277, 10]


    result = maxliste(list_test)

    print(result)


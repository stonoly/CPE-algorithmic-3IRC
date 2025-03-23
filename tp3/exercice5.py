def dicho(sorted_list: list, int_to_find: int) -> int:
    size_list = len(sorted_list)

    if sorted_list[size_list // 2] == int_to_find:
        return size_list // 2
    
    else:
        if size_list ==  1:
            return -1
        else:
            if sorted_list[size_list // 2] > int_to_find:
                return dicho(sorted_list[:size_list // 2], int_to_find)
            else:
                result_dicho_minus = dicho(sorted_list[size_list // 2:], int_to_find)
                if result_dicho_minus == -1:
                    return result_dicho_minus
                return size_list // 2 + result_dicho_minus


if __name__ == "__main__":
    list_of_test = [3, 4, 7, 10, 12, 15, 19, 28, 32, 45]
    int_test = 28
    index_int = dicho(list_of_test, int_test)
    if index_int == -1:
        print(f"Le nombre {str(int_test)} n'est pas dans la liste")
    else:
        print(f"Le nombre {str(int_test)} se trouve à la position {str(index_int)}")
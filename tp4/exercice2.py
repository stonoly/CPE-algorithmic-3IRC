# Question 1. Donnez, sous forme d’une équation de récurrence, le temps d’exécution T(n) de cet algorithme 
#             en fonction du nombre n d’éléments dans le tableau à trier.
# À chaque appel, le tableau de taille n est divisé en deux sous-tableaux de taille n/2.
# L'algorithme appelle récursivement le tri sur chacun des deux sous-tableaux.
# Chaque fusion entre deux sous-tableaux triés prend un temps proportionnel à n.
# L'équation de récurrence du temps d'exécution est donc :
# T(n) = 2 * T(n/2) + cn

# Question 2. 
#       a) Utilisez la méthode par itération vue dans le Cours 3, pour obtenir une expression de T(n) sous la forme d’un O(...).
# D'après la relation T(n) = 2 * T(n/2) + cn
#                     T(n) = 2 (2 * T(n/4) + c(2/n)) + cn
#                     T(n) = 4 T(n/4) + 2 cn
#                     T(n) = 8 T(n/8) + 3 cn
#                     T(n) = 2^k * T(n / 2^k) + k * cn
# On s'arrête quand n / 2^k = 1, donc k = log2(n)
# On obtient : T(n) = n * T(1) + cn * log2(n)
# Donc T(n) ∈ O(n log n)
#
#
#

def sort_by_fusion(list: list) -> list:
    middle_list = (len(list) + 1) // 2
    if len(list) > 2:

        first_slice_list = list[:middle_list]
        last_slice_list = list[middle_list:]

        first_slice_sort = sort_by_fusion(first_slice_list)
        last_slice_sort = sort_by_fusion(last_slice_list)

        sorted_list = []

        while first_slice_sort and last_slice_sort:
            if first_slice_sort[0] >= last_slice_sort[0]:
                sorted_list.append(last_slice_sort[0])
                last_slice_sort.pop(0)

            else:
                sorted_list.append(first_slice_sort[0])
                first_slice_sort.pop(0)

        if (first_slice_sort == []):
            sorted_list.extend(last_slice_sort)
        else:
            sorted_list.extend(first_slice_sort)

        return sorted_list

    else:

        if list[0] > list[len(list) - 1] and len(list) > 1:
            list[0], list[len(list) - 1] = list[len(list) - 1], list[0]

        return list

if __name__ == "__main__":


    list_of_test = [64, 34, 25, 12, 22, 11, 90, 45, 78, 3]


    print("Liste originale:", list_of_test)
    sorted_list = sort_by_fusion(list_of_test)
    print("Liste triée:", sorted_list)
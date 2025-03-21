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
    return list

if __name__ == "__main__":


    list_of_test = [64, 34, 25, 12, 22, 11, 90, 45, 78, 3]


    print("Liste originale:", list_of_test)
    sorted_list = sort_by_fusion(list_of_test)
    print("Liste triée:", sorted_list)
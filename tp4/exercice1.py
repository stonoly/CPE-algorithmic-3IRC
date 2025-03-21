# Question 1: Implémentez en Python le tri par sélection
def sort_by_selection(list: list) -> list:
    size_list = len(list)

    for i in range(size_list):
        min = list[size_list - 1]
        pos_min = size_list - 1

        for j in range(i, size_list):
            if list[j] < min:
                min = list[j]
                pos_min = j

        list[pos_min] = list[i]
        list[i] = min
        
    return list

# Question 2. Quel est l’invariant de boucle maintenu par cet algorithme ?
# Les i éléments de la liste sont triés et ne bouge pas de position et sont plus petit que les element d'indices supérieur à i.

# =Question 3. Donnez la complexité de votre algorithme dans le pire cas sous la forme d’un Θ(...). 
#            Est-ce que la complexité dans le meilleur cas est meilleure ?
# La compléxité de l'algorithme est de Θ(n²) car on parcour une première la fois la liste de taille
# n puis une deuxième fois de taille n/2 (car on parcours les éléments déjà triés) plus les constantes 
# 3 cela nous donnes T = n * n/2 + 3 si on utilise les règles de simplification cela nous donne Θ(n²).

if __name__ == "__main__":

    list_of_test = [64, 34, 25, 12, 22, 11, 90, 45, 78, 3]


    print("Liste originale:", list_of_test)
    sorted_list = sort_by_selection(list_of_test)
    print("Liste triée:", sorted_list)


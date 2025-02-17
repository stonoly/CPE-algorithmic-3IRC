class Node:

    def __init__(self, value: any) -> None:
        self.data = value
        self.next = None

    def __repr__(self):
        if self.next != None:
            return f'{self.data}-> '
        return f'{self.data}'
    
    def setNext(self, suivant: 'Node'):
        self.next = suivant

class ChainList:

    def __init__(self) -> None:
        self.first: Node = None
        self.last: Node = None
        self.size: int = 0

    def insertion_k(self, node_insertion: Node, position: int) -> None:

        if position >= self.size:
            self.insertion(node_insertion)
        
        else:
            if position == 0:
                next = self.first
                self.first = node_insertion
                self.first.next = next

            else:
            
                index = 0
                current = self.first

                while (position - 1 > index and current is not None):

                    current = current.next
                    index += 1
        
                next = current.next
                current.next = node_insertion
                current = current.next
                current.next = next
            self.size += 1

    def insertion(self, node_insertion: Node) -> None:
        if self.size == 0:
            self.first = node_insertion
        else:
            self.last.setNext(node_insertion)

        self.last = node_insertion
        self.size += 1

    def delete_k(self, position: int) -> None:
        if position >= self.size:
            self.delete_last()
        else:
            if position == 0:
                self.first = self.first.next
                self.size -= 1
            else:
                index = 0
                current = self.first
                while position - 1 > index:
                    current = current.next
                    index += 1

                current.next = current.next.next
                self.size -= 1

    def delete_last(self) -> None:
        if self.size == 0 or self.size == 1:
            if self.size == 1:
                self.first = None
                self.last = None
                self.size -= 1
            print("Liste vide")
        else:
            index = 1
            current = self.first
            while self.size - 1 > index:
                current = current.next
                index += 1

            current.next = None
            self.last = current
            self.size -= 1

    def search(self, value: any) -> bool:
        current = self.first
        while current is not None:
            if current.data == value:
                return True
            current = current.next
        return False

    def get(self, position: int) -> None:
        if position >= self.size:
            print("Position Invalide")

        else:
            index = 0
            current = self.first
            while position > index:
                current = current.next
                index += 1
            return current.data
    
    def set(self, position: int, new_value) -> None:
        if position >= self.size:
            self.last.data = new_value
        else:
            index = 0
            current = self.first
            while position > index:
                current =  current.next
                index += 1
            current.data = new_value

    
    def size_of(self) -> int:
        return self.size
    
    def is_empty(self) -> bool:
        return self.size == 0

    def display(self) -> None:
        print(f"-----------------------------------")
        print(f"Premier élément: {self.first.data}")
        print(f"Dernier élément: {self.last.data}")
        print(f"Taille de la liste: {self.size}")
        print()
        current = self.first
        while current is not None:
            print(current, end="")
            current = current.next
        print()
        print()


class Train(ChainList):
    def __init__(self, number_of_car) -> None:
        self.size = 0
        self.set_every_car_to_zero(number_of_car)

    def set_every_car_to_zero(self, number_of_car):
        index = 0
        while index < number_of_car:
            noeuds = Node(0)
            self.insertion_k(noeuds, 0)
            index += 1

    def mounted(self, position):
        if position >= self.size:
            print("Position invalide")
        else:
            inside_train = False
            while position < self.size and not inside_train:
                if self.get(position) < 4:
                    self.set(position, self.get(position) + 1)
                    inside_train = True
                    self.display()
                else:
                    position += 1

            if not inside_train:
                print("Train complet")
    
    def unmounted(self, position):
        if position >= self.size:
            print("Position invalide")
        else:
            if self.get(position) > 0:
                self.set(position, self.get(position) - 1)
                self.display()
            else:
                print("Wagon vide")


if __name__ == "__main__":
    noeud1 = Node(1)
    noeud2 = Node(3)
    noeud3 = Node(4)
    noeud4 = Node(23)
    noeud5 = Node(2)
    noeud6 = Node(7)
    noeud7 = Node(17)
    noeud8 = Node(562)
    noeud9 = Node(61)
    noeud10 = Node(12)

    liste_chainnée_1 = ChainList()
    liste_chainnée_1.insertion(noeud1)
    liste_chainnée_1.insertion(noeud2)
    liste_chainnée_1.insertion(noeud3)
    liste_chainnée_1.insertion(noeud4)
    liste_chainnée_1.insertion(noeud5)
    liste_chainnée_1.insertion(noeud6)
    liste_chainnée_1.display()
    liste_chainnée_1.insertion_k(noeud7, 2)
    liste_chainnée_1.display()
    liste_chainnée_1.insertion_k(noeud8, 22)
    liste_chainnée_1.display()
    liste_chainnée_1.insertion_k(noeud9, 0)
    liste_chainnée_1.display()
    liste_chainnée_1.insertion_k(noeud10, 8)
    liste_chainnée_1.display()
    liste_chainnée_1.delete_last()
    liste_chainnée_1.display()
    liste_chainnée_1.delete_k(2)
    liste_chainnée_1.display()
    print(liste_chainnée_1.search(4))
    liste_chainnée_1.get(7)

    print("")
    print("------------------")
    print("Train")
    print("")
    train = Train(4)
    train.display()
    train.mounted(2)
    train.mounted(2)
    train.mounted(2)
    train.mounted(2)
    train.mounted(2)
    train.mounted(2)
    train.mounted(2)
    train.mounted(2)
    train.unmounted(2)
    train.unmounted(2)
    train.unmounted(2)
    train.unmounted(2)
    train.unmounted(2)
    train.mounted(2)
    
    



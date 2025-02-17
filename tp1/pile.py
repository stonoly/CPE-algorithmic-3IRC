from chain_list import ChainList, Node

class Pile(ChainList):

    def __init__(self):
        super().__init__()
        self._parentheses_dict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        self._parentheses_list = ['(', ')', '[', ']', '{', '}']

    def stack(self, node_insertion: Node) -> None:
        return super().insertion(node_insertion)
    
    def depilate(self) -> None:
        return super().delete_last()
    
    
    def verification_parenthesis(self, string: str) -> bool:
        for i in range(len(string)):
            if string[i] in self._parentheses_list:
                if string[i] in ["{", "(", "["]:
                    noeud = Node(string[i])
                    self.stack(noeud)
                else:
                    if self.is_empty():
                        print("Ce n'est pas bien parenthésé 1")
                        return False

                    else:
                        taille_stack = self.size_of()
                        if string[i] != self._parentheses_dict[self.get(taille_stack-1)]:
                            print("Ce n'est pas bien parenthésé 2")
                            return False
                        else:
                            self.depilate()
        
        if not self.is_empty():
            print("Ce n'est pas bien parenthésé  3")
            return False
        
        print("C'est bon")
        return True
                    
    
    

if __name__ == "__main__":
    noeud1 = Node(1)
    noeud2 = Node(3)
    noeud3 = Node(4)
    noeud4 = Node(23)
    
    pile1 = Pile()
    pile1.stack(noeud1)
    pile1.stack(noeud2)
    pile1.stack(noeud3)
    pile1.stack(noeud4)
    pile1.display()
    pile1.depilate()
    pile1.depilate()
    pile1.display()

    pile2 = Pile()
    pile2.verification_parenthesis("salut (à toi), je c{che(re[e])}")
    

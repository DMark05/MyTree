class Node:
    pass

class MyTree:
    def __init__(self):
        self.root = Node() # Nó da raiz
        # Cores dos nós
        self.RED = True
        self.BLACK = False

    # Verifica se o Nó x tem ligação vermelha
    def is_red(self, x):
        pass

    # Insere um novo nó na árvore
    def put(self, key, val):
        pass

    def __put(self, h, key, val):
        pass

    # Orienta uma ligação vermelha (temporariamente) inclinada para a direita para inclinar para a esquerda
    def rotate_left(self, h):
        pass

    # Orienta uma ligação vermelha inclinada para a esquerda para inclinar-se para a direita (temporariamente).
    def rotate_right(self, h):
        pass

    # Altera a cor do nó para dividir um nó (temporário) de 4    
    def flip_colors(self, h):
        pass

    # Verifica se a árvore é 2-3
    def is23(self):
        pass

    def __is23(self, node):
        pass

def main():
    mt = MyTree()
    nodes = int(input())
    for i in range(nodes):
        mt.put(int(input()), "")
        print(mt.is23())

if __name__ == "__main__":
    main()
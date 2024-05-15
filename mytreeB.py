class Node:
    def __init__(self, key: float | None = None, value: str | None = None, color: bool = True) -> None:
        self.key = key
        self.value = value
        self.left: Node = None
        self.right: Node = None
        self.color = color

class MyTree:
    def __init__(self):
        self.root: Node = None # Nó da raiz
        # Cores dos nós
        self.RED: bool = True
        self.BLACK: bool = False

    # Verifica se o Nó x tem ligação vermelha
    def is_red(self, x: Node):
        if x is None:
            return False
        return x.color

    # Insere um novo nó na árvore
    def put(self, key: float, val: float):
        self.root = self.__put(self.root, key, val)
        self.root.color = self.BLACK

    def __put(self, h: Node, key: float, val: float):
        if h is None:
            return Node(key, val, self.RED)
        if h.key > key:
            h.left = self.__put(h.left, key, val)
        elif h.key < key:
            h.right = self.__put(h.right, key, val)
        else:
            h.value = val
        
        if self.is_red(h.right) and not self.is_red(h.left):
            h = self.rotate_left(h)
        if self.is_red(h.left) and self.is_red(h.left.left):
            h = self.rotate_right(h)
        if self.is_red(h.left) and self.is_red(h.right):
            h = self.flip_colors(h)

        return h

    # Orienta uma ligação vermelha (temporariamente) inclinada para a direita para inclinar para a esquerda
    def rotate_left(self, h: Node):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = self.RED
        return x

    # Orienta uma ligação vermelha inclinada para a esquerda para inclinar-se para a direita (temporariamente).
    def rotate_right(self, h: Node):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = self.RED
        return x

    # Altera a cor do nó para dividir um nó (temporário) de 4    
    def flip_colors(self, h: Node):
        h.color = not h.color
        h.left.color = not h.left.color
        h.right.color = not h.right.color
        return h

    # Verifica se a árvore é 2-3
    def is_balanced(self):
        return self.__is_within_difference(self.__is_balanced(self.root.left, 0), self.__is_balanced(self.root.right, 0))
    
    def __is_balanced(self, node: Node, black_nodes: int):
        if node is None:
            return 1
        if not self.is_red(node):
            black_nodes += 1
        return self.__biggest(self.__is_balanced(node.left, black_nodes), self.__is_balanced(node.right, black_nodes))
    
    def __biggest(self, a: int, b: int) -> int:
        if a > b:
            return a
        return b

    def __is_within_difference(self, a: int, b: int) -> bool:
        return a - 1 <= b or a + 1 >= b

def main():
    mt = MyTree()
    nodes = int(input())
    for _ in range(nodes):
        num, txt = input().split(" ")
        mt.put(int(num), txt)
    print(mt.is_balanced())
    
if __name__ == "__main__":
    main()
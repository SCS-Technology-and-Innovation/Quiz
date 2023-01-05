# pending: the translation of the code into english
class Node:
 
    def __init__(self):
        self.key = None
        self.left = None
        self.right = None
        self.padre = None
        self.altura = None
        self.profundidad = None

    def alt(self):
        opt = [0]
        if self.left is not None:
            opt.append(self.left.alt())
        if self.right is not None:
            opt.append(self.right.alt())
        self.altura = max(opt) + 1
        return self.altura

    def ubicar(self, buscado, cual):
        if self.key == buscado:
            if cual == 'padre':
                return self.padre
            elif cual == 'left':
                return self.left
            elif cual == 'right':
                return self.right
            elif cual == 'altura':
                return self.altura
            elif cual == 'profundidad':
                return self.profundidad
        if buscado < self.key and self.left is not None:
            return self.left.ubicar(buscado, cual)
        if buscado > self.key and self.right is not None:
            return self.right.ubicar(buscado, cual)
        return None
        
    def prof(self, p):
        self.profundidad = p
        if self.left is not None:
            self.left.prof(p + 1)
        if self.right is not None:
            self.right.prof(p + 1)

    def leaves(self):
        l = set()
        if self.left is not None:
            l |= self.left.leaves()
        if self.right is not None:
            l |= self.right.leaves()
        if len(l) == 0:
            return { self.key }
        else:
            return l
    
    def insert(self, elemento, padre = None):
        self.padre = padre
        if self.key is None:
            self.key = elemento
        else:
            if elemento < self.key:
                if self.left is None:
                    self.left = Node()
                self.left.insert(elemento, self)
            if elemento > self.key:
                if self.right is None:
                    self.right = Node()
                self.right.insert(elemento, self)
 
class Tree:
 
    def __init__(self):
        self.root = None
 
    def __str__(self):
        return str(self.root)
 
    def __repr__(self):
        return str(self.root)
 
    def insert(self, elemento):
        if self.root is None:
            self.root = Node()
        self.root.insert(elemento)

    def update(self):
        self.root.alt()
        self.root.prof(0)

    def leaves(self):
        return self.root.leaves()

    def ubicar(self, valor, cual):
        obtenido = self.root.ubicar(valor, cual)
        if obtenido is not None:
            if cual in ['padre', 'left', 'right']:
                return obtenido.key
            else:
                return obtenido
        else:
            return 'no tiene'

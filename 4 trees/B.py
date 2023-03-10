class Leaf:
    '''Лист дерева'''

    def __init__(self, x: int):
        self.x = x


class Node:
    '''Вершина'''

    def __init__(self):
        self.children = []
        self.max = None

def merge(l: Node, r: Node):
    '''Все ключи в l <= ключом r'''
    if l is None:
        return r
    if r is None:
        return l
    if l.p < r.p:
        l.right = merge(l.right, r)
        return l
    else:
        r.left = merge(l, r.left)
        return r

def split(node: Node, value):
    '''Берет поддерево Node и разделяет его на два по ключу x'''
    if node is None:
        return None, None
    if node.value < value:
        l, r = split(node.right, value)
        node.right = l
        return node, r
    else:
        l, r = split(node.left, value)
        node.left = r
        return l, node


def find(node: Node, value):
    '''Поиск по дереву'''
    if node is None:
        return None
    if node.value == value:
        return node
    elif node.value < value:
        return find(node.right, value)
    elif node.value > value:
        return find(node.left, value)
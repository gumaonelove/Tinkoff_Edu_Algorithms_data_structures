class Node:
    '''Вершина 2-3 дерева'''

    def __init__(self, k: int):
        self.size = 1
        self.key = [k, 0, 0]
        self.first = None # *first <= key[0];
        self.second = None # key[0] <= *second < key[1];
        self.third = None # key[1] <= *third < key[2];
        self.fourth = None # kye[2] <= *fourth.
        self.parent = None # Указатель на родителя нужен для того, потому что адрес корня может меняться при удалении

    def _find(self, value: int) -> bool:
        ''' Этот метод возвращает true, если ключ value находится в вершине, иначе false.'''
        for i in range(self.size):
            if self.key[i] == value:
                return True
        return False

    def _swap(self, x: int, y: int) -> tuple:
        x, y = y, x
        return x, y

    def _sort2(self, x: int, y: int) -> tuple:
        if x > y:
            return self._swap(x, y)

    def _sort3(self, x: int, y: int, z: int) -> tuple:
        if x > y:
            x, y = self._swap(x, y)
        if x > z:
            x, z = self._swap(x, z)
        if y > z:
            y, z = self._swap(y, z)

        return x, y, z

    def _sort(self) -> None:
        '''Ключи в вершинах должны быть отсортированы'''
        if self.size == 1:
            return
        if self.size == 2:
            self.key[0], self.key[1] = self._sort2(self.key[0], self.key[1])
        if self.size == 3:
            self.key[0], self.key[1], self.key[2] = self._sort3(self.key[0], self.key[1], self.key[2])

    def _insert_to_node(self, value: int) -> None:
        '''Вставляем ключ k в вершину (не в дерево)'''
        self.key[self.size] = value
        self.size += 1
        self._sort()

    def _remove_from_node(self, value: int) -> None:
        '''Удаляем ключ k из вершины (не из дерева)'''
        if self.size >= 1 and self.key[0] == value:
            self.key[0] = self.key[1]
            self.key[1] = self.key[2]
            self.size -= 1
        elif self.size == 2 and self.key[1] == value:
            self.key[1] = self.key[2]
            self.size -= 1

    def _become_node_2(self, value: int, _first, _second) -> None:
        '''Преобразовать в 2-вершину.'''
        self.key[0] = value
        self.first = _first
        self.second = _second
        self.third = None
        self.fourth = None
        self.parent = None
        self.size = 1

    def _is_leaf(self) -> bool:
        '''Является ли узел листом; проверка используется при вставке и удалении.'''
        return (self.first is None) and (self.second is None) and (self.third is None)

    def insert(self, p, k):
        '''Вставка ключа k в дерево с корнем p; всегда возвращаем корень дерева, т.к. он может меняться'''
        if p is None: # если дерево пусто, то создаем первую 2-3-вершину (корень)
            return Node(k)
        if p.is_leaf():
            self._insert_to_node(k)
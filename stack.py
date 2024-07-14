# Стек - это абстрактная структура данных, которая следует принципу
# "последним вошел, первым вышел" (Last-In-First-Out, LIFO). Это означает,
# что элементы добавляются и удаляются только с одного конца стека,
# который называется вершиной стека.

# Просто - элементы добавляются и удаляются только сверху.

class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class Stack:
    # инициализация стека
    def __init__(self):
        self.head = None
        self.size = 0

    # добавляет элемент на вершину стека
    def push(self, value):
        new_node = Node(value=value, next=self.head)
        self.head = new_node
        self.size += 1

    # удаляет и возвращает элемент с вершины стека
    def pop(self):
        if self.size == 0:
            return None

        removed_node = self.head
        self.head = self.head.next
        self.size -= 1
        return removed_node.value

    # не удаляет и возвращает элемент с вершины стека
    def peek(self):
        if self.head is None:
            return None
        return self.head.value
    
    # проверяет, пуст ли стек
    def is_empty(self):
        return self.size == 0
    
    # возвращает количество элементов в стеке
    def get_size(self):
        return self.size

    # красивый вывод
    def __str__(self):
        current = self.head
        result = ""

        while current is not None:
            result += str(current.value) + " "
            current = current.next

        return "Tail -> " + result

# # Инициализация стека
# stack = Stack()

# stack.push(10)
# stack.push(20)
# stack.push(30)
# print(stack)  # Ожидается: Tail -> 30 20 10 

# while stack.peek():
#     print(stack.pop())
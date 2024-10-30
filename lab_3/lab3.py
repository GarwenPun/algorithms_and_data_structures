class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_at_position(self, data, position):
        if position < 0:
            print("Позиция не может быть отрицательной.")
            return
        if position == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current_node = self.head
        for _ in range(position - 1):
            if current_node is None:
                print("Позиция выходит за пределы списка.")
                return
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node

    def display(self):
        current_node = self.head
        if not current_node:
            print("Список пуст.")
            return
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def search(self, key):
        current_node = self.head
        position = 0
        while current_node:
            if current_node.data == key:
                return position
            current_node = current_node.next
            position += 1
        return -1  # Элемент не найден

    def delete_from_beginning(self):
        if not self.head:
            print("Cписок пуст.")
            return
        self.head = self.head.next

    def delete_from_end(self):
        if not self.head:
            print("Cписок пуст.")
            return
        if not self.head.next:
            self.head = None
            return

        second_last_node = self.head
        while second_last_node.next.next:
            second_last_node = second_last_node.next
        second_last_node.next = None

    def delete_from_position(self, position):
        if position < 0:
            print("Позиция не может быть отрицательной.")
            return
        if not self.head:
            print("Список пуст.")
            return
        if position == 0:
            self.delete_from_beginning()
            return

        current_node = self.head
        for _ in range(position - 1):
            if current_node is None or current_node.next is None:
                print("Позиция выходит за пределы списка.")
                return
            current_node = current_node.next

        current_node.next = current_node.next.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


"""Индивидуальное задание"""

def difference_list(L1, L2):      #Функция формирует новый список из элементов L1, отсутствующих в L2
    result_list = LinkedList()
    L2_elements = set()

    # Заполняем множество элементами из L2 для быстрого поиска
    current = L2.head
    while current:
        L2_elements.add(current.data)
        current = current.next

    # Добавляем в результат элементы из L1, которые не входят в L2
    current = L1.head
    while current:
        if current.data not in L2_elements:
            result_list.insert_at_end(current.data)
        current = current.next

    return result_list

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)
    linked_list.display()  # 1 -> 2 -> 3 -> None

    linked_list.insert_at_beginning(100)
    linked_list.display()  # 100 -> 1 -> 2 -> 3 -> None

    linked_list.insert_at_position( 5, 2)
    linked_list.display()  # 100 -> 1 -> 5 -> 2 -> 3 -> None

    print("Индекс элемента 2:", linked_list.search(2))  # Индекс элемента 2: 3

    linked_list.delete_from_beginning()
    linked_list.display()  # 1 -> 5 -> 2 -> 3 -> None

    linked_list.delete_from_end()
    linked_list.display()  # 1 -> 5 -> 2 -> None

    linked_list.delete_from_position(2)
    linked_list.display()  # 1 -> 5 -> None

    linked_list.reverse()
    linked_list.display()  # 5 -> 1 -> None

    #проверка индивидуального задания
    print("Индивидуальное задание:")
    L1 = LinkedList()
    L1.insert_at_end(1)
    L1.insert_at_end(3)
    L1.insert_at_end(5)
    L1.insert_at_end(7)

    # Создаем и заполняем второй список L2
    L2 = LinkedList()
    L2.insert_at_end(3)
    L2.insert_at_end(5)

    # Отображаем исходные списки
    print("Список L1:")
    L1.display()  # 1 -> 3 -> 5 -> 7 -> None
    print("Список L2:")
    L2.display()  # 3 -> 5 -> None

    # Создаем список L с элементами из L1, которых нет в L2
    L = difference_list(L1, L2)
    print("Список L (элементы из L1, которых нет в L2):")
    L.display()  # Ожидаемый вывод: 1 -> 7 -> None

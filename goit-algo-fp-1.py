class Node:
    def __init__(self, data=None):
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
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def rev(self, current, prev=None):
        if current.next is None:
            current.next = prev
            self.head = current
            return current
        next_node = current.next
        current.next = prev
        self.rev(next_node, current)

    def reverse(self):
        if self.head is None:
            return None
        return self.rev(self.head)

    def sort(self):
        if self.head is None:
            return "The list is empty"

        # Створюємо пустий вузол для збереження посилання на початок відсортованого списку
        sorted_head = None

        # Ітеруємося по кожному вузлу у вихідному списку
        current = self.head  # Зберігаємо початкову вершину списку
        while current:
            # Зберігаємо наступний вузол перед зміною посилань
            next_node = current.next
            # Вставляємо поточний вузол у відсортований список
            sorted_head = self.sorted_insert(sorted_head, current)
            # Переходимо до наступного вузла у вихідному списку
            current = next_node
        # Замінюємо початок вихідного списку на початок відсортованого списку
        self.head = sorted_head
        return self

    def sorted_insert(self, sorted_head, new_node):
        # Якщо відсортований список порожній або новий вузол має значення менше початкового вузла
        if sorted_head is None or sorted_head.data >= new_node.data:
            new_node.next = sorted_head
            sorted_head = new_node
        else:
            # Знаходимо відповідне місце для вставки нового вузла
            current = sorted_head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

        return sorted_head


def merge(new_list, sort_list1, sort_list2):
    current1 = sort_list1
    current2 = sort_list2

    while current1 is not None and current2 is not None:
        if current1.data < current2.data:
            new_list.insert_at_end(current1.data)
            current1 = current1.next
        else:
            new_list.insert_at_end(current2.data)
            current2 = current2.next

    # Добавляем оставшиеся элементы из sort_list1
    while current1 is not None:
        new_list.insert_at_end(current1.data)
        current1 = current1.next

    # Добавляем оставшиеся элементы из sort_list2
    while current2 is not None:
        new_list.insert_at_end(current2.data)
        current2 = current2.next


def merge_sort(self, list2):
    sort_list1 = self.sort()
    sort_list2 = list2.sort()
    new_list = LinkedList()

    merge(new_list, sort_list1.head, sort_list2.head)

    return new_list


llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Видаляємо вузол
llist.delete_node(10)

print("\nЗв'язний список після видалення вузла з даними 10:")
llist.print_list()

# Пошук елемента у зв'язному списку
print("\nШукаємо елемент 15:")
element = llist.search_element(15)
if element:
    print(element.data)

llist.reverse()
print("\nЗв'язний список після реверсу:")
llist.print_list()
llist.sort()
print("\nЗв'язний список1 після сотування:")
llist.print_list()
llist2 = LinkedList()
llist2.insert_at_beginning(3)
llist2.insert_at_beginning(7)
llist2.insert_at_beginning(10)
llist2.insert_at_beginning(20)
llist2.sort()
print("\nЗв'язний список2 після сотування:")
llist2.print_list()

print("\nЗв'язний список2 після з'єднання:")
llist3 = LinkedList()
llist3 = LinkedList()
merge(llist3, llist.head, llist2.head)
llist3.print_list()
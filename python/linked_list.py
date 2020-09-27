class Node:

    def __init__(self, value):
        self.next = None
        self.value = value

    def __str__(self):
        return f'{self.value}'


class LinkedList:

    def __init__(self):
        self.size = 0
        self.head = None

    def __setitem__(self, index, value):
        self.add_to_index(index, value)

    def __getitem__(self, index):
        return self.get(index)

    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def add_last(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
        self.size += 1

    def add_to_index(self, index, value):
        new_node = Node(value)
        if index >= self.size:
            raise ValueError(f'Index passed in ({index}) is larger than the LinkedList size ({self.size}).')
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        previous_node = self.head
        current_index = 1
        target_node = self.head.next
        while target_node.next is not None:
            if current_index == index:
                previous_node.next = new_node
                new_node.next = target_node
                self.size += 1
                return
            current_index += 1
            previous_node = target_node
            target_node = target_node.next

    def add_after(self, target_value, value):
        new_node = Node(value)
        if self.head is None:
            raise Exception('LinkedList is empty and cannot perform add_after function.')

        current_node = self.head
        while current_node.next is not None:
            if current_node.value == target_value:
                new_node.next = current_node.next
                current_node.next = new_node
                self.size += 1
                return
            current_node = current_node.next
        raise ValueError(f'No node with value matching target_value {target_value} passed in.')

    def add_before(self, target_value, value):
        new_node = Node(value)
        if self.head is None:
            raise Exception('LinkedList is empty and cannot perform add_before function.')

        previous_node = None
        current_node = self.head
        while current_node.next is not None:
            if current_node.value == target_value:
                previous_node.next = new_node
                new_node.next = current_node
                self.size += 1
                return
            previous_node = current_node
            current_node = current_node.next
        raise ValueError(f'No node with matching target_value {target_value} passed in.')

    def get(self, index):
        if index >= self.size:
            raise Exception(f"Index {index} passed in is larger than the LinkedList's size")
        if self.head is None:
            raise Exception(f"LinkedList is empty and cannot retrieve index {index}")
        current_index = 0
        current_node = self.head
        while current_node is not None:
            if index == current_index:
                return current_node
            current_index += 1
            current_node = current_node.next

    def remove(self, value):
        if self.head is None:
            raise Exception('LinkedList is empty and cannot perform remove function.')
        if self.head.value == value:
            self.head = self.head.next
            return

        previous_node = None
        current_node = self.head
        while current_node.next is not None:
            if current_node.value == value:
                previous_node.next = current_node.next
                self.size -= 1
                return
            previous_node = current_node
            current_node = current_node.next
        raise ValueError(f'No node with matching value {value} found.')

    def __str__(self):
        if self.head is None:
            return ''
        to_return = f'{self.head} '
        node = self.head
        while node.next is not None:
            node = node.next
            to_return += f'{node} '
        return to_return


if __name__ == '__main__':
    numbers = LinkedList()
    numbers.add_first(5)
    numbers.add_first(10)
    numbers.add_last(15)
    print(f"{numbers}\n")  # 10, 5, 15

    numbers.add_before(5, 8)
    numbers.add_after(8, 12)
    print(f"{numbers}\n")  # 10, 8, 12, 5, 15

    numbers.remove(12)
    numbers.remove(10)
    print(f"{numbers}\n")  # 8, 5, 15

    numbers[1] = 20
    print(f"{numbers}\n")  # 8, 20, 5, 15
    print(numbers[1])  # 20

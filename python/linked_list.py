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

    def __getitem__(self, index):
        return self.get(index)

    def __setitem__(self, index, value):
        self.add_to_index(index, value)

    def __delitem__(self, index):
        self.remove_by_index(index)

    def get(self, index):
        if index >= self.size:
            raise ValueError(f'Index out of bound. Cannot retrieve index {index} from LinkedList with size {self.size}')
        if self.head is None:
            raise Exception(f'Cannot retrieve index {index} from an empty LinkedList.')
        current_index = 0
        node = self.head
        while node.next is not None:
            if current_index == index:
                return node
            current_index += 1
            node = node.next

    def add_to_index(self, index, value):
        if index >= self.size:
            raise ValueError(f'Index out of bound. Cannot add to index {index} into LinkedList with size {self.size}')
        if self.head is None:
            raise Exception(f'Cannot add to index {index} into an empty LinkedList.')
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1

        current_index = 1
        previous_node = self.head
        current_node = self.head.next
        while current_node.next is not None:
            if current_index == index:
                previous_node.next = new_node
                new_node.next = current_node
                self.size += 1
                return
            current_index += 1
            previous_node = current_node
            current_node = current_node.next

    def add_first(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def add_last(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node
        self.size += 1

    def remove_by_index(self, index):
        if index >= self.size:
            raise ValueError(f'Unable to remove index {index} from LinkedList with size {self.size}')
        if self.head is None:
            raise Exception(f'Cannot remove index {index} from an empty LinkedList')
        if index == 0:
            self.head = self.head.next
            return
        current_index = 1
        previous_node = self.head
        current_node = self.head.next
        while current_node.next is not None:
            if current_index == index:
                previous_node.next = current_node.next
                self.size -= 1
                return
            current_index += 1
            previous_node = current_node
            current_node = current_node.next

    def remove_by_value(self, value):
        if self.head is None:
            raise Exception(f'Cannot remove value {value} from an empty LinkedList')
        if self.head.value == value:
            self.head = self.head.next
            return
        previous_node = self.head
        current_node = self.head.next
        while current_node.next is not None:
            if current_node.value == value:
                previous_node.next = current_node.next
                self.size -= 1
                return
            previous_node = current_node
            current_node = current_node.next

    def __str__(self):
        to_return = ''
        node = self.head
        while node is not None:
            to_return += f'{node.value} '
            node = node.next
        return to_return


if __name__ == '__main__':
    numbers = LinkedList()
    numbers.add_first(7)
    numbers.add_first(10)
    numbers.add_first(-18)
    numbers.add_first(0)
    numbers.add_last(20)
    print(f'{numbers}\n')  # 0, -18, 10, 7, 20
    print(numbers[3])  # 7
    print(numbers[0])  # 0

    numbers[3] = 30
    numbers[0] = 12
    print(f'{numbers}\n')  # 12, 0, -18, 10, 30, 7, 20

    print(f'Before deleting size: {numbers.size}')  # 7
    del numbers[2]
    print(f'{numbers}')  # 12, 0, 10, 30, 7, 20
    print(f'After deleting size: {numbers.size}\n')  # 6

    numbers.remove_by_value(7)
    print(f'{numbers}\n')

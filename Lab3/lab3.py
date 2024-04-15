class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_from_beginning(self):
        if self.is_empty():
            return None
        data = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data

    def delete_from_end(self):
        if self.is_empty():
            return None
        data = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return data
    
    def display_forward(self):
        current = self.head
        print("None <= ", end="")
        while current:
            print(current.data, end="")
            if current.next:
                print(" <=> ", end="")
            current = current.next
        print(" => None")

    def display_back(self):
        current = self.tail
        print("None <= ", end="")
        while current:
            print(current.data, end="")
            if current.prev:
                print(" <=> ", end="")
            current = current.prev
        print(" => None")

    def insert_at_index(self, index, data):
        if index < 0:
            raise IndexError("Index out of range")

        new_node = Node(data)
        if index == 0:
            self.insert_at_beginning(data)
            return

        current = self.head
        current_index = 0

        while current_index < index - 1 and current:
            current = current.next
            current_index += 1

        if current is None:
            raise IndexError("Index out of range")
        
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        if new_node.next is None:
            self.tail = new_node

    def delete_at_index(self, index):
        if index < 0:
            raise IndexError("Index out of range")

        if index == 0:
            self.delete_from_beginning()
            return

        current = self.head
        current_index = 0
        while current_index < index and current:
            current = current.next
            current_index += 1
        if current is None:
            raise IndexError("Index out of range")

        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next
        if current == self.tail:
            self.tail = current.prev


def remove_chars(word):
    return ''.join(char for char in word if char not in 'ab.')    # видалення 'a', 'b', '.'

# Додаємо всі слова до dll

def text_to_dll(text):
    words = text.split()
    if words:
        # видалення знака пунктуації в кінці
        words[-1] = words[-1][:-1] if not words[-1][-1].isalpha() else words[-1]
        dll = DoublyLinkedList()
        for word in words:
            if not word.isalpha():
                raise ValueError("Wrong format: '{}'".format(word))
            dll.insert_at_end(word)
        return dll
    return None

# Показуємо тільки ті які відповідають вимогам

def show_text_with_condition(dll: DoublyLinkedList):
    if dll:
        first_letter = dll.head.data[0].lower()
        current_node = dll.head
        print("None <= ", end="")
        while current_node:
            if not current_node.data.startswith(first_letter):
                word_updated = remove_chars(current_node.data)
                
                print(word_updated, end="")
                if current_node.next:
                    print(" <=> ", end="")
            current_node = current_node.next
        print(" => None")
    else:
        print("No words found in the text.")

# Виконання завдання за допомогою масива

def show_text_with_condition_array(text: str):
    words = text.split()
    if not words:
        print("No words found in the text.")
        return
    
    words_filtered = []
    first_letter = words[0][0].lower()
    for word in words:
        if not word.startswith(first_letter):
            word_updated = remove_chars(word)
            if not word_updated.isalpha():
                raise ValueError("Wrong format: '{}'".format(word_updated))
            words_filtered.append(word_updated)

    for word in words_filtered:
        print(word, end=" ")


text = input("Введіть текст: ")
print("-------------")
print("Результат обробки тексту з допомогою dll")

dll_text = text_to_dll(text)
if dll_text:
    print("Повний текст у вигляді dll:")
    dll_text.display_forward()

print("Оброблений текст у вигляді dll:")
show_text_with_condition(dll_text)

print("-------------")

print("Результат обробки тексту з допомогою массиву:")
show_text_with_condition_array(text)

print("\n-------------")

# low turn measure hand balloon taste living lowly rob.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def is_empty(self):
        return self.head is None
    
    def add_node(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

def remove_chars(word):
    return ''.join(char for char in word if char not in 'ab')

def print_words_starting_with_different_letter(text):
    words = text.split()
    if not words:
        print("No words found in the text.")
        return

    dll = DoubleLinkedList()
    first_word = words[0]
    start_letter = first_word[0].lower()

    for word in words:
        if not word.isalpha():
            print("Wrong format")
            return
        elif word[0].lower() != start_letter:
            dll.add_node(remove_chars(word))

    current_node = dll.head
    while current_node:
        print(current_node.data)
        current_node = current_node.next

def print_words_starting_with_different_letter_array(text):
    words = text.split()
    if not words:
        print("No words found in the text.")
        return
    
    words_filtered = []
    first_word = words[0]
    start_letter = first_word[0].lower()
    for word in words:
        if not word.isalpha():
            print("Wrong format")
            return
        elif word[0].lower() != start_letter:
            words_filtered.append(remove_chars(word))

    for word in words_filtered:
        print(word)

# Приймати текст з клавіатури
text = input("Введіть текст: ")
print("Результат linkedlist:")
print_words_starting_with_different_letter(text)
print("Результат array:")
print_words_starting_with_different_letter_array(text)

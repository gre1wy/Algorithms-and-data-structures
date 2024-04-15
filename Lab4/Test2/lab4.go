package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// Queue представляє кільцеву чергу на основі масива або звичайну чергу на основі звязного списка
type Queue interface {
	Enqueue(item interface{})
	Dequeue() interface{}
	IsEmpty() bool
	Size() int
	Front() interface{}
	Rear() interface{}
	Display()
}

// CircularArrayQueue представляє кільцеву чергу на основі масива
type CircularArrayQueue struct {
	items    []interface{}
	size     int // Теперішній розмір
	capacity int // Максимальний розмір
	head     int // Індекс початку черги
	tail     int // Індекс кінця черги
}

// NewCircularArrayQueue функція конструктор
func NewCircularArrayQueue(capacity int) *CircularArrayQueue {
	return &CircularArrayQueue{
		items:    make([]interface{}, capacity),
		capacity: capacity,
		size:     0,
		head:     0,
		tail:     0,
	}
}

// Enqueue додає елемент в кінець черги
func (q *CircularArrayQueue) Enqueue(item interface{}) {
	if q.IsFull() {
		fmt.Println("Queue is full")
		return
	}
	q.items[q.tail] = item
	q.tail = (q.tail + 1) % q.capacity
	q.size++
}

// Dequeue видаляє и повертає елемент з початку черги
func (q *CircularArrayQueue) Dequeue() interface{} {
	if q.IsEmpty() {
		fmt.Println("Queue is empty")
		return nil
	}
	item := q.items[q.head]
	q.head = (q.head + 1) % q.capacity
	q.size--
	return item
}

// IsEmpty повертає true, якщо черга пуста
func (q *CircularArrayQueue) IsEmpty() bool {
	return q.size == 0
}

// IsFull повертає true, якшо черга заповнена
func (q *CircularArrayQueue) IsFull() bool {
	return q.size == q.capacity
}

// Size повертає поточний розмір черги
func (q *CircularArrayQueue) Size() int {
	return q.size
}

// Front повертає елемент в початку черги без його видалення
func (q *CircularArrayQueue) Front() interface{} {
	if q.IsEmpty() {
		fmt.Println("Queue is empty")
		return nil
	}
	return q.items[q.head]
}

// Rear повертає елемент в кінці черги без його видалення
func (q *CircularArrayQueue) Rear() interface{} {
	if q.IsEmpty() {
		fmt.Println("Queue is empty")
		return nil
	}
	return q.items[(q.tail-1+q.capacity)%q.capacity]
}

// Display відображає поточний стан черги
func (q *CircularArrayQueue) Display() {
	if q.IsEmpty() {
		fmt.Println("Queue is empty")
		return
	}
	fmt.Println("Current Queue:")
	i := q.head
	for {
		fmt.Printf("%v ", q.items[i])
		i = (i + 1) % q.capacity
		if i == q.tail {
			break
		}
	}
	fmt.Println()
}

// Node представляє вузол для звязного списку
type Node struct {
	data interface{}
	next *Node
}

// LinkedListQueue представляє чергу на основі звязного списку
type LinkedListQueue struct {
	front *Node
	rear  *Node
	size  int
}

// NewLinkedListQueue функція генератор
func NewLinkedListQueue() *LinkedListQueue {
	return &LinkedListQueue{}
}

// Enqueue додає елемент в кінець черги
func (q *LinkedListQueue) Enqueue(item interface{}) {
	newNode := &Node{data: item, next: nil}

	if q.rear == nil {
		q.front = newNode
		q.rear = newNode
	} else {
		q.rear.next = newNode
		q.rear = newNode
	}
	q.size++
}

// Dequeue видаляє и повертає елемент з початку черги
func (q *LinkedListQueue) Dequeue() interface{} {
	if q.IsEmpty() {
		fmt.Println("Queue is empty")
		return nil
	}
	item := q.front.data
	q.front = q.front.next
	if q.front == nil {
		q.rear = nil
	}
	q.size--
	return item
}

// IsEmpty повертає true, якщо черга пуста
func (q *LinkedListQueue) IsEmpty() bool {
	return q.size == 0
}

// Size повертає поточний розмір черги
func (q *LinkedListQueue) Size() int {
	return q.size
}

// Front повертає елемент в початку черги без його видалення
func (q *LinkedListQueue) Front() interface{} {
	if q.IsEmpty() {
		fmt.Println("Queue is empty")
		return nil
	}
	return q.front.data
}

// Rear повертає елемент в кінці черги без його видалення
func (q *LinkedListQueue) Rear() interface{} {
	if q.IsEmpty() {
		fmt.Println("Queue is empty")
		return nil
	}
	return q.rear.data
}

// Display відображає поточний стан черги
func (q *LinkedListQueue) Display() {
	if q.IsEmpty() {
		fmt.Println("Queue is empty")
		return
	}

	current := q.front
	fmt.Print("Current Queue: ")
	for current != nil {
		fmt.Printf("%v ", current.data)
		current = current.next
	}
	fmt.Println()
}

// Фабрика черг
func getQueue(queueType string) (Queue, error) {
	switch queueType {
	case "LinkedListQueue":
		return NewLinkedListQueue(), nil

	case "CircularArrayQueue":
		reader := bufio.NewReader(os.Stdin)
		fmt.Println("Вкажіть розмір кільцевої черги(додатнє число):")
		s, _ := reader.ReadString('\n')
		s = strings.TrimSpace(s)
		limit, err := strconv.ParseInt(s, 10, 0)
		if err != nil || limit < 0 {
			fmt.Println("Неправильний формат розміру. Введіть натуральне число.")
			userInteraction()
		}
		return NewCircularArrayQueue(int(limit)), nil
	}
	return nil, fmt.Errorf("Wrong gun type passed")
}

func userInteraction() {
	var queue Queue

	reader := bufio.NewReader(os.Stdin)

	fmt.Println("Виберіть структуру для реалізації черги:")
	fmt.Println("1 - Масив (кільцева черга)")
	fmt.Println("2 - Звязний список")
	fmt.Println("0 - Для виходу")

	choice, _ := reader.ReadString('\n')
	choice = strings.TrimSpace(choice)

	switch choice {
	case "1":
		queue, _ = getQueue("CircularArrayQueue")
	case "2":
		queue, _ = getQueue("LinkedListQueue")
	case "0":
		os.Exit(0)
	default:
		fmt.Println("Неправильний вибір операції. Введіть 1-2, або 0 для того щоб вийти.")
		userInteraction()
	}

	for {
		fmt.Println("\nВиберіть операцію (напишіть тільки число):")
		fmt.Println("1 - Enqueue (Додати елемент в чергу);")
		fmt.Println("2 - Dequeue (Видалити елемент з черги);")
		fmt.Println("3 - IsEmpty (Перевірити чи черга пуста);")
		fmt.Println("4 - Display (показати чергу);")
		fmt.Println("5 - Front (показати елемент в початку черги);")
		fmt.Println("6 - Rear (показати елемент в кінці черги);")
		fmt.Println("7 - Size (показати поточний розмір черги);")
		fmt.Println("0 - Вийти.")

		operation, _ := reader.ReadString('\n')
		operation = strings.TrimSpace(operation)

		switch operation {
		case "1":
			fmt.Println("Введіть елемент для вставки в чергу:")
			fmt.Println("Для відміни вставки напишіть 'cancel'")
			itemInput, _ := reader.ReadString('\n')
			itemInput = strings.TrimSpace(itemInput)

			if itemInput == "cancel" {
				return
			}

			queue.Enqueue(itemInput)

		case "2":
			item := queue.Dequeue()
			if item == nil {
				fmt.Println("Черга і так порожня.")
			} else {
				fmt.Println("Видалений елемент:", item)
			}

		case "3":
			if queue.IsEmpty() {
				fmt.Println("Черга порожня.")
			} else {
				fmt.Println("Черга не порожня.")
			}

		case "4":
			queue.Display()

		case "5":
			fmt.Println("Елемент на початку черги:", queue.Front())

		case "6":
			fmt.Println("Елемент вкінці черги:", queue.Rear())

		case "7":
			fmt.Println("Поточний розмір черги:", queue.Size())

		case "0":
			return

		default:
			fmt.Println("Неправильний вибір операції. Введіть 1-7, або 0 для того щоб вийти")
		}
	}
}

func main() {
	userInteraction()
}

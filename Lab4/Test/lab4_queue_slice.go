package main

import "fmt"

// RingQueue представляет кольцевую очередь
type RingQueue struct {
	items    []interface{} // Теперь тип элементов - пустой интерфейс
	size     int
	capacity int
	head     int // Индекс начала очереди
	tail     int // Индекс конца очереди
}

// NewRingQueue создает новую кольцевую очередь заданного размера
func NewRingQueue(capacity int) *RingQueue {
	return &RingQueue{
		items:    make([]interface{}, capacity),
		capacity: capacity,
		size:     0,
		head:     0,
		tail:     0,
	}
}

// Enqueue добавляет элемент в конец очереди
func (q *RingQueue) Enqueue(item interface{}) {
	if q.size == q.capacity {
		fmt.Println("Queue is full")
		return
	}
	q.items[q.tail] = item
	q.tail = (q.tail + 1) % q.capacity
	q.size++
}

// Dequeue удаляет элемент из начала очереди и возвращает его
func (q *RingQueue) Dequeue() interface{} {
	if q.size == 0 {
		fmt.Println("Queue is empty")
		return nil // Возвращаем nil, если очередь пуста
	}
	item := q.items[q.head]
	q.head = (q.head + 1) % q.capacity
	q.size--
	return item
}

// IsEmpty возвращает true, если очередь пуста
func (q *RingQueue) IsEmpty() bool {
	return q.size == 0
}

// IsFull возвращает true, если очередь заполнена
func (q *RingQueue) IsFull() bool {
	return q.size == q.capacity
}

func (q *RingQueue) Display() {
	if q.IsEmpty() {
		fmt.Println("Queue is empty")
		return
	}
	fmt.Println("Current Queue:")
	i := q.head
	for {
		fmt.Printf("%v ", q.items[i]) // Используем %v для форматирования любого типа
		i = (i + 1) % q.capacity
		if i == q.tail {
			break
		}
	}
	fmt.Println()
}

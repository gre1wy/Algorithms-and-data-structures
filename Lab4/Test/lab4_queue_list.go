package main

import "fmt"

// Node представляет узел в связанном списке
type Node struct {
	data interface{}
	next *Node
}

// Queue представляет очередь, основанную на связанном списке
type Queue struct {
	front *Node
	rear  *Node
	size  int
}

// NewQueue создает новую пустую очередь
func NewQueue() *Queue {
	return &Queue{}
}

// Enqueue добавляет элемент в конец очереди
func (q *Queue) Enqueue(item interface{}) {
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

// Dequeue удаляет и возвращает элемент из начала очереди
func (q *Queue) Dequeue() interface{} {
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

// IsEmpty возвращает true, если очередь пуста
func (q *Queue) IsEmpty() bool {
	return q.size == 0
}

// Size возвращает количество элементов в очереди
func (q *Queue) Size() int {
	return q.size
}

// Front возвращает элемент в начале очереди без удаления
func (q *Queue) Front() interface{} {
	if q.IsEmpty() {
		fmt.Println("Queue is empty")
		return nil
	}
	return q.front.data
}

// Rear возвращает элемент в конце очереди без удаления
func (q *Queue) Rear() interface{} {
	if q.IsEmpty() {
		fmt.Println("Queue is empty")
		return nil
	}
	return q.rear.data
}

package main

import (
	"testing"
)

func TestNewCircularArrayQueue(t *testing.T) {
	tests := []struct {
		name     string
		capacity int
	}{
		{"Capacity 0", 0},
		{"Positive Capacity", 5},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := NewCircularArrayQueue(tt.capacity)
			if got == nil {
				t.Errorf("NewCircularArrayQueue() returned nil for capacity %d", tt.capacity)
				return
			}
			if got.capacity != tt.capacity {
				t.Errorf("NewCircularArrayQueue() created queue with capacity %d, want %d", got.capacity, tt.capacity)
			}
			if got.size != 0 {
				t.Errorf("NewCircularArrayQueue() created queue with size %d, want 0", got.size)
			}
			if got.head != 0 {
				t.Errorf("NewCircularArrayQueue() created queue with head %d, want 0", got.head)
			}
			if got.tail != 0 {
				t.Errorf("NewCircularArrayQueue() created queue with tail %d, want 0", got.tail)
			}
		})
	}
}

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

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

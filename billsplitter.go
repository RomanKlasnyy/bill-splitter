package main

import (
	"fmt"
	"math"
	"math/rand"
	"time"
)

func main() {
	rand.NewSource(time.Now().UnixNano())

	friends := make(map[string]float64)
	luckyFeature := false
	var lucky string

	fmt.Println("Enter the number of friends joining (including you):")
	var num int
	fmt.Scan(&num)
	fmt.Println()

	if num > 0 {
		fmt.Println("Enter the name of every friend (including you), each on a new line:")
		for i := 0; i < num; i++ {
			var friend string
			fmt.Scan(&friend)
			friends[friend] = 0
		}
		fmt.Println()
		fmt.Println("Enter the total bill value:")
		var bill float64
		fmt.Scan(&bill)
		fmt.Println()
		fmt.Println("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
		var answer string
		fmt.Scan(&answer)
		if answer == "Yes" || answer == "yes" {
			fmt.Println()
			lucky = getRandomFriend(friends)
			fmt.Printf("%s is the lucky one!\n", lucky)
			luckyFeature = true
		} else {
			fmt.Println()
			fmt.Println("No one is going to be lucky")
		}
		var price float64
		if luckyFeature {
			price = round(bill/float64(len(friends)-1), 2)
		} else {
			price = round(bill/float64(len(friends)), 2)
		}
		fmt.Println()
		for friend, debt := range friends {
			if friend != lucky {
				friends[friend] = debt + price
			}
		}
		fmt.Println(friends)
	} else {
		fmt.Println("No one is joining for the party")
	}
}

func round(num float64, decimalPlaces int) float64 {
	precision := math.Pow(10, float64(decimalPlaces))
	return math.Round(num*precision) / precision
}

func getRandomFriend(friends map[string]float64) string {
	keys := make([]string, 0, len(friends))
	for key := range friends {
		keys = append(keys, key)
	}
	return keys[rand.Intn(len(keys))]
}


package main

import (
	"fmt"
	"sort"
)

func main() {

	// TODO: Sort the following slice of strings
	strs := []string{"c", "a", "b"}

	// TODO: Sort the following slice of integers
	ints := []int{7, 2, 4}

	// TODO: Use the sort.IntsAreSorted() function to check if the following slice of integers is already sorted
	s := sort.IntsAreSorted(ints)

	fmt.Println("Strings:", strs)
	fmt.Println("Ints:   ", ints)
	fmt.Println("Sorted: ", s)
}

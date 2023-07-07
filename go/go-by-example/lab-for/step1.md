# `for`

The code below contains different types of `for` loops. However, some parts of the code are incomplete, and you need to fill in the blanks to make the code work correctly.

- Basic knowledge of Golang syntax
- Familiarity with `for` loops in Golang

```sh
$ go run for.go
1
2
3
7
8
9
loop
1
3
5

# We'll see some other `for` forms later when we look at
# `range` statements, channels, and other data
# structures.
```

There is the full code below:

```go
// `for` is Go's only looping construct. Here are
// some basic types of `for` loops.

package main

import "fmt"

func main() {

	// The most basic type, with a single condition.
	i := 1
	for i <= 3 {
		fmt.Println(i)
		i = i + 1
	}

	// A classic initial/condition/after `for` loop.
	for j := 7; j <= 9; j++ {
		fmt.Println(j)
	}

	// `for` without a condition will loop repeatedly
	// until you `break` out of the loop or `return` from
	// the enclosing function.
	for {
		fmt.Println("loop")
		break
	}

	// You can also `continue` to the next iteration of
	// the loop.
	for n := 0; n <= 5; n++ {
		if n%2 == 0 {
			continue
		}
		fmt.Println(n)
	}
}

```

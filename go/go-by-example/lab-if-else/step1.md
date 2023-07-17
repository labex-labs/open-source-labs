# if-else

You are required to complete the `checkNumber` function that takes an integer as input and returns a string. If the number is even, return "even", otherwise return "odd".

- The function should be named `checkNumber`.
- The function should take an integer as input.
- The function should return a string.
- If the number is even, return "even".
- If the number is odd, return "odd".

```sh
$ go run if-else.go
7 is odd
8 is divisible by 4
9 has 1 digit

# There is no [ternary if](https://en.wikipedia.org/wiki/%3F:)
# in Go, so you'll need to use a full `if` statement even
# for basic conditions.
```

There is the full code below:

```go
// Branching with `if` and `else` in Go is
// straight-forward.

package main

import "fmt"

func main() {

	// Here's a basic example.
	if 7%2 == 0 {
		fmt.Println("7 is even")
	} else {
		fmt.Println("7 is odd")
	}

	// You can have an `if` statement without an else.
	if 8%4 == 0 {
		fmt.Println("8 is divisible by 4")
	}

	// A statement can precede conditionals; any variables
	// declared in this statement are available in the current
	// and all subsequent branches.
	if num := 9; num < 0 {
		fmt.Println(num, "is negative")
	} else if num < 10 {
		fmt.Println(num, "has 1 digit")
	} else {
		fmt.Println(num, "has multiple digits")
	}
}

// Note that you don't need parentheses around conditions
// in Go, but that the braces are required.

```

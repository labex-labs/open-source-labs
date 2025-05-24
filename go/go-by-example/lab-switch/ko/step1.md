# Switch (스위치)

이 랩에서는 입력 값에 따라 해당 메시지를 출력하기 위해 `switch` 문을 완성해야 합니다.

- 문제를 해결하기 위해 `switch` 문을 사용해야 합니다.
- 예상치 못한 입력 값을 처리하기 위해 `default` 케이스를 사용해야 합니다.

```sh
$ go run switch.go
Write 2 as two
It's a weekday
It's after noon
I'm a bool
I'm an int
Don't know type string

```

전체 코드는 다음과 같습니다.

```go
// _Switch statements_ express conditionals across many
// branches.

package main

import (
	"fmt"
	"time"
)

func main() {

	// Here's a basic `switch`.
	i := 2
	fmt.Print("Write ", i, " as ")
	switch i {
	case 1:
		fmt.Println("one")
	case 2:
		fmt.Println("two")
	case 3:
		fmt.Println("three")
	}

	// You can use commas to separate multiple expressions
	// in the same `case` statement. We use the optional
	// `default` case in this example as well.
	switch time.Now().Weekday() {
	case time.Saturday, time.Sunday:
		fmt.Println("It's the weekend")
	default:
		fmt.Println("It's a weekday")
	}

	// `switch` without an expression is an alternate way
	// to express if/else logic. Here we also show how the
	// `case` expressions can be non-constants.
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("It's before noon")
	default:
		fmt.Println("It's after noon")
	}

	// A type `switch` compares types instead of values.  You
	// can use this to discover the type of an interface
	// value.  In this example, the variable `t` will have the
	// type corresponding to its clause.
	whatAmI := func(i interface{}) {
		switch t := i.(type) {
		case bool:
			fmt.Println("I'm a bool")
		case int:
			fmt.Println("I'm an int")
		default:
			fmt.Printf("Don't know type %T\n", t)
		}
	}
	whatAmI(true)
	whatAmI(1)
	whatAmI("hey")
}
```

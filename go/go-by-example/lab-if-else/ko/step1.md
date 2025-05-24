# if-else

정수를 입력으로 받아 문자열을 반환하는 `checkNumber` 함수를 완성해야 합니다. 숫자가 짝수이면 "even"을 반환하고, 그렇지 않으면 "odd"를 반환합니다.

- 함수 이름은 `checkNumber`여야 합니다.
- 함수는 정수를 입력으로 받아야 합니다.
- 함수는 문자열을 반환해야 합니다.
- 숫자가 짝수이면 "even"을 반환합니다.
- 숫자가 홀수이면 "odd"를 반환합니다.

```sh
$ go run if-else.go
7 is odd
8 is divisible by 4
9 has 1 digit

# Go 에는 [삼항 연산자 (ternary if)](https://en.wikipedia.org/wiki/%3F:) 가 없으므로,
# 기본적인 조건에도 전체 `if` 문을 사용해야 합니다.
```

전체 코드는 다음과 같습니다.

```go
// Go 에서 `if` 와 `else` 를 사용한 분기는
// 간단합니다.

package main

import "fmt"

func main() {

	// 기본적인 예시입니다.
	if 7%2 == 0 {
		fmt.Println("7 is even")
	} else {
		fmt.Println("7 is odd")
	}

	// `else` 없이 `if` 문을 사용할 수 있습니다.
	if 8%4 == 0 {
		fmt.Println("8 is divisible by 4")
	}

	// 조건문 앞에 문장을 둘 수 있습니다; 이 문장에서 선언된 모든 변수는 현재
	// 및 모든 후속 분기에서 사용할 수 있습니다.
	if num := 9; num < 0 {
		fmt.Println(num, "is negative")
	} else if num < 10 {
		fmt.Println(num, "has 1 digit")
	} else {
		fmt.Println(num, "has multiple digits")
	}
}

// Go 에서는 조건 주위에 괄호가 필요하지 않지만, 중괄호는 필수입니다.
```

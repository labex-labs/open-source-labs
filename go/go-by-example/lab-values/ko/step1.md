# 값 타입 (Value Types)

두 개의 정수를 입력받아 합과 곱을 반환하는 `calculate` 함수를 완성하는 것이 과제입니다.

- `calculate` 함수는 두 개의 정수를 매개변수로 받아야 합니다.
- `calculate` 함수는 입력 매개변수의 합과 곱, 두 개의 정수를 반환해야 합니다.

```sh
$ go run values.go
golang
1+1 = 2
7.0/3.0 = 2.3333333333333335
false
true
false
```

전체 코드는 다음과 같습니다.

```go
// Go 는 문자열, 정수, 부동 소수점 숫자, 부울 (boolean) 등 다양한 값 타입을 가지고 있습니다. 다음은 몇 가지 기본 예시입니다.

package main

import "fmt"

func main() {

	// 문자열은 `+` 연산자를 사용하여 더할 수 있습니다.
	fmt.Println("go" + "lang")

	// 정수와 부동 소수점 숫자.
	fmt.Println("1+1 =", 1+1)
	fmt.Println("7.0/3.0 =", 7.0/3.0)

	// 부울 (boolean), 예상대로 부울 연산자를 사용합니다.
	fmt.Println(true && false)
	fmt.Println(true || false)
	fmt.Println(!true)
}
```

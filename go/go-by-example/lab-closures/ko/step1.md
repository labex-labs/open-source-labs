# 클로저 (Closures)

다른 함수를 반환하는 함수를 만들어야 합니다. 반환된 함수는 호출될 때마다 변수를 1 씩 증가시켜야 합니다. 변수는 반환된 각 함수에 고유해야 합니다.

- 함수 `intSeq`는 다른 함수를 반환해야 합니다.
- 반환된 함수는 호출될 때마다 변수를 1 씩 증가시켜야 합니다.
- 변수는 반환된 각 함수에 고유해야 합니다.

```sh
$ go run closures.go
1
2
3
1

# The last feature of functions we'll look at for now is
# recursion.
```

전체 코드는 다음과 같습니다.

```go
// Go 는 [_익명 함수_](https://en.wikipedia.org/wiki/Anonymous_function) 를 지원하며,
// 이를 통해 <a href="https://en.wikipedia.org/wiki/Closure_(computer_science)"><em>클로저</em></a>를 형성할 수 있습니다.
// 익명 함수는 이름을 지정하지 않고
// 함수를 인라인으로 정의하려는 경우 유용합니다.

package main

import "fmt"

// 이 함수 `intSeq` 는 `intSeq` 의 본문에서 익명으로 정의하는
// 다른 함수를 반환합니다. 반환된 함수는 변수 `i` 를 _클로징_하여
// 클로저를 형성합니다.
func intSeq() func() int {
	i := 0
	return func() int {
		i++
		return i
	}
}

func main() {

	// `intSeq` 를 호출하여 결과 (함수) 를
	// `nextInt` 에 할당합니다. 이 함수 값은
	// 자체 `i` 값을 캡처하며, 이는
	// `nextInt` 를 호출할 때마다 업데이트됩니다.
	nextInt := intSeq()

	// `nextInt` 를 몇 번 호출하여 클로저의 효과를 확인합니다.
	fmt.Println(nextInt())
	fmt.Println(nextInt())
	fmt.Println(nextInt())

	// 상태가 해당
	// 특정 함수에 고유한지 확인하려면 새 함수를 만들고 테스트합니다.
	newInts := intSeq()
	fmt.Println(newInts())
}
```

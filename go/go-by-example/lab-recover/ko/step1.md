# Recover (복구)

제공된 코드의 `mayPanic` 함수는 호출 시 패닉 (panic) 을 발생시킵니다. 여러분의 과제는 `main` 함수를 수정하여 패닉으로부터 복구하고 오류 메시지를 출력하는 것입니다.

- `recover` 함수를 사용하여 `mayPanic` 함수에서 패닉을 처리하십시오.
- 패닉이 발생하면 오류 메시지를 출력하십시오.

```sh
$ go run recover.go
Recovered. Error:
a problem
```

전체 코드는 다음과 같습니다.

```go
// Go 는 `recover` 내장 함수를 사용하여 패닉으로부터 _복구_하는 것을 가능하게 합니다. `recover` 는
// `panic` 이 프로그램을 중단시키는 것을 막고 대신 실행을 계속할 수 있도록 합니다.

// 이것이 유용할 수 있는 예: 서버는 클라이언트 연결 중 하나에서
// 치명적인 오류가 발생하더라도 충돌하고 싶어하지 않을 것입니다. 대신, 서버는
// 해당 연결을 닫고 다른 클라이언트를 계속 서비스하고 싶어할 것입니다. 실제로, 이것이 Go 의 `net/http` 가
// HTTP 서버에 대해 기본적으로 수행하는 것입니다.

package main

import "fmt"

// 이 함수는 패닉을 발생시킵니다.
func mayPanic() {
	panic("a problem")
}

func main() {
	// `recover` 는 defered 함수 내에서 호출되어야 합니다.
	// 래핑 함수가 패닉을 발생시키면 defer 가
	// 활성화되고 그 안의 `recover` 호출이
	// 패닉을 잡습니다.
	defer func() {
		if r := recover(); r != nil {
			// `recover` 의 반환 값은 `panic` 호출에서 발생한 오류입니다.
			fmt.Println("Recovered. Error:\n", r)
		}
	}()

	mayPanic()

	// 이 코드는 `mayPanic` 이 패닉을 발생시키기 때문에 실행되지 않습니다.
	// `main` 의 실행은 패닉 지점에서 중단되고
	// defered 클로저에서 재개됩니다.
	fmt.Println("After mayPanic()")
}
```

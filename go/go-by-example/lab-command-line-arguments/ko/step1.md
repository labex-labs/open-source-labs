# 명령줄 인자 (Command-line arguments)

현재 프로그램은 프로그램에 전달된 원시 명령줄 인자를 출력합니다. 하지만, 인덱스에 따라 특정 인자를 출력하도록 수정해야 합니다.

- Golang 에 대한 기본적인 지식
- 명령줄 인자에 대한 익숙함

```sh
# 명령줄 인자를 실험하려면 먼저
# `go build`로 바이너리를 빌드하는 것이 좋습니다.
$ go build command-line-arguments.go
$ ./command-line-arguments a b c d
[./command-line-arguments a b c d]
[a b c d]
c

# 다음으로 플래그를 사용하여
# 더 발전된 명령줄 처리를 살펴보겠습니다.
```

전체 코드는 다음과 같습니다.

```go
// [_명령줄 인자_](https://en.wikipedia.org/wiki/Command-line_interface#Arguments)
//는 프로그램 실행을 매개변수화하는 일반적인 방법입니다.
// 예를 들어, `go run hello.go`는 `go` 프로그램에 대한
// `run` 및 `hello.go` 인자를 사용합니다.

package main

import (
	"fmt"
	"os"
)

func main() {

	// `os.Args` 는 원시 명령줄
	// 인자에 대한 접근을 제공합니다. 이 슬라이스의 첫 번째 값은
	// 프로그램의 경로이고, `os.Args[1:]` 는
	// 프로그램에 대한 인자를 포함합니다.
	argsWithProg := os.Args
	argsWithoutProg := os.Args[1:]

	// 일반적인 인덱싱으로 개별 인자를 얻을 수 있습니다.
	arg := os.Args[3]

	fmt.Println(argsWithProg)
	fmt.Println(argsWithoutProg)
	fmt.Println(arg)
}
```

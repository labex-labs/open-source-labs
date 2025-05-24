# Exit

이 lab 에서 해결해야 할 문제는 `os.Exit` 함수를 사용하여 특정 상태 코드로 Go 프로그램을 종료하는 것입니다.

이 lab 을 완료하려면 Go 프로그래밍과 `os` 패키지에 대한 기본적인 이해가 필요합니다.

```sh
#  `go run`을 사용하여 `exit.go` 를 실행하면 종료
# 상태가 `go` 에 의해 감지되어 출력됩니다.
$ go run exit.go
exit status 3

# 바이너리를 빌드하고 실행하면
# 터미널에서 상태를 확인할 수 있습니다.
$ go build exit.go
$ ./exit
$ echo $?
3

# 프로그램의 `!` 는 출력되지 않습니다.
```

전체 코드는 다음과 같습니다.

```go
// `os.Exit` 를 사용하여 주어진
// 상태로 즉시 종료합니다.

package main

import (
	"fmt"
	"os"
)

func main() {

	// `os.Exit` 를 사용하면 `defer` 가 실행되지 않으므로,
	// 이 `fmt.Println` 은 호출되지 않습니다.
	defer fmt.Println("!")

	// 상태 3 으로 종료합니다.
	os.Exit(3)
}

// 예를 들어 C 와 달리 Go 는 정수를 사용하지 않습니다.
// `main` 에서 반환 값을 사용하여 종료 상태를 나타냅니다.
// 0 이 아닌 상태로 종료하려면
// `os.Exit` 를 사용해야 합니다.
```

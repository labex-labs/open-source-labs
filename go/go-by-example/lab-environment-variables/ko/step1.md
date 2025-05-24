# 환경 변수 (Environment Variables)

이 랩에서는 환경 변수를 설정, 가져오기 및 나열해야 합니다.

- `os.Setenv`를 사용하여 키/값 쌍을 설정합니다.
- `os.Getenv`를 사용하여 키에 대한 값을 가져옵니다.
- `os.Environ`을 사용하여 환경의 모든 키/값 쌍을 나열합니다.
- `strings.SplitN`을 사용하여 키와 값을 분할합니다.

```sh
# 프로그램을 실행하면 프로그램에서 설정한 `FOO` 의 값을 가져오지만,
# `BAR` 는 비어 있음을 알 수 있습니다.
$ go run environment-variables.go
FOO: 1
BAR:

# 환경의 키 목록은 사용자의
# 특정 머신에 따라 달라집니다.
TERM_PROGRAM
PATH
SHELL
...
FOO

# 먼저 환경에서 `BAR` 를 설정하면 실행 중인
# 프로그램이 해당 값을 가져옵니다.
$ BAR=2 go run environment-variables.go
FOO: 1
BAR: 2
...
```

전체 코드는 다음과 같습니다.

```go
// [환경 변수](https://en.wikipedia.org/wiki/Environment_variable) 는 [구성 정보를
// Unix 프로그램에 전달하는](https://www.12factor.net/config) 보편적인 메커니즘입니다.
// 환경 변수를 설정, 가져오기 및 나열하는 방법을 살펴보겠습니다.

package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {

	// 키/값 쌍을 설정하려면 `os.Setenv` 를 사용합니다. 키에 대한
	// 값을 가져오려면 `os.Getenv` 를 사용합니다. 이 함수는
	// 키가 환경에 존재하지 않으면 빈 문자열을 반환합니다.
	os.Setenv("FOO", "1")
	fmt.Println("FOO:", os.Getenv("FOO"))
	fmt.Println("BAR:", os.Getenv("BAR"))

	// 환경의 모든 키/값 쌍을 나열하려면 `os.Environ` 을 사용합니다.
	// 이 함수는 `KEY=value` 형식의 문자열 슬라이스를 반환합니다.
	// `strings.SplitN` 을 사용하여 키와 값을 얻을 수 있습니다.
	// 여기서는 모든 키를 출력합니다.
	fmt.Println()
	for _, e := range os.Environ() {
		pair := strings.SplitN(e, "=", 2)
		fmt.Println(pair[0])
	}
}
```

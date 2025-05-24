# Line Filters (라인 필터)

이 랩에서 해결해야 할 문제는 stdin 에서 입력 텍스트를 읽고, 텍스트의 모든 문자를 대문자로 변환한 다음, 수정된 텍스트를 stdout 으로 출력하는 Go 프로그램을 작성하는 것입니다.

- 프로그램은 stdin 에서 입력 텍스트를 읽어야 합니다.
- 프로그램은 입력 텍스트의 모든 문자를 대문자로 변환해야 합니다.
- 프로그램은 수정된 텍스트를 stdout 으로 출력해야 합니다.

```sh
# 라인 필터를 사용해 보려면 먼저 몇 줄의
# 소문자 텍스트가 있는 파일을 만듭니다.
$ echo 'hello' > /tmp/lines
$ echo 'filter' >> /tmp/lines

# 그런 다음 라인 필터를 사용하여 대문자 텍스트를 얻습니다.
$ cat /tmp/lines | go run line-filters.go
HELLO
FILTER
```

전체 코드는 다음과 같습니다.

```go
// _line filter_ (라인 필터) 는 stdin 에서 입력을 읽고, 처리한 다음,
// 파생된 결과를 stdout 으로 출력하는 일반적인 유형의 프로그램입니다.
// `grep` 과 `sed` 는 일반적인 라인 필터입니다.

// 다음은 모든 입력 텍스트의 대문자 버전을 쓰는 Go 의 라인 필터 예제입니다.
// 이 패턴을 사용하여 자신만의 Go 라인 필터를 작성할 수 있습니다.
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {

	// 버퍼링되지 않은 `os.Stdin` 을 버퍼링된
	// 스캐너로 래핑하면 다음 토큰으로 스캐너를 이동시키는 편리한 `Scan` 메서드를 사용할 수 있습니다.
	// 기본 스캐너에서 다음 줄입니다.
	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		// `Text` 는 현재 토큰, 여기서는 다음 줄을 반환합니다.
		// 입력에서.
		ucl := strings.ToUpper(scanner.Text())

		// 대문자로 변환된 줄을 출력합니다.
		fmt.Println(ucl)
	}

	// `Scan` 중에 오류가 있는지 확인합니다. 파일의 끝은
	// 예상되며 `Scan` 에서 오류로 보고되지 않습니다.
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, "error:", err)
		os.Exit(1)
	}
}
```

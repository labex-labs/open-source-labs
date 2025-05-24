# 명령줄 플래그 (Command-line flags)

명령줄 플래그를 파싱하고 파싱된 옵션과 후행 위치 인수를 출력하는 Golang 프로그램을 구현합니다. 이 프로그램은 다음 플래그를 지원해야 합니다.

- `word`: 기본값이 `"foo"`인 문자열 플래그.
- `numb`: 기본값이 `42`인 정수 플래그.
- `fork`: 기본값이 `false`인 부울 플래그.
- `svar`: 프로그램의 다른 곳에서 선언된 기존 변수를 사용하는 문자열 플래그.

- 프로그램은 `flag` 패키지를 사용하여 명령줄 플래그를 파싱해야 합니다.
- 프로그램은 파싱된 옵션과 후행 위치 인수를 출력해야 합니다.
- 프로그램은 위에 설명된 대로 `word`, `numb`, `fork`, 및 `svar` 플래그를 지원해야 합니다.

```sh
# 명령줄 플래그 프로그램을 실험하려면
# 먼저 컴파일한 다음 결과
# 바이너리를 직접 실행하는 것이 가장 좋습니다.
$ go build command-line-flags.go

# 먼저 모든 플래그에 값을 제공하여
# 빌드된 프로그램을 사용해 보세요.
$ ./command-line-flags -word=opt -numb=7 -fork -svar=flag
word: opt
numb: 7
fork: true
svar: flag
tail: []

# 플래그를 생략하면 자동으로
# 기본값을 사용합니다.
$ ./command-line-flags -word=opt
word: opt
numb: 42
fork: false
svar: bar
tail: []

# 후행 위치 인수는
# 모든 플래그 뒤에 제공될 수 있습니다.
$ ./command-line-flags -word=opt a1 a2 a3
word: opt
...
tail: [a1 a2 a3]

# `flag` 패키지는 모든 플래그가
# 위치 인자 앞에 나타나야 합니다 (그렇지 않으면 플래그가
# 위치 인자로 해석됩니다).
$ ./command-line-flags -word=opt a1 a2 a3 -numb=7
word: opt
numb: 42
fork: false
svar: bar
tail: [a1 a2 a3 -numb=7]

# `-h` 또는 `--help` 플래그를 사용하여
# 명령줄 프로그램에 대한 자동 생성된 도움말 텍스트를 얻습니다.
$ ./command-line-flags -h
Usage of ./command-line-flags:
-fork=false: a bool
-numb=42: an int
-svar="bar": a string var
-word="foo": a string

# `flag` 패키지에 지정되지 않은 플래그를 제공하면
# 프로그램은 오류 메시지를 인쇄하고
# 도움말 텍스트를 다시 표시합니다.
$ ./command-line-flags -wat
flag provided but not defined: -wat
Usage of ./command-line-flags:
...
```

전체 코드는 다음과 같습니다.

```go
// [_Command-line flags_](https://en.wikipedia.org/wiki/Command-line_interface#Command-line_option)
// 는 명령줄에 대한 옵션을 지정하는 일반적인 방법입니다.
// 프로그램. 예를 들어, `wc -l`에서 `-l` 은
// 명령줄 플래그입니다.

package main

// Go 는 기본을 지원하는 `flag` 패키지를 제공합니다.
// 명령줄 플래그 파싱. 이 패키지를 사용하여
// 예제 명령줄 프로그램을 구현합니다.
import (
	"flag"
	"fmt"
)

func main() {

	// 문자열,
	// 정수 및 부울 옵션에 사용할 수 있는 기본 플래그 선언. 여기서는
	// 기본값 `"foo"` 인 문자열 플래그 `word` 를 선언합니다.
	// 그리고 짧은 설명. 이 `flag.String` 함수
	// 문자열 포인터 (문자열 값이 아님) 를 반환합니다.
	// 아래에서 이 포인터를 사용하는 방법을 살펴보겠습니다.
	wordPtr := flag.String("word", "foo", "a string")

	// 이것은 `numb` 및 `fork` 플래그를 선언하며,
	// `word` 플래그와 유사한 접근 방식을 사용합니다.
	numbPtr := flag.Int("numb", 42, "an int")
	forkPtr := flag.Bool("fork", false, "a bool")

	// 프로그램의 다른 곳에서 선언된
	// 기존 var 를 사용하는 옵션을 선언하는 것도 가능합니다.
	// 플래그를 가리키는 포인터를 전달해야 합니다.
	// 선언 함수.
	var svar string
	flag.StringVar(&svar, "svar", "bar", "a string var")

	// 모든 플래그가 선언되면 `flag.Parse()` 를 호출합니다.
	// 명령줄 파싱을 실행합니다.
	flag.Parse()

	// 여기서는 파싱된 옵션과
	// 후행 위치 인수를 덤프합니다. 참고로
	// `*wordPtr` 과 같은 포인터를 역참조해야 합니다.
	// 실제 옵션 값을 얻습니다.
	fmt.Println("word:", *wordPtr)
	fmt.Println("numb:", *numbPtr)
	fmt.Println("fork:", *forkPtr)
	fmt.Println("svar:", svar)
	fmt.Println("tail:", flag.Args())
}
```

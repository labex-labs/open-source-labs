# 문자열 서식 지정

Golang 에서 다양한 서식 지정 동사 (formatting verbs) 를 사용하여 다양한 유형의 데이터를 서식 지정해야 합니다.

- `fmt` 패키지를 사용하여 데이터를 서식 지정해야 합니다.
- 각 데이터 유형에 맞는 올바른 서식 지정 동사를 사용해야 합니다.
- 정수, 부동 소수점 숫자, 문자열 및 구조체 (struct) 를 서식 지정할 수 있어야 합니다.
- 출력의 너비와 정밀도를 제어할 수 있어야 합니다.
- 출력을 왼쪽 정렬 또는 오른쪽 정렬할 수 있어야 합니다.

```sh
$ go run string-formatting.go
struct1: {1 2}
struct2: {x:1 y:2}
struct3: main.point{x:1, y:2}
type: main.point
bool: true
int: 123
bin: 1110
char: !
hex: 1c8
float1: 78.900000
float2: 1.234000e+08
float3: 1.234000E+08
str1: "string"
str2: "\"string\""
str3: 6865782074686973
pointer: 0xc0000ba000
width1: | 12 | 345 \
  | width2: | 1.20 | 3.45 \
  | width3: | 1.20 | 3.45 \
  | width4: | foo | b \
  | width5: | foo | b \
  | sprintf: a string
io: an error
```

전체 코드는 다음과 같습니다.

```go
// Go 는 `printf` 전통에서 문자열 서식 지정을 훌륭하게 지원합니다. 다음은
// 일반적인 문자열 서식 지정 작업의 몇 가지 예입니다.

package main

import (
	"fmt"
	"os"
)

type point struct {
	x, y int
}

func main() {

	// Go 는 일반적인 Go 값을 서식 지정하도록 설계된 여러 인쇄 "동사"를 제공합니다. 예를 들어, 이것은
	// `point` 구조체의 인스턴스를 인쇄합니다.
	p := point{1, 2}
	fmt.Printf("struct1: %v\n", p)

	// 값이 구조체인 경우 `%+v` 변형은
	// 구조체의 필드 이름을 포함합니다.
	fmt.Printf("struct2: %+v\n", p)

	// `%#v` 변형은 값의 Go 구문 표현을 인쇄합니다. 즉, 해당 값을
	// 생성하는 소스 코드 조각입니다.
	fmt.Printf("struct3: %#v\n", p)

	// 값의 유형을 인쇄하려면 `%T` 를 사용하십시오.
	fmt.Printf("type: %T\n", p)

	// 부울 값 서식 지정은 간단합니다.
	fmt.Printf("bool: %t\n", true)

	// 정수를 서식 지정하는 데는 많은 옵션이 있습니다.
	// 표준, 10 진수 서식 지정에는 `%d` 를 사용하십시오.
	fmt.Printf("int: %d\n", 123)

	// 이것은 이진 표현을 인쇄합니다.
	fmt.Printf("bin: %b\n", 14)

	// 이것은 주어진 정수에 해당하는 문자를 인쇄합니다.
	fmt.Printf("char: %c\n", 33)

	// `%x` 는 16 진수 인코딩을 제공합니다.
	fmt.Printf("hex: %x\n", 456)

	// 부동 소수점 숫자에도 여러 서식 지정 옵션이 있습니다. 기본 10 진수 서식 지정에는 `%f` 를 사용하십시오.
	fmt.Printf("float1: %f\n", 78.9)

	// `%e` 및 `%E` 는 부동 소수점 숫자를 (약간
	// 다른 버전의) 과학적 표기법으로 서식 지정합니다.
	fmt.Printf("float2: %e\n", 123400000.0)
	fmt.Printf("float3: %E\n", 123400000.0)

	// 기본 문자열 인쇄에는 `%s` 를 사용하십시오.
	fmt.Printf("str1: %s\n", "\"string\"")

	// Go 소스에서와 같이 문자열을 이중 인용하려면 `%q` 를 사용하십시오.
	fmt.Printf("str2: %q\n", "\"string\"")

	// 앞에서 본 정수와 마찬가지로 `%x` 는
	// 문자열을 16 진수로 렌더링하며, 입력 바이트당 두 개의 출력 문자가 있습니다.
	fmt.Printf("str3: %x\n", "hex this")

	// 포인터의 표현을 인쇄하려면 `%p` 를 사용하십시오.
	fmt.Printf("pointer: %p\n", &p)

	// 숫자를 서식 지정할 때 결과
	// 숫자의 너비와 정밀도를 제어하려는 경우가 많습니다. 정수의 너비를 지정하려면
	// 동사에서 `%` 뒤에 숫자를 사용하십시오. 기본적으로
	// 결과는 오른쪽 정렬되고 공백으로 채워집니다.
	fmt.Printf("width1: |%6d|%6d|\n", 12, 345)

	// 인쇄된 부동 소수점 숫자의 너비를 지정할 수도 있습니다.
	// 일반적으로 너비와 함께 소수점 정밀도를 제한하려는 경우도 있습니다.
	// width.precision 구문.
	fmt.Printf("width2: |%6.2f|%6.2f|\n", 1.2, 3.45)

	// 왼쪽 정렬하려면 `-` 플래그를 사용하십시오.
	fmt.Printf("width3: |%-6.2f|%-6.2f|\n", 1.2, 3.45)

	// 특히 테이블과 같은 출력에서 정렬되도록 하려면 문자열을 서식 지정할 때 너비를 제어할 수도 있습니다. 기본 오른쪽 정렬 너비의 경우.
	fmt.Printf("width4: |%6s|%6s|\n", "foo", "b")

	// 왼쪽 정렬하려면 숫자와 마찬가지로 `-` 플래그를 사용하십시오.
	fmt.Printf("width5: |%-6s|%-6s|\n", "foo", "b")

	// 지금까지 `Printf` 를 보았습니다. `os.Stdout` 에 서식 지정된 문자열을 인쇄합니다. `Sprintf` 는
	// 인쇄하지 않고 문자열을 서식 지정하고 반환합니다.
	s := fmt.Sprintf("sprintf: a %s", "string")
	fmt.Println(s)

	// `Fprintf` 를 사용하여 `os.Stdout` 이외의 `io.Writers` 에 서식 지정 + 인쇄할 수 있습니다.
	fmt.Fprintf(os.Stderr, "io: an %s\n", "error")
}
```

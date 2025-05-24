# 정규 표현식 (Regular Expressions)

이 랩에서는 Golang 에서 다양한 정규 표현식 관련 작업을 수행하기 위한 코드를 완성해야 합니다.

- `regexp` 패키지를 사용하여 정규 표현식 관련 작업을 수행합니다.
- `MatchString`을 사용하여 패턴이 문자열과 일치하는지 테스트합니다.
- `Compile`을 사용하여 `Regexp` 구조체를 최적화합니다.
- `MatchString`을 사용하여 `Compile`과 유사하게 일치 여부를 테스트합니다.
- `FindString`을 사용하여 정규 표현식에 대한 일치를 찾습니다.
- `FindStringIndex`를 사용하여 첫 번째 일치를 찾고 일치하는 텍스트 대신 일치의 시작 및 끝 인덱스를 반환합니다.
- `FindStringSubmatch`를 사용하여 `p([a-z]+)ch`와 `([a-z]+)` 모두에 대한 정보를 반환합니다.
- `FindStringSubmatchIndex`를 사용하여 일치 및 하위 일치의 인덱스에 대한 정보를 반환합니다.
- `FindAllString`을 사용하여 정규 표현식에 대한 모든 일치를 찾습니다.
- `FindAllStringSubmatchIndex`를 사용하여 첫 번째 일치뿐만 아니라 입력의 모든 일치에 적용합니다.
- `Match`를 사용하여 `[]byte` 인수를 사용하여 일치 여부를 테스트하고 함수 이름에서 `String`을 제거합니다.
- `MustCompile`을 사용하여 정규 표현식으로 전역 변수를 생성합니다.
- `ReplaceAllString`을 사용하여 문자열의 하위 집합을 다른 값으로 바꿉니다.
- `ReplaceAllFunc`를 사용하여 주어진 함수로 일치하는 텍스트를 변환합니다.

```sh
# Go 정규 표현식에 대한 전체 참조는
# [`regexp`](https://pkg.go.dev/regexp) 패키지 문서를 확인하십시오.
```

전체 코드는 다음과 같습니다.

```go
// Go 는 [정규 표현식](https://en.wikipedia.org/wiki/Regular_expression) 에 대한 내장 지원을 제공합니다.
// 다음은 Go 에서 일반적인 regexp 관련 작업의 몇 가지 예입니다.

package main

import (
	"bytes"
	"fmt"
	"regexp"
)

func main() {

	// 이것은 패턴이 문자열과 일치하는지 테스트합니다.
	match, _ := regexp.MatchString("p([a-z]+)ch", "peach")
	fmt.Println(match)

	// 위에서는 문자열 패턴을 직접 사용했지만,
	// 다른 regexp 작업의 경우 `Regexp` 구조체를 `Compile` 해야 합니다.
	r, _ := regexp.Compile("p([a-z]+)ch")

	// 이러한 구조체에서 많은 메서드를 사용할 수 있습니다. 다음은
	// 앞에서 본 것과 같은 일치 테스트입니다.
	fmt.Println(r.MatchString("peach"))

	// 이것은 정규 표현식에 대한 일치를 찾습니다.
	fmt.Println(r.FindString("peach punch"))

	// 이것은 또한 첫 번째 일치를 찾지만
	// 일치하는 텍스트 대신 일치의 시작 및 끝 인덱스를 반환합니다.
	fmt.Println("idx:", r.FindStringIndex("peach punch"))

	// `Submatch` 변형은 전체 패턴 일치와
	// 해당 일치 내의 하위 일치에 대한 정보를 포함합니다. 예를 들어, 이것은
	// `p([a-z]+)ch` 와 `([a-z]+)` 모두에 대한 정보를 반환합니다.
	fmt.Println(r.FindStringSubmatch("peach punch"))

	// 마찬가지로 이것은 일치 및 하위 일치의
	// 인덱스에 대한 정보를 반환합니다.
	fmt.Println(r.FindStringSubmatchIndex("peach punch"))

	// 이러한 함수의 `All` 변형은
	// 첫 번째 일치뿐만 아니라 입력의 모든 일치에 적용됩니다. 예를 들어,
	// 정규 표현식에 대한 모든 일치를 찾습니다.
	fmt.Println(r.FindAllString("peach punch pinch", -1))

	// 이러한 `All` 변형은
	// 위에서 본 다른 함수에서도 사용할 수 있습니다.
	fmt.Println("all:", r.FindAllStringSubmatchIndex(
		"peach punch pinch", -1))

	// 이러한 함수에 두 번째 인수로
	// 음수가 아닌 정수를 제공하면 일치하는 횟수를 제한합니다.
	fmt.Println(r.FindAllString("peach punch pinch", 2))

	// 위의 예에서는 문자열 인수를 사용했고
	// `MatchString` 과 같은 이름을 사용했습니다. 또한
	// `[]byte` 인수를 제공하고 함수 이름에서 `String` 을 삭제할 수 있습니다.
	fmt.Println(r.Match([]byte("peach")))

	// 정규 표현식으로 전역 변수를 만들 때
	// `Compile` 의 `MustCompile` 변형을 사용할 수 있습니다.
	// `MustCompile` 은 오류를 반환하는 대신 패닉을 발생시키므로
	// 전역 변수에 사용하는 것이 더 안전합니다.
	r = regexp.MustCompile("p([a-z]+)ch")
	fmt.Println("regexp:", r)

	// `regexp` 패키지는 또한
	// 문자열의 하위 집합을 다른 값으로 바꾸는 데 사용할 수 있습니다.
	fmt.Println(r.ReplaceAllString("a peach", "<fruit>"))

	// `Func` 변형을 사용하면 주어진 함수로
	// 일치하는 텍스트를 변환할 수 있습니다.
	in := []byte("a peach")
	out := r.ReplaceAllFunc(in, bytes.ToUpper)
	fmt.Println(string(out))
}
```

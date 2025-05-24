# 문자열과 룬 (rune)

이 랩에서 해결해야 할 문제는 Go 에서 문자열과 룬을 사용하는 방법을 이해하는 것입니다. 구체적으로, 이 랩에서는 문자열의 길이 얻기, 문자열 인덱싱, 문자열 내 룬 개수 세기, 문자열 내 룬 반복 처리를 다룹니다.

이 랩을 완료하려면 다음이 필요합니다.

- Go 구문에 대한 기본적인 이해
- Go 문자열과 룬에 대한 지식
- Go 표준 라이브러리

```sh
$ go run strings-and-runes.go
Len: 18
e0 b8 aa e0 b8 a7 e0 b8 b1 e0 b8 aa e0 b8 94 e0 b8 b5
Rune count: 6
U+0E2A 'ส' starts at 0
U+0E27 'ว' starts at 3
U+0E31 'ั' starts at 6
U+0E2A 'ส' starts at 9
U+0E14 'ด' starts at 12
U+0E35 'ี' starts at 15

Using DecodeRuneInString
U+0E2A 'ส' starts at 0
found so sua
U+0E27 'ว' starts at 3
U+0E31 'ั' starts at 6
U+0E2A 'ส' starts at 9
found so sua
U+0E14 'ด' starts at 12
U+0E35 'ี' starts at 15
```

전체 코드는 다음과 같습니다.

```go
// Go 문자열은 읽기 전용 바이트 슬라이스입니다. 언어와 표준 라이브러리는 문자열을 특별하게 처리합니다.
// 즉, [UTF-8](https://en.wikipedia.org/wiki/UTF-8) 로 인코딩된 텍스트의 컨테이너로 처리합니다.
// 다른 언어에서 문자열은 "문자"로 구성됩니다.
// Go 에서 문자의 개념은 `rune` 이라고 불립니다. 즉, 유니코드 코드 포인트를 나타내는 정수입니다.
// [이 Go 블로그 게시물](https://go.dev/blog/strings) 은 이 주제에 대한 좋은 소개입니다.

package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {

	// `s` 는 문자열 리터럴 값을 할당받아
	// 태국어 단어 "hello"를 나타냅니다. Go 문자열 리터럴은 UTF-8
	// 인코딩된 텍스트입니다.
	const s = "สวัสดี"

	// 문자열은 `[]byte` 와 동일하므로, 이 코드는
	// 저장된 원시 바이트의 길이를 생성합니다.
	fmt.Println("Len:", len(s))

	// 문자열을 인덱싱하면 각 인덱스에서 원시 바이트 값이 생성됩니다. 이 루프는
	// `s` 의 코드 포인트를 구성하는 모든 바이트의 16 진수 값을 생성합니다.
	for i := 0; i < len(s); i++ {
		fmt.Printf("%x ", s[i])
	}
	fmt.Println()

	// 문자열에 있는 _룬_의 수를 세려면
	// `utf8` 패키지를 사용할 수 있습니다. `RuneCountInString` 의
	// 런타임은 문자열의 크기에 따라 달라집니다.
	// 각 UTF-8 룬을 순차적으로 디코딩해야 하기 때문입니다.
	// 일부 태국어 문자는 여러 UTF-8 로 표현됩니다.
	// 코드 포인트이므로 이 카운트의 결과는 놀라울 수 있습니다.
	fmt.Println("Rune count:", utf8.RuneCountInString(s))

	// `range` 루프는 문자열을 특별하게 처리하고
	// 각 `rune` 을 문자열 내 오프셋과 함께 디코딩합니다.
	for idx, runeValue := range s {
		fmt.Printf("%#U starts at %d\n", runeValue, idx)
	}

	// `utf8.DecodeRuneInString` 함수를 명시적으로 사용하여
	// 동일한 반복을 수행할 수 있습니다.
	fmt.Println("\nUsing DecodeRuneInString")
	for i, w := 0, 0; i < len(s); i += w {
		runeValue, width := utf8.DecodeRuneInString(s[i:])
		fmt.Printf("%#U starts at %d\n", runeValue, i)
		w = width

		// 이것은 `rune` 값을 함수에 전달하는 것을 보여줍니다.
		examineRune(runeValue)
	}
}

func examineRune(r rune) {

	// 작은 따옴표로 묶인 값은 _룬 리터럴_입니다. 우리는
	// `rune` 값을 룬 리터럴과 직접 비교할 수 있습니다.
	if r == 't' {
		fmt.Println("found tee")
	} else if r == 'ส' {
		fmt.Println("found so sua")
	}
}
```

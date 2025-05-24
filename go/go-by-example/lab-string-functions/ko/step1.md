# 문자열 함수

`strings` 패키지에서 제공하는 다양한 문자열 함수의 출력을 인쇄하도록 아래 코드를 완성하십시오.

- `strings` 패키지를 사용하여 랩을 완료하십시오.
- `fmt.Println` 함수를 사용하여 출력을 인쇄하십시오.
- 함수 이름이나 매개변수를 수정하지 마십시오.

```sh
$ go run string-functions.go
Contains: true
Count: 2
HasPrefix: true
HasSuffix: true
Index: 1
Join: a-b
Repeat: aaaaa
Replace: f00
Replace: f0o
Split: [a b c d e]
ToLower: test
ToUpper: TEST
```

전체 코드는 다음과 같습니다.

```go
// The standard library's `strings` package provides many
// useful string-related functions. Here are some examples
// to give you a sense of the package.

package main

import (
	"fmt"
	s "strings"
)

// We alias `fmt.Println` to a shorter name as we'll use
// it a lot below.
var p = fmt.Println

func main() {

	// Here's a sample of the functions available in
	// `strings`. Since these are functions from the
	// package, not methods on the string object itself,
	// we need pass the string in question as the first
	// argument to the function. You can find more
	// functions in the [`strings`](https://pkg.go.dev/strings)
	// package docs.
	p("Contains:  ", s.Contains("test", "es"))
	p("Count:     ", s.Count("test", "t"))
	p("HasPrefix: ", s.HasPrefix("test", "te"))
	p("HasSuffix: ", s.HasSuffix("test", "st"))
	p("Index:     ", s.Index("test", "e"))
	p("Join:      ", s.Join([]string{"a", "b"}, "-"))
	p("Repeat:    ", s.Repeat("a", 5))
	p("Replace:   ", s.Replace("foo", "o", "0", -1))
	p("Replace:   ", s.Replace("foo", "o", "0", 1))
	p("Split:     ", s.Split("a-b-c-d-e", "-"))
	p("ToLower:   ", s.ToLower("TEST"))
	p("ToUpper:   ", s.ToUpper("test"))
}
```

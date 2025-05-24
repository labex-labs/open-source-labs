# 숫자 파싱 (Number Parsing)

문자열에서 숫자를 파싱하는 것은 많은 프로그램에서 흔한 작업입니다. 이 랩에서는 내장된 `strconv` 패키지를 사용하여 문자열에서 다양한 유형의 숫자를 파싱해야 합니다.

- `strconv` 패키지를 사용하여 문자열에서 숫자를 파싱합니다.
- `ParseFloat`를 사용하여 float 를 파싱합니다.
- `ParseInt`를 사용하여 int 를 파싱합니다.
- `ParseInt`를 사용하여 16 진수 형식의 숫자를 파싱합니다.
- `ParseUint`를 사용하여 부호 없는 int (unsigned int) 를 파싱합니다.
- `Atoi`를 사용하여 10 진수 int 를 파싱합니다.
- 파싱 함수에서 반환된 오류를 처리합니다.

```sh
$ go run number-parsing.go
1.234
123
456
789
135
strconv.ParseInt: parsing "wat": invalid syntax

# Next we'll look at another common parsing task: URLs.
```

전체 코드는 다음과 같습니다.

```go
// Parsing numbers from strings is a basic but common task
// in many programs; here's how to do it in Go.

package main

// The built-in package `strconv` provides the number
// parsing.
import (
	"fmt"
	"strconv"
)

func main() {

	// With `ParseFloat`, this `64` tells how many bits of
	// precision to parse.
	f, _ := strconv.ParseFloat("1.234", 64)
	fmt.Println(f)

	// For `ParseInt`, the `0` means infer the base from
	// the string. `64` requires that the result fit in 64
	// bits.
	i, _ := strconv.ParseInt("123", 0, 64)
	fmt.Println(i)

	// `ParseInt` will recognize hex-formatted numbers.
	d, _ := strconv.ParseInt("0x1c8", 0, 64)
	fmt.Println(d)

	// A `ParseUint` is also available.
	u, _ := strconv.ParseUint("789", 0, 64)
	fmt.Println(u)

	// `Atoi` is a convenience function for basic base-10
	// `int` parsing.
	k, _ := strconv.Atoi("135")
	fmt.Println(k)

	// Parse functions return an error on bad input.
	_, e := strconv.Atoi("wat")
	fmt.Println(e)
}
```

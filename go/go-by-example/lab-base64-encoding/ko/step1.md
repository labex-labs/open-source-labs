# Base64 인코딩

제공된 문자열을 표준 및 URL 호환 base64 인코딩을 사용하여 인코딩하고 디코딩하는 Golang 프로그램을 작성해야 합니다.

- 프로그램은 기본 `base64` 대신 `b64` 이름을 사용하여 `encoding/base64` 패키지를 임포트해야 합니다.
- 프로그램은 제공된 문자열을 표준 및 URL 호환 base64 인코딩을 사용하여 인코딩해야 합니다.
- 프로그램은 인코딩된 문자열을 표준 및 URL 호환 base64 디코딩을 사용하여 디코딩해야 합니다.
- 프로그램은 인코딩 및 디코딩된 문자열을 콘솔에 출력해야 합니다.

```sh
# The string encodes to slightly different values with the
# standard and URL base64 encoders (trailing `+` vs `-`)
# but they both decode to the original string as desired.
```

전체 코드는 다음과 같습니다.

```go
// Go provides built-in support for [base64
// encoding/decoding](https://en.wikipedia.org/wiki/Base64).

package main

// This syntax imports the `encoding/base64` package with
// the `b64` name instead of the default `base64`. It'll
// save us some space below.
import (
	b64 "encoding/base64"
	"fmt"
)

func main() {

	// Here's the `string` we'll encode/decode.
	data := "abc123!?$*&()'-=@~"

	// Go supports both standard and URL-compatible
	// base64. Here's how to encode using the standard
	// encoder. The encoder requires a `[]byte` so we
	// convert our `string` to that type.
	sEnc := b64.StdEncoding.EncodeToString([]byte(data))
	fmt.Println(sEnc)

	// Decoding may return an error, which you can check
	// if you don't already know the input to be
	// well-formed.
	sDec, _ := b64.StdEncoding.DecodeString(sEnc)
	fmt.Println(string(sDec))
	fmt.Println()

	// This encodes/decodes using a URL-compatible base64
	// format.
	uEnc := b64.URLEncoding.EncodeToString([]byte(data))
	fmt.Println(uEnc)
	uDec, _ := b64.URLEncoding.DecodeString(uEnc)
	fmt.Println(string(uDec))
}
```

# Base64 编码

你需要编写一个 Go 语言程序，使用标准的和 URL 兼容的 Base64 编码对给定字符串进行编码和解码。

- 程序应导入 `encoding/base64` 包，并将其命名为 `b64`，而不是默认的 `base64`。
- 程序应使用标准的和 URL 兼容的 Base64 编码对给定字符串进行编码。
- 程序应使用标准的和 URL 兼容的 Base64 解码对编码后的字符串进行解码。
- 程序应将编码和解码后的字符串打印到控制台。

```sh
# 使用标准 Base64 编码器和 URL Base64 编码器对字符串进行编码时，结果会稍有不同（末尾分别是 `+` 和 `-`），
# 但它们都能按预期解码为原始字符串。
```

以下是完整代码：

```go
// Go 语言为 [Base64 编码/解码](https://en.wikipedia.org/wiki/Base64) 提供了内置支持。

package main

// 这种语法将 `encoding/base64` 包导入为 `b64`，而不是默认的 `base64`。这样在下面可以节省一些空间。
import (
	b64 "encoding/base64"
	"fmt"
)

func main() {

	// 这是我们要编码/解码的 `string`。
	data := "abc123!?$*&()'-=@~"

	// Go 语言支持标准的和 URL 兼容的 Base64。以下是使用标准编码器进行编码的方法。编码器需要一个 `[]byte` 类型，所以我们将 `string` 转换为该类型。
	sEnc := b64.StdEncoding.EncodeToString([]byte(data))
	fmt.Println(sEnc)

	// 解码可能会返回一个错误，如果你不确定输入是否格式良好，可以检查该错误。
	sDec, _ := b64.StdEncoding.DecodeString(sEnc)
	fmt.Println(string(sDec))
	fmt.Println()

	// 这使用 URL 兼容的 Base64 格式进行编码/解码。
	uEnc := b64.URLEncoding.EncodeToString([]byte(data))
	fmt.Println(uEnc)
	uDec, _ := b64.URLEncoding.DecodeString(uEnc)
	fmt.Println(string(uDec))
}

```

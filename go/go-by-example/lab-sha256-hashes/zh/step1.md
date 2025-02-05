# SHA256哈希值

给定一个字符串，计算其SHA256哈希值。

- 程序应导入 `crypto/sha256` 和 `fmt` 包。
- 程序应使用 `sha256.New()` 函数创建一个新的哈希。
- 程序应使用 `Write` 函数将字符串的字节写入哈希。
- 程序应使用 `Sum` 函数获取最终的哈希结果作为字节切片。
- 程序应以十六进制格式打印原始字符串和哈希结果。

```sh
# 运行该程序会计算哈希值并以人类可读的十六进制格式打印出来。
$ go run sha256-hashes.go
sha256 this string
1af1dfa857bf1d8814fe1af8983c18080019922e557f15a8a...

# 你可以使用与上述类似的模式计算其他哈希值。例如，要计算
# SHA512哈希值，导入 `crypto/sha512` 并使用
# `sha512.New()`。

# 请注意，如果你需要加密安全的哈希值，
# 你应该仔细研究
# [哈希强度](https://en.wikipedia.org/wiki/Cryptographic_hash_function)!
```

以下是完整代码：

```go
// [_SHA256哈希值_](https://en.wikipedia.org/wiki/SHA-2) 常用于计算二进制
// 或文本块的简短标识。例如，TLS/SSL证书使用SHA256来计算证书的签名。以下是在Go中计算
// SHA256哈希值的方法。

package main

// Go在各种 `crypto/*` 包中实现了多个哈希函数。
import (
	"crypto/sha256"
	"fmt"
)

func main() {
	s := "sha256 this string"

	// 这里我们从一个新的哈希开始。
	h := sha256.New()

	// `Write` 期望传入字节。如果你有一个字符串 `s`，
	// 使用 `[]byte(s)` 将其转换为字节。
	h.Write([]byte(s))

	// 这会获取最终的哈希结果作为字节
	// 切片。`Sum` 的参数可用于追加到现有的字节切片：通常不需要。
	bs := h.Sum(nil)

	fmt.Println(s)
	fmt.Printf("%x\n", bs)
}

```

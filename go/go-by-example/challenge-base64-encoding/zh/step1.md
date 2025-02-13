# Base64 编码

你需要编写一个 Go 语言程序，使用标准的和与 URL 兼容的 Base64 编码对给定字符串进行编码和解码。

## 要求

- 程序应导入 `encoding/base64` 包，并将其命名为 `b64`，而不是默认的 `base64`。
- 程序应使用标准的和与 URL 兼容的 Base64 编码对给定字符串进行编码。
- 程序应使用标准的和与 URL 兼容的 Base64 解码对编码后的字符串进行解码。
- 程序应将编码和解码后的字符串打印到控制台。

## 示例

```sh
# 使用标准 Base64 编码器和 URL Base64 编码器对字符串进行编码，
# 会得到略有不同的值（末尾的 `+` 与 `-`），
# 但它们都能按预期解码为原始字符串。
$ go run base64-encoding.go
YWJjMTIzIT8kKiYoKSctPUB+
abc123!?$*&()'-=@~

YWJjMTIzIT8kKiYoKSctPUB-
abc123!?$*&()'-=@~

```

# 字符串格式化

你需要在 Go 语言中使用各种格式化动词来格式化不同类型的数据。

## 要求

- 你必须使用 `fmt` 包来格式化数据。
- 对于每种数据类型，你必须使用正确的格式化动词。
- 你必须能够格式化整数、浮点数、字符串和结构体。
- 你必须能够控制输出的宽度和精度。
- 你必须能够使输出左对齐或右对齐。

## 示例

```sh
$ go run string-formatting.go
struct1: {1 2}
struct2: {x:1 y:2}
struct3: main.point{x:1, y:2}
type: main.point
bool: true
int: 123
bin: 1110
char:!
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

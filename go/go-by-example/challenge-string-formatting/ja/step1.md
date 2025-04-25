# 文字列フォーマット

Go 言語では、様々なフォーマット動詞を使ってさまざまな種類のデータをフォーマットする必要があります。

## 要件

- データをフォーマットするには `fmt` パッケージを使用する必要があります。
- 各データ型に対して正しいフォーマット動詞を使用する必要があります。
- 整数、浮動小数点数、文字列、構造体をフォーマットできる必要があります。
- 出力の幅と精度を制御できる必要があります。
- 出力を左寄せまたは右寄せできる必要があります。

## 例

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

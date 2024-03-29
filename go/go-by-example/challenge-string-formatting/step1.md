# String Formatting

You are required to format different types of data using various formatting verbs in Golang.

## Requirements

- You must use the `fmt` package to format the data.
- You must use the correct formatting verb for each data type.
- You must be able to format integers, floats, strings, and structs.
- You must be able to control the width and precision of the output.
- You must be able to left-justify or right-justify the output.

## Example

```sh
$ go run string-formatting.go
struct1: {1 2}
struct2: {x:1 y:2}
struct3: main.point{x:1, y:2}
type: main.point
bool: true
int: 123
bin: 1110
char: !
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

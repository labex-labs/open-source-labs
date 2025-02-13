# 数字解析

在许多程序中，从字符串解析数字是一项常见的任务。本次挑战要求你使用内置的 `strconv` 包从字符串中解析不同类型的数字。

## 要求

- 使用 `strconv` 包从字符串中解析数字。
- 使用 `ParseFloat` 解析浮点数。
- 使用 `ParseInt` 解析整数。
- 使用 `ParseInt` 解析十六进制格式的数字。
- 使用 `ParseUint` 解析无符号整数。
- 使用 `Atoi` 解析十进制整数。
- 处理解析函数返回的错误。

## 示例

```sh
$ go run number-parsing.go
1.234
123
456
789
135
strconv.ParseInt: 解析 "wat": 语法无效

# 接下来我们将看看另一个常见的解析任务：URL。
```

# 正则表达式

本挑战要求你完成代码，以在 Go 语言中执行各种与正则表达式相关的任务。

## 要求

- 使用 `regexp` 包来执行与正则表达式相关的任务。
- 使用 `MatchString` 来测试一个模式是否与一个字符串匹配。
- 使用 `Compile` 来优化一个 `Regexp` 结构体。
- 使用 `MatchString` 来像 `Compile` 那样测试匹配。
- 使用 `FindString` 来找到正则表达式的匹配项。
- 使用 `FindStringIndex` 来找到第一个匹配项，并返回匹配项的起始和结束索引，而不是匹配的文本。
- 使用 `FindStringSubmatch` 来返回 `p([a-z]+)ch` 和 `([a-z]+)` 的信息。
- 使用 `FindStringSubmatchIndex` 来返回匹配项和子匹配项的索引信息。
- 使用 `FindAllString` 来找到正则表达式的所有匹配项。
- 使用 `FindAllStringSubmatchIndex` 来应用于输入中的所有匹配项，而不仅仅是第一个。
- 使用 `Match` 来使用 `[]byte` 参数测试匹配，并从函数名中去掉 `String`。
- 使用 `MustCompile` 来创建带有正则表达式的全局变量。
- 使用 `ReplaceAllString` 用其他值替换字符串的子集。
- 使用 `ReplaceAllFunc` 用给定的函数转换匹配的文本。

## 示例

```sh
$ go run regular-expressions.go
true
true
peach
idx: [0 5]
[peach ea]
[0 5 1 3]
[peach punch pinch]
all: [[0 5 1 3] [6 11 7 9] [12 17 13 15]]
[peach punch]
true
regexp: p([a-z]+)ch
a <fruit>
a PEACH

# 有关 Go 正则表达式的完整参考，请查看
# [`regexp`](https://pkg.go.dev/regexp) 包文档。

```

# 常量

需要解决的问题是展示 Go 语言中常量在字符、字符串、布尔值和数值方面的使用。

## 要求

该挑战有以下要求：

- 使用 `const` 关键字声明常量值。
- 常量应为字符、字符串、布尔值和数值类型。
- 常量声明可以出现在 `var` 声明可以出现的任何位置。
- 证明常量表达式可以进行任意精度的算术运算。
- 数值常量在被赋予类型之前没有类型，例如通过显式转换。
- 数字可以通过在需要类型的上下文中使用它来赋予类型，例如变量赋值或函数调用。

## 示例

```sh
$ go run constant.go
常量
6e+11
600000000000
-0.28470407323754404
```

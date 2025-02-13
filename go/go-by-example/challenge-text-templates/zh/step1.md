# 文本模板

在这个挑战中，你需要演示如何使用 `text/template` 包来生成动态内容。

## 要求

- 使用 `text/template` 包生成动态内容。
- 如果 `Parse` 返回错误，使用 `template.Must` 函数使程序恐慌。
- 使用 `{{.FieldName}}` 操作访问结构体字段。
- 使用 `{{if..}} yes {{else..}} no {{end}}\n` 操作实现模板的条件执行。
- 使用 `{{range.}}{{.}} {{end}}\n` 操作遍历切片、数组、映射或通道。

## 示例

```sh
$ go run templates.go
值: 一些文本
值: 5
值: [Go Rust C++ C#]
姓名: Jane Doe
姓名: Mickey Mouse
是
否
遍历: Go Rust C++ C#
```

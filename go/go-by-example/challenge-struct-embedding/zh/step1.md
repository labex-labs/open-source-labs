# 结构体嵌入

创建一个名为 `container` 的结构体，该结构体嵌入一个名为 `base` 的结构体。`base` 结构体应具有一个类型为 `int` 的字段 `num` 和一个返回字符串的方法 `describe()`。`container` 结构体应具有一个类型为 `string` 的字段 `str`。`container` 结构体应能够访问 `base` 结构体的 `num` 字段和 `describe()` 方法。

## 要求

- `base` 结构体应具有一个类型为 `int` 的字段 `num`。
- `base` 结构体应具有一个返回字符串的方法 `describe()`。
- `container` 结构体应具有一个类型为 `string` 的字段 `str`。
- `container` 结构体应嵌入 `base` 结构体。
- `container` 结构体应能够访问 `base` 结构体的 `num` 字段和 `describe()` 方法。

## 示例

```sh
$ go run struct-embedding.go
co={num: 1, str: some name}
also num: 1
describe: base with num=1
describer: base with num=1
```

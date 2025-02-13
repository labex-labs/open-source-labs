# 使用函数进行排序

本次挑战要解决的问题是在 Go 语言中实现一个自定义排序函数，该函数按字符串长度对字符串切片进行排序。

## 要求

- 应将 `byLength` 类型创建为 `[]string` 类型的别名。
- 应在 `byLength` 类型上实现 `sort.Interface`。
- 应在 `byLength` 类型上实现 `Len` 和 `Swap` 函数。
- 应在 `byLength` 类型上实现 `Less` 函数，以保存实际的自定义排序逻辑。
- `main` 函数应将原始的 `fruits` 切片转换为 `byLength` 类型，然后对该类型化的切片使用 `sort.Sort`。

## 示例

```sh
# 运行我们的程序会显示一个按字符串长度排序的列表，
# 符合预期。
$ go run sorting-by-functions.go
[kiwi peach banana]

# 通过遵循这种创建自定义类型、在该类型上实现三个
# `Interface` 方法，然后对该自定义类型的集合调用
# sort.Sort 的相同模式，我们可以使用任意函数对 Go 切片进行排序。
```

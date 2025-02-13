# 接口

问题是要在 Go 语言中实现一个接口，我们只需要实现接口中的所有方法即可。在这里，我们在 `rect`（矩形）和 `circle`（圆形）上实现 `geometry`（几何图形）接口。

## 要求

- 在 Go 语言中实现一个接口。
- 实现接口中的所有方法。
- 使用一个通用的 `measure` 函数来处理任何 `geometry`。
- 使用 `circle` 和 `rect` 结构体的实例作为 `measure` 的参数。

## 示例

```sh
$ go run interfaces.go
{3 4}
12
14
{5}
78.53981633974483
31.41592653589793

# 要了解更多关于 Go 语言接口的信息，请查看这篇
# [很棒的博客文章](https://jordanorelli.tumblr.com/post/32665860244/how-to-use-interfaces-in-go)。
```

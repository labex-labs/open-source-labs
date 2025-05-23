# 随机数

你需要编写一个程序，生成指定范围内的随机整数和浮点数。该程序还应能够通过更改种子来生成不同的数字序列。

## 要求

- 程序应使用 `math/rand` 包生成随机数。
- 程序应生成指定范围内的随机整数。
- 程序应生成指定范围内的随机浮点数。
- 程序应能够通过更改种子来生成不同的数字序列。

## 示例

```sh
# 根据你运行此示例的位置，一些生成的数字可能会有所不同。请注意，在 Go Playground 上，由于其实现方式，使用 `time.Now()` 作为种子仍然会产生确定性的结果。
$ go run random-numbers.go
81,87
0.6645600532184904
7.123187485356329,8.434115364335547
0,28
5,87
5,87

# 有关 Go 可以提供的其他随机量的参考，请参阅 [`math/rand`](https://pkg.go.dev/math/rand) 包文档。
```

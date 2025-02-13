# 测试与基准测试

在此挑战中要解决的问题是，对一个名为 `IntMin` 的整数最小值函数的简单实现进行测试和基准测试。

## 要求

- 必须导入 `testing` 包。
- `IntMin` 函数必须接受两个整数参数并返回一个整数。
- `TestIntMinBasic` 函数必须针对基本输入值测试 `IntMin` 函数。
- `TestIntMinTableDriven` 函数必须使用表驱动风格测试 `IntMin` 函数。
- `BenchmarkIntMin` 函数必须对 `IntMin` 函数进行基准测试。

## 示例

```sh
# 在详细模式下运行当前项目中的所有测试。
$ go test -v
== RUN   TestIntMinBasic
--- PASS: TestIntMinBasic (0.00s)
=== RUN   TestIntMinTableDriven
=== RUN   TestIntMinTableDriven/0,1
=== RUN   TestIntMinTableDriven/1,0
=== RUN   TestIntMinTableDriven/2,-2
=== RUN   TestIntMinTableDriven/0,-1
=== RUN   TestIntMinTableDriven/-1,0
--- PASS: TestIntMinTableDriven (0.00s)
    --- PASS: TestIntMinTableDriven/0,1 (0.00s)
    --- PASS: TestIntMinTableDriven/1,0 (0.00s)
    --- PASS: TestIntMinTableDriven/2,-2 (0.00s)
    --- PASS: TestIntMinTableDriven/0,-1 (0.00s)
    --- PASS: TestIntMinTableDriven/-1,0 (0.00s)
PASS
ok  	examples/testing-and-benchmarking	0.023s

# 运行当前项目中的所有基准测试。所有测试
# 在基准测试之前运行。`bench` 标志使用正则表达式过滤
# 基准测试函数名。
$ go test -bench=.
goos: darwin
goarch: arm64
pkg: examples/testing
BenchmarkIntMin-8 1000000000 0.3136 ns/op
PASS
ok  	examples/testing-and-benchmarking	0.351s

```

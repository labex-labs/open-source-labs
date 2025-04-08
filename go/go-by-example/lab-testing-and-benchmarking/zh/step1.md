# 测试与基准测试

本实验要解决的问题是对一个名为 `IntMin` 的整数最小值函数的简单实现进行测试和基准测试。

- 必须导入 `testing` 包。
- `IntMin` 函数必须接受两个整数参数并返回一个整数。
- `TestIntMinBasic` 函数必须针对基本输入值测试 `IntMin` 函数。
- `TestIntMinTableDriven` 函数必须使用表驱动风格测试 `IntMin` 函数。
- `BenchmarkIntMin` 函数必须对 `IntMin` 函数进行基准测试。

```sh
# 以详细模式运行当前项目中的所有测试。

# 运行当前项目中的所有基准测试。所有测试
# 在基准测试之前运行。`bench` 标志使用正则表达式过滤
# 基准测试函数名。
```

以下是完整代码：

```go
// 单元测试是编写规范的 Go 程序的重要组成部分。`testing` 包
// 提供了我们编写单元测试所需的工具，而 `go test` 命令则运行测试。

// 为了演示，这段代码在 `main` 包中，但它可以是任何包。测试代码
// 通常与它所测试的代码位于同一个包中。
package main

import (
	"fmt"
	"testing"
)

// 我们将测试这个简单的整数最小值实现。通常，我们要测试的代码
// 会在一个名为 `intutils.go` 的源文件中，而它的测试文件则会被命名为
// `intutils_test.go`。
func IntMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// 通过编写一个以 `Test` 开头的函数来创建一个测试。
func TestIntMinBasic(t *testing.T) {
	ans := IntMin(2, -2)
	if ans!= -2 {
		// `t.Error*` 会报告测试失败但继续
		// 执行测试。`t.Fatal*` 会报告测试
		// 失败并立即停止测试。
		t.Errorf("IntMin(2, -2) = %d; want -2", ans)
	}
}

// 编写测试可能会很重复，所以习惯上使用 *表驱动风格*，
// 其中测试输入和预期输出列在一个表中，一个循环遍历它们并执行测试逻辑。
func TestIntMinTableDriven(t *testing.T) {
	var tests = []struct {
		a, b int
		want int
	}{
		{0, 1, 0},
		{1, 0, 0},
		{2, -2, -2},
		{0, -1, -1},
		{-1, 0, -1},
	}

	for _, tt := range tests {
		// t.Run 允许运行 "子测试"，每个表项一个。在执行 `go test -v` 时，这些会单独显示。
		testname := fmt.Sprintf("%d,%d", tt.a, tt.b)
		t.Run(testname, func(t *testing.T) {
			ans := IntMin(tt.a, tt.b)
			if ans!= tt.want {
				t.Errorf("got %d, want %d", ans, tt.want)
			}
		})
	}
}

// 基准测试通常放在 `_test.go` 文件中，并且以 `Benchmark` 开头命名。测试运行器
// 会多次执行每个基准测试函数，每次运行时增加 `b.N`，直到收集到精确的测量结果。
func BenchmarkIntMin(b *testing.B) {
	// 通常，基准测试会在一个循环中运行我们要基准测试的函数 `b.N` 次。
	for i := 0; i < b.N; i++ {
		IntMin(1, 2)
	}
}

```

# 随机数

你需要编写一个程序，在指定范围内生成随机整数和浮点数。该程序还应能够通过更改种子来生成不同的数字序列。

- 程序应使用 `math/rand` 包生成随机数。
- 程序应在指定范围内生成随机整数。
- 程序应在指定范围内生成随机浮点数。
- 程序应能够通过更改种子来生成不同的数字序列。

```sh
# 根据你运行此示例的位置，一些生成的数字可能会有所不同。请注意，在Go Playground上，由于其实现方式，使用 `time.Now()` 进行种子设定仍然会产生确定性结果。
$ go run random-numbers.go
81,87
0.6645600532184904
7.123187485356329,8.434115364335547
0,28
5,87
5,87

# 有关Go可以提供的其他随机量的参考，请参阅[`math/rand`](https://pkg.go.dev/math/rand)包文档。
```

以下是完整代码：

```go
// Go的 `math/rand` 包提供
// [伪随机数](https://en.wikipedia.org/wiki/Pseudorandom_number_generator)
// 生成。

package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {

	// 例如，`rand.Intn` 返回一个随机的 `int` n，
	// `0 <= n < 100`。
	fmt.Print(rand.Intn(100), ",")
	fmt.Print(rand.Intn(100))
	fmt.Println()

	// `rand.Float64` 返回一个 `float64` `f`，
	// `0.0 <= f < 1.0`。
	fmt.Println(rand.Float64())

	// 这可用于在其他范围内生成随机浮点数，例如 `5.0 <= f' < 10.0`。
	fmt.Print((rand.Float64()*5)+5, ",")
	fmt.Print((rand.Float64() * 5) + 5)
	fmt.Println()

	// 默认的数字生成器是确定性的，因此默认情况下每次都会生成相同的数字序列。
	// 要生成不同的序列，请给它一个变化的种子。
	// 请注意，对于你想要保密的随机数，这样做并不安全；对于那些情况，请使用 `crypto/rand`。
	s1 := rand.NewSource(time.Now().UnixNano())
	r1 := rand.New(s1)

	// 像调用 `rand` 包上的函数一样调用生成的 `rand.Rand`。
	fmt.Print(r1.Intn(100), ",")
	fmt.Print(r1.Intn(100))
	fmt.Println()

	// 如果你用相同的数字为源设定种子，它会
	// 生成相同的随机数序列。
	s2 := rand.NewSource(42)
	r2 := rand.New(s2)
	fmt.Print(r2.Intn(100), ",")
	fmt.Print(r2.Intn(100))
	fmt.Println()
	s3 := rand.NewSource(42)
	r3 := rand.New(s3)
	fmt.Print(r3.Intn(100), ",")
	fmt.Print(r3.Intn(100))
}

```

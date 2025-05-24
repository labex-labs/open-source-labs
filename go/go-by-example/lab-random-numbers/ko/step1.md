# 난수 (Random Numbers)

지정된 범위 내에서 랜덤 정수와 부동 소수점을 생성하는 프로그램을 작성해야 합니다. 또한 시드 (seed) 를 변경하여 다양한 시퀀스의 숫자를 생성할 수 있어야 합니다.

- 프로그램은 `math/rand` 패키지를 사용하여 난수를 생성해야 합니다.
- 프로그램은 지정된 범위 내에서 랜덤 정수를 생성해야 합니다.
- 프로그램은 지정된 범위 내에서 랜덤 부동 소수점을 생성해야 합니다.
- 프로그램은 시드를 변경하여 다양한 시퀀스의 숫자를 생성할 수 있어야 합니다.

```sh
# 이 샘플을 실행하는 위치에 따라
# 생성된 일부 숫자가 다를 수 있습니다.
# Go playground 에서 `time.Now()` 로 시딩하면
# playground 가 구현된 방식 때문에
# 여전히 결정론적 결과가 생성됩니다.
$ go run random-numbers.go
81,87
0.6645600532184904
7.123187485356329,8.434115364335547
0,28
5,87
5,87

# Go 가 제공할 수 있는 다른 랜덤 값에 대한
# 참조는 [`math/rand`](https://pkg.go.dev/math/rand)
# 패키지 문서를 참조하십시오.
```

전체 코드는 다음과 같습니다.

```go
// Go 의 `math/rand` 패키지는
// [의사 난수](https://en.wikipedia.org/wiki/Pseudorandom_number_generator)
// 생성을 제공합니다.

package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {

	// 예를 들어, `rand.Intn` 은 랜덤 `int` n 을 반환하며,
	// `0 <= n < 100`입니다.
	fmt.Print(rand.Intn(100), ",")
	fmt.Print(rand.Intn(100))
	fmt.Println()

	// `rand.Float64` 는 `float64` `f` 를 반환하며,
	// `0.0 <= f < 1.0`입니다.
	fmt.Println(rand.Float64())

	// 이것은 다른 범위, 예를 들어 `5.0 <= f' < 10.0`에서
	// 랜덤 부동 소수점을 생성하는 데 사용될 수 있습니다.
	fmt.Print((rand.Float64()*5)+5, ",")
	fmt.Print((rand.Float64() * 5) + 5)
	fmt.Println()

	// 기본 숫자 생성기는 결정론적이므로,
	// 기본적으로 매번 동일한 시퀀스의 숫자를 생성합니다.
	// 다양한 시퀀스를 생성하려면 변경되는 시드를 제공하십시오.
	// 이것은 비밀로 하려는 난수에 사용하는 것은 안전하지 않습니다;
	// 그런 경우에는 `crypto/rand` 를 사용하십시오.
	s1 := rand.NewSource(time.Now().UnixNano())
	r1 := rand.New(s1)

	// 결과 `rand.Rand` 를 `rand` 패키지의
	// 함수처럼 호출하십시오.
	fmt.Print(r1.Intn(100), ",")
	fmt.Print(r1.Intn(100))
	fmt.Println()

	// 동일한 숫자로 소스를 시딩하면
	// 동일한 시퀀스의 난수를 생성합니다.
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

# 인터페이스 (Interfaces)

문제는 Go 에서 인터페이스를 구현하는 것입니다. 인터페이스의 모든 메서드를 구현하기만 하면 됩니다. 여기서는 `rect`와 `circle`에 `geometry`를 구현합니다.

- Go 에서 인터페이스를 구현합니다.
- 인터페이스의 모든 메서드를 구현합니다.
- 제네릭 (generic) `measure` 함수를 사용하여 모든 `geometry`에서 작동합니다.
- `circle` 및 `rect` 구조체의 인스턴스를 `measure`의 인수로 사용합니다.

```sh
$ go run interfaces.go
{3 4}
12
14
{5}
78.53981633974483
31.41592653589793

# Go 의 인터페이스에 대해 자세히 알아보려면 다음을 확인하세요.
# [훌륭한 블로그 게시물](https://jordanorelli.tumblr.com/post/32665860244/how-to-use-interfaces-in-go).
```

전체 코드는 다음과 같습니다.

```go
// _Interfaces_는 메서드
// 시그니처의 명명된 컬렉션입니다.

package main

import (
	"fmt"
	"math"
)

// 다음은 기하학적 도형을 위한 기본 인터페이스입니다.
type geometry interface {
	area() float64
	perim() float64
}

// 예시를 위해 `rect` 및 `circle` 타입에 이 인터페이스를 구현합니다.
type rect struct {
	width, height float64
}
type circle struct {
	radius float64
}

// Go 에서 인터페이스를 구현하려면 인터페이스의 모든 메서드를
// 구현하기만 하면 됩니다. 여기서는 `rect` 에 `geometry` 를 구현합니다.
func (r rect) area() float64 {
	return r.width * r.height
}
func (r rect) perim() float64 {
	return 2*r.width + 2*r.height
}

// `circle` 에 대한 구현입니다.
func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}
func (c circle) perim() float64 {
	return 2 * math.Pi * c.radius
}

// 변수가 인터페이스 타입을 가지면 명명된 인터페이스에 있는
// 메서드를 호출할 수 있습니다. 다음은 이를 활용하여
// 모든 `geometry` 에서 작동하는 제네릭 `measure` 함수입니다.
func measure(g geometry) {
	fmt.Println(g)
	fmt.Println(g.area())
	fmt.Println(g.perim())
}

func main() {
	r := rect{width: 3, height: 4}
	c := circle{radius: 5}

	// `circle` 및 `rect` 구조체 타입은 모두
	// `geometry` 인터페이스를 구현하므로
	// 이러한 구조체의 인스턴스를 `measure` 의 인수로 사용할 수 있습니다.
	measure(r)
	measure(c)
}
```

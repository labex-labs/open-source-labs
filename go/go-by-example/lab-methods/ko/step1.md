# 메서드 (Methods)

제공된 코드는 `width`와 `height` 두 개의 필드를 가진 `rect`라는 구조체 타입을 정의합니다. 이 구조체 타입에 대해 `area`와 `perim` 두 개의 메서드가 정의되어 있습니다. `area` 메서드는 사각형의 면적을 계산하고, `perim` 메서드는 사각형의 둘레를 계산합니다. `main` 함수는 이 두 메서드를 호출하고 결과를 출력합니다.

- `area` 메서드는 `*rect`의 리시버 (receiver) 타입을 가져야 합니다.
- `perim` 메서드는 `rect`의 리시버 타입을 가져야 합니다.
- `area` 메서드는 사각형의 면적을 반환해야 합니다.
- `perim` 메서드는 사각형의 둘레를 반환해야 합니다.
- `main` 함수는 두 메서드를 모두 호출하고 결과를 출력해야 합니다.

```sh
$ go run methods.go
area: 50
perim: 30
area: 50
perim: 30

# Next we'll look at Go's mechanism for grouping and
# naming related sets of methods: interfaces.
```

전체 코드는 다음과 같습니다.

```go
// Go supports _methods_ defined on struct types.

package main

import "fmt"

type rect struct {
	width, height int
}

// This `area` method has a _receiver type_ of `*rect`.
func (r *rect) area() int {
	return r.width * r.height
}

// Methods can be defined for either pointer or value
// receiver types. Here's an example of a value receiver.
func (r rect) perim() int {
	return 2*r.width + 2*r.height
}

func main() {
	r := rect{width: 10, height: 5}

	// Here we call the 2 methods defined for our struct.
	fmt.Println("area: ", r.area())
	fmt.Println("perim:", r.perim())

	// Go automatically handles conversion between values
	// and pointers for method calls. You may want to use
	// a pointer receiver type to avoid copying on method
	// calls or to allow the method to mutate the
	// receiving struct.
	rp := &r
	fmt.Println("area: ", rp.area())
	fmt.Println("perim:", rp.perim())
}
```

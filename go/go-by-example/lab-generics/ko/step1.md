# 제네릭 (Generics)

이 랩에서 해결해야 할 문제는 Golang 에서 제네릭 함수와 타입을 정의하고 사용하는 방법을 이해하는 것입니다.

- Golang 의 제네릭 개념을 이해합니다.
- 타입 매개변수 (type parameters) 와 제약 조건 (constraints) 을 사용하여 제네릭 함수를 정의하는 방법을 압니다.
- 타입 매개변수를 사용하여 제네릭 타입을 정의하는 방법을 압니다.
- 제네릭 타입에 메서드를 정의하는 방법을 이해합니다.
- 타입 추론 (type inference) 을 사용하여 제네릭 함수를 호출하는 방법을 압니다.

```sh
$ go run generics.go
keys: [4 1 2]
list: [10 13 23]
```

전체 코드는 다음과 같습니다.

```go
// 버전 1.18 부터 Go 는 _제네릭_ (generics), 즉 _타입 매개변수_ (type parameters) 에 대한 지원을 추가했습니다.

package main

import "fmt"

// 제네릭 함수의 예로, `MapKeys` 는 모든 타입의 맵을 받아 해당 키의 슬라이스를 반환합니다.
// 이 함수는 두 개의 타입 매개변수 `K` 와 `V` 를 갖습니다.
// `K` 는 `comparable` _제약 조건_ (constraint) 을 가지며, 이는 이 타입의 값을 `==` 및
// `!=` 연산자로 비교할 수 있음을 의미합니다. 이것은 Go 에서 맵 키에 필요합니다.
// `V` 는 `any` 제약 조건을 가지며, 이는 어떤 방식으로든 제한되지 않음을 의미합니다 (`any` 는 `interface{}` 의 별칭입니다).
func MapKeys[K comparable, V any](m map[K]V) []K {
	r := make([]K, 0, len(m))
	for k := range m {
		r = append(r, k)
	}
	return r
}

// 제네릭 타입의 예로, `List` 는 모든 타입의 값을 갖는 단일 연결 리스트입니다.
type List[T any] struct {
	head, tail *element[T]
}

type element[T any] struct {
	next *element[T]
	val  T
}

// 일반 타입에서 하는 것처럼 제네릭 타입에 메서드를 정의할 수 있지만,
// 타입 매개변수를 유지해야 합니다. 타입은 `List[T]` 이며, `List` 가 아닙니다.
func (lst *List[T]) Push(v T) {
	if lst.tail == nil {
		lst.head = &element[T]{val: v}
		lst.tail = lst.head
	} else {
		lst.tail.next = &element[T]{val: v}
		lst.tail = lst.tail.next
	}
}

func (lst *List[T]) GetAll() []T {
	var elems []T
	for e := lst.head; e != nil; e = e.next {
		elems = append(elems, e.val)
	}
	return elems
}

func main() {
	var m = map[int]string{1: "2", 2: "4", 4: "8"}

	// 제네릭 함수를 호출할 때, 종종 _타입 추론_ (type inference) 에 의존할 수 있습니다.
	// `MapKeys` 를 호출할 때 `K` 와 `V` 의 타입을 지정할 필요가 없다는 점에 유의하십시오.
	// 컴파일러가 자동으로 추론합니다.
	fmt.Println("keys:", MapKeys(m))

	// ... 하지만 명시적으로 지정할 수도 있습니다.
	_ = MapKeys[int, string](m)

	lst := List[int]{}
	lst.Push(10)
	lst.Push(13)
	lst.Push(23)
	fmt.Println("list:", lst.GetAll())
}
```

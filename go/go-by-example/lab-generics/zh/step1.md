# 泛型

本实验要解决的问题是理解如何在Go语言中定义和使用泛型函数及类型。

- 理解Go语言中泛型的概念。
- 了解如何定义带类型参数和约束的泛型函数。
- 了解如何定义带类型参数的泛型类型。
- 理解如何在泛型类型上定义方法。
- 了解如何通过类型推断调用泛型函数。

```sh
$ go run generics.go
keys: [4 1 2]
list: [10 13 23]
```

以下是完整代码：

```go
// 从1.18版本开始，Go语言增加了对
// 泛型（也称为类型参数）的支持。

package main

import "fmt"

// 作为泛型函数的一个示例，`MapKeys` 接受
// 任意类型的映射，并返回其键的切片。
// 此函数有两个类型参数 —— `K` 和 `V`；
// `K` 具有 `comparable` 约束，这意味着
// 我们可以使用 `==` 和 `!=` 运算符比较此类型的值。
// 这是Go语言中映射键所必需的。
// `V` 具有 `any` 约束，这意味着它没有任何限制
// （`any` 是 `interface{}` 的别名）。
func MapKeys[K comparable, V any](m map[K]V) []K {
	r := make([]K, 0, len(m))
	for k := range m {
		r = append(r, k)
	}
	return r
}

// 作为泛型类型的一个示例，`List` 是一个
// 包含任意类型值的单链表。
type List[T any] struct {
	head, tail *element[T]
}

type element[T any] struct {
	next *element[T]
	val  T
}

// 我们可以像在常规类型上一样在泛型类型上定义方法，
// 但必须保留类型参数。类型是 `List[T]`，而不是 `List`。
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
	for e := lst.head; e!= nil; e = e.next {
		elems = append(elems, e.val)
	}
	return elems
}

func main() {
	var m = map[int]string{1: "2", 2: "4", 4: "8"}

	// 在调用泛型函数时，我们通常可以依赖
	// 类型推断。请注意，在调用 `MapKeys` 时，
	// 我们不必为 `K` 和 `V` 指定类型 —— 编译器会自动推断它们。
	fmt.Println("keys:", MapKeys(m))

	//... 不过我们也可以显式指定它们。
	_ = MapKeys[int, string](m)

	lst := List[int]{}
	lst.Push(10)
	lst.Push(13)
	lst.Push(23)
	fmt.Println("list:", lst.GetAll())
}

```

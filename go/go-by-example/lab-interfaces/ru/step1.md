# Интерфейсы

Проблема заключается в том, чтобы реализовать интерфейс в Go, для этого достаточно реализовать все методы в интерфейсе. Здесь мы реализуем `geometry` для `rect` и `circle`.

- Реализовать интерфейс в Go.
- Реализовать все методы в интерфейсе.
- Использовать обобщенную функцию `measure`, чтобы работать с любыми геометрическими фигурами (`geometry`).
- Использовать экземпляры структур `circle` и `rect` в качестве аргументов для `measure`.

```sh
$ go run interfaces.go
{3 4}
12
14
{5}
78.53981633974483
31.41592653589793

# Чтобы узнать больше о интерфейсах Go, ознакомьтесь с этой
# [отличной статьей в блоге](https://jordanorelli.tumblr.com/post/32665860244/how-to-use-interfaces-in-go).
```

Ниже представлен полный код:

```go
// _Интерфейсы_ - это именованные коллекции сигнатур методов.

package main

import (
	"fmt"
	"math"
)

// Вот базовый интерфейс для геометрических фигур.
type geometry interface {
	area() float64
	perim() float64
}

// Для нашего примера мы реализуем этот интерфейс для
// типов `rect` и `circle`.
type rect struct {
	width, height float64
}
type circle struct {
	radius float64
}

// Чтобы реализовать интерфейс в Go, нам нужно только
// реализовать все методы в интерфейсе. Здесь мы
// реализуем `geometry` для `rect`.
func (r rect) area() float64 {
	return r.width * r.height
}
func (r rect) perim() float64 {
	return 2*r.width + 2*r.height
}

// Реализация для `circle`.
func (c circle) area() float64 {
	return math.Pi * c.radius * c.radius
}
func (c circle) perim() float64 {
	return 2 * math.Pi * c.radius
}

// Если переменная имеет интерфейсный тип, то мы можем
// вызывать методы, определенные в именованном интерфейсе.
// Вот обобщенная функция `measure`, которая использует
// это свойство, чтобы работать с любыми геометрическими
// фигурами (`geometry`).
func measure(g geometry) {
	fmt.Println(g)
	fmt.Println(g.area())
	fmt.Println(g.perim())
}

func main() {
	r := rect{width: 3, height: 4}
	c := circle{radius: 5}

	// Типы структур `circle` и `rect` оба
	// реализуют интерфейс `geometry`, поэтому мы можем
	// использовать экземпляры
	// этих структур в качестве аргументов для `measure`.
	measure(r)
	measure(c)
}

```

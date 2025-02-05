# 结构体

在本实验中，你需要完成 `newPerson` 函数，该函数用于创建一个具有给定名字的新的人员结构体。`person` 结构体类型包含 `name` 和 `age` 字段。

- `person` 结构体类型必须包含 `name` 和 `age` 字段。
- `newPerson` 函数必须使用给定的名字创建一个新的人员结构体。
- `newPerson` 函数必须返回指向新创建的人员结构体的指针。
- `main` 函数必须打印以下内容：
  - 一个名字为 "Bob" 且年龄为 20 的新结构体。
  - 一个名字为 "Alice" 且年龄为 30 的新结构体。
  - 一个名字为 "Fred" 且年龄为 0 的新结构体。
  - 一个指向名字为 "Ann" 且年龄为 40 的新结构体的指针。
  - 一个使用 `newPerson` 函数创建的名字为 "Jon" 且年龄为 42 的新结构体。
  - 一个名字为 "Sean" 且年龄为 50 的结构体的 `name` 字段。
  - 一个指向名字为 "Sean" 且年龄为 50 的结构体的指针的 `age` 字段。
  - 将年龄字段更新为 51 后，一个指向名字为 "Sean" 且年龄为 50 的结构体的指针的 `age` 字段。

```sh
$ go run structs.go
{Bob 20}
{Alice 30}
{Fred 0}
&{Ann 40}
&{Jon 42}
Sean
50
51
```

以下是完整代码：

```go
// Go 语言的 _结构体_ 是字段的类型化集合。
// 它们对于将数据组合在一起形成记录很有用。

package main

import "fmt"

// 这个 `person` 结构体类型包含 `name` 和 `age` 字段。
type person struct {
	name string
	age  int
}

// `newPerson` 使用给定的名字创建一个新的人员结构体。
func newPerson(name string) *person {
	// 你可以安全地返回指向局部变量的指针
	// 因为局部变量在函数作用域结束后仍然存在。
	p := person{name: name}
	p.age = 42
	return &p
}

func main() {

	// 这种语法创建一个新的结构体。
	fmt.Println(person{"Bob", 20})

	// 初始化结构体时可以为字段命名。
	fmt.Println(person{name: "Alice", age: 30})

	// 省略的字段将被赋予零值。
	fmt.Println(person{name: "Fred"})

	// `&` 前缀会产生指向结构体的指针。
	fmt.Println(&person{name: "Ann", age: 40})

	// 将新结构体的创建封装在构造函数中是一种惯用做法
	fmt.Println(newPerson("Jon"))

	// 使用点号访问结构体字段。
	s := person{name: "Sean", age: 50}
	fmt.Println(s.name)

	// 也可以对结构体指针使用点号 - 指针会自动解引用。
	sp := &s
	fmt.Println(sp.age)

	// 结构体是可变的。
	sp.age = 51
	fmt.Println(sp.age)
}

```

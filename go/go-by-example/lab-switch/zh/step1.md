# `switch` 语句

在这个实验中，你需要完成 `switch` 语句，以便根据输入值打印出相应的消息。

- 必须使用 `switch` 语句来解决问题。
- 必须使用 `default` 分支来处理意外的输入值。

```sh
$ go run switch.go
将 2 写成 two
这是工作日
这是午后
我是一个布尔值
我是一个整数
不知道类型 string
```

以下是完整代码：

```go
// `switch` 语句可以跨多个分支表达条件。

package main

import (
	"fmt"
	"time"
)

func main() {

	// 这是一个基本的 `switch` 语句。
	i := 2
	fmt.Print("将 ", i, " 写成 ")
	switch i {
	case 1:
		fmt.Println("one")
	case 2:
		fmt.Println("two")
	case 3:
		fmt.Println("three")
	}

	// 你可以在同一个 `case` 语句中使用逗号分隔多个表达式。在这个例子中，我们也使用了可选的 `default` 分支。
	switch time.Now().Weekday() {
	case time.Saturday, time.Sunday:
		fmt.Println("这是周末")
	default:
		fmt.Println("这是工作日")
	}

	// 没有表达式的 `switch` 是表达 if/else 逻辑的另一种方式。在这里，我们还展示了 `case` 表达式可以是非常量的。
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("这是中午之前")
	default:
		fmt.Println("这是午后")
	}

	// 类型 `switch` 比较的是类型而不是值。你可以用它来发现接口值的类型。在这个例子中，变量 `t` 将具有与其子句相对应的类型。
	whatAmI := func(i interface{}) {
		switch t := i.(type) {
		case bool:
			fmt.Println("我是一个布尔值")
		case int:
			fmt.Println("我是一个整数")
		default:
			fmt.Printf("不知道类型 %T\n", t)
		}
	}
	whatAmI(true)
	whatAmI(1)
	whatAmI("嘿")
}

```

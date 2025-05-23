# 时间格式化与解析

问题在于使用提供的布局在 Go 语言中格式化和解析时间。

- 使用`time`包来格式化和解析时间。
- 使用`time.RFC3339`布局来格式化和解析时间。
- 使用`Mon Jan 2 15:04:05 MST 2006`这个参考时间来展示用于格式化/解析给定时间/字符串的模式。
- 使用`Parse`函数来解析时间。
- 使用`Format`函数来格式化时间。
- 使用`fmt.Println`函数来打印格式化后的时间。
- 使用`fmt.Printf`函数来打印带有提取组件的格式化时间。

```sh
$ go run time-formatting-parsing.go
2014-04-15T18:00:15-07:00
2012-11-01 22:08:41 +0000 +0000
6:00PM
Tue Apr 15 18:00:15 2014
2014-04-15T18:00:15.161182-07:00
0000-01-01 20:41:00 +0000 UTC
2014-04-15T18:00:15-00:00
解析时间“8:41PM”为“Mon Jan _2 15:04:05 2006”时：...
```

以下是完整代码：

```go
// Go 语言通过基于模式的布局支持时间格式化和解析。

package main

import (
	"fmt"
	"time"
)

func main() {
	p := fmt.Println

	// 这是一个根据 RFC3339 格式化时间的基本示例，使用相应的布局常量。
	t := time.Now()
	p(t.Format(time.RFC3339))

	// 时间解析使用与 `Format` 相同的布局值。
	t1, e := time.Parse(
		time.RFC3339,
		"2012-11-01T22:08:41+00:00")
	p(t1)

	// `Format` 和 `Parse` 使用基于示例的布局。通常，你会为这些布局使用 `time` 包中的常量，但你也可以提供自定义布局。布局必须使用参考时间`Mon Jan 2 15:04:05 MST 2006`来展示用于格式化/解析给定时间/字符串的模式。示例时间必须与显示的完全一致：2006 年，小时为 15，星期一是一周中的某天，等等。
	p(t.Format("3:04PM"))
	p(t.Format("Mon Jan _2 15:04:05 2006"))
	p(t.Format("2006-01-02T15:04:05.999999-07:00"))
	form := "3 04 PM"
	t2, e := time.Parse(form, "8 41 PM")
	p(t2)

	// 对于纯数字表示，你也可以使用标准字符串格式化以及时间值的提取组件。
	fmt.Printf("%d-%02d-%02dT%02d:%02d:%02d-00:00\n",
		t.Year(), t.Month(), t.Day(),
		t.Hour(), t.Minute(), t.Second())

	// `Parse` 在输入格式错误时将返回一个错误，解释解析问题。
	ansic := "Mon Jan _2 15:04:05 2006"
	_, e = time.Parse(ansic, "8:41PM")
	p(e)
}

```

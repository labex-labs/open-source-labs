# 时间

以下代码包含了在 Go 语言中处理时间和时长的示例。不过，代码的某些部分缺失了。你的任务是补全代码，使其按预期运行。

- 具备 Go 编程语言的基础知识。
- 熟悉 Go 语言对时间和时长的支持。

```sh
$ go run time.go
2012-10-31 15:50:13.793654 +0000 UTC
2009-11-17 20:34:58.651387237 +0000 UTC
2009
November
17
20
34
58
651387237
UTC
Tuesday
true
false
false
25891h15m15.142266763s
25891.25420618521
1.5534752523711128e+06
9.320851514226677e+07
93208515142266763
2012-10-31 15:50:13.793654 +0000 UTC
2006-12-05 01:19:43.509120474 +0000 UTC

# 接下来我们将探讨与相对于 Unix 纪元的时间相关的概念。
```

以下是完整代码：

```go
// Go 对时间和时长提供了广泛的支持；
// 这里有一些示例。

package main

import (
	"fmt"
	"time"
)

func main() {
	p := fmt.Println

	// 我们先获取当前时间。
	now := time.Now()
	p(now)

	// 你可以通过提供年、月、日等来构建一个 `time` 结构体。时间总是与一个 `Location` 相关联，即时区。
	then := time.Date(
		2009, 11, 17, 20, 34, 58, 651387237, time.UTC)
	p(then)

	// 你可以按预期提取时间值的各个组件。
	p(then.Year())
	p(then.Month())
	p(then.Day())
	p(then.Hour())
	p(then.Minute())
	p(then.Second())
	p(then.Nanosecond())
	p(then.Location())

	// 周一到周日的 `Weekday` 也可用。
	p(then.Weekday())

	// 这些方法比较两个时间，分别测试第一个时间是否在第二个时间之前、之后或同时发生。
	p(then.Before(now))
	p(then.After(now))
	p(then.Equal(now))

	// `Sub` 方法返回一个 `Duration`，表示两个时间之间的间隔。
	diff := now.Sub(then)
	p(diff)

	// 我们可以计算时长在各种单位下的长度。
	p(diff.Hours())
	p(diff.Minutes())
	p(diff.Seconds())
	p(diff.Nanoseconds())

	// 你可以使用 `Add` 方法按给定的时长推进一个时间，或者用 `-` 按时长向后移动。
	p(then.Add(diff))
	p(then.Add(-diff))
}

```

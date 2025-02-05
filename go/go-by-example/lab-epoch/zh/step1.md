# 纪元时间

本实验要解决的问题是编写一个 Go 语言程序，该程序能够计算出自 Unix 纪元以来的秒数、毫秒数或纳秒数。

要完成本实验，你需要对 Go 语言有基本的了解，并满足以下要求：

- 熟悉 Go 语言中的 `time` 包。
- 了解如何使用 `time` 包中的 `Unix`、`UnixMilli` 和 `UnixNano` 函数。

```sh
$ go run epoch.go
2012-10-31 16:13:58.292387 +0000 UTC
1351700038
1351700038292
1351700038292387000
2012-10-31 16:13:58 +0000 UTC
2012-10-31 16:13:58.292387 +0000 UTC

# 接下来我们将看看另一个与时间相关的任务：时间
# 解析和格式化。
```

以下是完整代码：

```go
// 程序中一个常见的需求是获取自
// [Unix 纪元](https://en.wikipedia.org/wiki/Unix_time) 以来的
// 秒数、毫秒数或纳秒数。
// 这是在 Go 语言中实现的方法。

package main

import (
	"fmt"
	"time"
)

func main() {

	// 使用 `time.Now` 结合 `Unix`、`UnixMilli` 或 `UnixNano`
	// 分别获取自 Unix 纪元以来经过的秒数、
	// 毫秒数或纳秒数。
	now := time.Now()
	fmt.Println(now)

	fmt.Println(now.Unix())
	fmt.Println(now.UnixMilli())
	fmt.Println(now.UnixNano())

	// 你也可以将自纪元以来的整数秒数或纳秒数
	// 转换为相应的 `time`。
	fmt.Println(time.Unix(now.Unix(), 0))
	fmt.Println(time.Unix(0, now.UnixNano()))
}

```

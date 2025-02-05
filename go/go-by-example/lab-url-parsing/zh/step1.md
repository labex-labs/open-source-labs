# URL 解析

本实验要求解析一个示例 URL，该 URL 包含协议、认证信息、主机、端口、路径、查询参数和查询片段。解析后的 URL 应用于提取 URL 的各个组成部分。

- 应导入 `url` 和 `net` 包。
- 应解析示例 URL 并检查是否有错误。
- 应从解析后的 URL 中提取协议、认证信息、主机、端口、路径、查询参数和查询片段。
- 应使用 `SplitHostPort` 函数从 `Host` 字段中提取主机名和端口。
- 应使用 `ParseQuery` 函数将查询参数解析为一个映射。

```sh
# 运行我们的 URL 解析程序会显示我们提取的所有不同部分。
$ go run url-parsing.go
postgres
user:pass
user
pass
host.com:5432
host.com
5432
/path
f
k=v
map[k:[v]]
v

```

以下是完整代码：

```go
// URL 提供了一种 [统一的资源定位方式](https://adam.herokuapp.com/past/2010/3/30/urls_are_the_uniform_way_to_locate_resources/)。
// 以下是在 Go 中解析 URL 的方法。

package main

import (
	"fmt"
	"net"
	"net/url"
)

func main() {

	// 我们将解析这个示例 URL，它包含一个
	// 协议、认证信息、主机、端口、路径、
	// 查询参数和查询片段。
	s := "postgres://user:pass@host.com:5432/path?k=v#f"

	// 解析 URL 并确保没有错误。
	u, err := url.Parse(s)
	if err!= nil {
		panic(err)
	}

	// 访问协议很简单。
	fmt.Println(u.Scheme)

	// `User` 包含所有认证信息；调用
	// `Username` 和 `Password` 来获取单个
	// 值。
	fmt.Println(u.User)
	fmt.Println(u.User.Username())
	p, _ := u.User.Password()
	fmt.Println(p)

	// `Host` 包含主机名和端口（如果有）。使用
	// `SplitHostPort` 来提取它们。
	fmt.Println(u.Host)
	host, port, _ := net.SplitHostPort(u.Host)
	fmt.Println(host)
	fmt.Println(port)

	// 这里我们提取 `path` 和 `#` 后面的片段。
	fmt.Println(u.Path)
	fmt.Println(u.Fragment)

	// 要获取格式为 `k=v` 的查询参数字符串，
	// 使用 `RawQuery`。你也可以将查询参数
	// 解析为一个映射。解析后的查询参数字典是从
	// 字符串到字符串切片的映射，所以如果你只想要
	// 第一个值，可以索引到 `[0]`。
	fmt.Println(u.RawQuery)
	m, _ := url.ParseQuery(u.RawQuery)
	fmt.Println(m)
	fmt.Println(m["k"][0])
}

```

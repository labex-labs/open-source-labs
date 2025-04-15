# JSON

你需要完成提供的代码，以在Go语言中对JSON数据进行编码和解码。代码包含了编码和解码基本数据类型以及自定义数据类型的示例。

- 具备Go语言编程语言的基础知识。
- 熟悉在Go语言中对JSON数据进行编码和解码。
- 具备阅读和理解现有Go语言代码的能力。

```sh
# 我们在这里已经介绍了Go语言中JSON的基础知识，但是请查看
# [JSON与Go](https://go.dev/blog/json)
# 博客文章以及[JSON包文档](https://pkg.go.dev/encoding/json)
# 以获取更多信息。
```

以下是完整代码：

```go
// Go语言为JSON编码和解码提供了内置支持，
// 包括对内置和自定义数据类型的编码和解码。

package main

import (
	"encoding/json"
	"fmt"
	"os"
)

// 我们将使用这两个结构体来演示下面自定义类型的编码和解码。
type response1 struct {
	Page   int
	Fruits []string
}

// 只有导出的字段才会在JSON中进行编码/解码。
// 字段必须以大写字母开头才能被导出。
type response2 struct {
	Page   int      `json:"page"`
	Fruits []string `json:"fruits"`
}

func main() {

	// 首先，我们来看一下将基本数据类型编码为
	// JSON字符串。这里有一些原子值的示例。
	bolB, _ := json.Marshal(true)
	fmt.Println(string(bolB))

	intB, _ := json.Marshal(1)
	fmt.Println(string(intB))

	fltB, _ := json.Marshal(2.34)
	fmt.Println(string(fltB))

	strB, _ := json.Marshal("gopher")
	fmt.Println(string(strB))

	// 这里有一些切片和映射的示例，它们会按照预期编码为
	// JSON数组和对象。
	slcD := []string{"apple", "peach", "pear"}
	slcB, _ := json.Marshal(slcD)
	fmt.Println(string(slcB))

	mapD := map[string]int{"apple": 5, "lettuce": 7}
	mapB, _ := json.Marshal(mapD)
	fmt.Println(string(mapB))

	// JSON包可以自动编码你的自定义数据类型。
	// 它只会在编码输出中包含导出的字段，并且默认会
	// 使用这些名称作为JSON键。
	res1D := &response1{
		Page:   1,
		Fruits: []string{"apple", "peach", "pear"}}
	res1B, _ := json.Marshal(res1D)
	fmt.Println(string(res1B))

	// 你可以在结构体字段声明上使用标签来
	// 自定义编码后的JSON键名。查看上面
	// `response2`的定义以了解此类标签的示例。
	res2D := &response2{
		Page:   1,
		Fruits: []string{"apple", "peach", "pear"}}
	res2B, _ := json.Marshal(res2D)
	fmt.Println(string(res2B))

	// 现在让我们来看一下将JSON数据解码为Go
	// 值。这里有一个通用数据结构的示例。
	byt := []byte(`{"num":6.13,"strs":["a","b"]}`)

	// 我们需要提供一个变量，JSON包可以将解码后的数据放入其中。
	// 这个`map[string]interface{}`将保存一个字符串到任意数据类型的映射。
	var dat map[string]interface{}

	// 这是实际的解码过程，并检查相关错误。
	if err := json.Unmarshal(byt, &dat); err!= nil {
		panic(err)
	}
	fmt.Println(dat)

	// 为了使用解码后的映射中的值，
	// 我们需要将它们转换为适当的类型。
	// 例如，这里我们将`num`中的值转换为
	// 预期的`float64`类型。
	num := dat["num"].(float64)
	fmt.Println(num)

	// 访问嵌套数据需要一系列转换。
	strs := dat["strs"].([]interface{})
	str1 := strs[0].(string)
	fmt.Println(str1)

	// 我们也可以将JSON解码为自定义数据类型。
	// 这具有为我们的程序添加额外类型安全性的优点，
	// 并且在访问解码后的数据时无需进行类型断言。
	str := `{"page": 1, "fruits": ["apple", "peach"]}`
	res := response2{}
	json.Unmarshal([]byte(str), &res)
	fmt.Println(res)
	fmt.Println(res.Fruits[0])

	// 在上面的示例中，我们总是使用字节和
	// 字符串作为数据与标准输出上的JSON表示之间的中间介质。
	// 我们也可以将JSON编码直接流式传输到`os.Writer`，
	// 如`os.Stdout`，甚至HTTP响应体。
	enc := json.NewEncoder(os.Stdout)
	d := map[string]int{"apple": 5, "lettuce": 7}
	enc.Encode(d)
}

```

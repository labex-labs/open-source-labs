# 文本模板

在这个实验中，你需要演示如何使用`text/template`包来生成动态内容。

- 使用`text/template`包生成动态内容。
- 使用`template.Must`函数，以便在`Parse`返回错误时引发恐慌。
- 使用`{{.FieldName}}`操作来访问结构体字段。
- 使用`{{if.. -}} yes {{else -}} no {{end}}\n`操作来为模板提供条件执行。
- 使用`{{range.}}{{.}} {{end}}\n`操作来遍历切片、数组、映射或通道。

```sh
$ go run templates.go
值: some text
值: 5
值: [Go Rust C++ C#]
姓名: Jane Doe
姓名: Mickey Mouse
是
否
遍历: Go Rust C++ C#
```

以下是完整代码：

```go
// Go通过`text/template`包提供了对创建动态内容或向用户展示定制化输出的内置支持。一个名为`html/template`的姊妹包提供相同的API，但具有额外的安全特性，应用于生成HTML。

package main

import (
	"os"
	"text/template"
)

func main() {

	// 我们可以创建一个新模板，并从字符串解析其主体。
	// 模板是静态文本和包含在`{{...}}`中的“操作”的混合，用于动态插入内容。
	t1 := template.New("t1")
	t1, err := t1.Parse("值是 {{.}}\n")
	if err!= nil {
		panic(err)
	}

	// 或者，我们可以使用`template.Must`函数，以便在`Parse`返回错误时引发恐慌。这在全局作用域中初始化的模板中特别有用。
	t1 = template.Must(t1.Parse("值: {{.}}\n"))

	// 通过“执行”模板，我们使用其操作的特定值生成其文本。`{{.}}`操作被替换为作为参数传递给`Execute`的值。
	t1.Execute(os.Stdout, "some text")
	t1.Execute(os.Stdout, 5)
	t1.Execute(os.Stdout, []string{
		"Go",
		"Rust",
		"C++",
		"C#",
	})

	// 我们将在下面使用的辅助函数。
	Create := func(name, t string) *template.Template {
		return template.Must(template.New(name).Parse(t))
	}

	// 如果数据是结构体，我们可以使用`{{.FieldName}}`操作来访问其字段。在执行模板时，字段应导出才能访问。
	t2 := Create("t2", "姓名: {{.Name}}\n")

	t2.Execute(os.Stdout, struct {
		Name string
	}{"Jane Doe"})

	// 映射也是如此；对于映射，键名的大小写没有限制。
	t2.Execute(os.Stdout, map[string]string{
		"Name": "Mickey Mouse",
	})

	// if/else为模板提供条件执行。如果值是类型的默认值，例如0、空字符串、空指针等，则该值被视为假。
	// 此示例演示了模板的另一个特性：在操作中使用`-`来修剪空白。
	t3 := Create("t3",
		"{{if.. -}} 是 {{else -}} 否 {{end}}\n")
	t3.Execute(os.Stdout, "not empty")
	t3.Execute(os.Stdout, "")

	// range块让我们遍历切片、数组、映射或通道。在range块内，`{{.}}`被设置为迭代的当前项。
	t4 := Create("t4",
		"遍历: {{range.}}{{.}} {{end}}\n")
	t4.Execute(os.Stdout,
		[]string{
			"Go",
			"Rust",
			"C++",
			"C#",
		})
}

```

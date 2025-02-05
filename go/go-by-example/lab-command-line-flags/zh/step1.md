# 命令行标志

实现一个 Go 语言程序，该程序解析命令行标志并输出解析后的选项以及任何尾随的位置参数。该程序应支持以下标志：

- `word`：一个字符串标志，默认值为 `"foo"`。
- `numb`：一个整数标志，默认值为 `42`。
- `fork`：一个布尔标志，默认值为 `false`。
- `svar`：一个字符串标志，它使用在程序其他地方声明的现有变量。

- 程序应使用 `flag` 包来解析命令行标志。
- 程序应输出解析后的选项以及任何尾随的位置参数。
- 程序应支持如上所述的 `word`、`numb`、`fork` 和 `svar` 标志。

```sh
# 要试验命令行标志程序，最好先编译它，然后直接运行生成的二进制文件。
$ go build command-line-flags.go

# 通过首先为所有标志提供值来试用构建好的程序。
$./command-line-flags -word=opt -numb=7 -fork -svar=flag
word: opt
numb: 7
fork: true
svar: flag
tail: []

# 请注意，如果省略标志，它们将自动采用默认值。
$./command-line-flags -word=opt
word: opt
numb: 42
fork: false
svar: bar
tail: []

# 尾随的位置参数可以在任何标志之后提供。
$./command-line-flags -word=opt a1 a2 a3
word: opt
...
tail: [a1 a2 a3]

# 请注意，`flag` 包要求所有标志出现在位置参数之前（否则标志将被解释为位置参数）。
$./command-line-flags -word=opt a1 a2 a3 -numb=7
word: opt
numb: 42
fork: false
svar: bar
tail: [a1 a2 a3 -numb=7]

# 使用 `-h` 或 `--help` 标志来获取命令行程序自动生成的帮助文本。
$./command-line-flags -h
Usage of./command-line-flags:
-fork=false: a bool
-numb=42: an int
-svar="bar": a string var
-word="foo": a string

# 如果你提供了一个未在 `flag` 包中指定的标志，程序将打印错误消息并再次显示帮助文本。
$./command-line-flags -wat
flag provided but not defined: -wat
Usage of./command-line-flags:
...
```

以下是完整代码：

```go
// [_命令行标志_](https://en.wikipedia.org/wiki/Command-line_interface#Command-line_option)
// 是为命令行程序指定选项的常用方式。例如，在 `wc -l` 中，`-l` 就是一个命令行标志。

package main

// Go 提供了一个 `flag` 包，支持基本的命令行标志解析。我们将使用这个包来实现我们的示例命令行程序。
import (
	"flag"
	"fmt"
)

func main() {

	// 基本的标志声明可用于字符串、整数和布尔选项。这里我们声明一个字符串标志 `word`，默认值为 `"foo"`，并给出简短描述。这个 `flag.String` 函数返回一个字符串指针（不是字符串值）；我们将在下面看到如何使用这个指针。
	wordPtr := flag.String("word", "foo", "a string")

	// 这使用与 `word` 标志类似的方法声明了 `numb` 和 `fork` 标志。
	numbPtr := flag.Int("numb", 42, "an int")
	forkPtr := flag.Bool("fork", false, "a bool")

	// 也可以声明一个使用在程序其他地方声明的现有变量的选项。请注意，我们需要传入一个指向标志声明函数的指针。
	var svar string
	flag.StringVar(&svar, "svar", "bar", "a string var")

	// 一旦所有标志都声明完毕，调用 `flag.Parse()` 来执行命令行解析。
	flag.Parse()

	// 这里我们将直接输出解析后的选项以及任何尾随的位置参数。请注意，我们需要使用例如 `*wordPtr` 来解引用指针以获取实际的选项值。
	fmt.Println("word:", *wordPtr)
	fmt.Println("numb:", *numbPtr)
	fmt.Println("fork:", *forkPtr)
	fmt.Println("svar:", svar)
	fmt.Println("tail:", flag.Args())
}

```

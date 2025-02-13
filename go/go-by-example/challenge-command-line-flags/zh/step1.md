# 命令行标志

实现一个 Go 语言程序，该程序解析命令行标志并输出解析后的选项以及任何尾随的位置参数。该程序应支持以下标志：

- `word`：一个字符串标志，默认值为 `"foo"`。
- `numb`：一个整数标志，默认值为 `42`。
- `fork`：一个布尔标志，默认值为 `false`。
- `svar`：一个字符串标志，它使用在程序其他地方声明的现有变量。

## 要求

- 程序应使用 `flag` 包来解析命令行标志。
- 程序应输出解析后的选项以及任何尾随的位置参数。
- 程序应支持上述的 `word`、`numb`、`fork` 和 `svar` 标志。

## 示例

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

# 如果提供了 `flag` 包中未指定的标志，程序将打印错误消息并再次显示帮助文本。
$./command-line-flags -wat
flag provided but not defined: -wat
Usage of./command-line-flags:
...
```

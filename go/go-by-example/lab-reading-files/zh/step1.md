# 读取文件

你需要在Go程序中读取文件，并对文件中的数据执行不同的操作。

- 你应该熟悉基本的Go编程概念。
- 你的计算机上应安装了Go。

```sh
$ echo "hello" > /tmp/dat
$ echo "go" >> /tmp/dat
$ go run reading-files.go
hello
go
5字节: hello
2字节 @ 6: go
2字节 @ 6: go
5字节: hello

# 接下来我们将看看如何写入文件。
```

以下是完整代码：

```go
// 读取和写入文件是许多Go程序所需的基本任务。首先我们来看一些读取文件的示例。

package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
)

// 读取文件时需要检查大多数调用是否出错。
// 这个辅助函数将简化我们下面的错误检查。
func check(e error) {
    if e!= nil {
        panic(e)
    }
}

func main() {

    // 也许最基本的文件读取任务是
    // 将文件的全部内容读入内存。
    dat, err := os.ReadFile("/tmp/dat")
    check(err)
    fmt.Print(string(dat))

    // 你通常会希望对如何读取文件以及读取文件的哪些部分有更多控制。对于这些任务，
    // 首先通过`Open`打开一个文件以获得一个`os.File`值。
    f, err := os.Open("/tmp/dat")
    check(err)

    // 从文件开头读取一些字节。
    // 最多允许读取5个字节，但也要注意实际读取的字节数。
    b1 := make([]byte, 5)
    n1, err := f.Read(b1)
    check(err)
    fmt.Printf("%d字节: %s\n", n1, string(b1[:n1]))

    // 你也可以`Seek`到文件中的已知位置并从那里`Read`。
    o2, err := f.Seek(6, 0)
    check(err)
    b2 := make([]byte, 2)
    n2, err := f.Read(b2)
    check(err)
    fmt.Printf("%d字节 @ %d: ", n2, o2)
    fmt.Printf("%v\n", string(b2[:n2]))

    // `io`包提供了一些可能对文件读取有帮助的函数。例如，
    // 像上面那样的读取可以用`ReadAtLeast`更健壮地实现。
    o3, err := f.Seek(6, 0)
    check(err)
    b3 := make([]byte, 2)
    n3, err := io.ReadAtLeast(f, b3, 2)
    check(err)
    fmt.Printf("%d字节 @ %d: %s\n", n3, o3, string(b3))

    // 没有内置的倒带功能，但`Seek(0, 0)`可以实现这一点。
    _, err = f.Seek(0, 0)
    check(err)

    // `bufio`包实现了一个带缓冲的读取器，
    // 它对于许多小读取的效率以及它提供的额外读取方法可能都很有用。
    r4 := bufio.NewReader(f)
    b4, err := r4.Peek(5)
    check(err)
    fmt.Printf("5字节: %s\n", string(b4))

    // 完成后关闭文件（通常这会在`Open`后立即用`defer`安排）。
    f.Close()
}

```

# 派生进程

本实验要求实现一个 Go 程序，该程序能够派生外部进程并收集其输出。

- 程序应能够派生外部进程。
- 程序应能够收集外部进程的输出。
- 程序应处理外部进程执行期间可能出现的错误。

```sh
# 派生的程序返回的输出与我们直接从命令行运行它们时相同。
$ go run spawning-processes.go
> date
2022年5月5日 星期四 晚上10:10:12 太平洋夏令时

# date 没有 `-x` 标志，因此它将以错误消息和非零返回码退出。
命令以返回码 rc = 1 退出
hello > grep
hello grep

-a > ls -l -h
drwxr-xr-x 4 mark 136B 10月3日 16:29.
drwxr-xr-x 91 mark 3.0K 10月3日 12:50..
-rw-r--r-- 1 mark 1.3K 10月3日 16:28 spawning-processes.go
```

以下是完整代码：

```go
// 有时我们的 Go 程序需要派生其他非 Go 进程。

package main

import (
	"fmt"
	"io"
	"os/exec"
)

func main() {

	// 我们先从一个简单的命令开始，该命令不接受参数或输入，只向标准输出打印一些内容。`exec.Command` 助手创建一个对象来表示这个外部进程。
	dateCmd := exec.Command("date")

	// `Output` 方法运行命令，等待它完成并收集其标准输出。
	// 如果没有错误，`dateOut` 将包含日期信息的字节。
	dateOut, err := dateCmd.Output()
	if err!= nil {
		panic(err)
	}
	fmt.Println("> date")
	fmt.Println(string(dateOut))

	// 如果执行命令时出现问题（例如路径错误），`Output` 和 `Command` 的其他方法将返回 `*exec.Error`，
	// 如果命令运行但以非零返回码退出，则返回 `*exec.ExitError`。
	_, err = exec.Command("date", "-x").Output()
	if err!= nil {
		switch e := err.(type) {
		case *exec.Error:
			fmt.Println("执行失败：", err)
		case *exec.ExitError:
			fmt.Println("命令退出返回码 =", e.ExitCode())
		default:
			panic(err)
		}
	}

	// 接下来我们看一个稍微复杂一点的情况，我们将数据通过标准输入管道传输到外部进程，并从其标准输出收集结果。
	grepCmd := exec.Command("grep", "hello")

	// 在这里，我们显式地获取输入/输出管道，启动进程，向其写入一些输入，读取结果输出，最后等待进程退出。
	grepIn, _ := grepCmd.StdinPipe()
	grepOut, _ := grepCmd.StdoutPipe()
	grepCmd.Start()
	grepIn.Write([]byte("hello grep\ngoodbye grep"))
	grepIn.Close()
	grepBytes, _ := io.ReadAll(grepOut)
	grepCmd.Wait()

	// 我们在上面的示例中省略了错误检查，但你可以对所有这些操作使用通常的 `if err!= nil` 模式。我们也只收集了 `StdoutPipe` 的结果，但你可以用完全相同的方式收集 `StderrPipe` 的结果。
	fmt.Println("> grep hello")
	fmt.Println(string(grepBytes))

	// 请注意，在派生命令时，我们需要提供一个明确划分的命令和参数数组，而不是只传入一个命令行字符串。如果你想用一个字符串派生一个完整的命令，可以使用 `bash` 的 `-c` 选项：
	lsCmd := exec.Command("bash", "-c", "ls -a -l -h")
	lsOut, err := lsCmd.Output()
	if err!= nil {
		panic(err)
	}
	fmt.Println("> ls -a -l -h")
	fmt.Println(string(lsOut))
}

```

# 执行进程

问题在于用另一个进程（比如非 Go 进程）替换当前的 Go 进程。

- Go 编程语言
- 对 Go 语言的 `exec` 函数有基本了解
- 熟悉环境变量

```sh
# 当我们运行程序时，它会被 `ls` 替换。
$ go run execing-processes.go
total 16
drwxr-xr-x 4 mark 136B Oct 3 16:29.
drwxr-xr-x 91 mark 3.0K Oct 3 12:50..
-rw-r--r-- 1 mark 1.3K Oct 3 16:28 execing-processes.go

# 注意，Go 语言没有提供经典的 Unix `fork` 函数。不过通常这不是问题，因为启动 goroutine、生成进程以及执行进程涵盖了 `fork` 的大多数用例。
```

以下是完整代码：

```go
// 在之前的示例中，我们研究了 [生成外部进程](spawning-processes)。当我们需要一个正在运行的 Go 进程能够访问外部进程时，就会这样做。有时我们只是想用另一个（可能是非 Go 的）进程完全替换当前的 Go 进程。为此，我们将使用 Go 语言对经典的
// <a href="https://en.wikipedia.org/wiki/Exec_(operating_system)"><code>exec</code></a>
// 函数的实现。

package main

import (
	"os"
	"os/exec"
	"syscall"
)

func main() {

	// 对于我们的示例，我们将执行 `ls`。Go 语言要求我们提供要执行的二进制文件的绝对路径，所以我们将使用 `exec.LookPath` 来查找它（可能是 `/bin/ls`）。
	binary, lookErr := exec.LookPath("ls")
	if lookErr!= nil {
		panic(lookErr)
	}

	// `Exec` 要求参数以切片形式提供（而不是一个大字符串）。我们将给 `ls` 一些常见参数。请注意，第一个参数应该是程序名。
	args := []string{"ls", "-a", "-l", "-h"}

	// `Exec` 还需要一组 [环境变量](environment-variables) 来使用。这里我们只提供当前环境。
	env := os.Environ()

	// 这是实际的 `syscall.Exec` 调用。如果此调用成功，我们的进程执行将在此处结束，并被 `/bin/ls -a -l -h` 进程替换。如果有错误，我们将得到一个返回值。
	execErr := syscall.Exec(binary, args, env)
	if execErr!= nil {
		panic(execErr)
	}
}

```

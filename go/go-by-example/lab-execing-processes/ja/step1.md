# プロセスの実行

問題は、現在の Go プロセスを別のプロセス（たとえば非 Go プロセス）に置き換えることです。

- Go 言語
- Go の `exec` 関数の基本知識
- 環境変数に慣れていること

```sh
# 私たちのプログラムを実行すると、`ls` に置き換えられます。
$ go run execing-processes.go
total 16
drwxr-xr-x 4 mark 136B Oct 3 16:29.
drwxr-xr-x 91 mark 3.0K Oct 3 12:50..
-rw-r--r-- 1 mark 1.3K Oct 3 16:28 execing-processes.go

# 注意：Go には古典的な Unix の `fork` 関数はありません。
# 通常は問題になりません。なぜなら、ゴルーチンの起動、
# プロセスの生成、およびプロセスの実行は、
# `fork` のほとんどのユースケースをカバーしているからです。
```

以下が完全なコードです：

```go
// 前の例では、[外部プロセスの生成](spawning-processes) を見ました。
// 実行中の Go プロセスがアクセスできる外部プロセスが必要な場合に行います。
// 時々、私たちはただ現在の Go プロセスを別の（おそらく非 Go）プロセスに
// 完全に置き換えたいだけです。これを行うには、古典的な
// <a href="https://en.wikipedia.org/wiki/Exec_(operating_system)"><code>exec</code></a>
// 関数の Go 実装を使用します。

package main

import (
	"os"
	"os/exec"
	"syscall"
)

func main() {

	// 私たちの例では、`ls` を実行します。Go は実行したいバイナリの
	// 絶対パスを必要とするため、`exec.LookPath` を使って見つけます
	// （おそらく `/bin/ls`）。
	binary, lookErr := exec.LookPath("ls")
	if lookErr!= nil {
		panic(lookErr)
	}

	// `Exec` にはスライス形式の引数が必要です（1 つの大きな文字列とは
	// 対照的）。私たちは `ls` にいくつかの一般的な引数を与えます。
	// 最初の引数はプログラム名であることに注意してください。
	args := []string{"ls", "-a", "-l", "-h"}

	// `Exec` には使用する [環境変数](environment-variables) のセットも必要です。
	// ここでは、現在の環境をそのまま提供します。
	env := os.Environ()

	// ここが実際の `syscall.Exec` 呼び出しです。この呼び出しが成功すると、
	// 私たちのプロセスの実行はここで終了し、`/bin/ls -a -l -h` プロセスに
	// 置き換えられます。エラーがある場合は戻り値が返されます。
	execErr := syscall.Exec(binary, args, env)
	if execErr!= nil {
		panic(execErr)
	}
}

```

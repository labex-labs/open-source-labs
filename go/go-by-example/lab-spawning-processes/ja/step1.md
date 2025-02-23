# プロセスの生成

この実験では、外部プロセスを生成してその出力を収集する Go プログラムの実装が必要です。

- プログラムは外部プロセスを生成できる必要があります。
- プログラムは外部プロセスの出力を収集できる必要があります。
- プログラムは外部プロセスの実行中に発生する可能性のあるエラーを処理する必要があります。

```sh
# 生成されたプログラムは、コマンドラインから直接実行した場合と同じ出力を返します。
$ go run spawning-processes.go
> date
Thu 05 May 2022 10:10:12 PM PDT

# date には `-x` フラグがないため、エラーメッセージと非ゼロの戻りコードで終了します。
command exited with rc = 1
hello > grep
hello grep

-a > ls -l -h
drwxr-xr-x 4 mark 136B Oct 3 16:29.
drwxr-xr-x 91 mark 3.0K Oct 3 12:50..
-rw-r--r-- 1 mark 1.3K Oct 3 16:28 spawning-processes.go
```

以下に完全なコードがあります：

```go
// 時々、私たちの Go プログラムは他の非 Go プロセスを生成する必要があります。

package main

import (
	"fmt"
	"io"
	"os/exec"
)

func main() {

	// 最初に、引数や入力を必要とせず、単に何かを標準出力に出力する簡単なコマンドから始めます。`exec.Command` ヘルパーは、この外部プロセスを表すオブジェクトを作成します。
	dateCmd := exec.Command("date")

	// `Output` メソッドはコマンドを実行し、終了するのを待ち、その標準出力を収集します。エラーがなければ、`dateOut` に日付情報のバイトが格納されます。
	dateOut, err := dateCmd.Output()
	if err!= nil {
		panic(err)
	}
	fmt.Println("> date")
	fmt.Println(string(dateOut))

	// `Output` や `Command` の他のメソッドは、コマンドの実行に問題があった場合（たとえば、パスが間違っている場合）に `*exec.Error` を返し、コマンドが実行されたが非ゼロの戻りコードで終了した場合に `*exec.ExitError` を返します。
	_, err = exec.Command("date", "-x").Output()
	if err!= nil {
		switch e := err.(type) {
		case *exec.Error:
			fmt.Println("failed executing:", err)
		case *exec.ExitError:
			fmt.Println("command exit rc =", e.ExitCode())
		default:
			panic(err)
		}
	}

	// 次に、もう少し複雑なケースを見てみましょう。ここでは、外部プロセスの `stdin` にデータをパイプし、`stdout` から結果を収集します。
	grepCmd := exec.Command("grep", "hello")

	// ここでは明示的に入力/出力パイプを取得し、プロセスを開始し、いくつかの入力を書き込み、結果の出力を読み取り、最後にプロセスが終了するのを待ちます。
	grepIn, _ := grepCmd.StdinPipe()
	grepOut, _ := grepCmd.StdoutPipe()
	grepCmd.Start()
	grepIn.Write([]byte("hello grep\ngoodbye grep"))
	grepIn.Close()
	grepBytes, _ := io.ReadAll(grepOut)
	grepCmd.Wait()

	// 上の例ではエラーチェックを省略しましたが、すべてに対して通常の `if err!= nil` パターンを使用できます。また、`StdoutPipe` の結果のみを収集していますが、`StderrPipe` もまったく同じ方法で収集できます。
	fmt.Println("> grep hello")
	fmt.Println(string(grepBytes))

	// コマンドを生成する際には、明示的に区切られたコマンドと引数の配列を提供する必要があります。コマンドライン文字列を 1 つだけ渡せるわけではありません。文字列を使って完全なコマンドを生成する場合は、`bash` の `-c` オプションを使用できます：
	lsCmd := exec.Command("bash", "-c", "ls -a -l -h")
	lsOut, err := lsCmd.Output()
	if err!= nil {
		panic(err)
	}
	fmt.Println("> ls -a -l -h")
	fmt.Println(string(lsOut))
}

```

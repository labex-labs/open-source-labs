# チャネルの方向付け

この実験で解くべき問題は、与えられたコードを修正して、関数パラメータとして使用されるチャネルが値の送信のみまたは受信のみに指定されるようにすることです。

- Go言語の基本知識
- チャネルとそのGo言語における使用方法の理解

```sh
$ go run channel-directions.go
passed message
```

以下に完全なコードがあります。

```go
// チャネルを関数パラメータとして使用する場合、
// チャネルが値の送信のみまたは受信のみを行うように指定できます。
// この特定性により、プログラムの型安全性が向上します。

package main

import "fmt"

// この`ping`関数は値の送信のみを行うチャネルのみを受け付けます。
// このチャネルで受信を試みるとコンパイル時エラーになります。
func ping(pings chan<- string, msg string) {
	pings <- msg
}

// `pong`関数は受信用の1つのチャネル(`pings`)と送信用の2番目のチャネル(`pongs`)を受け付けます。
func pong(pings <-chan string, pongs chan<- string) {
	msg := <-pings
	pongs <- msg
}

func main() {
	pings := make(chan string, 1)
	pongs := make(chan string, 1)
	ping(pings, "passed message")
	pong(pings, pongs)
	fmt.Println(<-pongs)
}

```

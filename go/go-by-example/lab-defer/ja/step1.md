# defer

この実験では、`defer` を使ってファイルを作成し、そこに書き込み、終了したら閉じる必要があります。

- `createFile` 関数は、指定されたパスでファイルを作成し、そのファイルへのポインタを返す必要があります。
- `writeFile` 関数は、文字列 "data" をファイルに書き込む必要があります。
- `closeFile` 関数は、ファイルを閉じ、エラーをチェックする必要があります。

```sh
# プログラムを実行すると、書き込み後にファイルが閉じていることが確認できます。
$ go run defer.go
creating
writing
closing
```

以下が完全なコードです：

```go
// _Defer_ は、通常はクリーンアップの目的で、プログラムの実行の後半で関数呼び出しが行われることを保証するために使用されます。`defer` は、他の言語では `ensure` や `finally` が使用される場所でよく使用されます。

package main

import (
	"fmt"
	"os"
)

// ファイルを作成し、そこに書き込み、終了したら閉じたいとしましょう。これを `defer` を使って行う方法を以下に示します。
func main() {

	// `createFile` でファイルオブジェクトを取得した直後、`closeFile` でそのファイルのクローズを延期します。これは、囲まれた関数 (`main`) の終了時に、`writeFile` が終了した後に実行されます。
	f := createFile("/tmp/defer.txt")
	defer closeFile(f)
	writeFile(f)
}

func createFile(p string) *os.File {
	fmt.Println("creating")
	f, err := os.Create(p)
	if err!= nil {
		panic(err)
	}
	return f
}

func writeFile(f *os.File) {
	fmt.Println("writing")
	fmt.Fprintln(f, "data")

}

func closeFile(f *os.File) {
	fmt.Println("closing")
	err := f.Close()
	// ファイルを閉じるときには、エラーをチェックすることが重要です。延期された関数であっても同様です。
	if err!= nil {
		fmt.Fprintf(os.Stderr, "error: %v\n", err)
		os.Exit(1)
	}
}

```

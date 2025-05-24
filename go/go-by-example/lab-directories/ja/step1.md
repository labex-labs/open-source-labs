# ディレクトリ

現在の作業ディレクトリに新しいサブディレクトリを作成し、親ディレクトリを含むディレクトリ階層を作成し、ディレクトリの内容を一覧表示し、現在の作業ディレクトリを変更し、再帰的にディレクトリを訪問する Go プログラムを作成します。

- 現在の作業ディレクトリに新しいサブディレクトリを作成します。
- 一時的なディレクトリを作成する場合、削除を`defer`で行うのが良い作法です。`os.RemoveAll`は、ディレクトリツリー全体を削除します（`rm -rf`と同様）。
- `MkdirAll`を使って、親ディレクトリを含むディレクトリ階層を作成します。これはコマンドラインの`mkdir -p`に似ています。
- `ReadDir`はディレクトリの内容を一覧表示し、`os.DirEntry`オブジェクトのスライスを返します。
- `Chdir`を使って、現在の作業ディレクトリを変更できます。これは`cd`と同様です。
- 再帰的にディレクトリを訪問し、そのサブディレクトリすべてを含めます。`Walk`は、訪問されるすべてのファイルまたはディレクトリを処理するためのコールバック関数を受け取ります。

```sh
$ go run directories.go
Listing subdir/parent
child true
file2 false
file3 false
Listing subdir/parent/child
file4 false
Visiting subdir
subdir true
subdir/file1 false
subdir/parent true
subdir/parent/child true
subdir/parent/child/file4 false
subdir/parent/file2 false
subdir/parent/file3 false
```

以下が完全なコードです：

```go
// Go は、ファイルシステム内の*ディレクトリ*を操作するためのいくつかの便利な関数を持っています。

package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func check(e error) {
	if e!= nil {
		panic(e)
	}
}

func main() {

	// 現在の作業ディレクトリに新しいサブディレクトリを作成します。
	err := os.Mkdir("subdir", 0755)
	check(err)

	// 一時的なディレクトリを作成する場合、削除を `defer` で行うのが良い作法です。`os.RemoveAll` は、ディレクトリツリー全体を削除します（`rm -rf`と同様）。
	defer os.RemoveAll("subdir")

	// 新しい空のファイルを作成するためのヘルパー関数。
	createEmptyFile := func(name string) {
		d := []byte("")
		check(os.WriteFile(name, d, 0644))
	}

	createEmptyFile("subdir/file1")

	// `MkdirAll` を使って、親ディレクトリを含むディレクトリ階層を作成します。これはコマンドラインの`mkdir -p`に似ています。
	err = os.MkdirAll("subdir/parent/child", 0755)
	check(err)

	createEmptyFile("subdir/parent/file2")
	createEmptyFile("subdir/parent/file3")
	createEmptyFile("subdir/parent/child/file4")

	// `ReadDir` はディレクトリの内容を一覧表示し、`os.DirEntry` オブジェクトのスライスを返します。
	c, err := os.ReadDir("subdir/parent")
	check(err)

	fmt.Println("Listing subdir/parent")
	for _, entry := range c {
		fmt.Println(" ", entry.Name(), entry.IsDir())
	}

	// `Chdir` を使って、現在の作業ディレクトリを変更できます。これは `cd` と同様です。
	err = os.Chdir("subdir/parent/child")
	check(err)

	// 現在のディレクトリを一覧表示するときに、`subdir/parent/child` の内容が表示されます。
	c, err = os.ReadDir(".")
	check(err)

	fmt.Println("Listing subdir/parent/child")
	for _, entry := range c {
		fmt.Println(" ", entry.Name(), entry.IsDir())
	}

	// 元の場所に `cd` します。
	err = os.Chdir("../../..")
	check(err)

	// 再帰的にディレクトリを訪問し、そのサブディレクトリすべてを含めることもできます。`Walk` は、訪問されるすべてのファイルまたはディレクトリを処理するためのコールバック関数を受け取ります。
	fmt.Println("Visiting subdir")
	err = filepath.Walk("subdir", visit)
}

// `visit` は、`filepath.Walk` によって再帰的に見つけられたすべてのファイルまたはディレクトリに対して呼び出されます。
func visit(p string, info os.FileInfo, err error) error {
	if err!= nil {
		return err
	}
	fmt.Println(" ", p, info.IsDir())
	return nil
}

```

# 一時ファイルとディレクトリ

この実験では、Go 言語で一時ファイルとディレクトリを作成する必要があります。

- `os.CreateTemp` を使用して一時ファイルを作成します。
- `os.MkdirTemp` を使用して一時ディレクトリを作成します。
- `os.RemoveAll` を使用して一時ディレクトリを削除します。
- `os.WriteFile` を使用してファイルにデータを書き込みます。

```sh
$ go run temporary-files-and-directories.go
Temp file name: /tmp/sample610887201
Temp dir name: /tmp/sampledir898854668
```

以下に完全なコードを示します。

```go
// プログラムの実行中、プログラムが終了した後に必要ないデータを作成することがよくあります。
// *一時ファイルとディレクトリ*はこの目的に役立ちます。なぜなら、時間の経過とともにファイルシステムを汚染しないからです。

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

	// 一時ファイルを作成する最も簡単な方法は、`os.CreateTemp` を呼び出すことです。
	// これはファイルを作成し、読み書き用に開きます。最初の引数として `""` を提供することで、
	// `os.CreateTemp` は OS の既定の場所にファイルを作成します。
	f, err := os.CreateTemp("", "sample")
	check(err)

	// 一時ファイルの名前を表示します。Unix 系の OS では、ディレクトリはおそらく `/tmp` になります。
	// ファイル名は、`os.CreateTemp` の 2 番目の引数として与えられた接頭辞から始まり、
	// 残りは自動的に選択されて、同時実行時に常に異なるファイル名が作成されるようにします。
	fmt.Println("Temp file name:", f.Name())

	// 終了後にファイルをクリーンアップします。OS はおそらく一定時間後に自動的に一時ファイルをクリーンアップしますが、
	// 明示的に行うのが良い慣例です。
	defer os.Remove(f.Name())

	// ファイルにいくつかのデータを書き込むことができます。
	_, err = f.Write([]byte{1, 2, 3, 4})
	check(err)

	// 一時ファイルを多数作成する予定の場合、一時 *ディレクトリ* を作成する方が好ましい場合があります。
	// `os.MkdirTemp` の引数は `CreateTemp` と同じですが、オープンファイルではなくディレクトリ *名* を返します。
	dname, err := os.MkdirTemp("", "sampledir")
	check(err)
	fmt.Println("Temp dir name:", dname)

	defer os.RemoveAll(dname)

	// これで、一時ディレクトリの接頭辞を付けて一時ファイル名を合成することができます。
	fname := filepath.Join(dname, "file1")
	err = os.WriteFile(fname, []byte{1, 2}, 0666)
	check(err)
}

```

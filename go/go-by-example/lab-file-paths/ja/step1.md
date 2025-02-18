# ファイルパス

この実験では、`filepath` パッケージを使用して、ファイルパスに対するさまざまな操作を行います。たとえば、移植可能な方法でパスを構築したり、パスをディレクトリとファイルのコンポーネントに分割したり、パスが絶対パスかどうかを確認したり、ファイルの拡張子を見つけたり、2 つのパス間の相対パスを見つけたりします。

- `Join` を使用して、移植可能な方法でパスを構築します。
- `Dir` と `Base` を使用して、パスをディレクトリとファイルのコンポーネントに分割します。
- `IsAbs` を使用して、パスが絶対パスかどうかを確認します。
- `Ext` を使用して、ファイルの拡張子を見つけます。
- `TrimSuffix` を使用して、ファイル名から拡張子を削除します。
- `Rel` を使用して、2 つのパス間の相対パスを見つけます。

```sh
$ go run file-paths.go
p: dir1/dir2/filename
dir1/filename
dir1/filename
Dir(p): dir1/dir2
Base(p): filename
false
true
.json
config
t/file
../c/t/file

```

以下に完全なコードがあります。

```go
// The `filepath` package provides functions to parse
// and construct *file paths* in a way that is portable
// between operating systems; `dir/file` on Linux vs.
// `dir\file` on Windows, for example.
package main

import (
	"fmt"
	"path/filepath"
	"strings"
)

func main() {

	// `Join` should be used to construct paths in a
	// portable way. It takes any number of arguments
	// and constructs a hierarchical path from them.
	p := filepath.Join("dir1", "dir2", "filename")
	fmt.Println("p:", p)

	// You should always use `Join` instead of
	// concatenating `/`s or `\`s manually. In addition
	// to providing portability, `Join` will also
	// normalize paths by removing superfluous separators
	// and directory changes.
	fmt.Println(filepath.Join("dir1//", "filename"))
	fmt.Println(filepath.Join("dir1/../dir1", "filename"))

	// `Dir` and `Base` can be used to split a path to the
	// directory and the file. Alternatively, `Split` will
	// return both in the same call.
	fmt.Println("Dir(p):", filepath.Dir(p))
	fmt.Println("Base(p):", filepath.Base(p))

	// We can check whether a path is absolute.
	fmt.Println(filepath.IsAbs("dir/file"))
	fmt.Println(filepath.IsAbs("/dir/file"))

	filename := "config.json"

	// Some file names have extensions following a dot. We
	// can split the extension out of such names with `Ext`.
	ext := filepath.Ext(filename)
	fmt.Println(ext)

	// To find the file's name with the extension removed,
	// use `strings.TrimSuffix`.
	fmt.Println(strings.TrimSuffix(filename, ext))

	// `Rel` finds a relative path between a *base* and a
	// *target*. It returns an error if the target cannot
	// be made relative to base.
	rel, err := filepath.Rel("a/b", "a/b/t/file")
	if err!= nil {
		panic(err)
	}
	fmt.Println(rel)

	rel, err = filepath.Rel("a/b", "a/c/t/file")
	if err!= nil {
		panic(err)
	}
	fmt.Println(rel)
}

```

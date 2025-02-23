# コマンドラインのサブコマンド

2つのサブコマンド `foo` と `bar` をサポートするプログラムを作成する必要があります。それぞれには独自のフラグのセットがあります。`foo` サブコマンドには `enable` と `name` の2つのフラグがあり、`bar` サブコマンドには `level` の1つのフラグがあります。

- プログラムは `flag` パッケージを使用してフラグを定義して解析する必要があります。
- `foo` サブコマンドには `enable` と `name` の2つのフラグがあり、どちらも文字列型です。
- `bar` サブコマンドには `level` の1つのフラグがあり、整数型です。
- 無効なサブコマンドが提供された場合、プログラムはエラーメッセージを表示する必要があります。
- プログラムは、呼び出されたサブコマンドのフラグの値を表示する必要があります。

```sh
$ go build command-line-subcommands.go

# まずは foo サブコマンドを呼び出します。
$./command-line-subcommands foo -enable -name=joe a1 a2
サブコマンド 'foo'
enable: true
name: joe
tail: [a1 a2]

# 次に bar を試してみます。
$./command-line-subcommands bar -level 8 a1
サブコマンド 'bar'
level: 8
tail: [a1]

# しかし bar は foo のフラグを受け付けません。
$./command-line-subcommands bar -enable a1
定義されていないフラグが提供されました: -enable
bar の使用方法:
-level int
レベル

# 次に、プログラムをパラメータ化する一般的な別の方法である環境変数を見てみましょう。
```

以下が完全なコードです：

```go
// いくつかのコマンドラインツール、たとえば `go` ツールや `git` は、
// それぞれ独自のフラグのセットを持つ多くの *サブコマンド* を持っています。
// たとえば、`go build` と `go get` は `go` ツールの2つの異なるサブコマンドです。
// `flag` パッケージを使うと、独自のフラグを持つ簡単なサブコマンドを簡単に定義できます。

package main

import (
	"flag"
	"fmt"
	"os"
)

func main() {

	// `NewFlagSet` 関数を使ってサブコマンドを宣言し、
	// このサブコマンドに固有の新しいフラグを定義します。
	fooCmd := flag.NewFlagSet("foo", flag.ExitOnError)
	fooEnable := fooCmd.Bool("enable", false, "enable")
	fooName := fooCmd.String("name", "", "name")

	// 別のサブコマンドには、異なるサポートされるフラグを定義できます。
	barCmd := flag.NewFlagSet("bar", flag.ExitOnError)
	barLevel := barCmd.Int("level", 0, "level")

	// サブコマンドは、プログラムの最初の引数として期待されます。
	if len(os.Args) < 2 {
		fmt.Println("'foo' または 'bar' のサブコマンドが必要です")
		os.Exit(1)
	}

	// どのサブコマンドが呼び出されたかを確認します。
	switch os.Args[1] {

	// すべてのサブコマンドでは、独自のフラグを解析し、
	// 末尾の位置引数にアクセスできます。
	case "foo":
		fooCmd.Parse(os.Args[2:])
		fmt.Println("サブコマンド 'foo'")
		fmt.Println("  enable:", *fooEnable)
		fmt.Println("  name:", *fooName)
		fmt.Println("  tail:", fooCmd.Args())
	case "bar":
		barCmd.Parse(os.Args[2:])
		fmt.Println("サブコマンド 'bar'")
		fmt.Println("  level:", *barLevel)
		fmt.Println("  tail:", barCmd.Args())
	default:
		fmt.Println("'foo' または 'bar' のサブコマンドが必要です")
		os.Exit(1)
	}
}

```

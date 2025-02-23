# コマンドラインフラグ

コマンドラインフラグを解析し、解析されたオプションと任意の末尾の位置引数を出力するGo言語のプログラムを実装します。このプログラムは以下のフラグをサポートする必要があります。

- `word`：デフォルト値が `"foo"` の文字列フラグ。
- `numb`：デフォルト値が `42` の整数フラグ。
- `fork`：デフォルト値が `false` のブールフラグ。
- `svar`：プログラムの他の場所で宣言された既存の変数を使用する文字列フラグ。

- プログラムは `flag` パッケージを使用してコマンドラインフラグを解析する必要があります。
- プログラムは解析されたオプションと任意の末尾の位置引数を出力する必要があります。
- プログラムは上記の `word`、`numb`、`fork`、および `svar` フラグをサポートする必要があります。

```sh
# コマンドラインフラグプログラムを試すには、まずコンパイルしてから、
# 生成されたバイナリを直接実行するのが最善です。
$ go build command-line-flags.go

# まずすべてのフラグに値を与えて、ビルドされたプログラムを試してみましょう。
$./command-line-flags -word=opt -numb=7 -fork -svar=flag
word: opt
numb: 7
fork: true
svar: flag
tail: []

# フラグを省略すると、自動的にデフォルト値が採用されることに注意してください。
$./command-line-flags -word=opt
word: opt
numb: 42
fork: false
svar: bar
tail: []

# 末尾の位置引数は、任意のフラグの後に指定できます。
$./command-line-flags -word=opt a1 a2 a3
word: opt
...
tail: [a1 a2 a3]

# 注意：`flag` パッケージでは、すべてのフラグが位置引数の前に表示される必要があります
# （そうでない場合、フラグは位置引数として解釈されます）。
$./command-line-flags -word=opt a1 a2 a3 -numb=7
word: opt
numb: 42
fork: false
svar: bar
tail: [a1 a2 a3 -numb=7]

# `-h` または `--help` フラグを使用して、コマンドラインプログラムの自動生成された
# ヘルプテキストを取得します。
$./command-line-flags -h
Usage of./command-line-flags:
-fork=false: a bool
-numb=42: an int
-svar="bar": a string var
-word="foo": a string

# `flag` パッケージに指定されていないフラグを提供すると、
# プログラムはエラーメッセージを表示し、再度ヘルプテキストを表示します。
$./command-line-flags -wat
flag provided but not defined: -wat
Usage of./command-line-flags:
...
```

以下が完全なコードです：

```go
// [_コマンドラインフラグ_](https://en.wikipedia.org/wiki/Command-line_interface#Command-line_option)
// は、コマンドラインプログラムのオプションを指定する一般的な方法です。
// たとえば、`wc -l` の `-l` はコマンドラインフラグです。

package main

// Goは、基本的なコマンドラインフラグ解析をサポートする `flag` パッケージを提供しています。
// このパッケージを使用して、私たちのコマンドラインプログラムの例を実装します。
import (
	"flag"
	"fmt"
)

func main() {

	// 基本的なフラグ宣言は、文字列、整数、およびブールオプションに利用できます。
	// ここでは、デフォルト値が `"foo"` で短い説明がある文字列フラグ `word` を宣言します。
	// この `flag.String` 関数は、文字列ポインタ（文字列値ではない）を返します。
	// このポインタの使い方については、後で説明します。
	wordPtr := flag.String("word", "foo", "a string")

	// これは、`word` フラグと同じ方法で `numb` と `fork` フラグを宣言します。
	numbPtr := flag.Int("numb", 42, "an int")
	forkPtr := flag.Bool("fork", false, "a bool")

	// プログラムの他の場所で宣言された既存の変数を使用するオプションも宣言できます。
	// フラグ宣言関数にポインタを渡す必要があることに注意してください。
	var svar string
	flag.StringVar(&svar, "svar", "bar", "a string var")

	// すべてのフラグを宣言したら、`flag.Parse()` を呼び出してコマンドライン解析を実行します。
	flag.Parse()

	// ここでは、解析されたオプションと任意の末尾の位置引数を出力します。
	// 実際のオプション値を取得するには、たとえば `*wordPtr` のようにポインタを参照解除する必要があります。
	fmt.Println("word:", *wordPtr)
	fmt.Println("numb:", *numbPtr)
	fmt.Println("fork:", *forkPtr)
	fmt.Println("svar:", svar)
	fmt.Println("tail:", flag.Args())
}

```

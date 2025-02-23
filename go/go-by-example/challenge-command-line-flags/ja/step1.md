# コマンドラインフラグ

コマンドラインフラグを解析し、解析されたオプションとその後に続く位置引数を出力するGo言語のプログラムを実装します。このプログラムは以下のフラグをサポートする必要があります。

- `word`：デフォルト値が`"foo"`の文字列フラグ。
- `numb`：デフォルト値が`42`の整数フラグ。
- `fork`：デフォルト値が`false`のブールフラグ。
- `svar`：プログラムの他の場所で宣言された既存の変数を使用する文字列フラグ。

## 要件

- プログラムは`flag`パッケージを使用してコマンドラインフラグを解析する必要があります。
- プログラムは解析されたオプションとその後に続く位置引数を出力する必要があります。
- プログラムは上記の`word`、`numb`、`fork`、および`svar`フラグをサポートする必要があります。

## 例

```sh
# コマンドラインフラグプログラムを試すには、まずコンパイルしてから生成されたバイナリを直接実行するのが最善です。
$ go build command-line-flags.go

# すべてのフラグに値を与えて、ビルドされたプログラムを試してみましょう。
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

# 位置引数は、任意のフラグの後に指定できます。
$./command-line-flags -word=opt a1 a2 a3
word: opt
...
tail: [a1 a2 a3]

# 注意：`flag`パッケージでは、すべてのフラグは位置引数の前に表示する必要があります（そうしないと、フラグが位置引数として解釈されます）。
$./command-line-flags -word=opt a1 a2 a3 -numb=7
word: opt
numb: 42
fork: false
svar: bar
tail: [a1 a2 a3 -numb=7]

# `-h`または`--help`フラグを使用して、コマンドラインプログラムの自動生成されたヘルプテキストを取得します。
$./command-line-flags -h
Usage of./command-line-flags:
-fork=false: a bool
-numb=42: an int
-svar="bar": a string var
-word="foo": a string

# `flag`パッケージに指定されていないフラグを提供すると、プログラムはエラーメッセージを表示し、再度ヘルプテキストを表示します。
$./command-line-flags -wat
flag provided but not defined: -wat
Usage of./command-line-flags:
...
```

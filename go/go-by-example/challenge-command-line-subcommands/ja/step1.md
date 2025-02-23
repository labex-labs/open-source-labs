# コマンドラインのサブコマンド

2つのサブコマンド、`foo` と `bar` をサポートするプログラムを作成するよう求められています。それぞれには独自のフラグのセットがあります。`foo` サブコマンドは `enable` と `name` の2つのフラグを持ち、`bar` サブコマンドは `level` の1つのフラグを持つ必要があります。

## 要件

- プログラムは `flag` パッケージを使用してフラグを定義および解析する必要があります。
- `foo` サブコマンドは `enable` と `name` の2つのフラグを持ち、どちらも文字列型です。
- `bar` サブコマンドは `level` の1つのフラグを持ち、整数型です。
- 無効なサブコマンドが提供された場合、プログラムはエラーメッセージを表示する必要があります。
- プログラムは、呼び出されたサブコマンドのフラグの値を表示する必要があります。

## 例

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
定義されていないフラグが指定されました: -enable
bar の使用方法:
-level int
レベル

# 次に、プログラムをパラメータ化する一般的な別の方法である環境変数を見てみましょう。
```

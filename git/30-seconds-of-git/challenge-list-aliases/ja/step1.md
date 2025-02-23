# すべての Git エイリアスを一覧表示する

開発者として、システムに設定されているすべての Git エイリアスを一覧表示したい場合があります。これは、以下のようないくつかの理由で役立ちます。

- 利用可能なエイリアスを確認する
- エイリアスがどのコマンドにマップされているかを調べる
- 既存のエイリアスを削除または変更する

## タスク

`https://github.com/labex-labs/git-playground` にある `git-playground` という名前の Git リポジトリがあるとします。

以下のエイリアスを設定しています。

```shell
alias.st=status
alias.co=checkout
alias.rb=rebase
```

1. ローカル マシンでこのリポジトリに移動します。
2. すべての Git エイリアスの一覧表示中に `sed` コマンドを使用します。

コマンドを実行すると、以下のように出力されます。

```shell
st=status
co=checkout
rb=rebase
```

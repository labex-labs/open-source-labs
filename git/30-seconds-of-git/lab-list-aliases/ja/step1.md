# すべての Git エイリアスを一覧表示する

開発者として、システムに設定されているすべての Git エイリアスを一覧表示したい場合があります。これは、以下のようないくつかの理由で役立ちます。

- 利用可能なエイリアスを確認する
- エイリアスがどのコマンドにマップされているかを確認する
- 既存のエイリアスを削除または変更する

`https://github.com/labex-labs/git-playground` にある `git-playground` という名前の Git リポジトリがあるとしましょう。

1. ローカル マシン上でこのリポジトリに移動します。

```shell
cd git-playground
```

2. 以下のエイリアスを設定します。

```shell
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.rb rebase
```

3. すべての Git エイリアスの一覧表示中に `sed` コマンドを使用します。

```shell
git config -l | grep alias | sed 's/^alias\.//g'
```

このコマンドを実行すると、以下のように出力されます。

```shell
st=status
co=checkout
rb=rebase
```

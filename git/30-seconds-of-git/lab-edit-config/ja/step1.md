# Git 設定ファイルを編集する

開発者として、Git の動作をカスタマイズするために Git 設定ファイルを変更する必要がある場合があります。Git 設定ファイルは、キーと値のペアの形式で設定を含む平文ファイルです。このファイルは任意のテキストエディタを使用して編集できますが、Git には設定ファイルを変更するために使用できる組み込みのテキストエディタがあります。

この例では、`https://github.com/labex-labs/git-playground` ディレクトリにある Git リポジトリを使用して、Git 設定ファイルを編集する方法を示します。

1. ターミナルを開き、Git リポジトリディレクトリに移動します。

```shell
cd git-playground
```

2. 次のコマンドを使用して、Git のテキストエディタで Git 設定ファイルを開きます。

```shell
git config --global -e
```

3. 上記のコマンドで、既定の Git テキストエディタで Git 設定ファイルが開きます。ユーザー名を `labex_git` に、ユーザー メールを `labex_git@example.com` に変更できます。
4. 必要な変更を行ったら、<kbd>Esc</kbd> キーを押して <kbd>:wq</kbd> コマンドを入力し、その後 <kbd>Enter</kbd> キーを押して変更を保存してエディタを終了します。

これが完了後の結果です。

```shell
# This is Git's per-user configuration file.
[user]
name = labex_git
email = labex_git@example.com
# Please adapt and uncomment the following lines:
#   name =
#   email = labex@64b8c76af840a200973e9d16.(none)
```

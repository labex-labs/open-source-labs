# Git 設定ファイルを編集する

開発者として、Git の動作をカスタマイズするために Git 設定ファイルを変更する必要がある場合があります。Git 設定ファイルは、キーと値のペア形式の設定を含む平文ファイルです。このファイルは任意のテキストエディタを使用して編集できますが、Git には設定ファイルを変更するために使用できる組み込みのテキストエディタが用意されています。

## タスク

この例では、`https://github.com/labex-labs/git-playground` ディレクトリにある Git リポジトリを使用します。

1. ターミナルを開き、Git リポジトリ ディレクトリに移動します。
2. Git のテキストエディタで Git 設定ファイルを開きます。
3. ユーザー名を `labex_git` に、ユーザー メールを `labex_git@example.com` に変更します。
4. 必要な変更を行ったら、<kbd>Esc</kbd> キーを押して <kbd>:wq</kbd> コマンドを入力し、その後 <kbd>Enter</kbd> キーを押して変更を保存してエディタを終了します。

これが完了後の結果です：

```shell
# This is Git's per-user configuration file.
[user]
name = labex_git
email = labex_git@example.com
# Please adapt and uncomment the following lines:
#   name =
#   email = labex@64b8c76af840a200973e9d16.(none)
```

# 最後のコミットからファイルを削除する

意図せずに最後のコミットに追加したファイルがあります。メッセージを変更することなく、最後のコミットからそのファイルを削除したいと思います。

## タスク

このチャレンジでは、`https://github.com/labex-labs/git-playground` のリポジトリを使用します。`git-playground` という名前の Git リポジトリがあり、`file2.txt` という名前のファイルがあり、これを誤って最後のコミットに追加したとします。

1. リポジトリディレクトリに移動し、GitHub の ID を設定します。
2. インデックスから指定された `file2.txt` を削除します。
3. 最後のコミットの内容を更新し、メッセージを変更しません。

これらのコマンドを実行した後、`file2.txt` ファイルはメッセージを変更することなく最後のコミットから削除されます。

Git バージョン管理から `file2.txt` を削除するときの様子はこうなります：

```shell
On branch master

Changes to be committed:
(use "git restore --staged <file>..." to unstage)
deleted: file2.txt

Untracked files:
(use "git add <file>..." to include in what will be committed)
file2.txt
```

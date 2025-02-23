# ステージングエリアからファイルを削除する

あなたは `git-playground` リポジトリのプロジェクトを作業しています。ファイルにいくつかの変更を加え、それらをステージングエリアに追加しました。しかし、コミットしたくないファイルを誤って追加してしまったことに気づきました。このファイルをステージングエリアから削除する必要があります。

## タスク

1. 現在の作業ディレクトリの状態を表示する。
2. `newfile.txt` ファイルをステージングエリアから削除する。
3. ファイルがステージングエリアから削除されたことを確認する。

これが最終結果です：

```shell
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
(use "git push" to publish your local commits)

Changes to be committed:
(use "git restore --staged <file>..." to unstage)
modified: README.md

Untracked files:
(use "git add <file>..." to include in what will be committed)
newfile.txt
```

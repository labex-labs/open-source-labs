# ステージングエリアからファイルを削除する

あなたは `git-playground` リポジトリ内のプロジェクトを作業しています。ファイルにいくつかの変更を加え、`git add` コマンドを使ってそれらをステージングエリアに追加しました。しかし、コミットしたくないファイルを誤って追加してしまったことに気づきました。このファイルをステージングエリアから削除する必要があります。

1. 現在の作業ディレクトリの状態を表示する：

```shell
git status
```

2. `git restore --staged` コマンドを使って `newfile.txt` ファイルをステージングエリアから削除する：

```shell
git restore --staged newfile.txt
```

3. `git status` コマンドを使って、ファイルがステージングエリアから削除されたことを確認する：

```shell
git status
```

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

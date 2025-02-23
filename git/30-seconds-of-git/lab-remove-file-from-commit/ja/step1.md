# 最後のコミットからファイルを削除する

意図せずに最後のコミットに追加したファイルがあります。メッセージを変更することなく、最後のコミットからそのファイルを削除したいと思います。

この実験では、`https://github.com/labex-labs/git-playground` のリポジトリを使用します。`git-playground` という名前の Git リポジトリがあり、`file2.txt` という名前のファイルを意図せずに最後のコミットに追加したとします。最後のコミットからファイルを削除する手順は以下の通りです。

1. リポジトリをクローンし、ディレクトリに移動して ID を設定します。

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. `git rm --cached <file>` を使用して、指定された `<file>` をインデックスから削除します。

```shell
git rm --cached file2.txt
```

3. `git commit --amend` を使用して、最後のコミットの内容を更新し、メッセージを変更しません。

```shell
git commit --amend --allow-empty
```

ファイルを削除した後のコミットが空のコミットの場合、`--allow-empty` を使用します。そうでない場合は省略できます。

これらのコマンドを実行すると、`file2.txt` ファイルがメッセージを変更することなく最後のコミットから削除されます。

Git バージョン管理から `file2.txt` を削除したときの状況は以下の通りです。

```shell
On branch master

Changes to be committed:
(use "git restore --staged <file>..." to unstage)
deleted: file2.txt

Untracked files:
(use "git add <file>..." to include in what will be committed)
file2.txt
```

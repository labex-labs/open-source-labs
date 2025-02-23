# 削除されたファイルを復元する

あなたは Git を使ってプロジェクトを行っており、必要な `file2.txt` という名前のファイルを誤って削除してしまいました。幸いなことに、そのファイルが削除されたコミットを知っています。あなたのタスクは、Git を使って削除されたファイルを復元することです。

この実験を完了するには、`https://github.com/labex-labs/git-playground.git` の Git リポジトリ `git-playground` を使用します。以下の手順に従ってください：

1. `cd git-playground` コマンドを使ってリポジトリディレクトリに移動します。
2. `git log --oneline` コマンドを実行してコミット履歴を表示します。
3. 「Added file2.txt」というメッセージでファイルが削除されたコミットを特定します。
4. `git checkout <commit> -- <file>` コマンドを実行して、指定された `<commit>` で削除された指定された `<file>` を復元します。`<commit>` をコミットハッシュに、`<file>` を削除されたファイルの名前に置き換えます。

たとえば、ファイル `file2.txt` がコミット `d22f46b` で削除された場合、次のコマンドを実行します：

```shell
git checkout d22f46b -- file2.txt
```

これにより、`file2.txt` ファイルがローカルリポジトリに復元されます。

`ll` コマンドを実行した結果は次のとおりです：

```shell
total 12K
-rw-r--r-- 1 labex labex 15 Jun 18 18:05 file1.txt
-rw-r--r-- 1 labex labex 15 Jun 18 18:13 file2.txt
-rw-r--r-- 1 labex labex 32 Jun 18 18:05 README.md
```

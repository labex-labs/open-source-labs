# 削除されたファイルを復元する

あなたは Git を使ってプロジェクトを行っており、必要な `file2.txt` という名前のファイルを誤って削除してしまいました。幸いなことに、そのファイルが削除されたコミットを知っています。あなたのタスクは、Git を使って削除されたファイルを復元することです。

## タスク

このチャレンジを完了するには、`https://github.com/labex-labs/git-playground.git` の Git リポジトリ `git-playground` を使います。

1. 「Added file2.txt」というメッセージでファイルが削除されたコミットを特定します。
2. 削除の前のコミットをチェックアウトすることで、削除されたファイルを復元します。

これにより、`file2.txt` ファイルがあなたのローカルリポジトリに復元されます。

これが `ll` コマンドを実行した結果です：

```shell
total 12K
-rw-r--r-- 1 labex labex 15 Jun 18 18:05 file1.txt
-rw-r--r-- 1 labex labex 15 Jun 18 18:13 file2.txt
-rw-r--r-- 1 labex labex 32 Jun 18 18:05 README.md
```

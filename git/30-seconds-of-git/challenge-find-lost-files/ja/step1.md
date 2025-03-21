# 失われたファイルを見つける

あなたは `git-playground` リポジトリのプロジェクトを作業してきました。ただし、一部のファイルが欠けていることに気付き、それらがいつ削除されたか、またどのように復元するかわかりません。あなたのタスクは、Git を使ってリポジトリ内の失われたファイルとコミットを見つけることです。

## タスク

1. ディレクトリに移動して ID を設定します。
2. `one-branch` という名前のブランチを作成して切り替え、`file2.txt` を削除して "Remove file2" というメッセージでコミットします。
3. `master` ブランチに戻り、`one-branch` ブランチを削除します。
4. 失われたファイルとコミットを見つけます。
5. `.git/lost-found` ディレクトリを確認して、失われたファイルが回復されたかどうかを確認します。
6. 失われたファイルが見つかった場合、それらが欠けているファイルであるかどうかを確認します。

これは `ls.git/lost-found` コマンドを実行した結果です：

```shell
commit
```

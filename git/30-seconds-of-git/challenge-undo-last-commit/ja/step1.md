# 最後のコミットを取り消す

あなたはたった今、Git リポジトリに変更をコミットしましたが、間違いを犯したことに気づきました。失うことなく最後のコミットを取り消したいです。これをどのように行えばよいでしょうか。

## タスク

このチャレンジでは、`https://github.com/labex-labs/git-playground` のリポジトリを使用しましょう。

1. コミット履歴を確認します。
2. 最後のコミットを取り消し、コミットの変更の逆を使って新しいコミットを作成します。

これは `git log --oneline` コマンドを実行した結果です。

```shell
532b49b (HEAD -> master) Revert "Added file2.txt"
d22f46b (origin/master, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```

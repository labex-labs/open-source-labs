# 最後のコミットを取り消す

あなたはたった今、Git リポジトリに変更をコミットしましたが、間違いを犯したことに気づきました。失うことなく最後のコミットを取り消したいです。これをどのように行えばよいでしょうか。

この実験では、`https://github.com/labex-labs/git-playground` のリポジトリを使用しましょう。以下の手順に従ってください。

1. リポジトリをクローンし、ディレクトリに移動して ID を設定します。

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. コミット履歴を確認します。

```shell
git log
```

3. 最後のコミットを取り消し、コミットの変更の逆を使って新しいコミットを作成します。

```shell
git revert HEAD
```

4. 再びコミット履歴を確認します。

```shell
git log
```

これが `git log --oneline` コマンドを実行した結果です。

```shell
532b49b (HEAD -> master) Revert "Added file2.txt"
d22f46b (origin/master, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```

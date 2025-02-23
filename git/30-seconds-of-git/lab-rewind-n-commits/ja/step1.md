# コミットを巻き戻す

開発者として、あるプロジェクトに取り組んでいて、いくつかのコミットを行ってきました。しかし、最後の数回のコミットにエラーが含まれており、以前のコードバージョンに戻る必要があることに気づきました。Git を使ってコミットを巻き戻し、以前のコードバージョンに戻る必要があります。

この実験を完了するには、GitHub アカウントから Git リポジトリ `git-playground` を使用します。これは、`https://github.com/labex-labs/git-playground.git` のフォークから来ています。以下の手順に従ってください。

1. リポジトリをローカルマシンにクローンします。

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
```

2. `rewind-commits` という名前の新しいブランチを作成します。

```shell
git checkout -b rewind-commits
```

3. リポジトリのコミット履歴を表示し、最後のコミットにエラーが含まれており、以前のコードバージョンに戻る必要があることに気づきます。

```shell
git log
```

4. Git を使ってコミットを 1 つ巻き戻します。

```shell
git reset HEAD~1 --hard
```

5. コミットを正常に巻き戻したことを確認します。

```shell
git log
```

6. 変更を `rewind-commits` ブランチにプッシュします。

```shell
git push --force origin rewind-commits
```

これが最終結果です。

```shell
cf80005 (HEAD -> rewind-commits, origin/rewind-commits) Added file1.txt
b00b937 Initial commit
```

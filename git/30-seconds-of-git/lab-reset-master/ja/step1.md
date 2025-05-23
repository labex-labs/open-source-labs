# ローカルの master ブランチをリモートに合わせる

あなたはプロジェクトに取り組んでおり、ローカルの `master` ブランチに変更を加えてきました。しかし、ローカルブランチにはない新しい変更がリモートの `master` ブランチに更新されていることに気づきました。あなたはローカルの `master` ブランチをリモートのブランチに合わせるためにリセットする必要があります。

1. `master` ブランチに切り替えます：
   ```shell
   git checkout master
   ```
2. リモートから最新の更新を取得します：
   ```shell
   git fetch origin
   ```
3. 現在のブランチのコミット履歴を表示します：
   ```shell
   git log
   ```
4. ローカルの `master` ブランチをリモートのブランチに合わせるためにリセットします：
   ```shell
   git reset --hard origin/master
   ```
5. ローカルの `master` ブランチが現在リモートの `master` ブランチと最新であることを確認します：
   ```shell
   git log
   ```

これが完成した結果です：

```shell
[object Object]
```

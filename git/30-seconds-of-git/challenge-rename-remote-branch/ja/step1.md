# リモートブランチをリネームする

このチャレンジを完了するには、GitHub アカウントの Git リポジトリ `git-playground` を使用します。これは `https://github.com/labex-labs/git-playground.git` のフォークから来ています。フォークする際は、「マスターブランチのみをコピーする」をオフにしてください。

`https://github.com/your-username/git-playground` という名前の Git リポジトリがあります。`feature-branch` という名前のブランチを作成し、リモートにプッシュしました。今、そのブランチをローカルとリモートの両方で `new-feature-1` にリネームしたいと思っています。

## タスク

1. リポジトリをクローンし、ディレクトリに移動して ID を設定します。
2. `feature-branch` という名前のブランチに切り替えます。
3. ブランチをローカルとリモートの両方でリネームします。
4. ブランチがリネームされたことを確認します。

これが `git branch -a` を実行した結果です：

```shell
* master
new-feature-1
remotes/origin/HEAD - > origin/master
remotes/origin/master
remotes/origin/new-feature-1
```

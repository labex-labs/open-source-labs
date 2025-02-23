# リモートブランチをリネームする

この実験を完了するには、GitHub アカウントから Git リポジトリ `git-playground` を使用します。これは `https://github.com/labex-labs/git-playground.git` のフォークから来ています。フォークする際は、「マスターブランチのみをコピーする」をオフにしてください。

`https://github.com/your-username/git-playground` という名前の Git リポジトリがあります。`feature-branch` という名前のブランチを作成し、リモートにプッシュしました。今では、ローカルおよびリモートでブランチ名を `new-feature-1` に変更したいと思っています。

1. リポジトリをクローンし、ディレクトリに移動して ID を設定します。
   ```shell
   git clone https://github.com/your-username/git-playground.git
   cd git-playground
   git config --global user.name "your-username"
   git config --global user.email "your-email"
   ```
2. `feature-branch` という名前のブランチに切り替えます。
   ```shell
   git checkout feature-branch
   ```
3. ローカルおよびリモートでブランチをリネームします。
   ```shell
   git branch -m feature-branch new-feature-1
   git push origin --delete feature-branch
   git push -u origin new-feature-1
   ```
4. ブランチがリネームされたことを確認します。
   ```shell
   git branch -a
   ```

これが `git branch -a` を実行した結果です。

```shell
* master
new-feature-1
remotes/origin/HEAD - > origin/master
remotes/origin/master
remotes/origin/new-feature-1
```

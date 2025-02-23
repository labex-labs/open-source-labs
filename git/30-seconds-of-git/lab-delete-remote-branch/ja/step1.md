# リモートブランチを削除する

時々、不要になったリモートブランチを削除する必要がある場合があります。たとえば、機能ブランチがメインブランチにマージされた場合、リポジトリをクリーンに保つために、リモートの機能ブランチを削除したいかもしれません。

`git-playground` という GitHub リポジトリが、`https://github.com/labex-labs/git-playground.git` のフォークからのあなたの GitHub アカウントからクローンされたものとします。不要になった `feature-branch` という名前のリモートブランチを削除したいとします。以下が、リモートブランチを削除する手順です。

1. リポジトリをクローンし、ディレクトリに移動して ID を設定します。
   ```shell
   git clone https://github.com/your-username/git-playground.git
   cd git-playground
   git config --global user.name "your-username"
   git config --global user.email "your-email"
   ```
2. `feature-branch` ブランチを `origin` リモートリポジトリに追加します。
   ```shell
   git checkout -b feature-branch
   git push -u origin feature-branch
   ```
3. `git branch -r` コマンドを使用して、すべてのリモートブランチを一覧表示します。
   ```shell
   git branch -r
   ```
   出力には、`feature-branch` のリモートブランチが含まれているはずです。
   ```
   origin/HEAD -> origin/master
   origin/feature-branch
   origin/master
   ```
4. `git push -d <remote> <branch>` コマンドを使用して、指定された `<remote>` 上の指定されたリモート `<branch>` を削除します。
   ```shell
   git push -d origin feature-branch
   ```
   このコマンドは、`origin` リモートリポジトリ上の `feature-branch` のリモートブランチを削除します。
5. 再度、`git branch -r` コマンドを使用して、リモートブランチが削除されたことを確認します。
   ```shell
   git branch -r
   ```
   出力には、`feature-branch` のリモートブランチが含まれていないはずです。
   ```
   origin/HEAD -> origin/master
   origin/master
   ```

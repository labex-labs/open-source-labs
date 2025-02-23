# 分離ブランチの削除

不要になったいくつかの分離ブランチが含まれる Git リポジトリがあります。これらのブランチがリポジトリを混乱させ、管理が困難になっています。リポジトリを整理するために、すべての分離ブランチを削除したいと思っています。

この実験を完了するには、GitHub アカウントの Git リポジトリ `git-playground` を使用します。これは `https://github.com/labex-labs/git-playground.git` のフォークから来ています。「マスターブランチのみをコピーする」をチェックしないでください。

1. リポジトリをクローンし、ディレクトリに移動して ID を設定します。

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. リモートリポジトリに `feature-branch` ブランチがあるため、`feature-branch` に切り替えます。これにより、ローカルの `feature-branch` がリモートリポジトリの `feature-branch` ブランチを追跡するようになり、リモートリポジトリの `feature-branch` ブランチが削除されます。

```shell
git checkout feature-branch
git push origin --delete feature-branch
```

3. ローカルブランチとそれが追跡するリモートブランチの間のトレース関係を表示します。

```shell
git branch -vv
```

4. `master` ブランチに戻ります。

```shell
git checkout master
```

5. ローカルリポジトリからすべての分離ブランチを削除します。

```shell
git branch -vv | grep ': gone]' | awk '{print $1}' | xargs git branch -D
```

6. 分離ブランチが削除されたことを確認します。

```shell
git branch
```

出力は、特定のブランチに関連付けられているブランチのみを表示する必要があります。

```shell
* master d22f46b [origin/master] Added file2.txt
```

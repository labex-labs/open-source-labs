# 別のブランチにリベースする

開発者として、複数のブランチがあるプロジェクトを担当しています。自分のブランチに変更を加え、それらの変更を別のブランチに取り込みたいと思っています。ただし、クリーンで線形の履歴を維持したいため、ブランチをマージしたくありません。この場合、`git rebase` コマンドを使用して、自分のブランチを別のブランチにリベースすることができます。

この実験では、`https://github.com/labex-labs/git-playground` のリポジトリを使用します。以下の手順に従って実験を完了してください。

1. リポジトリをクローンし、ディレクトリに移動して ID を設定します。

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. `one-branch` という名前のブランチを作成して切り替えます。

```shell
git checkout -b one-branch
```

3. `README.md` ファイルに "hello,world" を追加し、ステージング エリアに追加して、メッセージ "Added some changes to README.md" でコミットします。

```shell
echo "hello,world" >> README.md
git add.
git commit -am "Added some changes to README.md"
```

4. `master` ブランチに切り替えます。

```shell
git checkout master
```

5. ローカルの `master` ブランチがリモート リポジトリと最新であることを確認します。

```shell
git pull
```

6. `one-branch` を `master` ブランチにリベースします。

```shell
git rebase one-branch
```

7. リベース プロセス中に発生するすべてのコンフリクトを解消します。

これが `git log` を実行した結果です。

```shell
commit eccff423dd6bf5335f76f2f364fa3b95130ff805 (HEAD -> master, one-branch)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Sat Jul 22 23:10:04 2023 +0800

    Added some changes to README.md
```

# ローカルの変更をリモートにプッシュする

開発者として、他のチームメンバーと作業を共有したり、コードを本番環境にデプロイしたりするために、ローカルの変更をリモートリポジトリにプッシュする必要がある場合があります。`git push` コマンドは、ローカルブランチの最新の変更をリモートにプッシュするために使用されます。ただし、変更をプッシュする前に、ローカルブランチがリモートブランチと最新状態であることを確認する必要があります。ローカルブランチとリモートブランチの間に競合がある場合は、変更をプッシュする前に解決する必要があります。

この実験を完了するには、GitHub アカウントの Git リポジトリ `git-playground` を使用します。これは、`https://github.com/labex-labs/git-playground.git` のフォークから来ています。`master` ブランチにいくつかの変更を加え、それをリモートリポジトリにプッシュしたいと思います。次の手順に従ってください。

1. 次のコマンドを実行して、リポジトリをローカルマシンにクローンし、ディレクトリに移動します。

```shell
git clone https://github.com/your-username/git-playground
cd git-playground
```

2. 次のコマンドを実行して、ローカルブランチがリモートブランチと最新状態であることを確認します。

```shell
git pull origin master
```

3. リモートブランチから最新の変更をプルしたら、ローカルブランチに変更を加えることができます。

```shell
echo "hello,world" >> file1.txt
```

4. 変更を加えた後、`git add` コマンドを使用してステージングします。

```shell
git add.
```

5. `git commit` コマンドを使用して変更をコミットします。

```shell
git commit -m "Added new feature"
```

6. 最後に、`git push` コマンドを使用して変更をリモートリポジトリにプッシュします。

```shell
git push origin master
```

これが `git log` を実行した結果です。

```shell
commit 1f1949955387a1549f1bb5286d3d0a2b993f87e0 (HEAD -> master,origin/master,origin/HEAD)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Added new feature
```

# ローカルの変更をリモートにプッシュする

開発者として、他のチームメンバーと作業を共有したり、コードを本番環境にデプロイしたりするために、ローカルの変更をリモートリポジトリにプッシュする必要がある場合があります。ただし、変更をプッシュする前に、ローカルブランチがリモートブランチと最新状態であることを確認する必要があります。ローカルブランチとリモートブランチの間に競合がある場合は、変更をプッシュする前に解決する必要があります。

## タスク

このチャレンジを完了するには、GitHub アカウントの Git リポジトリ `git-playground` を使用します。これは、`https://github.com/labex-labs/git-playground.git` のフォークから来ています。`master` ブランチにいくつかの変更を加え、それらをリモートリポジトリにプッシュしたいと思っています。

1. `https://github.com/your-username/git-playground` からリポジトリをローカルマシンにクローンし、ディレクトリに移動して ID を設定します。
2. ローカルブランチがリモートブランチと最新状態であることを確認します。
3. リモートブランチから最新の変更をプルした後、`master` ブランチの `file1.txt` ファイルに "hello,world" を書き込み、ステージングエリアに追加して "Added new feature " というメッセージでコミットします。
4. 最後に、変更をリモートリポジトリにプッシュします。

これが `git log` を実行した結果です。

```shell
commit 1f1949955387a1549f1bb5286d3d0a2b993f87e0 (HEAD -> master,origin/master,origin/HEAD)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 19:26:57 2023 +0800

    Added new feature
```

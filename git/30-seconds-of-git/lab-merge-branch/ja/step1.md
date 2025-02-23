# ブランチをマージする

あなたのタスクは、Git を使ってブランチを現在のブランチにマージすることです。ターゲットブランチに切り替え、その後ソースブランチをマージする必要があります。これは、`feature-branch-A` ブランチの変更をプロジェクトの `master` ブランチに結合したい場合に便利です。

この実験では、`https://github.com/labex-labs/git-playground` のリポジトリを使用します。`feature-branch-A` を `master` ブランチにマージするには、次の手順に従ってください。

1. リポジトリをクローンし、ディレクトリに移動して ID を設定します。

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. `feature-branch-A` ブランチを作成し、切り替えます。

```shell
git checkout -b feature-branch-A
```

3. `file2.txt` ファイルに "hello,world" を追加し、ステージングエリアに追加して、"fix file2.txt" というメッセージでコミットします。

```shell
echo "hello,world" >> file2.txt
git add.
git commit -m "fix file2.txt"
```

4. `master` ブランチに切り替えます。

```shell
git checkout master
```

5. `feature-branch-A` を `master` ブランチにマージします。

```shell
git merge feature-branch-A
```

6. マージプロセス中に発生する可能性のあるコンフリクトを解消します。

これが `git log` を実行した結果です。

```shell
commit e2b80358ae6e4c3b8439cf111a4672a188739290 (HEAD -> master, feature-branch-A)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 18:51:00 2023 +0800

    fix file2.txt
```

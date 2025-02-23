# コミットを新しいブランチに移動させる

この実験では、`https://github.com/labex-labs/git-playground` のリポジトリを使用します。あなたは `master` ブランチでプロジェクトを作業してきました。あなたが行った一部の変更は、別のブランチで行われるべきだったことに気付きました。これらの変更を `feature` と呼ばれる新しいブランチに移動させたいと思います。

1. リポジトリをクローンし、ディレクトリに移動して ID を設定します。

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. `master` ブランチにチェックアウトします。

```shell
git checkout master
```

3. `hello.txt` という名前のファイルを作成し、そこに "hello, world" を追加し、ステージングエリアに追加して、"Added hello.txt" というメッセージでコミットします。

```shell
echo "hello,world" >> hello.txt
git add.
git commit -m "Added hello.txt"
```

4. `feature` という新しいブランチを作成して切り替えません。`master` ブランチで新しいブランチを作成するとき、新しいブランチの状態は `master` ブランチと同じです。つまり、新しいブランチのファイルは `master` ブランチのファイルと同じで、同じ内容とバージョン履歴を持っています。

```shell
git branch feature
```

5. `master` の最後のコミットを元に戻します。

```shell
git reset HEAD~1 --hard
```

6. `master` ブランチのコミット履歴と `feature` ブランチのコミット履歴を確認して結果を確認します。

```shell
git log
git checkout feature
git log
```

これが `git log` を実行した結果です。

```shell
commit 7969ab5d6606e2a40c9fd826c732206b835976e9 (HEAD -> feature)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Fri Jul 21 20:19:22 2023 +0800

    Added hello.txt
```

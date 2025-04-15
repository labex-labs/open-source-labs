# Git Cherry-Pick

開発者として、複数のブランチを持つプロジェクトに取り組んでいるとします。以前のコミットで行われた特定の変更を現在のブランチに適用したいと思っています。しかし、そのブランチには必要のない他の変更も含まれているため、ブランチ全体をマージしたくありません。このようなシチュエーションでは、`git cherry-pick` コマンドを使用して、特定の変更を現在のブランチに適用することができます。

この実験（Lab）では、`https://github.com/labex-labs/git-playground` のリポジトリを使用しましょう。以下の手順に従ってチャレンジ（Challenge）を完了してください。

1. リポジトリをクローンし、ディレクトリに移動して、アイデンティティを設定します。

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. `one-branch` という名前のブランチを作成して切り替え、`hello.txt` という名前のファイルを作成し、その中に "hello,world" と書き込み、ステージングエリアに追加して、「add hello.txt」というメッセージでコミットします。

```shell
git checkout -b one-branch
echo "hello,world" > hello.txt
git add.
git commit -m "add hello.txt"
```

3. 前の手順で作成したコミットのハッシュを特定して、`master` ブランチに適用します。

```shell
git log
```

4. `master` ブランチに切り替えて、その変更を `master` ブランチに適用します。

```shell
git checkout master
git cherry-pick 1609c283ec86ee4
```

5. 変更が `master` ブランチに適用されたことを確認します。

```shell
git log
```

これは `master` ブランチで `git log` を実行した結果です。

```shell
ADD hello.txt
```

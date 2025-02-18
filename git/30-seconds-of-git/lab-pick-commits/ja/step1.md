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
commit e2f3c6af9570f4eac2580dea93ca8133f1547d53 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Sat Jul 15 14:30:31 2023 +0800

    add hello.txt

commit d22f46ba8c2d4e07d773c5126e9c803933eb5898 (origin/master, origin/HEAD)
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt

commit cf80005e40a3c661eb212fcea5fad06f8283f08f
Author: Hang <huhuhang@users.noreply.github.com>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file1.txt

commit b00b9374a7c549d1af111aa777fdcc868d8a2a01
Author: Hang <huhuhang@gmail.com>
Date:   Wed Apr 26 14:16:00 2023 +0800

    Initial commit
```

# ファストフォワードマージの無効化

デフォルトでは、Git は分岐したコミットがないブランチをマージするためにファストフォワードマージを使用します。これは、新しいコミットがないブランチがある場合、Git が単にマージ先のブランチのポインタをマージ元のブランチの最新コミットに移動することを意味します。これは一部のケースで便利ですが、特に複数の貢献者がいる大規模なプロジェクトで作業する場合、問題を引き起こす場合もあります。たとえば、2 人の開発者が同じブランチで作業して両方が変更を加えた場合、ファストフォワードマージは解決が困難な競合を引き起こす可能性があります。

ファストフォワードマージを無効にするには、`https://github.com/labex-labs/git-playground` のリポジトリを使用しましょう。

1. リポジトリをクローンし、ディレクトリに移動して ID を構成します。

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. `my-branch` と呼ばれるブランチを作成して切り替え、`hello.txt` ファイルを作成してそこに "hello,world" を追加し、ステージングエリアに追加して "Added hello.txt" というメッセージでコミットします。

```shell
git checkout -b my-branch
echo "hello,world" > hello.txt
git add.
git commit -m "Added hello.txt"
```

3. 次のコマンドを実行してファストフォワードマージを無効にします。

```shell
git config --add merge.ff false
```

これにより、可能であってもすべてのブランチのファストフォワードマージが無効になります。このオプションをグローバルに構成するには、`--global` フラグを使用します。

```shell
git config --global --add merge.ff false
```

4. `master` ブランチに戻り、`my-branch` ブランチをマージし、テキストを変更せずに保存して終了します。

```shell
git checkout master
git merge my-branch
```

これで、可能であっても常にマージコミットが作成されます。

```shell
commit 6e17a776ab51a89ace069614b0caf1c07915a92c (HEAD -> master)
Merge: ec5ea6d 6d7de91
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Mon Jul 17 13:30:44 2023 +0800

    Merge branch'my-branch'
```

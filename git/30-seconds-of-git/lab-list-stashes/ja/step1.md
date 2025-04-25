# すべてのスタッシュを一覧表示する

あなたは Git リポジトリ内のプロジェクトに取り組んでおり、コミットする準備ができていないいくつかの変更を加えました。これらの変更をスタッシュして、別のタスクに取り組めるようにすることにします。後で、作成したすべてのスタッシュの一覧を見て、どれを適用するか決めたいと思います。Git リポジトリ内のすべてのスタッシュをどのように一覧表示しますか？

1. `git-playground` ディレクトリに移動します。

```
cd git-playground
```

2. 新しいファイル `test.txt` を作成し、そこにいくつかのコンテンツを追加します。

```
echo "hello,world" > test.txt
git add.
```

3. 次のコマンドを使用して変更をスタッシュします。

```
git stash save "Added test.txt"
```

4. もう 1 つの新しいファイル `test2.txt` を作成し、そこにいくつかのコンテンツを追加します。

```
echo "hello,labex" > test2.txt
git add.
```

5. 次のコマンドを使用して変更をスタッシュします。

```
git stash save "Added test2.txt"
```

6. 次のコマンドを使用してすべてのスタッシュを一覧表示します。

```
git stash list
```

以下のような出力が表示されるはずです。

```
stash@{0}: On master: Added test2.txt
stash@{1}: On master: Added test.txt
```

# トラックされていない変更を破棄する

あなたは Git を使ってプロジェクトを行っており、作業ディレクトリにいくつかの変更を加えました。しかし、これらの変更が必要ないことに気づき、破棄したいと思います。現在のブランチのすべてのトラックされていない変更を破棄したいのです。

この実験を完了するには、`https://github.com/labex-labs/git-playground` という名前の Git リポジトリを使用します。以下の手順に従ってください。

1. リポジトリディレクトリに移動します。

```shell
cd git-playground
```

2. 作業ディレクトリの状態を確認します。

```shell
git status
```

以下の出力が表示されるはずです。

```shell
[object Object]
```

3. 現在のブランチのすべてのトラックされていない変更を破棄します。

```shell
git clean -f -d
```

4. 再度、作業ディレクトリの状態を確認します。

```shell
git status
```

以下の出力が表示されるはずです。

```shell
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

`git clean -f -d` コマンドは、現在のブランチのすべてのトラックされていない変更を破棄しました。

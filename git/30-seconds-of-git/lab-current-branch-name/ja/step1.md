# 現在のブランチ名を取得する

Git リポジトリ内の現在のブランチ名を表示するコマンドを書きましょう。

`https://github.com/labex-labs/git-playground` リポジトリに保存されているプロジェクトを作業しているとします。`README.md` ファイルにいくつかの変更を加え、それらを現在のブランチにコミットしたいと思っています。ただし、その前に、正しいブランチにいることを確認したいと思います。

現在のブランチを確認するには、次のコマンドを使用できます。

```shell
git rev-parse --abbrev-ref HEAD
```

これにより、現在のブランチ名がコンソールに表示されます。たとえば、現在 `master` ブランチにいる場合、出力は次のようになります。

```shell
master
```

`feature-branch` などの別のブランチに切り替えると、出力もそれに応じて変わります。

```shell
git checkout -b feature-branch
git rev-parse --abbrev-ref HEAD
```

これにより、次のような出力が得られます。

```shell
feature-branch
```

# 特定のコミットを含むブランチを見つける

`https://github.com/labex-labs/git-playground` という名前の Git リポジトリが与えられています。 あなたのタスクは、コミットメッセージが "Added file2.txt" のハッシュを含むすべてのブランチを見つけることです。

1. リポジトリディレクトリに移動します。

```shell
cd git-playground
```

2. `git branch --contains` コマンドを使用して、コミットメッセージが "Added file2.txt" のハッシュを含むすべてのブランチを見つけます。

```shell
git branch --contains d22f46b
```

出力は以下のようになるはずです。

```shell
* master
new-branch
new-branch-1
new-branch-2
```

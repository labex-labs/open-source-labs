# 新しいブランチを作成する

この実験では、`https://github.com/labex-labs/git-playground` という名前の Git リポジトリを GitHub アカウントにフォークします。`https://github.com/your-username/git-playground` という名前の Git リポジトリでプロジェクトを行っています。新しい機能を開発するために、`feature-1` という名前の新しいブランチを作成する必要があります。

1. リポジトリをクローンし、ディレクトリに移動して ID を設定します。

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. 現在のブランチを確認します。

```shell
git branch
```

3. `feature-1` という名前の新しいブランチを作成します。

```shell
git checkout -b feature-1
```

4. 現在 `feature-1` ブランチにいることを確認します。

```shell
git branch
```

5. 変更をリモートリポジトリにプッシュします。

```shell
git push -u origin feature-1
```

`git branch -r` コマンドを実行したときの結果は次のとおりです。

![git branch remote output](../assets/challenge-create-branch-step1-1.png)

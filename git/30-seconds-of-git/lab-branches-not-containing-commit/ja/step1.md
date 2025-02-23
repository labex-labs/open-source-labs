# 特定のコミットを含まないブランチを見つける

複数のブランチがあるプロジェクトを作業しており、特定のコミットを含まないすべてのブランチを見つける必要があります。特定の変更がすべてのブランチに適用されていることを確認したい場合、またはどのブランチが古くなって更新が必要かを知りたい場合に役立ちます。

この実験では、`https://github.com/your-username/git-playground` という名前の Git リポジトリを使用します。

1. 次のコマンドを使用して、このリポジトリをローカルマシンにクローンします。

```shell
git clone https://github.com/your-username/git-playground.git
```

2. リポジトリをクローンした後、次のコマンドを使用してディレクトリに移動し、識別情報を設定します。

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. `new-branch` ブランチを作成して切り替え、そのブランチでいくつかのコード変更を行ってからコミットします。コミットメッセージは "Create a new-branch branch" です。

```shell
git checkout -b new-branch
echo "hello,world" > file1.txt
git commit -am "Create a new-branch branch"
```

4. コミットメッセージ "Create a new-branch branch" のハッシュを確認します。

```shell
git log
```

5. コミットメッセージ "Create a new-branch branch" のハッシュを持たないすべてのブランチを見つけます。これを行うには、次のコマンドを使用できます。

```shell
git branch --no-contains 31c5ac20129151af1
```

これにより、指定されたコミットを含まないすべてのブランチのリストが出力されます。この場合、出力は次のようになります。

```shell
master
```

これは、`master` ブランチがハッシュ `31c5ac20129151af1` のコミットを含まないことを意味します。

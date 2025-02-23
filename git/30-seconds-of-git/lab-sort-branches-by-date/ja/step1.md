# 日付で Git ブランチをソートする

複数のブランチがある Git リポジトリがあり、それらを日付でソートしたいと思います。これにより、最近更新されたブランチと更新されていないブランチを確認できます。ブランチを日付でソートすることで、注意やマージが必要なブランチを特定するのにも役立ちます。

この実験では、`https://github.com/labex-labs/git-playground` のリポジトリを使用します。

1. リポジトリをローカルマシンにクローンします。

```shell
git clone https://github.com/labex-labs/git-playground
```

2. リポジトリディレクトリに移動し、GitHub の ID を設定します。

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. `one` という名前のブランチを作成し、コードを変更してコミットします。

```shell
git checkout -b one
touch hello.txt
git add.
git commit -m "hello.txt"
```

4. `master` ブランチに切り替え、`two` という名前のブランチを作成します。

```shell
git checkout master
git checkout -b two
```

5. 次に、ブランチを日付でソートするには、次のコマンドを使用します。

```shell
git branch --sort=-committerdate
```

これにより、すべてのローカルブランチのリストが表示され、それらが最終コミットの日付に基づいてソートされます。矢印キーを使用してリストを移動し、<kbd>Q</kbd> キーを押して終了できます。

これが完成した結果です。

![sorted git branches list](../assets/challenge-sort-branches-by-date.png)

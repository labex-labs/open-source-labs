# 失われたファイルを見つける

あなたは `git-playground` リポジトリでプロジェクトを作業してきました。ただし、一部のファイルが欠けていることに気付き、それらがいつ削除されたか、またどのように復元するか分かりません。あなたのタスクは、Git を使ってリポジトリ内の失われたファイルとコミットを見つけることです。

1. `git-playground` リポジトリをクローンします：

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. ディレクトリに移動して ID を設定します：

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. `one-branch` という名前のブランチを作成して切り替え、`file2.txt` を削除して "Remove file2" というメッセージでコミットします：

```shell
git checkout -b one-branch
git rm file2.txt
git commit -m "Remove file2"
```

4. `master` ブランチに戻り、`one-branch` ブランチを削除します：

```shell
git checkout master
git branch -D one-branch
```

5. 失われたファイルとコミットを見つけるために `git fsck --lost-found` コマンドを実行します：

```shell
git fsck --lost-found
```

6. 復元された失われたファイルがあるかどうかを確認するために `.git/lost-found` ディレクトリを確認します：

```shell
ls.git/lost-found
```

7. 失われたファイルが見つかった場合、それらが欠けているファイルであるかどうかを確認します。

これが `ls.git/lost-found` コマンドを実行した結果です：

```shell
commit
```

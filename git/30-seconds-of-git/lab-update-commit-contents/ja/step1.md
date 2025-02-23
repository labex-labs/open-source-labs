# 最後のコミットを編集する

あなたはたった今、Git リポジトリにいくつかの変更をコミットしましたが、ファイルを含め忘れていたり、小さな変更を加えていないことに気づきました。この小さな変更のためだけに新しいコミットを作成したくないですが、コミットメッセージも変更したくありません。コミットメッセージを変更することなく最後のコミットをどのように編集できるでしょうか。

最後のコミットをどのように編集するかを示すために、`https://github.com/labex-labs/git-playground` のリポジトリを使用しましょう。

1. リポジトリをクローンし、ディレクトリに移動して ID を設定します。

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

2. ファイルを含め忘れていたり、小さな変更を加えていないことに気づきます。`README.md` ファイルの末尾に "New content" というテキストを追加します。コミットメッセージを変更することなく、最後のコミットにステージングされた変更を追加します。

```shell
echo "New content" >> README.md
git add README.md
git commit --amend --no-edit
```

3. 最後のコミットに今追加した変更が含まれていることを確認します。

```shell
git show HEAD
```

これが最後のコミットの内容です。
![更新されたコミット内容の表示](../assets/challenge-update-commit-contents.png)

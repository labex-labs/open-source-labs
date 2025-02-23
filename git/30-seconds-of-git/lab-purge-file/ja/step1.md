# 履歴からファイルを削除する

API キーやパスワードなどの機密情報を含むファイルを誤って Git リポジトリにコミットしたとしましょう。このファイルは決してコミットすべきではなかったことに気づき、リポジトリの履歴から完全に削除したいと思います。ただし、単にファイルを削除して変更をコミットしても、リポジトリの履歴からは削除されません。このファイルは以前のコミットでもアクセス可能であり、セキュリティ上のリスクを引き起こす可能性があります。

この実験を完了するには、GitHub アカウントの Git リポジトリ `git-playground` を使用します。このリポジトリは `https://github.com/labex-labs/git-playground.git` のフォークから来ています。このリポジトリには、決してコミットすべきではなかった `file1.txt` という名前のファイルが含まれています。`file1.txt` をリポジトリの履歴から削除するには、次の手順に従ってください。

1. リポジトリをローカルマシンにクローンします。

```shell
git clone https://github.com/your-username/git-playground
```

2. 次のコマンドを使用してディレクトリに移動し、識別情報を設定します。

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. リポジトリのインデックスからファイルを削除します。

```shell
git rm --cached --ignore-unmatch file1.txt
```

4. この変更を "Remove sensitive file1.txt" というコミットメッセージでコミットします。

```shell
git commit -m "Remove sensitive file1.txt"
```

5. リポジトリの履歴を書き換えて、`file1.txt` のすべてのインスタンスを削除します。

```shell
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch file1.txt" --prune-empty --tag-name-filter cat -- --all
```

6. 変更を強制的にリモートリポジトリにプッシュします。

```shell
git push origin --force --all
```

これらの手順を完了すると、`file1.txt` はリポジトリの履歴から完全に削除され、`git log --remotes` を実行した後、`file1.txt` のコミットは表示されません。

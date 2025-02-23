# 最後のコミットのメッセージを変更する

あなたがただ今、Git リポジトリにいくつかの変更をコミットしたとしましょう。しかし、コミットメッセージに誤字があることに気づきました。実際に行った変更を変更することなく、この間違いを修正したいです。これをどのように行えばよいでしょうか。

最後のコミットのメッセージを変更する方法を示すために、`https://github.com/labex-labs/git-playground` のリポジトリを使用しましょう。以下の手順に従ってください。

1. リポジトリをクローンし、ディレクトリに移動して ID を設定します。
   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   git config --global user.name "your-username"
   git config --global user.email "your-email"
   ```
2. 最後のコミットのコミットメッセージを "Fix the network bug" に修正します。
   ```
   git commit --amend -m "Fix the network bug"
   ```
   これにより、コミットメッセージを変更できる既定のテキストエディタが開きます。プロセスを完了するには、エディタを保存して閉じてください。
3. コミットメッセージが変更されたことを確認します。
   ```
   git log --oneline
   ```

ログに更新されたコミットメッセージが表示されるはずです。

```
54b830b (HEAD -> master) Fix the network bug
cf80005 Added file1.txt
b00b937 Initial commit
```

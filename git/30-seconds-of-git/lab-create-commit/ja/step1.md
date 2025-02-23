# Git コミットを作成する

コードにいくつかの変更を加え、それらを Git リポジトリにスナップショットとして保存したいと思っています。ただし、すべての変更を保存するのではなく、現在の機能またはバグ修正に関連するものだけを保存したいと考えています。どのようにして関連する変更のみを含むコミットを作成することができますか？

この実験では、`https://github.com/labex-labs/git-playground` のリポジトリを使用して、次の手順に従います：

1. リポジトリをクローンして移動します：

   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   ```

2. 環境で GitHub アカウントを設定します：

   ```
   git config --global user.name "your-name"
   git config --global user.email "your-email"
   ```

3. `README.md` ファイルに "hello,labex" を追加し、ステージング エリアに追加して、メッセージ "Update README.md" でコミットします：

   ```
   echo "hello,labex" >> README.md
   git add.
   git commit -m "Update README.md"
   ```

   `-m` オプションを使用すると、コミット メッセージを指定できます。メッセージが分かりやすく、コミットに含まれる変更を説明していることを確認してください。

これが `git log` コマンドを実行した結果です：

![git log command output](../assets/challenge-create-commit-step1-1.png)

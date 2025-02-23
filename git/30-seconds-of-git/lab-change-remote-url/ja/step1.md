# リモートURLを変更する

あなたはGitHubからリポジトリをクローンし、それにいくつかの変更を加えました。しかし、今ではリモートリポジトリのURLを変更する必要があることに気づきました。これは、元のリポジトリが別の場所に移動したため、または変更を別のリモートリポジトリにプッシュしたいためかもしれません。あなたのタスクは、Gitコマンドを使用してリポジトリのリモートURLを変更することです。

あなたは、リポジトリ `https://github.com/labex-labs/git-playground` をローカルマシンにクローンする必要があります。リポジトリのリモートURLを `https://github.com/your-username/git-playground` に変更するには、次の手順に従ってください。

1. ターミナルまたはコマンドプロンプトを開き、リポジトリをクローンしてローカルリポジトリに移動します。
   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   ```
2. 次のコマンドを使用して、現在のリモートURLを表示します。
   ```
   git remote -v
   ```
3. 次のコマンドを使用して、リモートURLを新しいURLに変更します。
   ```
   git remote set-url origin https://github.com/your-username/git-playground
   ```
4. 次のコマンドを使用して、リモートURLが変更されたことを確認します。
   ```
   git remote -v
   ```

出力には古いURLの代わりに新しいURLが表示されるはずです。

![Updated remote URL output](../assets/challenge-change-remote-url-step1-1.png)

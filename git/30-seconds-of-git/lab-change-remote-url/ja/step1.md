# リモート URL を変更する

あなたは GitHub からリポジトリをクローンし、それにいくつかの変更を加えました。しかし、今ではリモートリポジトリの URL を変更する必要があることに気づきました。これは、元のリポジトリが別の場所に移動したため、または変更を別のリモートリポジトリにプッシュしたいためかもしれません。あなたのタスクは、Git コマンドを使用してリポジトリのリモート URL を変更することです。

あなたは、リポジトリ `https://github.com/labex-labs/git-playground` をローカルマシンにクローンする必要があります。リポジトリのリモート URL を `https://github.com/your-username/git-playground` に変更するには、次の手順に従ってください。

1. ターミナルまたはコマンドプロンプトを開き、リポジトリをクローンしてローカルリポジトリに移動します。
   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   ```
2. 次のコマンドを使用して、現在のリモート URL を表示します。
   ```
   git remote -v
   ```
3. 次のコマンドを使用して、リモート URL を新しい URL に変更します。
   ```
   git remote set-url origin https://github.com/your-username/git-playground
   ```
4. 次のコマンドを使用して、リモート URL が変更されたことを確認します。
   ```
   git remote -v
   ```

出力には古い URL の代わりに新しい URL が表示されるはずです。

![Updated remote URL output](../assets/challenge-change-remote-url-step1-1.png)

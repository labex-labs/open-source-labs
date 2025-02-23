# コミットを元に戻す

Git リポジトリにコミットを行った後、その中に誤りが含まれていることに気付いたとしましょう。リポジトリの履歴を書き換えることなく、コミットを元に戻したいと思います。これをどのように行うことができますか？

コミットを元に戻す方法を示すために、`https://github.com/labex-labs/git-playground` のリポジトリを使用しましょう。以下の手順に従ってください。

1. リポジトリをクローンし、ディレクトリに移動して ID を設定します。
   ```
   git clone https://github.com/labex-labs/git-playground
   cd git-playground
   git config --global user.name "your-username"
   git config --global user.email "your-email"
   ```
2. コミット履歴を表示します。
   ```
   git log
   ```
   コミットのリストが表示され、それぞれには一意の識別子（長い英数字の文字列）が付いているはずです。
3. メッセージ "Added file1.txt" のコミットを選択し、その識別子をコピーします。
4. `git revert` コマンドを使用してコミットを元に戻します。
   ```
   git revert <commit>
   ```
   `<commit>` を、元に戻したいコミットの識別子に置き換えます。
5. Git はテキストエディタを開き、コミットメッセージを入力させますが、デフォルトのメッセージのままにしておきます。
6. テキストエディタを保存して閉じます。
7. 再度コミット履歴を表示します。
   ```
   git log
   ```
   元のコミットによって行われた変更を元に戻す新しいコミットが表示されるはずです。

これが `git log` コマンドを実行した結果です。

```
commit 0d01f357a798f8960959546750d89a7e56a04a44 (HEAD -> master)
Author: xiaoshengyunan <@users.noreply.github.com>
Date:   Mon Jul 24 21:52:43 2023 +0800

    Revert "Added file1.txt"

    This reverts commit cf80005e40a3c661eb212fcea5fad06f8283f08f.
```

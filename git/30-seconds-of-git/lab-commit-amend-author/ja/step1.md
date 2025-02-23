# 最後のコミットの作者を変更する

あなたはたった今、Git リポジトリにコミットを行いましたが、作者の名前とメールアドレスが間違っていることに気づきました。コミットの内容を変更することなく、作者の情報を更新したいです。Git を使ってこれを達成するにはどうすればよいでしょうか。

最後のコミットの作者を変更するには、`git commit --amend` コマンドを使用できます。このコマンドを使うと、Git リポジトリの最後のコミットを変更できます。以下は、作者の名前とメールアドレスを変更する方法の例です。

1. `https://github.com/labex-labs/git-playground` という名前の Git リポジトリをローカルマシンにクローンします。

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. GitHub アカウントを使って Git の識別情報を設定します。

```shell
cd git-playground
git config user.email "your email"
git config user.name "your username"
```

3. `git commit --amend` コマンドを使って最後のコミットの作者を変更し、内容を保存します。

```shell
git commit --amend --author="Duck Quackers <cool.duck@qua.ck>"
```

4. 作者の情報が更新されたことを確認します。

```shell
git log
```

最後のコミットの作者が現在 `Duck Quackers` であることがわかるはずです。

```shell
commit d5a385cc354f3528472a215b66cbb7c628ba47d5
Author: Duck Quackers <cool.duck@qua.ck>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt
```

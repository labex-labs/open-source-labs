# 別の作者によるコミットの作成

開発者チームでプロジェクトを行っているとしましょう。チームメンバーの一人がコードにいくつかの変更を加えました。しかし、彼らは自分たちで変更をコミットすることができず、あなたが彼らの代わりにコミットを作成する必要があります。このシナリオでは、`--author` オプションを使用して、コミットの作者の名前とメールを変更することができます。このオプションは、休暇中や病気休暇中の同僚の代わりにコードをコミットするなど、別の人にコミットを帰属させる必要がある場合に便利です。

別の作者によるコミットを作成するには、次のコマンドを使用します。

```shell
git commit -m < message > --author="<name> <email>"
```

`https://github.com/labex-labs/git-playground` リポジトリにホストされているプロジェクトを作業しているとしましょう。コードにいくつかの変更を加えましたが、自分で変更をコミットできない同僚の John Doe の代わりにコミットを作成する必要があります。これを行うには、次のコマンドを使用します。

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.email "your email"
git config --global user.name "your username"
echo "Fix the network bug" > README.md
git add.
git commit -m "Fix the bug" --author="John Doe <john.doe@example.com>"
```

このコマンドは、メッセージ "Fix the bug" で新しいコミットを作成し、それを John Doe に帰属させます。

これが完成した結果です。

![Git commit author change result](../assets/challenge-commit-set-author-step1-1.png)

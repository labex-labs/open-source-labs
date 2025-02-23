# Git のユーザー情報を構成する

あなたはちょうど新しいプロジェクトに取り組み始めたばかりで、Git のユーザー情報を構成したいと思っています。リポジトリに加える変更にあなたの名前とメールアドレスが関連付けられていることを確認したいです。

この実験では、`https://github.com/labex-labs/git-playground` という名前の Git リポジトリを使用します。このリポジトリのユーザー情報を構成するには、次の手順に従ってください。

1. 次のコマンドを使用してリポジトリをクローンします。

```
git clone https://github.com/labex-labs/git-playground.git
```

2. 次のコマンドを使用してクローンしたリポジトリに移動します。

```
cd git-playground
```

3. `git config` コマンドを使用して、リポジトリのユーザー情報を設定します。たとえば、あなたのメールアドレスが `jane.doe@example.com` で、名前が `Jane Doe` の場合、次のコマンドを使用します。

```
git config user.email "jane.doe@example.com"
git config user.name "Jane Doe"
```

4. 次のコマンド `git config --list` を使用して、ユーザー情報が正しく設定されていることを確認します。`user.email` と `user.name` のキーの下にそれぞれあなたのメールアドレスと名前が表示されるはずです。

これが実験を完了した後の結果です。

![Git user configuration result](../assets/challenge-config-user-step1-1.png)

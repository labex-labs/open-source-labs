# Git のユーザー情報を構成する

あなたはたった今新しいプロジェクトに取り組み始めたばかりで、Git のユーザー情報を構成したいと思っています。リポジトリに対して行う変更に自分の名前とメールアドレスが関連付けられていることを確認したいです。

## タスク

このチャレンジでは、`https://github.com/labex-labs/git-playground` という名前の Git リポジトリを使用します。これは VM 上の `~/project/` にクローンされています。

あなたのタスクは、Git リポジトリのユーザー情報を構成することです。たとえば、あなたのメールアドレスが `jane.doe@example.com` で、名前が `Jane Doe` の場合です。

## 例

チャレンジを完了した後、次のコマンドを実行して設定を確認できます。

```bash
git config --list
```

次のように、あなたのユーザー情報が表示されるはずです。

![Git config user info output](../assets/challenge-config-user-step1-1.png)

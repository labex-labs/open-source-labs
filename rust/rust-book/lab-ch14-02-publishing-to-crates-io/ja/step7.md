# Crates.io アカウントの設定

クレートを公開する前に、*https://crates.io* でアカウントを作成し、APIトークンを取得する必要があります。そのためには、*https://crates.io* のホームページにアクセスし、GitHubアカウントでログインします。（現在はGitHubアカウントが必要ですが、将来的には他のアカウント作成方法をサポートする可能性があります。）ログイン後、*https://crates.io/me* のアカウント設定にアクセスしてAPIキーを取得します。そして、次のようにAPIキーを使って `cargo login` コマンドを実行します。

```bash
cargo login abcdefghijklmnopqrstuvwxyz012345
```

このコマンドにより、CargoにAPIトークンを通知し、それを _\~/.cargo/credentials_ にローカルに保存します。このトークンは _秘密情報_ であることに注意してください。他の誰かと共有しないでください。何らかの理由で誰かと共有した場合は、それを取り消し、*https://crates.io* で新しいトークンを生成する必要があります。

# Crates.io アカウントの設定

クレートを公開する前に、*https://crates.io* でアカウントを作成し、API トークンを取得する必要があります。そのためには、*https://crates.io* のホームページにアクセスし、GitHub アカウントでログインします。（現在は GitHub アカウントが必要ですが、将来的には他のアカウント作成方法をサポートする可能性があります。）ログイン後、*https://crates.io/me* のアカウント設定にアクセスして API キーを取得します。そして、次のように API キーを使って `cargo login` コマンドを実行します。

```bash
cargo login abcdefghijklmnopqrstuvwxyz012345
```

このコマンドにより、Cargo に API トークンを通知し、それを _\~/.cargo/credentials_ にローカルに保存します。このトークンは _秘密情報_ であることに注意してください。他の誰かと共有しないでください。何らかの理由で誰かと共有した場合は、それを取り消し、*https://crates.io* で新しいトークンを生成する必要があります。

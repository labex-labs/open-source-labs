# Crates.io に公開する

アカウントを作成し、APIトークンを保存し、クレートの名前を選び、必要なメタデータを指定したので、公開の準備が整いました！クレートを公開すると、特定のバージョンが *https://crates.io* にアップロードされ、他の人が使用できるようになります。

注意してください。公開は _恒久的_ です。バージョンは決して上書きできず、コードを削除することもできません。Crates.ioの主な目的の1つは、コードの恒久的なアーカイブとして機能することです。そうすることで、*https://crates.io* のクレートに依存するすべてのプロジェクトのビルドが継続して機能するようになります。バージョンの削除を許可すると、その目的を達成することが不可能になります。ただし、公開できるクレートのバージョン数に制限はありません。

再度 `cargo publish` コマンドを実行します。今回は成功するはずです。

```bash
$ cargo publish
    Updating crates.io index
   Packaging guessing_game v0.1.0 (file:///projects/guessing_game)
   Verifying guessing_game v0.1.0 (file:///projects/guessing_game)
   Compiling guessing_game v0.1.0
(file:///projects/guessing_game/target/package/guessing_game-0.1.0)
    Finished dev [unoptimized + debuginfo] target(s) in 0.19s
   Uploading guessing_game v0.1.0 (file:///projects/guessing_game)
```

おめでとうございます！あなたは今、あなたのコードをRustコミュニティと共有しました。そして、誰でも簡単にあなたのクレートを自分のプロジェクトの依存関係として追加できます。

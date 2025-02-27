# 本物のHTMLを返す

空白のページだけでなく、より多くの内容を返す機能を実装しましょう。プロジェクトディレクトリのルートに、`src`ディレクトリではなく新しいファイル`hello.html`を作成します。好きなHTMLを入力できます。リスト20-4に1つの例を示します。

ファイル名：`hello.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Hello!</title>
  </head>
  <body>
    <h1>Hello!</h1>
    <p>Hi from Rust</p>
  </body>
</html>
```

リスト20-4：応答で返すサンプルHTMLファイル

これは、見出しといくつかのテキストがある最小限のHTML5ドキュメントです。要求があったときにこれをサーバーから返すには、`handle_connection`をリスト20-5のように変更して、HTMLファイルを読み取り、応答の本文として追加して送信します。

ファイル名：`src/main.rs`

```rust
use std::{
  1 fs,
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
};
--snip--

fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
    let http_request: Vec<_> = buf_reader
       .lines()
       .map(|result| result.unwrap())
       .take_while(|line|!line.is_empty())
       .collect();

    let status_line = "HTTP/1.1 200 OK";
    let contents = fs::read_to_string("hello.html").unwrap();
    let length = contents.len();

  2 let response = format!(
        "{status_line}\r\n\
         Content-Length: {length}\r\n\r\n\
         {contents}"
    );

    stream.write_all(response.as_bytes()).unwrap();
}
```

リスト20-5：`hello.html`の内容を応答の本文として送信する

`use`文に`fs`を追加して、標準ライブラリのファイルシステムモジュールをスコープに入れます\[1\]。ファイルの内容を文字列に読み取るコードはおそらくおなじみでしょう。リスト12-4のI/Oプロジェクトでファイルの内容を読み取るときに使用しました。

次に、`format!`を使用して、成功応答の本文としてファイルの内容を追加します\[2\]。有効なHTTP応答を確保するために、`Content-Length`ヘッダーを追加します。これは、応答本文のサイズ、つまりこの場合の`hello.html`のサイズに設定されます。

`cargo run`でこのコードを実行し、ブラウザで*127.0.0.1:7878*を読み込むと、HTMLがレンダリングされるはずです！

現在、`http_request`の要求データを無視して、無条件にHTMLファイルの内容を返しています。つまり、ブラウザで*127.0.0.1:7878/something-else*を要求しても、同じHTML応答が返されます。現時点では、私たちのサーバーは非常に制限されており、ほとんどのWebサーバーが行うことを行っていません。私たちは、要求に応じて応答をカスタマイズし、*/*に対する適切な形式の要求に対してのみHTMLファイルを返すようにしたいと思います。

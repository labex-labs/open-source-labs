# 要求を検証して選択的に応答する

今のところ、私たちのWebサーバーは、クライアントが何を要求しようと、ファイル内のHTMLを返します。HTMLファイルを返す前に、ブラウザが*/*を要求しているかどうかを確認する機能を追加し、ブラウザがそれ以外の何かを要求した場合はエラーを返すようにしましょう。このために、`handle_connection`をリスト20-6のように変更する必要があります。この新しいコードは、受け取った要求の内容を、*/*の要求がどのように見えるかを知っているものと照合し、要求を異なる方法で処理するための`if`と`else`ブロックを追加します。

ファイル名：`src/main.rs`

```rust
--snip--

fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
  1 let request_line = buf_reader
      .lines()
      .next()
      .unwrap()
      .unwrap();

  2 if request_line == "GET / HTTP/1.1" {
        let status_line = "HTTP/1.1 200 OK";
        let contents = fs::read_to_string("hello.html").unwrap();
        let length = contents.len();

        let response = format!(
            "{status_line}\r\n\
             Content-Length: {length}\r\n\r\n\
             {contents}"
        );

        stream.write_all(response.as_bytes()).unwrap();
  3 } else {
        // some other request
    }
}
```

リスト20-6：*/*への要求とその他の要求を異なる方法で処理する

HTTP要求の最初の行だけを見ることにしているので、要求全体をベクトルに読み込む代わりに、`next`を呼び出してイテレータから最初の項目を取得します\[1\]。最初の`unwrap`は`Option`を処理し、イテレータに項目がない場合にプログラムを停止します。2番目の`unwrap`は`Result`を処理し、リスト20-2で追加した`map`内の`unwrap`と同じ効果を持ちます。

次に、`request_line`をチェックして、*/*パスへのGET要求の要求行と一致するかどうかを確認します\[2\]。一致する場合は、`if`ブロックがHTMLファイルの内容を返します。

`request_line`が*/*パスへのGET要求と一致しない場合、それは他の要求を受け取ったことを意味します。`else`ブロック\[3\]に、他のすべての要求に応答するコードを追加します。

このコードを実行して、*127.0.0.1:7878*を要求してください。*hello.html*内のHTMLが表示されるはずです。*127.0.0.1:7878/something-else*のような他の要求を行うと、リスト20-1とリスト20-2のコードを実行したときに見たような接続エラーが表示されます。

次に、リスト20-7のコードを`else`ブロックに追加して、ステータスコード404を返す応答を返します。これは、要求のコンテンツが見つからないことを示します。また、エンドユーザーに対する応答を示すために、ブラウザでレンダリングするためのページ用のHTMLも返します。

ファイル名：`src/main.rs`

```rust
--snip--
} else {
  1 let status_line = "HTTP/1.1 404 NOT FOUND";
  2 let contents = fs::read_to_string("404.html").unwrap();
    let length = contents.len();

    let response = format!(
        "{status_line}\r\n\
         Content-Length: {length}\r\n\r\n
         {contents}"
    );

    stream.write_all(response.as_bytes()).unwrap();
}
```

リスト20-7：*/*以外の何かが要求された場合、ステータスコード404とエラーページで応答する

ここでは、応答にはステータスコード404と理由フレーズ`NOT FOUND`が含まれるステータス行があります\[1\]。応答の本文は、ファイル*404.html*内のHTMLになります\[1\]。エラーページ用に、*hello.html*の隣に*404.html*ファイルを作成する必要があります。好きなHTMLを使っても構いませんし、リスト20-8の例のHTMLを使っても構いません。

ファイル名：`404.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Hello!</title>
  </head>
  <body>
    <h1>Oops!</h1>
    <p>Sorry, I don't know what you're asking for.</p>
  </body>
</html>
```

リスト20-8：404応答で返すページ用のサンプルコンテンツ

これらの変更を加えて、サーバーを再度実行します。*127.0.0.1:7878*を要求すると、*hello.html*の内容が返され、*127.0.0.1:7878/foo*のような他の要求は、*404.html*のエラーHTMLが返されます。

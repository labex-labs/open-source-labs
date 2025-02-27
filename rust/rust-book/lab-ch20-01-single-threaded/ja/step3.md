# 要求を読み取る

ブラウザからの要求を読み取る機能を実装しましょう！ 最初に接続を取得し、その後接続に対して何かアクションを行うという関心事を分離するために、接続を処理するための新しい関数を始めます。この新しい`handle_connection`関数では、TCPストリームからデータを読み取り、それを表示して、ブラウザから送信されるデータを確認できるようにします。コードをリスト20-2のように変更します。

ファイル名：`src/main.rs`

```rust
1 use std::{
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
};

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();

      2 handle_connection(stream);
    }
}

fn handle_connection(mut stream: TcpStream) {
  3 let buf_reader = BufReader::new(&mut stream);
  4 let http_request: Vec<_> = buf_reader
      5.lines()
      6.map(|result| result.unwrap())
      7.take_while(|line|!line.is_empty())
       .collect();

  8 println!("Request: {:#?}", http_request);
}
```

リスト20-2：`TcpStream`から読み取り、データを表示する

`std::io::prelude`と`std::io::BufReader`をスコープに入れて、ストリームから読み書きするためのトレイトと型にアクセスできるようにします\[1\]。`main`関数の`for`ループでは、接続を確立したというメッセージを表示する代わりに、新しい`handle_connection`関数を呼び出し、`stream`を渡します\[2\]。

`handle_connection`関数では、`stream`への可変参照をラップする新しい`BufReader`インスタンスを作成します\[3\]。`BufReader`は、`std::io::Read`トレイトメソッドへの呼び出しを管理することでバッファリングを追加します。

ブラウザがサーバーに送信する要求の行を収集するために、`http_request`という名前の変数を作成します。`Vec<_>`型注釈を追加することで、これらの行をベクトルに収集することを示します\[4\]。

`BufReader`は`std::io::BufRead`トレイトを実装しており、これが`lines`メソッドを提供します\[5\]。`lines`メソッドは、データのストリームを改行バイトを見つけるたびに分割することで、`Result<String, std::io::Error>`のイテレータを返します。各`String`を取得するには、各`Result`に対してマップと`unwrap`を行います\[6\]。データが有効なUTF-8でない場合や、ストリームからの読み取りに問題がある場合、`Result`はエラーになる可能性があります。再び、本番用のプログラムはこれらのエラーをもっとスマートに処理する必要がありますが、簡単のためにエラーの場合にプログラムを停止することにします。

ブラウザは、HTTP要求の終了を2つの改行文字を連続して送信することで示します。したがって、ストリームから1つの要求を取得するには、空文字列になる行まで行を取得します\[7\]。行をベクトルに収集したら、それらをきれいなデバッグ形式で表示します\[8\]。これで、Webブラウザがサーバーに送信している指示を見ることができます。

このコードを試してみましょう！ プログラムを起動し、Webブラウザで要求を行います。ブラウザではまだエラーページが表示されますが、ターミナルでのプログラムの出力は次のようになります。

```bash
$ cargo run
   Compiling hello v0.1.0 (file:///projects/hello)
    Finished dev [unoptimized + debuginfo] target(s) in 0.42s
     Running `target/debug/hello`
Request: [
    "GET / HTTP/1.1",
    "Host: 127.0.0.1:7878",
    "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0)
Gecko/20100101 Firefox/99.0",
    "Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*
;q=0.8",
    "Accept-Language: en-US,en;q=0.5",
    "Accept-Encoding: gzip, deflate, br",
    "DNT: 1",
    "Connection: keep-alive",
    "Upgrade-Insecure-Requests: 1",
    "Sec-Fetch-Dest: document",
    "Sec-Fetch-Mode: navigate",
    "Sec-Fetch-Site: none",
    "Sec-Fetch-User:?1",
    "Cache-Control: max-age=0",
]
```

ブラウザによっては、やや異なる出力が得られる場合があります。今、要求データを表示しているので、要求の最初の行の`GET`の後のパスを見ることで、1つのブラウザ要求から複数の接続が得られる理由がわかります。繰り返しの接続がすべて*/*を要求している場合、ブラウザがプログラムから応答を得られないため、*/*を繰り返し取得しようとしていることがわかります。

この要求データを分解して、ブラウザがプログラムに要求している内容を理解しましょう。

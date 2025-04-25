# 送信機をクローン化して複数の生成元を作成する

先ほど、`mpsc` は「複数の生成元、単一の消費者」の略語であると述べました。では、`mpsc` を使って、リスト 16-10 のコードを拡張して、すべてが同じ受信機に値を送信する複数のスレッドを作成してみましょう。送信機をクローン化することで、これを行うことができます。リスト 16-11 を参照してください。

ファイル名：`src/main.rs`

```rust
--snip--

let (tx, rx) = mpsc::channel();

let tx1 = tx.clone();
thread::spawn(move || {
    let vals = vec![
        String::from("hi"),
        String::from("from"),
        String::from("the"),
        String::from("thread"),
    ];

    for val in vals {
        tx1.send(val).unwrap();
        thread::sleep(Duration::from_secs(1));
    }
});

thread::spawn(move || {
    let vals = vec![
        String::from("more"),
        String::from("messages"),
        String::from("for"),
        String::from("you"),
    ];

    for val in vals {
        tx.send(val).unwrap();
        thread::sleep(Duration::from_secs(1));
    }
});

for received in rx {
    println!("Got: {received}");
}

--snip--
```

リスト 16-11: 複数の生成元から複数のメッセージを送信する

今回は、最初の生成されたスレッドを作成する前に、送信機に対して `clone` を呼び出します。これにより、最初の生成されたスレッドに渡すことができる新しい送信機が得られます。元の送信機を 2 番目の生成されたスレッドに渡します。これにより、2 つのスレッドが得られ、それぞれが異なるメッセージを 1 つの受信機に送信します。

コードを実行すると、出力は以下のようになるはずです。

    Got: hi
    Got: more
    Got: from
    Got: messages
    Got: for
    Got: the
    Got: thread
    Got: you

システムによっては、値が別の順序で表示される場合があります。これが、並列処理を興味深く、また難しくするところです。`thread::sleep` を試してみて、異なるスレッドでさまざまな値を与えると、各実行はより非決定的になり、毎回異なる出力が生成されます。

ここまでチャネルの仕組みを見てきましたので、別の並列処理の方法を見てみましょう。

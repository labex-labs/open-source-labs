# チャネルと所有権の移転

所有権のルールはメッセージ送信において重要な役割を果たします。なぜなら、それが安全で並列処理可能なコードを書くのに役立つからです。並列プログラミングにおけるエラーを防ぐことは、Rust プログラム全体で所有権について考えることの利点です。チャネルと所有権がどのように協働して問題を防ぐかを示すために、実験を行いましょう。チャネルを通じて値を送信した後、生成されたスレッドで `val` 値を使用しようとします。リスト 16-9 のコードをコンパイルして、なぜこのコードが許されないかを確認してみましょう。

ファイル名：`src/main.rs`

```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let val = String::from("hi");
        tx.send(val).unwrap();
        println!("val is {val}");
    });

    let received = rx.recv().unwrap();
    println!("Got: {received}");
}
```

リスト 16-9: チャネルを通じて値を送信した後に `val` を使用しようとする

ここでは、`tx.send` を通じてチャネルに値を送信した後に `val` を出力しようとしています。これを許すのは良い考えではありません。値が別のスレッドに送信されると、そのスレッドが値を再利用しようとする前に、そのスレッドが値を変更または破棄する可能性があります。おそらく、他のスレッドによる変更が、データの不整合または存在しないデータにより、エラーや予期しない結果を引き起こす可能性があります。しかし、Rust はリスト 16-9 のコードをコンパイルしようとするとエラーを表示します。

```bash
error[E0382]: borrow of moved value: `val`
  --> src/main.rs:10:31
   |
8  |         let val = String::from("hi");
   |             --- move occurs because `val` has type `String`, which does
not implement the `Copy` trait
9  |         tx.send(val).unwrap();
   |                 --- value moved here
10 |         println!("val is {val}");
   |                           ^^^ value borrowed here after move
```

私たちの並列処理上のミスが、コンパイル時のエラーを引き起こしました。`send` 関数はそのパラメータの所有権を取得し、値が移動すると、受信側がその所有権を取得します。これにより、値を送信した後に偶然再利用することが防がれます。所有権システムがすべてが正常であることを確認します。

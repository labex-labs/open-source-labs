# 複数の値を送信し、受信側が待機する様子を見る

リスト16-8のコードはコンパイルされて実行されましたが、2つの別々のスレッドがチャネルを通じて相互に通信していることを明確に示していません。リスト16-10では、いくつかの修正を加えて、リスト16-8のコードが並列実行されていることを証明します。生成されたスレッドは、今回は複数のメッセージを送信し、各メッセージの間に1秒間停止します。

ファイル名: `src/main.rs`

```rust
use std::sync::mpsc;
use std::thread;
use std::time::Duration;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let vals = vec![
            String::from("hi"),
            String::from("from"),
            String::from("the"),
            String::from("thread"),
        ];

        for val in vals {
            tx.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });

    for received in rx {
        println!("Got: {received}");
    }
}
```

リスト16-10: 複数のメッセージを送信し、各メッセージの間に停止する

今回、生成されたスレッドには、メインスレッドに送信したい文字列のベクトルがあります。それらを反復処理して個別に送信し、各送信の間に1秒間の `Duration` 値を持つ `thread::sleep` 関数を呼び出すことで、各送信の間に停止します。

メインスレッドでは、もはや明示的に `recv` 関数を呼び出していません。代わりに、`rx` をイテレータとして扱っています。受信した各値に対して、それを出力します。チャネルがクローズされると、反復処理は終了します。

リスト16-10のコードを実行すると、各行の間に1秒間の停止があり、以下の出力が表示されるはずです。

    Got: hi
    Got: from
    Got: the
    Got: thread

メインスレッドの `for` ループには、停止または遅延するコードがないため、メインスレッドが生成されたスレッドから値を受信するのを待っていることがわかります。

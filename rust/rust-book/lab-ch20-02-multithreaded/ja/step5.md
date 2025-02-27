# 有限数のスレッドを作成する

私たちは、スレッドプールが同じような慣れ親しんだ方法で動作するようにしたいので、スレッドからスレッドプールに切り替える際に、APIを使用するコードに大きな変更を加える必要はありません。リスト20-12は、`thread::spawn` の代わりに使用したい `ThreadPool` 構造体の仮想インターフェイスを示しています。

ファイル名: `src/main.rs`

```rust
fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
  1 let pool = ThreadPool::new(4);

    for stream in listener.incoming() {
        let stream = stream.unwrap();

      2 pool.execute(|| {
            handle_connection(stream);
        });
    }
}
```

リスト20-12: 理想的な `ThreadPool` インターフェイス

この場合、4つのスレッド数を設定できる新しいスレッドプールを作成するために、`ThreadPool::new` を使用しています \[1\]。そして、`for` ループでは、`pool.execute` は `thread::spawn` と同じようなインターフェイスを持っています。つまり、各ストリームに対して実行するクロージャを受け取ります \[2\]。`pool.execute` を実装する必要があります。そうすることで、クロージャを受け取り、プール内のスレッドに実行させることができます。このコードはまだコンパイルされませんが、修正方法を教えてくれるように、コンパイラに挑戦してみましょう。

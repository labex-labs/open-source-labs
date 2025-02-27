# チャネル

Rustは、スレッド間の通信に非同期の「チャネル」を提供します。チャネルは、2つのエンドポイントである「送信者（Sender）」と「受信者（Receiver）」の間で情報を単方向に流すことができます。

```rust
use std::sync::mpsc::{Sender, Receiver};
use std::sync::mpsc;
use std::thread;

static NTHREADS: i32 = 3;

fn main() {
    // チャネルには2つのエンドポイントがあります。「Sender<T>」と「Receiver<T>」で、
    // ここで「T」は送信するメッセージの型です（型注釈は不要です）
    let (tx, rx): (Sender<i32>, Receiver<i32>) = mpsc::channel();
    let mut children = Vec::new();

    for id in 0..NTHREADS {
        // 送信者エンドポイントはコピー可能です
        let thread_tx = tx.clone();

        // 各スレッドはチャネルを通じてそのIDを送信します
        let child = thread::spawn(move || {
            // スレッドは「thread_tx」の所有権を取得します
            // 各スレッドはチャネルにメッセージをキューに入れます
            thread_tx.send(id).unwrap();

            // 送信はブロッキング操作ではなく、メッセージを送信した直後にスレッドは続行します
            println!("thread {} finished", id);
        });

        children.push(child);
    }

    // ここで、すべてのメッセージが収集されます
    let mut ids = Vec::with_capacity(NTHREADS as usize);
    for _ in 0..NTHREADS {
        // 「recv」メソッドはチャネルからメッセージを1つ選択します
        // 利用可能なメッセージがない場合、「recv」は現在のスレッドをブロックします
        ids.push(rx.recv());
    }

    // スレッドが残りの作業を完了するのを待ちます
    for child in children {
        child.join().expect("oops! the child thread panicked");
    }

    // メッセージが送信された順序を表示します
    println!("{:?}", ids);
}
```

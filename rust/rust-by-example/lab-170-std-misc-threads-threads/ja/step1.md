# スレッド

Rust は、`spawn` 関数を通じてネイティブな OS スレッドを生成するメカニズムを提供しています。この関数の引数は、移動クロージャです。

```rust
use std::thread;

const NTHREADS: u32 = 10;

// これは「メイン」スレッドです
fn main() {
    // 生成される子スレッドを保持するためのベクトルを作成します。
    let mut children = vec![];

    for i in 0..NTHREADS {
        // 別のスレッドを起動します
        children.push(thread::spawn(move || {
            println!("this is thread number {}", i);
        }));
    }

    for child in children {
        // スレッドが終了するのを待ちます。結果を返します。
        let _ = child.join();
    }
}
```

これらのスレッドは、OS によってスケジュールされます。

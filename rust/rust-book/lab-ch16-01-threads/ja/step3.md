# join ハンドルを使ってすべてのスレッドが終了するのを待つ

リスト 16-1 のコードは、主にメインスレッドが終了するために生成されたスレッドを不適切に早期に終了させるだけでなく、スレッドが実行される順序が保証されていないため、生成されたスレッドがまったく実行されないことさえ保証できません！

生成されたスレッドが実行されないか、または早期に終了する問題を解決するには、`thread::spawn` の戻り値を変数に保存します。`thread::spawn` の戻り型は `JoinHandle<T>` です。`JoinHandle<T>` は、所有された値であり、その `join` メソッドを呼び出すと、そのスレッドが終了するまで待ちます。リスト 16-2 は、リスト 16-1 で作成したスレッドの `JoinHandle<T>` を使用して、`join` を呼び出して、生成されたスレッドが `main` が終了する前に終了することを確認する方法を示しています。

ファイル名：`src/main.rs`

```rust
use std::thread;
use std::time::Duration;

fn main() {
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {i} from the spawned thread!");
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("hi number {i} from the main thread!");
        thread::sleep(Duration::from_millis(1));
    }

    handle.join().unwrap();
}
```

リスト 16-2: `thread::spawn` からの `JoinHandle<T>` を保存して、スレッドが完了するまで実行されることを保証する

ハンドルに対して `join` を呼び出すと、現在実行中のスレッドがブロックされ、ハンドルによって表されるスレッドが終了するまで待機します。スレッドを _ブロック_ するとは、そのスレッドが作業を実行したり終了したりできなくなることを意味します。`join` の呼び出しをメインスレッドの `for` ループの後に置いているため、リスト 16-2 を実行すると、次のような出力が生成されるはずです。

    hi number 1 from the main thread!
    hi number 2 from the main thread!
    hi number 1 from the spawned thread!
    hi number 3 from the main thread!
    hi number 2 from the spawned thread!
    hi number 4 from the main thread!
    hi number 3 from the spawned thread!
    hi number 4 from the spawned thread!
    hi number 5 from the spawned thread!
    hi number 6 from the spawned thread!
    hi number 7 from the spawned thread!
    hi number 8 from the spawned thread!
    hi number 9 from the spawned thread!

2 つのスレッドは引き続き交互になりますが、`handle.join()` の呼び出しのためにメインスレッドが待機し、生成されたスレッドが終了するまで終了しません。

では、`main` の `for` ループの前に `handle.join()` を移動するとどうなるか見てみましょう。このように：

ファイル名：`src/main.rs`

```rust
use std::thread;
use std::time::Duration;

fn main() {
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {i} from the spawned thread!");
            thread::sleep(Duration::from_millis(1));
        }
    });

    handle.join().unwrap();

    for i in 1..5 {
        println!("hi number {i} from the main thread!");
        thread::sleep(Duration::from_millis(1));
    }
}
```

メインスレッドは生成されたスレッドが終了するのを待ち、その後に `for` ループを実行するため、出力はもはや交互に表示されません。ここに示すように：

    hi number 1 from the spawned thread!
    hi number 2 from the spawned thread!
    hi number 3 from the spawned thread!
    hi number 4 from the spawned thread!
    hi number 5 from the spawned thread!
    hi number 6 from the spawned thread!
    hi number 7 from the spawned thread!
    hi number 8 from the spawned thread!
    hi number 9 from the spawned thread!
    hi number 1 from the main thread!
    hi number 2 from the main thread!
    hi number 3 from the main thread!
    hi number 4 from the main thread!

`join` を呼び出す場所などの小さな詳細が、スレッドが同時に実行されるかどうかに影響を与えることがあります。

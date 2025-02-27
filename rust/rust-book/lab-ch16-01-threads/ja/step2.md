# spawn を使って新しいスレッドを作成する

新しいスレッドを作成するには、`thread::spawn` 関数を呼び出し、そこに新しいスレッドで実行したいコードを含むクロージャ（第13章でクロージャについて説明しました）を渡します。リスト16-1の例では、メインスレッドからいくつかのテキストと、新しいスレッドから他のテキストを表示します。

ファイル名: `src/main.rs`

```rust
use std::thread;
use std::time::Duration;

fn main() {
    thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {i} from the spawned thread!");
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("hi number {i} from the main thread!");
        thread::sleep(Duration::from_millis(1));
    }
}
```

リスト16-1: 新しいスレッドを作成して、メインスレッドが別のものを表示する間に何かを表示する

Rust プログラムのメインスレッドが完了すると、すべての生成されたスレッドは、実行が完了しているかどうかに関係なく終了します。このプログラムの出力は、毎回少し異なる場合がありますが、次のようになるでしょう。

    hi number 1 from the main thread!
    hi number 1 from the spawned thread!
    hi number 2 from the main thread!
    hi number 2 from the spawned thread!
    hi number 3 from the main thread!
    hi number 3 from the spawned thread!
    hi number 4 from the main thread!
    hi number 4 from the spawned thread!
    hi number 5 from the spawned thread!

`thread::sleep` への呼び出しにより、スレッドは短時間実行を停止し、別のスレッドが実行できるようになります。スレッドはおそらく交互になるでしょうが、それは保証されていません。どのようにオペレーティングシステムがスレッドをスケジュールするかに依存します。この実行では、生成されたスレッドの print 文がコード内で最初に表示されているにもかかわらず、メインスレッドが最初に表示されました。また、生成されたスレッドに `i` が 9 になるまで表示するように指示しましたが、メインスレッドが終了する前に 5 までしか表示されませんでした。

このコードを実行して、メインスレッドの出力のみが表示されるか、または何も重複して表示されない場合は、範囲内の数値を増やして、オペレーティングシステムがスレッド間で切り替える機会を増やしてみてください。

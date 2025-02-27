# Arc

スレッド間で共有所有権が必要な場合、`Arc`（原子的参照カウント）を使用できます。この構造体は、`Clone`実装を通じて、メモリヒープ内の値の場所に対する参照ポインタを作成しながら参照カウンタを増やします。スレッド間で所有権を共有するため、値への最後の参照ポインタがスコープ外になると、変数が破棄されます。

```rust
use std::time::Duration;
use std::sync::Arc;
use std::thread;

fn main() {
    // この変数宣言では、その値が指定されています。
    let apple = Arc::new("the same apple");

    for _ in 0..10 {
        // ここでは値の指定がないため、メモリヒープ内の参照へのポインタです。
        let apple = Arc::clone(&apple);

        thread::spawn(move || {
            // Arcを使用したため、Arc変数ポインタの場所に割り当てられた値を使用してスレッドを生成できます。
            println!("{:?}", apple);
        });
    }

    // すべてのArcインスタンスが生成されたスレッドから出力されることを確認します。
    thread::sleep(Duration::from_secs(1));
}
```

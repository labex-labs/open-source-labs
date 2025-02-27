# トレイト

もちろん、`trait` も汎用的にすることができます。ここでは、`Drop` `trait` を再実装して、自身と入力を破棄する汎用メソッドとして定義します。

```rust
// コピー不可能な型。
struct Empty;
struct Null;

// `T` を汎用化したトレイト。
trait DoubleDrop<T> {
    // 呼び出し元の型に対して、追加の単一パラメータ `T` を取り、それに何もせずに済むメソッドを定義します。
    fn double_drop(self, _: T);
}

// 任意の汎用パラメータ `T` と呼び出し元 `U` に対して `DoubleDrop<T>` を実装します。
impl<T, U> DoubleDrop<T> for U {
    // このメソッドは渡された両方の引数の所有権を取得し、両方を解放します。
    fn double_drop(self, _: T) {}
}

fn main() {
    let empty = Empty;
    let null  = Null;

    // `empty` と `null` を解放します。
    empty.double_drop(null);

    //empty;
    //null;
    // ^ TODO: これらの行をコメントアウト解除してみてください。
}
```

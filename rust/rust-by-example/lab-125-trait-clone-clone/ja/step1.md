# Clone

リソースを扱う際、代入や関数呼び出し時の既定の動作は、それらを移すことです。しかし、時にはリソースのコピーも必要になります。

`Clone` トレイトは、まさにこれを可能にします。最も一般的には、`Clone` トレイトによって定義された `.clone()` メソッドを使用します。

```rust
// リソースのないユニット構造体
#[derive(Debug, Clone, Copy)]
struct Unit;

// `Clone` トレイトを実装するリソースを持つタプル構造体
#[derive(Clone, Debug)]
struct Pair(Box<i32>, Box<i32>);

fn main() {
    // `Unit` をインスタンス化
    let unit = Unit;
    // `Unit` をコピーする。移動するリソースはない
    let copied_unit = unit;

    // 両方の `Unit` は独立して使用できる
    println!("original: {:?}", unit);
    println!("copy: {:?}", copied_unit);

    // `Pair` をインスタンス化
    let pair = Pair(Box::new(1), Box::new(2));
    println!("original: {:?}", pair);

    // `pair` を `moved_pair` に移動する。リソースを移動する
    let moved_pair = pair;
    println!("moved: {:?}", moved_pair);

    // エラー！`pair` はリソースを失っている
    //println!("original: {:?}", pair);
    // TODO ^ この行のコメントを外してみる

    // `moved_pair` を `cloned_pair` にクローンする（リソースも含む）
    let cloned_pair = moved_pair.clone();
    // 元のペアを std::mem::drop を使って破棄する
    drop(moved_pair);

    // エラー！`moved_pair` は既に破棄されている
    //println!("copy: {:?}", moved_pair);
    // TODO ^ この行のコメントを外してみる

    // `.clone()` の結果は依然として使用できる！
    println!("clone: {:?}", cloned_pair);
}
```

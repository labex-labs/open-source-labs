# 表示

`fmt::Debug` はほとんど見やすくてクリーンな印象を与えませんので、出力の外観をカスタマイズすることが多くて有利です。これは、`{}` プリントマーカーを使用する `fmt::Display` を手動で実装することによって行われます。実装は次のようになります。

```rust
// `fmt` モジュールをインポート（`use` を通じて）して利用可能にします。
use std::fmt;

// `fmt::Display` を実装する構造体を定義します。これは、`i32` を含むタプル構造体 `Structure` です。
struct Structure(i32);

// `{}` マーカーを使用するには、型に対して `fmt::Display` トレイトを手動で実装する必要があります。
impl fmt::Display for Structure {
    // このトレイトにはこの正確なシグネチャの `fmt` が必要です。
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // 提供された出力ストリーム `f` に厳密に最初の要素を書き込みます。`fmt::Result` を返し、これは操作が成功したか失敗したかを示します。`write!` は `println!` と非常に似た構文を使用することに注意してください。
        write!(f, "{}", self.0)
    }
}
```

`fmt::Display` は `fmt::Debug` よりもクリーンになるかもしれませんが、これは `std` ライブラリにとって問題になります。曖昧な型はどのように表示するべきでしょうか？たとえば、`std` ライブラリがすべての `Vec<T>` に対して単一のスタイルを実装した場合、どのスタイルにするべきでしょうか？これらのどちらかになりますか？

- `Vec<path>`: `/:/etc:/home/username:/bin` (`:` で分割)
- `Vec<number>`: `1,2,3` (`, `で分割)

いいえ、すべての型に理想的なスタイルはなく、`std` ライブラリはそれを決めつけるつもりはありません。`Vec<T>` やその他のジェネリックコンテナに対しては `fmt::Display` が実装されていません。そのため、これらのジェネリックケースでは `fmt::Debug` を使用する必要があります。

ただし、これは問題ではありません。なぜなら、ジェネリックでない新しい _コンテナ_ 型に対しては、`fmt::Display` を実装できるからです。

```rust
use std::fmt; // `fmt` をインポート

// 2つの数値を保持する構造体。`Debug` を派生させるので、結果を `Display` と比較できます。
#[derive(Debug)]
struct MinMax(i64, i64);

// `MinMax` に対して `Display` を実装します。
impl fmt::Display for MinMax {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // `self.number` を使用して各位置データポイントを参照します。
        write!(f, "({}, {})", self.0, self.1)
    }
}

// フィールドが名前付きで比較できる構造体を定義します。
#[derive(Debug)]
struct Point2D {
    x: f64,
    y: f64,
}

// 同様に、`Point2D` に対して `Display` を実装します。
impl fmt::Display for Point2D {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // カスタマイズして、`x` と `y` のみを表示するようにします。
        write!(f, "x: {}, y: {}", self.x, self.y)
    }
}

fn main() {
    let minmax = MinMax(0, 14);

    println!("構造体を比較します:");
    println!("表示: {}", minmax);
    println!("デバッグ: {:?}", minmax);

    let big_range =   MinMax(-300, 300);
    let small_range = MinMax(-3, 3);

    println!("大きな範囲は {big} で、小さな範囲は {small} です",
             small = small_range,
             big = big_range);

    let point = Point2D { x: 3.3, y: 7.2 };

    println!("点を比較します:");
    println!("表示: {}", point);
    println!("デバッグ: {:?}", point);

    // エラー。`Debug` と `Display` の両方が実装されていますが、`{:b}` には `fmt::Binary` の実装が必要です。これは機能しません。
    // println!("Point2D を2進数で見るとどうなるでしょう: {:b}?", point);
}
```

したがって、`fmt::Display` は実装されていますが、`fmt::Binary` は実装されておらず、したがって使用できません。`std::fmt` には多くのそのような `トレイト` があり、それぞれ独自の実装が必要です。これについては、`std::fmt` でさらに詳しく説明されています。

## アクティビティ

上記の例の出力を確認した後、`Point2D` 構造体を参考に例に `Complex` 構造体を追加してください。同じ方法で印刷した場合、出力は次のようになるはずです。

```txt
表示: 3.3 + 7.2i
デバッグ: Complex { real: 3.3, imag: 7.2 }
```

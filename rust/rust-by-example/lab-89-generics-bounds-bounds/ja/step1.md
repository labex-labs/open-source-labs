# 制限

ジェネリクスを使用する場合、型パラメータは、型が実装する機能を規定するために、トレイトを _制限_ として使用することが多いです。たとえば、次の例では、トレイト `Display` を使用して印刷しているため、`T` が `Display` によって制限される必要があります。つまり、`T` _は_ `Display` を実装 _しなければなりません_。

```rust
// トレイト `Display` を実装しなければならないジェネリック型 `T` を受け取る関数 `printer` を定義します。
fn printer<T: Display>(t: T) {
    println!("{}", t);
}
```

制限は、制限に準拠する型にジェネリックを制限します。つまり：

```rust
struct S<T: Display>(T);

// エラー！`Vec<T>` は `Display` を実装していません。この
// 特殊化は失敗します。
let s = S(vec![1]);
```

制限のもう 1 つの効果は、ジェネリック インスタンスが、制限で指定されたトレイトの \[メソッド\] にアクセスできるようになることです。たとえば：

```rust
// 印刷マーカー `{:?}` を実装するトレイト。
use std::fmt::Debug;

trait HasArea {
    fn area(&self) -> f64;
}

impl HasArea for Rectangle {
    fn area(&self) -> f64 { self.length * self.height }
}

#[derive(Debug)]
struct Rectangle { length: f64, height: f64 }
#[allow(dead_code)]
struct Triangle  { length: f64, height: f64 }

// ジェネリック `T` は `Debug` を実装しなければなりません。
// 型に関係なく、これは正常に機能します。
fn print_debug<T: Debug>(t: &T) {
    println!("{:?}", t);
}

// `T` は `HasArea` を実装しなければなりません。
// 制限を満たす任意の型は、`HasArea` の関数 `area` にアクセスできます。
fn area<T: HasArea>(t: &T) -> f64 { t.area() }

fn main() {
    let rectangle = Rectangle { length: 3.0, height: 4.0 };
    let _triangle = Triangle  { length: 3.0, height: 4.0 };

    print_debug(&rectangle);
    println!("Area: {}", area(&rectangle));

    //print_debug(&_triangle);
    //println!("Area: {}", area(&_triangle));
    // ^ TODO: これらをコメントアウトしてみてください。
    // | エラー：`Debug` または `HasArea` のいずれかを実装していません。
}
```

追加の注意として、`where` 句を使用すると、場合によっては制限を適用して、表現力を高めることができます。

# ボックス、スタックとヒープ

Rust のすべての値はデフォルトでスタック割り当てされます。値は `Box<T>` を作成することで _ボクシング_（ヒープ上に割り当てる）することができます。ボックスは、型 `T` のヒープ上に割り当てられた値へのスマートポインタです。ボックスがスコープ外になると、そのデストラクタが呼び出され、内部オブジェクトが破棄され、ヒープ上のメモリが解放されます。

ボクシングされた値は `*` 演算子を使用して参照解除することができます。これにより、1 層の間接参照が取り除かれます。

```rust
use std::mem;

#[allow(dead_code)]
#[derive(Debug, Clone, Copy)]
struct Point {
    x: f64,
    y: f64,
}

// 長方形は、その左上と右下の角が空間上のどこにあるかで指定できます
#[allow(dead_code)]
struct Rectangle {
    top_left: Point,
    bottom_right: Point,
}

fn origin() -> Point {
    Point { x: 0.0, y: 0.0 }
}

fn boxed_origin() -> Box<Point> {
    // この点をヒープ上に割り当て、それへのポインタを返す
    Box::new(Point { x: 0.0, y: 0.0 })
}

fn main() {
    // （すべての型注釈は余分です）
    // スタック割り当ての変数
    let point: Point = origin();
    let rectangle: Rectangle = Rectangle {
        top_left: origin(),
        bottom_right: Point { x: 3.0, y: -4.0 }
    };

    // ヒープ割り当ての長方形
    let boxed_rectangle: Box<Rectangle> = Box::new(Rectangle {
        top_left: origin(),
        bottom_right: Point { x: 3.0, y: -4.0 },
    });

    // 関数の出力をボクシングすることができます
    let boxed_point: Box<Point> = Box::new(origin());

    // 二重の間接参照
    let box_in_a_box: Box<Box<Point>> = Box::new(boxed_origin());

    println!("Point はスタック上で {} バイトを占めています",
             mem::size_of_val(&point));
    println!("Rectangle はスタック上で {} バイトを占めています",
             mem::size_of_val(&rectangle));

    // ボックスのサイズ == ポインタのサイズ
    println!("ボックス化された点はスタック上で {} バイトを占めています",
             mem::size_of_val(&boxed_point));
    println!("ボックス化された長方形はスタック上で {} バイトを占めています",
             mem::size_of_val(&boxed_rectangle));
    println!("ボックスのボックスはスタック上で {} バイトを占めています",
             mem::size_of_val(&box_in_a_box));

    // `boxed_point` に含まれるデータを `unboxed_point` にコピーする
    let unboxed_point: Point = *boxed_point;
    println!("参照解除された点はスタック上で {} バイトを占めています",
             mem::size_of_val(&unboxed_point));
}
```

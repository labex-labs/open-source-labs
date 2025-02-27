# 構造体

`struct` キーワードを使って作成できる構造体（「struct」）には 3 種類あります。

- タプル構造体、基本的には名前付きのタプルです。
- 古典的な C 構造体
- ユニット構造体、フィールドがなく、ジェネリクスに便利です。

```rust
// 未使用のコードに対する警告を非表示にする属性。
#![allow(dead_code)]

#[derive(Debug)]
struct Person {
    name: String,
    age: u8,
}

// ユニット構造体
struct Unit;

// タプル構造体
struct Pair(i32, f32);

// 2 つのフィールドを持つ構造体
struct Point {
    x: f32,
    y: f32,
}

// 構造体は、別の構造体のフィールドとして再利用できます
struct Rectangle {
    // 矩形は、左上と右下の角が空間上のどこにあるかで指定できます。
    top_left: Point,
    bottom_right: Point,
}

fn main() {
    // フィールド初期化ショートハンドを使って構造体を作成
    let name = String::from("Peter");
    let age = 27;
    let peter = Person { name, age };

    // デバッグ用の構造体を出力
    println!("{:?}", peter);

    // `Point` をインスタンス化
    let point: Point = Point { x: 10.3, y: 0.4 };

    // 点のフィールドにアクセス
    println!("point coordinates: ({}, {})", point.x, point.y);

    // 構造体更新構文を使って、他の点のフィールドを使って新しい点を作成
    let bottom_right = Point { x: 5.2,..point };

    // `bottom_right.y` は `point.y` と同じになります。なぜなら、`point` のそのフィールドを使ったからです。
    println!("second point: ({}, {})", bottom_right.x, bottom_right.y);

    // `let` バインドを使って点を分解
    let Point { x: left_edge, y: top_edge } = point;

    let _rectangle = Rectangle {
        // 構造体のインスタンス化も式です
        top_left: Point { x: left_edge, y: top_edge },
        bottom_right: bottom_right,
    };

    // ユニット構造体をインスタンス化
    let _unit = Unit;

    // タプル構造体をインスタンス化
    let pair = Pair(1, 0.1);

    // タプル構造体のフィールドにアクセス
    println!("pair contains {:?} and {:?}", pair.0, pair.1);

    // タプル構造体を分解
    let Pair(integer, decimal) = pair;

    println!("pair contains {:?} and {:?}", integer, decimal);
}
```

## チャレンジ

1. `Rectangle` の面積を計算する関数 `rect_area` を追加します（ネストした分解を使ってみてください）。
2. `Point` と `f32` を引数に取り、その点を左上隅とし、幅と高さが `f32` に対応する `Rectangle` を返す関数 `square` を追加します。

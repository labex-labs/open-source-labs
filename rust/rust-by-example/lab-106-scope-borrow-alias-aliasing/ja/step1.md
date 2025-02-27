# エイリアシング

データは不変参照で任意の回数借りることができますが、不変参照中は、元のデータを可変参照で借りることはできません。一方、可変参照は一度に1つだけ許されます。可変参照が最後に使用された後にのみ、元のデータを再び借りることができます。

```rust
struct Point { x: i32, y: i32, z: i32 }

fn main() {
    let mut point = Point { x: 0, y: 0, z: 0 };

    let borrowed_point = &point;
    let another_borrow = &point;

    // 参照や元の所有者を通じてデータにアクセスできます
    println!("Point has coordinates: ({}, {}, {})",
                borrowed_point.x, another_borrow.y, point.z);

    // エラー！`point`を可変参照で借りることができません。なぜなら、現在は不変参照で借りられているからです。
    // let mutable_borrow = &mut point;
    // TODO ^ この行のコメントを外してみてください

    // ここでは借りた値を再利用します
    println!("Point has coordinates: ({}, {}, {})",
                borrowed_point.x, another_borrow.y, point.z);

    // 不変参照はコードの残りではもはや使用されないので、
    // 可変参照で再借用することができます。
    let mutable_borrow = &mut point;

    // 可変参照を通じてデータを変更します
    mutable_borrow.x = 5;
    mutable_borrow.y = 2;
    mutable_borrow.z = 1;

    // エラー！`point`を不変参照で借りることができません。なぜなら、現在は可変参照で借りられているからです。
    // let y = &point.y;
    // TODO ^ この行のコメントを外してみてください

    // エラー！`println!`は不変参照を取るため、出力できません。
    // println!("Point Z coordinate is {}", point.z);
    // TODO ^ この行のコメントを外してみてください

    // オッケー！可変参照は不変参照として`println!`に渡すことができます
    println!("Point has coordinates: ({}, {}, {})",
                mutable_borrow.x, mutable_borrow.y, mutable_borrow.z);

    // 可変参照はコードの残りではもはや使用されないので、再借用することができます
    let new_borrowed_point = &point;
    println!("Point now has coordinates: ({}, {}, {})",
             new_borrowed_point.x, new_borrowed_point.y, new_borrowed_point.z);
}
```

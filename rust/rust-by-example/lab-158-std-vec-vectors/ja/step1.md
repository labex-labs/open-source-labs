# ベクトル

ベクトルはリサイズ可能な配列です。スライスと同様に、そのサイズはコンパイル時にはわかりませんが、いつでも拡大または縮小できます。ベクトルは 3 つのパラメータを使用して表されます。

- データへのポインタ
- 長さ
- 容量

容量は、ベクトルに予約されているメモリ量を示します。長さが容量より小さい限り、ベクトルは拡大できます。このしきい値を超える必要がある場合、ベクトルはより大きな容量で再割り当てされます。

```rust
fn main() {
    // 反復子をベクトルに収集できます
    let collected_iterator: Vec<i32> = (0..10).collect();
    println!("Collected (0..10) into: {:?}", collected_iterator);

    // `vec!` マクロを使用してベクトルを初期化できます
    let mut xs = vec![1i32, 2, 3];
    println!("Initial vector: {:?}", xs);

    // ベクトルの末尾に新しい要素を挿入します
    println!("Push 4 into the vector");
    xs.push(4);
    println!("Vector: {:?}", xs);

    // エラー！ 不変ベクトルは拡大できません
    collected_iterator.push(0);
    // FIXME ^ Comment out this line

    // `len` メソッドは、現在ベクトルに格納されている要素数を返します
    println!("Vector length: {}", xs.len());

    // インデックス付けは角かっこを使用して行われます (インデックスは 0 から始まります)
    println!("Second element: {}", xs[1]);

    // `pop` はベクトルから最後の要素を削除して返します
    println!("Pop last element: {:?}", xs.pop());

    // 範囲外のインデックス付けはパニックを引き起こします
    println!("Fourth element: {}", xs[3]);
    // FIXME ^ Comment out this line

    // `Vector` は簡単に反復処理できます
    println!("Contents of xs:");
    for x in xs.iter() {
        println!("> {}", x);
    }

    // `Vector` は、反復処理回数を別の変数 (`i`) で列挙しながらも反復処理できます
    for (i, x) in xs.iter().enumerate() {
        println!("In position {} we have value {}", i, x);
    }

    // `iter_mut` のおかげで、可変 `Vector` も各値を変更できるように反復処理できます
    for x in xs.iter_mut() {
        *x *= 3;
    }
    println!("Updated vector: {:?}", xs);
}
```

さらに多くの `Vec` メソッドは `std::vec` モジュールの下で見つけることができます。

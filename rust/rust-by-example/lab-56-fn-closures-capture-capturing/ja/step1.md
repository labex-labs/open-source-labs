# キャプチャ

クロージャは本質的に柔軟であり、注釈なしでクロージャを動作させるために機能が必要とすることを行います。これにより、キャプチャは使用ケースに柔軟に適応でき、時には移動し、時には借用します。クロージャは変数を次のようにキャプチャできます。

- 参照による：`&T`
- 可変参照による：`&mut T`
- 値による：`T`

クロージャは参照によって優先的に変数をキャプチャし、必要に応じて下位に行きます。

```rust
fn main() {
    use std::mem;

    let color = String::from("green");

    // `color` を出力するクロージャ。これはすぐに `color` を借用 (`&`) し、
    // 借用とクロージャを `print` 変数に格納します。`print` が最後に使用されるまで、
    // 借用されたままになります。
    //
    // `println!` は不変参照による引数のみを必要とするため、
    // それ以上制限の厳しいものは要求しません。
    let print = || println!("`color`: {}", color);

    // 借用を使用してクロージャを呼び出します。
    print();

    // `color` は再び不変に借用できます。なぜなら、クロージャは `color` への不変参照のみを保持しているからです。
    let _reborrow = &color;
    print();

    // `print` の最終使用後は、移動または再借用が許可されます
    let _color_moved = color;


    let mut count = 0;
    // `count` をインクリメントするクロージャは、`&mut count` または `count` のどちらかを取ることができますが、
    // `&mut count` の制限が少ないため、それを採用します。すぐに `count` を借用します。
    //
    // `inc` には `mut` が必要です。なぜなら、内部に `&mut` が格納されているからです。
    // したがって、クロージャを呼び出すと、`mut` が必要なクロージャが変更されます。
    let mut inc = || {
        count += 1;
        println!("`count`: {}", count);
    };

    // 可変借用を使用してクロージャを呼び出します。
    inc();

    // クロージャはまだ `count` を可変に借用しています。なぜなら、後で呼び出されるからです。
    // 再借用の試みはエラーにつながります。
    // let _reborrow = &count;
    // ^ TODO: この行のコメントを外してみてください。
    inc();

    // クロージャはもはや `&mut count` を借用する必要がありません。したがって、エラーなく再借用することができます
    let _count_reborrowed = &mut count;


    // コピーできない型。
    let movable = Box::new(3);

    // `mem::drop` は `T` を必要とするため、これは値によって取る必要があります。コピー可能な型は、
    // クロージャにコピーされ、元のものは変更されません。
    // コピーできない型は移動する必要があり、したがって `movable` はすぐにクロージャに移動します。
    let consume = || {
        println!("`movable`: {:?}", movable);
        mem::drop(movable);
    };

    // `consume` は変数を消費するため、これは一度だけ呼び出すことができます。
    consume();
    // consume();
    // ^ TODO: この行のコメントを外してみてください。
}
```

垂直パイプの前に `move` を使用すると、クロージャがキャプチャした変数の所有権を取得するように強制されます。

```rust
fn main() {
    // `Vec` はコピーできないセマンティクスを持っています。
    let haystack = vec![1, 2, 3];

    let contains = move |needle| haystack.contains(needle);

    println!("{}", contains(&1));
    println!("{}", contains(&4));

    // println!("There're {} elements in vec", haystack.len());
    // ^ 上の行のコメントを外すと、コンパイル時エラーが発生します。
    // なぜなら、借用チェッカーは変数が移動された後は再利用を許可しないからです。

    // クロージャのシグネチャから `move` を削除すると、クロージャが _haystack_ 変数を不変に借用するようになります。
    // したがって、_haystack_ はまだ利用可能であり、上の行のコメントを外してもエラーにはなりません。
}
```

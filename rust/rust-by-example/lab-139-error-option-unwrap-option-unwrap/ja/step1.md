# `Option` と `unwrap`

前の例では、意図的にプログラムを失敗させることができることを示しました。私たちは、砂糖入りのレモネードを飲んだ場合にプログラムに`panic`させるように指示しました。しかし、何か飲み物を期待しているのに何も受け取らなかった場合どうでしょうか。その場合も同じくらい悪いので、対処する必要があります！

私たちは、レモネードの場合と同じように、空の文字列 (`""`) と比較することができます。Rustを使っているので、代わりにコンパイラに飲み物がない場合を指摘してもらいましょう。

存在しない可能性がある場合には、`std`ライブラリにある`Option<T>`と呼ばれる列挙型が使用されます。これは、2つの「オプション」のいずれかとして表れます。

- `Some(T)`: 型`T`の要素が見つかった
- `None`: 要素が見つからなかった

これらのケースは、`match`を使って明示的に処理することも、`unwrap`を使って暗黙的に処理することもできます。暗黙的な処理では、内部要素が返されるか、`panic`が発生します。

`expect`を使って`panic`を手動でカスタマイズすることも可能ですが、それ以外の場合、`unwrap`は明示的な処理よりも意味のない出力になります。次の例では、明示的な処理が、望む場合は`panic`するオプションを維持しながら、より制御された結果をもたらします。

```rust
// 大人はすべてを見てきており、どんな飲み物でも上手に扱えます。
// すべての飲み物は `match` を使って明示的に処理されます。
fn give_adult(drink: Option<&str>) {
    // 各ケースに対するアクションを指定します。
    match drink {
        Some("lemonade") => println!("Yuck! Too sugary."),
        Some(inner)   => println!("{}? How nice.", inner),
        None          => println!("No drink? Oh well."),
    }
}

// 他の人は、砂糖入りの飲み物を飲む前に `panic` します。
// すべての飲み物は `unwrap` を使って暗黙的に処理されます。
fn drink(drink: Option<&str>) {
    // `unwrap` は `None` を受け取ったときに `panic` を返します。
    let inside = drink.unwrap();
    if inside == "lemonade" { panic!("AAAaaaaa!!!!"); }

    println!("I love {}s!!!!!", inside);
}

fn main() {
    let water  = Some("water");
    let lemonade = Some("lemonade");
    let void  = None;

    give_adult(water);
    give_adult(lemonade);
    give_adult(void);

    let coffee = Some("coffee");
    let nothing = None;

    drink(coffee);
    drink(nothing);
}
```

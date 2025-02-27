# 値にバインドされるパターン

マッチのアームのもう一つの便利な機能は、パターンに一致する値の一部にバインドできることです。これが、列挙型のバリアントから値を抽出する方法です。

例として、列挙型のバリアントの一つを変更して、その中にデータを保持させましょう。1999年から2008年まで、アメリカは50州それぞれに異なるデザインの1セント硬貨を発行しました。他の硬貨には州のデザインはありませんので、1セント硬貨だけがこの追加の値を持っています。この情報を`enum`に追加するには、`Quarter`バリアントを変更して、その中に格納された`UsState`値を含めます。これをリスト6-4で行っています。

```rust
#[derive(Debug)] // これですぐに状態を調べることができます
enum UsState {
    Alabama,
    Alaska,
    --snip--
}

enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(UsState),
}
```

リスト6-4：`Quarter`バリアントが`UsState`値も保持する`Coin`列挙型

友人が50州の1セント硬貨をすべて集めようとしていると想像してみましょう。私たちが硬貨の種類で零銭を分類する間、各1セント硬貨に関連付けられた州の名前も呼び出します。もし友人が持っていない硬貨があれば、彼らはそれをコレクションに追加できるようにします。

このコードのマッチ式では、`Coin::Quarter`の値と一致するパターンに`state`という変数を追加します。`Coin::Quarter`が一致すると、`state`変数はその1セント硬貨の州の値にバインドされます。そして、そのアームのコードで`state`を使うことができます。例えばこのように：

```rust
fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter(state) => {
            println!("State quarter from {:?}!", state);
            25
        }
    }
}
```

`value_in_cents(Coin::Quarter(UsState::Alaska))`を呼び出した場合、`coin`は`Coin::Quarter(UsState::Alaska)`になります。その値を各マッチのアームと比較すると、`Coin::Quarter(state)`に到達するまでは一致しません。その時点で、`state`のバインドは値`UsState::Alaska`になります。そして、そのバインドを`println!`式で使うことができるので、`Quarter`の`Coin`列挙型のバリアントから内部の州の値を取り出すことができます。

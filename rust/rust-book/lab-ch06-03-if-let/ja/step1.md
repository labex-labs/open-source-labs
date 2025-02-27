# if letによる簡潔な制御フロー

`if let`構文を使うと、`if`と`let`を組み合わせて、1つのパターンに一致する値を処理し、それ以外を無視するための、より簡潔な方法ができます。リスト6-6のプログラムを見てみましょう。このプログラムは、`config_max`変数の`Option<u8>`値をマッチングしますが、値が`Some`バリアントの場合にのみコードを実行したいと思っています。

```rust
let config_max = Some(3u8);
match config_max {
    Some(max) => println!("The maximum is configured to be {max}"),
    _ => (),
}
```

リスト6-6：値が`Some`の場合にのみコードを実行する`match`

値が`Some`の場合、パターン内の変数`max`に値をバインドすることで、`Some`バリアント内の値を表示します。`None`値には何もしたくありません。`match`式を満たすために、1つのバリアントを処理した後に`_ => ()`を追加する必要がありますが、これは面倒なボイラープレートコードです。

代わりに、`if let`を使ってもっと短い方法で書くことができます。以下のコードは、リスト6-6の`match`と同じ動作をします。

```rust
let config_max = Some(3u8);
if let Some(max) = config_max {
    println!("The maximum is configured to be {max}");
}
```

`if let`構文は、等号で区切られたパターンと式を取ります。これは`match`と同じように動作します。式は`match`に渡され、パターンは最初のアームになります。この場合、パターンは`Some(max)`で、`max`は`Some`内の値にバインドされます。その後、`if let`ブロックの本体では、対応する`match`アームで`max`を使ったのと同じ方法で`max`を使うことができます。値がパターンに一致しない場合、`if let`ブロック内のコードは実行されません。

`if let`を使うと、入力が少なく、インデントが少なく、ボイラープレートコードが少なくなります。ただし、`match`が強制する網羅的なチェックが失われます。`match`と`if let`の間で選ぶかどうかは、特定の状況で何をしているか、および網羅的なチェックを失うことに対して簡潔さを得ることが適切なトレードオフかどうかに依存します。

言い換えると、`if let`は、値が1つのパターンに一致したときにコードを実行し、その後他のすべての値を無視する`match`のシンタックスシュガーと考えることができます。

`if let`には`else`を含めることができます。`else`に付随するコードブロックは、`if let`と`else`に等価な`match`式の`_`ケースに付随するコードブロックと同じです。リスト6-4の`Coin`列挙型の定義を思い出してください。`Quarter`バリアントには`UsState`値も含まれていました。4分の1硬貨以外の硬貨をすべてカウントしながら、4分の1硬貨の状態も表示したい場合、`match`式を使ってこれを行うことができます。

```rust
let mut count = 0;
match coin {
    Coin::Quarter(state) => println!("State quarter from {:?}!", state),
    _ => count += 1,
}
```

または、`if let`と`else`式を使うこともできます。

```rust
let mut count = 0;
if let Coin::Quarter(state) = coin {
    println!("State quarter from {:?}!", state);
} else {
    count += 1;
}
```

プログラムに`match`を使って表現するのが面倒くさい論理がある場合、`if let`もRustのツールボックスにあることを忘れないでください。

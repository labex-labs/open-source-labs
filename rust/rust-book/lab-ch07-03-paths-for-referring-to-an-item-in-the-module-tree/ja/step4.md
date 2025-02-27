# 構造体と列挙体の公開

構造体と列挙体を公開として指定するためにも `pub` を使用できますが、構造体と列挙体に対する `pub` の使用にはいくつかの追加の詳細があります。構造体定義の前に `pub` を使用すると、構造体が公開されますが、構造体のフィールドは依然として非公開になります。各フィールドを個別に公開するかどうかは、ケースバイケースで決定することができます。リスト7-9では、公開された `toast` フィールドと非公開の `seasonal_fruit` フィールドを持つ公開 `back_of_house::Breakfast` 構造体を定義しています。これは、レストランのケースをモデル化しており、お客様は食事に付くパンの種類を選ぶことができますが、シェフが季節に応じて在庫のある果物を選んで食事に添えます。利用可能な果物は急速に変化するため、お客様は果物を選ぶことも、また、どの果物が届くかを見ることもできません。

ファイル名: `src/lib.rs`

```rust
mod back_of_house {
    pub struct Breakfast {
        pub toast: String,
        seasonal_fruit: String,
    }

    impl Breakfast {
        pub fn summer(toast: &str) -> Breakfast {
            Breakfast {
                toast: String::from(toast),
                seasonal_fruit: String::from("peaches"),
            }
        }
    }
}

pub fn eat_at_restaurant() {
    // 夏にライ麦トーストの朝食を注文する
    let mut meal = back_of_house::Breakfast::summer("Rye");
    // 食べたいパンの種類を変更する
    meal.toast = String::from("Wheat");
    println!("I'd like {} toast please", meal.toast);

    // 次の行をコメントアウトを解除するとコンパイルエラーになります。食事に添えられる季節限定の果物を見たり変更したりすることはできません
    // meal.seasonal_fruit = String::from("blueberries");
}
```

リスト7-9: 一部の公開フィールドと一部の非公開フィールドを持つ構造体

`back_of_house::Breakfast` 構造体の `toast` フィールドが公開されているため、`eat_at_restaurant` ではドット表記を使用して `toast` フィールドに書き込み、読み取りすることができます。`seasonal_fruit` フィールドは非公開であるため、`eat_at_restaurant` では使用できないことに注意してください。`seasonal_fruit` フィールドの値を変更する行のコメントアウトを解除して、どのエラーが表示されるか確認してみてください！

また、`back_of_house::Breakfast` が非公開フィールドを持っているため、構造体には `Breakfast` のインスタンスを構築する公開関連関数（ここでは `summer` と名付けました）が必要です。`Breakfast` にそのような関数がない場合、`eat_at_restaurant` で `Breakfast` のインスタンスを作成できないことになります。なぜなら、`eat_at_restaurant` で非公開の `seasonal_fruit` フィールドの値を設定できないからです。

対照的に、列挙体を公開すると、そのすべてのバリアントが公開されます。`enum` キーワードの前に `pub` だけが必要です。これは、リスト7-10に示すようになります。

ファイル名: `src/lib.rs`

```rust
mod back_of_house {
    pub enum Appetizer {
        Soup,
        Salad,
    }
}

pub fn eat_at_restaurant() {
    let order1 = back_of_house::Appetizer::Soup;
    let order2 = back_of_house::Appetizer::Salad;
}
```

リスト7-10: 列挙体を公開として指定すると、そのすべてのバリアントが公開されます。

`Appetizer` 列挙体を公開として指定したため、`eat_at_restaurant` では `Soup` と `Salad` のバリアントを使用できます。

列挙体のバリアントが公開されない限り、列挙体はあまり役に立ちません。すべてのケースで列挙体のバリアントすべてに `pub` を付けるのは面倒です。したがって、列挙体のバリアントの既定値は公開になっています。構造体は、フィールドが公開されていなくてもよく使われるため、構造体のフィールドは、`pub` で注釈付けされていない限り、既定ですべてが非公開であるという一般的なルールに従います。

`pub` に関するもう1つの状況がありますが、ここでは扱っていません。それは、最後のモジュールシステム機能である `use` キーワードです。まずは `use` 自体を扱い、その後、`pub` と `use` を組み合わせる方法を示します。

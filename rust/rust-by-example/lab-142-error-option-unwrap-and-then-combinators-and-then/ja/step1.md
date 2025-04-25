# コンビネータ：`and_then`

`map()` は、`match` 文を単純化するための連鎖可能な方法として説明されました。ただし、`Option<T>` を返す関数に `map()` を使用すると、ネストされた `Option<Option<T>>` が生成されます。複数の呼び出しを連鎖させると混乱することがあります。そこで、一部の言語では flatmap として知られる別のコンビネータである `and_then()` が登場します。

`and_then()` は、ラップされた値で関数入力を呼び出し、結果を返します。`Option` が `None` の場合は代わりに `None` を返します。

次の例では、`cookable_v3()` は `Option<Food>` を返します。`map()` を使用して `and_then()` の代わりにすると、`Option<Option<Food>>` が返され、これは `eat()` にとって無効な型になります。

```rust
#![allow(dead_code)]

#[derive(Debug)] enum Food { CordonBleu, Steak, Sushi }
#[derive(Debug)] enum Day { Monday, Tuesday, Wednesday }

// すしを作る材料がありません。
fn have_ingredients(food: Food) -> Option<Food> {
    match food {
        Food::Sushi => None,
        _           => Some(food),
    }
}

// コルドンブルー以外のすべてのレシピがあります。
fn have_recipe(food: Food) -> Option<Food> {
    match food {
        Food::CordonBleu => None,
        _                => Some(food),
    }
}

// 料理を作るには、レシピと材料の両方が必要です。
// このロジックを `match` のチェーンで表現できます。
fn cookable_v1(food: Food) -> Option<Food> {
    match have_recipe(food) {
        None       => None,
        Some(food) => have_ingredients(food),
    }
}

// これは便利にも `and_then()` を使ってよりコンパクトに書き直すことができます。
fn cookable_v3(food: Food) -> Option<Food> {
    have_recipe(food).and_then(have_ingredients)
}

// そうでなければ、`Option<Option<Food>>` を `flatten()` して
// `Option<Food>` を取得する必要があります。
fn cookable_v2(food: Food) -> Option<Food> {
    have_recipe(food).map(have_ingredients).flatten()
}

fn eat(food: Food, day: Day) {
    match cookable_v3(food) {
        Some(food) => println!("Yay! On {:?} we get to eat {:?}.", day, food),
        None       => println!("Oh no. We don't get to eat on {:?}?", day),
    }
}

fn main() {
    let (cordon_bleu, steak, sushi) = (Food::CordonBleu, Food::Steak, Food::Sushi);

    eat(cordon_bleu, Day::Monday);
    eat(steak, Day::Tuesday);
    eat(sushi, Day::Wednesday);
}
```

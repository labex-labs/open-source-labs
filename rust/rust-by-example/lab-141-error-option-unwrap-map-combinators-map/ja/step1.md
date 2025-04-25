# コンビネータ：`map`

`match` は `Option` を処理するための有効なメソッドです。ただし、最終的には、特に入力に対してのみ有効な操作の場合、頻繁に使用するのが面倒くさい場合があります。これらの場合、コンビネータを使用して、モジューラな方法で制御フローを管理できます。

`Option` には、`Some -> Some` と `None -> None` の単純なマッピング用のコンビネータである `map()` と呼ばれる組み込みメソッドがあります。さらに柔軟性を持たせるために、複数の `map()` 呼び出しをチェーン化できます。

次の例では、`process()` は以前のすべての関数を置き換えますが、コンパクトなままです。

```rust
#![allow(dead_code)]

#[derive(Debug)] enum Food { Apple, Carrot, Potato }

#[derive(Debug)] struct Peeled(Food);
#[derive(Debug)] struct Chopped(Food);
#[derive(Debug)] struct Cooked(Food);

// 食材を皮む。何もない場合は `None` を返します。
// そうでない場合は、皮をむいた食材を返します。
fn peel(food: Option<Food>) -> Option<Peeled> {
    match food {
        Some(food) => Some(Peeled(food)),
        None       => None,
    }
}

// 食材を刻む。何もない場合は `None` を返します。
// そうでない場合は、刻んだ食材を返します。
fn chop(peeled: Option<Peeled>) -> Option<Chopped> {
    match peeled {
        Some(Peeled(food)) => Some(Chopped(food)),
        None               => None,
    }
}

// 食材を調理する。ここでは、ケース処理に `match` の代わりに `map()` を使っています。
fn cook(chopped: Option<Chopped>) -> Option<Cooked> {
    chopped.map(|Chopped(food)| Cooked(food))
}

// 食材を順番に皮む、刻む、調理する関数。
// `map()` の複数の使用をチェーン化してコードを簡略化します。
fn process(food: Option<Food>) -> Option<Cooked> {
    food.map(|f| Peeled(f))
     .map(|Peeled(f)| Chopped(f))
     .map(|Chopped(f)| Cooked(f))
}

// 食べる前に食材があるかどうかを確認します！
fn eat(food: Option<Cooked>) {
    match food {
        Some(food) => println!("Mmm. I love {:?}", food),
        None       => println!("Oh no! It wasn't edible."),
    }
}

fn main() {
    let apple = Some(Food::Apple);
    let carrot = Some(Food::Carrot);
    let potato = None;

    let cooked_apple = cook(chop(peel(apple)));
    let cooked_carrot = cook(chop(peel(carrot)));
    // 今度は見た目が簡単な `process()` を試してみましょう。
    let cooked_potato = process(potato);

    eat(cooked_apple);
    eat(cooked_carrot);
    eat(cooked_potato);
}
```

# オプションとデフォルト値の展開

`Option` を展開し、`None` の場合にはデフォルト値に切り替える方法は複数あります。私たちのニーズに合う方法を選ぶために、以下のことを考慮する必要があります。

- 即時評価または遅延評価が必要か？
- 元の空の値をそのままに保つ必要があるか、置き換える必要があるか？

## `or()` はチェーン可能で、即時評価し、空の値をそのままに保つ

`or()` はチェーン可能で、引数を即時評価します。以下の例に示すように、`or` の引数は即時評価されるため、`or` に渡される変数は移動されます。

```rust
#[derive(Debug)]
enum Fruit { Apple, Orange, Banana, Kiwi, Lemon }

fn main() {
    let apple = Some(Fruit::Apple);
    let orange = Some(Fruit::Orange);
    let no_fruit: Option<Fruit> = None;

    let first_available_fruit = no_fruit.or(orange).or(apple);
    println!("first_available_fruit: {:?}", first_available_fruit);
    // first_available_fruit: Some(Orange)

    // `or` はその引数を移動します。
    // 上の例では、`or(orange)` は `Some` を返したため、`or(apple)` は呼び出されませんでした。
    // ただし、`apple` という名前の変数は移動されており、もはや使用できません。
    // println!("Variable apple was moved, so this line won't compile: {:?}", apple);
    // TODO: 上の行をコメントアウト解除してコンパイラエラーを確認してください
 }
```

## `or_else()` はチェーン可能で、遅延評価し、空の値をそのままに保つ

別の方法は、`or_else` を使用することです。これもチェーン可能で、遅延評価されます。以下の例に示すように：

```rust
#[derive(Debug)]
enum Fruit { Apple, Orange, Banana, Kiwi, Lemon }

fn main() {
    let apple = Some(Fruit::Apple);
    let no_fruit: Option<Fruit> = None;
    let get_kiwi_as_fallback = || {
        println!("Providing kiwi as fallback");
        Some(Fruit::Kiwi)
    };
    let get_lemon_as_fallback = || {
        println!("Providing lemon as fallback");
        Some(Fruit::Lemon)
    };

    let first_available_fruit = no_fruit
     .or_else(get_kiwi_as_fallback)
     .or_else(get_lemon_as_fallback);
    println!("first_available_fruit: {:?}", first_available_fruit);
    // Providing kiwi as fallback
    // first_available_fruit: Some(Kiwi)
}
```

## `get_or_insert()` は即時評価し、空の値を置き換える

`Option` に値が含まれていることを確認するには、`get_or_insert` を使用して、デフォルト値で置き換えることができます。以下の例に示すように、`get_or_insert` は引数を即時評価するため、`apple` 変数が移動されます。

```rust
#[derive(Debug)]
enum Fruit { Apple, Orange, Banana, Kiwi, Lemon }

fn main() {
    let mut my_fruit: Option<Fruit> = None;
    let apple = Fruit::Apple;
    let first_available_fruit = my_fruit.get_or_insert(apple);
    println!("first_available_fruit is: {:?}", first_available_fruit);
    println!("my_fruit is: {:?}", my_fruit);
    // first_available_fruit is: Apple
    // my_fruit is: Some(Apple)
    //println!("Variable named `apple` is moved: {:?}", apple);
    // TODO: 上の行をコメントアウト解除してコンパイラエラーを確認してください
}
```

## `get_or_insert_with()` は遅延評価し、空の値を置き換える

明示的なデフォルト値を指定する代わりに、クロージャを `get_or_insert_with` に渡すことができます。以下のように：

```rust
#[derive(Debug)]
enum Fruit { Apple, Orange, Banana, Kiwi, Lemon }

fn main() {
    let mut my_fruit: Option<Fruit> = None;
    let get_lemon_as_fallback = || {
        println!("Providing lemon as fallback");
        Fruit::Lemon
    };
    let first_available_fruit = my_fruit
     .get_or_insert_with(get_lemon_as_fallback);
    println!("first_available_fruit is: {:?}", first_available_fruit);
    println!("my_fruit is: {:?}", my_fruit);
    // Providing lemon as fallback
    // first_available_fruit is: Lemon
    // my_fruit is: Some(Lemon)

    // Option に値がある場合、それは変更されず、クロージャは呼び出されません
    let mut my_apple = Some(Fruit::Apple);
    let should_be_apple = my_apple.get_or_insert_with(get_lemon_as_fallback);
    println!("should_be_apple is: {:?}", should_be_apple);
    println!("my_apple is unchanged: {:?}", my_apple);
    // 出力は以下の通りです。クロージャ `get_lemon_as_fallback` は呼び出されません
    // should_be_apple is: Apple
    // my_apple is unchanged: Some(Apple)
}
```

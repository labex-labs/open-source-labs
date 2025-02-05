# 解包选项与默认值

解包 `Option` 并在其值为 `None` 时使用默认值的方法不止一种。为了选择符合我们需求的方法，我们需要考虑以下几点：

- 我们需要急切求值还是惰性求值？
- 我们需要保持原始的空值不变，还是就地修改它？

## `or()` 可链式调用，急切求值，保持空值不变

`or()` 可链式调用，并且会急切地计算其参数，如下例所示。请注意，由于 `or` 的参数是急切求值的，传递给 `or` 的变量会被移动。

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

    // `or` 会移动其参数。
    // 在上面的例子中，`or(orange)` 返回了一个 `Some`，所以 `or(apple)` 没有被调用。
    // 但是名为 `apple` 的变量无论如何都已经被移动了，不能再使用了。
    // println!("Variable apple was moved, so this line won't compile: {:?}", apple);
    // TODO: 取消注释上面的行以查看编译器错误
 }
```

## `or_else()` 可链式调用，惰性求值，保持空值不变

另一种选择是使用 `or_else`，它同样可链式调用，并且是惰性求值的，如下例所示：

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

## `get_or_insert()` 急切求值，就地修改空值

为确保 `Option` 包含一个值，我们可以使用 `get_or_insert` 就地用一个回退值修改它，如下例所示。请注意，`get_or_insert` 会急切地计算其参数，所以变量 `apple` 会被移动：

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
    // TODO: 取消注释上面的行以查看编译器错误
}
```

## `get_or_insert_with()` 惰性求值，就地修改空值

我们可以向 `get_or_insert_with` 传递一个闭包，而不是显式地提供一个回退值，如下所示：

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

    // 如果 `Option` 有值，它将保持不变，闭包不会被调用
    let mut my_apple = Some(Fruit::Apple);
    let should_be_apple = my_apple.get_or_insert_with(get_lemon_as_fallback);
    println!("should_be_apple is: {:?}", should_be_apple);
    println!("my_apple is unchanged: {:?}", my_apple);
    // 输出如下。请注意，闭包 `get_lemon_as_fallback` 没有被调用
    // should_be_apple is: Apple
    // my_apple is unchanged: Some(Apple)
}
```

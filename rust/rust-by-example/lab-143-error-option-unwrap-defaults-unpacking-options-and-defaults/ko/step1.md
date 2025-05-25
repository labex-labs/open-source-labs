# Option 언팩 (unpack) 및 기본값

`Option`을 언팩하고 `None`인 경우 기본값으로 대체하는 방법은 여러 가지가 있습니다. 필요에 맞는 방법을 선택하려면 다음 사항을 고려해야 합니다.

- 즉시 평가 (eager evaluation) 또는 지연 평가 (lazy evaluation) 가 필요한가?
- 원래의 빈 값을 그대로 유지해야 하는가, 아니면 제자리에서 수정해야 하는가?

## `or()`은 체이닝 (chainable) 가능하며, 즉시 평가하고, 빈 값을 그대로 유지합니다.

`or()`은 체이닝이 가능하며 인수를 즉시 평가합니다. 다음 예제에서 볼 수 있습니다. `or`의 인수는 즉시 평가되므로 `or`에 전달된 변수는 이동 (moved) 됩니다.

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

    // `or` 은 인수를 이동시킵니다.
    // 위의 예제에서 `or(orange)` 는 `Some` 을 반환했으므로 `or(apple)` 은 호출되지 않았습니다.
    // 하지만 `apple` 이라는 변수는 이미 이동되었으므로 더 이상 사용할 수 없습니다.
    // println!("Variable apple was moved, so this line won't compile: {:?}", apple);
    // TODO: uncomment the line above to see the compiler error
 }
```

## `or_else()`는 체이닝 가능하며, 지연 평가하고, 빈 값을 그대로 유지합니다.

또 다른 대안은 `or_else`를 사용하는 것입니다. `or_else` 역시 체이닝이 가능하며 지연 평가합니다. 다음 예제에서 볼 수 있습니다.

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

## `get_or_insert()`는 즉시 평가하고, 빈 값을 제자리에서 수정합니다.

`Option`에 값이 포함되어 있는지 확인하기 위해 `get_or_insert`를 사용하여 대체 값으로 제자리에서 수정할 수 있습니다. 다음 예제에서 볼 수 있습니다. `get_or_insert`는 매개변수를 즉시 평가하므로 변수 `apple`이 이동됩니다.

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
    // TODO: uncomment the line above to see the compiler error
}
```

## `get_or_insert_with()`는 지연 평가하고, 빈 값을 제자리에서 수정합니다.

대체할 값을 명시적으로 제공하는 대신, 다음과 같이 클로저 (closure) 를 `get_or_insert_with`에 전달할 수 있습니다.

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

    // Option 에 값이 있는 경우 변경되지 않고 클로저는 호출되지 않습니다.
    let mut my_apple = Some(Fruit::Apple);
    let should_be_apple = my_apple.get_or_insert_with(get_lemon_as_fallback);
    println!("should_be_apple is: {:?}", should_be_apple);
    println!("my_apple is unchanged: {:?}", my_apple);
    // The output is a follows. Note that the closure `get_lemon_as_fallback` is not invoked
    // should_be_apple is: Apple
    // my_apple is unchanged: Some(Apple)
}
```

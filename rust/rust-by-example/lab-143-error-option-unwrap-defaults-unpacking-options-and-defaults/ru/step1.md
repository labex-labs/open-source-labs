# Распаковка вариантов и значений по умолчанию

Есть несколько способов распаковать `Option` и вернуться к значению по умолчанию, если оно равно `None`. Чтобы выбрать подходящий для наших нужд, нужно рассмотреть следующие аспекты:

- нужна eager или lazy evaluation?
- нужно ли оставить исходное пустое значение неизменным или изменить его на месте?

## `or()` можно цеплять, eager evaluation, пустое значение остается неизменным

`or()` можно цеплять и eager evaluation аргумента, как показано в следующем примере. Обратите внимание, что поскольку аргументы `or` eager evaluation, переменная, переданная в `or`, перемещается.

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

    // `or` перемещает свой аргумент.
    // В примере выше `or(orange)` вернул `Some`, поэтому `or(apple)` не вызывался.
    // Но переменная с именем `apple` все равно переместилась и больше не может быть использована.
    // println!("Variable apple was moved, so this line won't compile: {:?}", apple);
    // TODO: раскомментируйте строку выше, чтобы увидеть ошибку компиляции
 }
```

## `or_else()` можно цеплять, lazy evaluation, пустое значение остается неизменным

Другой вариант — использовать `or_else`, который также можно цеплять и lazy evaluation, как показано в следующем примере:

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

## `get_or_insert()` eager evaluation, изменяет пустое значение на месте

Чтобы убедиться, что `Option` содержит значение, можно использовать `get_or_insert`, чтобы изменить его на месте с помощью значения по умолчанию, как показано в следующем примере. Обратите внимание, что `get_or_insert` eager evaluation своего параметра, поэтому переменная `apple` перемещается:

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
    // TODO: раскомментируйте строку выше, чтобы увидеть ошибку компиляции
}
```

## `get_or_insert_with()` lazy evaluation, изменяет пустое значение на месте

Вместо явного указания значения по умолчанию можно передать замыкание в `get_or_insert_with`, как показано ниже:

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

    // Если Option имеет значение, оно остается неизменным, и замыкание не вызывается
    let mut my_apple = Some(Fruit::Apple);
    let should_be_apple = my_apple.get_or_insert_with(get_lemon_as_fallback);
    println!("should_be_apple is: {:?}", should_be_apple);
    println!("my_apple is unchanged: {:?}", my_apple);
    // Вывод будет следующим. Обратите внимание, что замыкание `get_lemon_as_fallback` не вызывается
    // should_be_apple is: Apple
    // my_apple is unchanged: Some(Apple)
}
```

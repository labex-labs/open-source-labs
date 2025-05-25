# Desempacotando opções e valores padrão

Há mais de uma maneira de desembalar um `Option` e recorrer a um valor padrão se for `None`. Para escolher a que melhor atende às nossas necessidades, precisamos considerar o seguinte:

- precisamos de avaliação ansiosa (eager evaluation) ou preguiçosa (lazy evaluation)?
- precisamos manter o valor vazio original intacto ou modificá-lo no local?

## `or()` é encadeável, avalia ansiosamente, mantém o valor vazio intacto

`or()` é encadeável e avalia ansiosamente seu argumento, como é mostrado no exemplo a seguir. Observe que, como os argumentos de `or` são avaliados ansiosamente, a variável passada para `or` é movida.

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

    // `or` moves its argument.
    // In the example above, `or(orange)` returned a `Some`, so `or(apple)` was not invoked.
    // But the variable named `apple` has been moved regardless, and cannot be used anymore.
    // println!("Variable apple was moved, so this line won't compile: {:?}", apple);
    // TODO: uncomment the line above to see the compiler error
 }
```

## `or_else()` é encadeável, avalia preguiçosamente, mantém o valor vazio intacto

Outra alternativa é usar `or_else`, que também é encadeável e avalia preguiçosamente, como é mostrado no exemplo a seguir:

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

## `get_or_insert()` avalia ansiosamente, modifica o valor vazio no local

Para garantir que um `Option` contenha um valor, podemos usar `get_or_insert` para modificá-lo no local com um valor de fallback, como é mostrado no exemplo a seguir. Observe que `get_or_insert` avalia ansiosamente seu parâmetro, então a variável `apple` é movida:

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

## `get_or_insert_with()` avalia preguiçosamente, modifica o valor vazio no local

Em vez de fornecer explicitamente um valor para recorrer, podemos passar um closure para `get_or_insert_with`, da seguinte forma:

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

    // If the Option has a value, it is left unchanged, and the closure is not invoked
    let mut my_apple = Some(Fruit::Apple);
    let should_be_apple = my_apple.get_or_insert_with(get_lemon_as_fallback);
    println!("should_be_apple is: {:?}", should_be_apple);
    println!("my_apple is unchanged: {:?}", my_apple);
    // The output is a follows. Note that the closure `get_lemon_as_fallback` is not invoked
    // should_be_apple is: Apple
    // my_apple is unchanged: Some(Apple)
}
```

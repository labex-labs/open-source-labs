# Entpacken von Optionen und Standardwerten

Es gibt mehrere Möglichkeiten, eine `Option` zu entpacken und auf einen Standardwert zurückzugreifen, wenn sie `None` ist. Um diejenige auszuwählen, die unseren Anforderungen entspricht, müssen wir die folgenden Aspekte berücksichtigen:

- Brauchen wir eager oder lazy Evaluation?
- Brauchen wir den ursprünglichen leeren Wert unberührt zu lassen oder ihn in situ zu modifizieren?

## `or()` ist kettenbar, wertet eager aus, behält leeren Wert unberührt

`or()` ist kettenbar und wertet seinen Argument eager aus, wie im folgenden Beispiel gezeigt. Beachten Sie, dass die Argumente von `or` eager ausgewertet werden, sodass die Variable, die an `or` übergeben wird, bewegt wird.

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

    // `or` bewegt sein Argument.
    // Im obigen Beispiel hat `or(orange)` ein `Some` zurückgegeben, sodass `or(apple)` nicht aufgerufen wurde.
    // Aber die Variable mit dem Namen `apple` wurde dennoch bewegt und kann nicht mehr verwendet werden.
    // println!("Variable apple was moved, so this line won't compile: {:?}", apple);
    // TODO: Entkommentieren Sie die obige Zeile, um den Compilerfehler zu sehen
 }
```

## `or_else()` ist kettenbar, wertet lazy aus, behält leeren Wert unberührt

Eine weitere Möglichkeit ist die Verwendung von `or_else`, die ebenfalls kettenbar ist und lazy ausgewertet wird, wie im folgenden Beispiel gezeigt:

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

## `get_or_insert()` wertet eager aus, modifiziert leeren Wert in situ

Um sicherzustellen, dass eine `Option` einen Wert enthält, können wir `get_or_insert` verwenden, um sie in situ mit einem Fallback-Wert zu modifizieren, wie im folgenden Beispiel gezeigt. Beachten Sie, dass `get_or_insert` seinen Parameter eager auswertet, sodass die Variable `apple` bewegt wird:

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
    // TODO: Entkommentieren Sie die obige Zeile, um den Compilerfehler zu sehen
}
```

## `get_or_insert_with()` wertet lazy aus, modifiziert leeren Wert in situ

Anstatt explizit einen Wert zum Fallback bereitzustellen, können wir eine Closure an `get_or_insert_with` übergeben, wie folgt:

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

    // Wenn die Option einen Wert hat, bleibt er unverändert und die Closure wird nicht aufgerufen
    let mut my_apple = Some(Fruit::Apple);
    let should_be_apple = my_apple.get_or_insert_with(get_lemon_as_fallback);
    println!("should_be_apple is: {:?}", should_be_apple);
    println!("my_apple is unchanged: {:?}", my_apple);
    // Die Ausgabe lautet wie folgt. Beachten Sie, dass die Closure `get_lemon_as_fallback` nicht aufgerufen wird
    // should_be_apple is: Apple
    // my_apple is unchanged: Some(Apple)
}
```

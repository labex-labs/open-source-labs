# Desempaquetar opciones y valores predeterminados

Hay más de una manera de desempaquetar una `Option` y recurrir a un valor predeterminado si es `None`. Para elegir la que se ajuste a nuestras necesidades, debemos considerar lo siguiente:

- ¿necesitamos evaluación ágil o perezosa?
- ¿necesitamos mantener intacto el valor original vacío o modificarlo en su lugar?

## `or()` es encadenable, evalúa de manera ágil, mantiene el valor vacío intacto

`or()` es encadenable y evalúa su argumento de manera ágil, como se muestra en el siguiente ejemplo. Tenga en cuenta que debido a que los argumentos de `or` se evalúan de manera ágil, la variable pasada a `or` se mueve.

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

    // `or` mueve su argumento.
    // En el ejemplo anterior, `or(orange)` devolvió un `Some`, por lo que `or(apple)` no se invocó.
    // Pero la variable llamada `apple` se ha movido de todos modos y ya no se puede usar.
    // println!("Variable apple was moved, so this line won't compile: {:?}", apple);
    // TODO: descomente la línea anterior para ver el error del compilador
 }
```

## `or_else()` es encadenable, evalúa de manera perezosa, mantiene el valor vacío intacto

Otra alternativa es usar `or_else`, que también es encadenable y evalúa de manera perezosa, como se muestra en el siguiente ejemplo:

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

## `get_or_insert()` evalúa de manera ágil, modifica el valor vacío en su lugar

Para asegurarnos de que una `Option` contenga un valor, podemos usar `get_or_insert` para modificarla en su lugar con un valor de retorno, como se muestra en el siguiente ejemplo. Tenga en cuenta que `get_or_insert` evalúa su parámetro de manera ágil, por lo que la variable `apple` se mueve:

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
    // TODO: descomente la línea anterior para ver el error del compilador
}
```

## `get_or_insert_with()` evalúa de manera perezosa, modifica el valor vacío en su lugar

En lugar de proporcionar explícitamente un valor de retorno, podemos pasar una clausura a `get_or_insert_with`, como sigue:

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

    // Si la Option tiene un valor, se deja inalterado y la clausura no se invoca
    let mut my_apple = Some(Fruit::Apple);
    let should_be_apple = my_apple.get_or_insert_with(get_lemon_as_fallback);
    println!("should_be_apple is: {:?}", should_be_apple);
    println!("my_apple is unchanged: {:?}", my_apple);
    // La salida es la siguiente. Tenga en cuenta que la clausura `get_lemon_as_fallback` no se invoca
    // should_be_apple is: Apple
    // my_apple is unchanged: Some(Apple)
}
```

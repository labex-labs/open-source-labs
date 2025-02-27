# Iterando sobre `Result`

Una operación `Iter::map` puede fallar, por ejemplo:

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Vec<_> = strings
     .into_iter()
     .map(|s| s.parse::<i32>())
     .collect();
    println!("Results: {:?}", numbers);
}
```

Veamos las estrategias para manejar esto.

## Ignorar los elementos que fallan con `filter_map()`

`filter_map` llama a una función y filtra los resultados que son `None`.

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Vec<_> = strings
     .into_iter()
     .filter_map(|s| s.parse::<i32>().ok())
     .collect();
    println!("Results: {:?}", numbers);
}
```

## Recopilar los elementos que fallan con `map_err()` y `filter_map()`

`map_err` llama a una función con el error, por lo que al agregarlo a la solución `filter_map` anterior podemos guardarlos por otro lado mientras iteramos.

```rust
fn main() {
    let strings = vec!["42", "tofu", "93", "999", "18"];
    let mut errors = vec![];
    let numbers: Vec<_> = strings
     .into_iter()
     .map(|s| s.parse::<u8>())
     .filter_map(|r| r.map_err(|e| errors.push(e)).ok())
     .collect();
    println!("Numbers: {:?}", numbers);
    println!("Errors: {:?}", errors);
}
```

## Hacer que toda la operación falle con `collect()`

`Result` implementa `FromIterator` para que un vector de resultados (`Vec<Result<T, E>>`) se pueda convertir en un resultado con un vector (`Result<Vec<T>, E>`). Una vez que se encuentra un `Result::Err`, la iteración se detendrá.

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let numbers: Result<Vec<_>, _> = strings
     .into_iter()
     .map(|s| s.parse::<i32>())
     .collect();
    println!("Results: {:?}", numbers);
}
```

Esta misma técnica se puede usar con `Option`.

## Recopilar todos los valores válidos y fallos con `partition()`

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let (numbers, errors): (Vec<_>, Vec<_>) = strings
     .into_iter()
     .map(|s| s.parse::<i32>())
     .partition(Result::is_ok);
    println!("Numbers: {:?}", numbers);
    println!("Errors: {:?}", errors);
}
```

Cuando mires los resultados, notarás que todo sigue envuelto en `Result`. Se necesita un poco más de código boilerplate para esto.

```rust
fn main() {
    let strings = vec!["tofu", "93", "18"];
    let (numbers, errors): (Vec<_>, Vec<_>) = strings
     .into_iter()
     .map(|s| s.parse::<i32>())
     .partition(Result::is_ok);
    let numbers: Vec<_> = numbers.into_iter().map(Result::unwrap).collect();
    let errors: Vec<_> = errors.into_iter().map(Result::unwrap_err).collect();
    println!("Numbers: {:?}", numbers);
    println!("Errors: {:?}", errors);
}
```

# Varios tipos de error

Los ejemplos anteriores siempre han sido muy convenientes; los `Result` interactúan con otros `Result` y las `Option` interactúan con otras `Option`.

A veces una `Option` necesita interactuar con un `Result`, o un `Result<T, Error1>` necesita interactuar con un `Result<T, Error2>`. En esos casos, queremos manejar nuestros diferentes tipos de error de manera que sean composables y fáciles de interactuar.

En el siguiente código, dos instancias de `unwrap` generan diferentes tipos de error. `Vec::first` devuelve una `Option`, mientras que `parse::<i32>` devuelve un `Result<i32, ParseIntError>`:

```rust
fn double_first(vec: Vec<&str>) -> i32 {
    let first = vec.first().unwrap(); // Generar error 1
    2 * first.parse::<i32>().unwrap() // Generar error 2
}

fn main() {
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    println!("El primer número duplicado es {}", double_first(numbers));

    println!("El primer número duplicado es {}", double_first(empty));
    // Error 1: el vector de entrada está vacío

    println!("El primer número duplicado es {}", double_first(strings));
    // Error 2: el elemento no se puede analizar como un número
}
```

En las siguientes secciones, veremos varias estrategias para manejar este tipo de problemas.

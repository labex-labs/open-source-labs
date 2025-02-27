# `Result`

`Result` es una versión más compleja del tipo `Option` que describe posibles _errores_ en lugar de posibles _ausencias_.

Es decir, `Result<T, E>` puede tener uno de dos resultados:

- `Ok(T)`: Se encontró un elemento `T`
- `Err(E)`: Se encontró un error con el elemento `E`

Por convención, el resultado esperado es `Ok` mientras que el resultado inesperado es `Err`.

Como `Option`, `Result` tiene muchos métodos asociados. `unwrap()`, por ejemplo, produce el elemento `T` o causa un `panic`. Para el manejo de casos, hay muchos combinadores entre `Result` y `Option` que se superponen.

Al trabajar con Rust, es probable que encuentres métodos que devuelven el tipo `Result`, como el método `parse()`. No siempre es posible analizar una cadena en el otro tipo, por lo que `parse()` devuelve un `Result` que indica un posible error.

Veamos qué pasa cuando analizamos correctamente e incorrectamente una cadena con `parse()`:

```rust
fn multiply(first_number_str: &str, second_number_str: &str) -> i32 {
    // Intentemos usar `unwrap()` para extraer el número. ¿Nos causará problemas?
    let first_number = first_number_str.parse::<i32>().unwrap();
    let second_number = second_number_str.parse::<i32>().unwrap();
    first_number * second_number
}

fn main() {
    let twenty = multiply("10", "2");
    println!("double is {}", twenty);

    let tt = multiply("t", "2");
    println!("double is {}", tt);
}
```

En el caso en que no se tenga éxito, `parse()` nos deja con un error para que `unwrap()` lance un `panic`. Además, el `panic` sale de nuestro programa y proporciona un mensaje de error desagradable.

Para mejorar la calidad de nuestro mensaje de error, deberíamos ser más específicos sobre el tipo de retorno y considerar manejar explícitamente el error.

## Usando `Result` en `main`

El tipo `Result` también puede ser el tipo de retorno de la función `main` si se especifica explícitamente. Normalmente, la función `main` tendrá la forma:

```rust
fn main() {
    println!("Hello World!");
}
```

Sin embargo, `main` también puede tener un tipo de retorno de `Result`. Si se produce un error dentro de la función `main`, devolverá un código de error e imprimirá una representación de depuración del error (usando el trato \[`Debug`\]). El siguiente ejemplo muestra un escenario de este tipo y toca aspectos cubiertos en \[la siguiente sección\].

```rust
use std::num::ParseIntError;

fn main() -> Result<(), ParseIntError> {
    let number_str = "10";
    let number = match number_str.parse::<i32>() {
        Ok(number)  => number,
        Err(e) => return Err(e),
    };
    println!("{}", number);
    Ok(())
}
```

# Anotación explícita

El verificador de préstamos utiliza anotaciones de tiempo de vida explícitas para determinar durante cuánto tiempo las referencias deben ser válidas. En casos en los que los tiempos de vida no se omiten, Rust requiere anotaciones explícitas para determinar cuál debe ser el tiempo de vida de una referencia. La sintaxis para anotar explícitamente un tiempo de vida utiliza el carácter apóstrofe de la siguiente manera:

```rust
foo<'a>
// `foo` tiene un parámetro de tiempo de vida `'a`
```

Similar a las clausuras, utilizar tiempos de vida requiere genéricos. Además, esta sintaxis de tiempo de vida indica que el tiempo de vida de `foo` no puede exceder el de `'a`. La anotación explícita de un tipo tiene la forma `&'a T` donde `'a` ya ha sido introducido.

En casos con múltiples tiempos de vida, la sintaxis es similar:

```rust
foo<'a, 'b>
// `foo` tiene parámetros de tiempo de vida `'a` y `'b`
```

En este caso, el tiempo de vida de `foo` no puede exceder el de `'a` _o_ `'b`.

Vea el siguiente ejemplo para ver la anotación de tiempo de vida explícita en uso:

```rust
// `print_refs` toma dos referencias a `i32` que tienen diferentes
// tiempos de vida `'a` y `'b`. Ambos tiempos de vida deben ser al
// menos tan largos como la función `print_refs`.
fn print_refs<'a, 'b>(x: &'a i32, y: &'b i32) {
    println!("x is {} and y is {}", x, y);
}

// Una función que no toma argumentos, pero tiene un parámetro de tiempo de vida `'a`.
fn failed_borrow<'a>() {
    let _x = 12;

    // ERROR: `_x` no tiene un tiempo de vida lo suficientemente largo
    let y: &'a i32 = &_x;
    // Intentar utilizar el tiempo de vida `'a` como una anotación de tipo explícita
    // dentro de la función fallará porque el tiempo de vida de `&_x` es más corto
    // que el de `y`. Un tiempo de vida corto no se puede forzar a ser más largo.
}

fn main() {
    // Crea variables para prestar más adelante.
    let (four, nine) = (4, 9);

    // Las prestas (`&`) de ambas variables se pasan a la función.
    print_refs(&four, &nine);
    // Cualquier entrada que sea prestada debe tener un tiempo de vida mayor que el del prestamista.
    // En otras palabras, el tiempo de vida de `four` y `nine` debe
    // ser más largo que el de `print_refs`.

    failed_borrow();
    // `failed_borrow` no contiene referencias para forzar `'a` a ser
    // más largo que el tiempo de vida de la función, pero `'a` es más largo.
    // Debido a que el tiempo de vida nunca está restringido, por defecto es `'static`.
}
```

# Lifetimes genéricos en funciones

Escribiremos una función que devuelva la cadena más larga de dos trozos de cadena. Esta función tomará dos trozos de cadena y devolverá un solo trozo de cadena. Después de implementar la función `longest`, el código de la Lista 10-19 debería imprimir `The longest string is abcd`.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let string1 = String::from("abcd");
    let string2 = "xyz";

    let result = longest(string1.as_str(), string2);
    println!("The longest string is {result}");
}
```

Lista 10-19: Una función `main` que llama a la función `longest` para encontrar la cadena más larga de dos trozos de cadena

Tenga en cuenta que queremos que la función tome trozos de cadena, que son referencias, en lugar de cadenas, porque no queremos que la función `longest` tome posesión de sus parámetros. Consulte "Trozos de cadena como parámetros" para más discusión sobre por qué los parámetros que usamos en la Lista 10-19 son los que queremos.

Si intentamos implementar la función `longest` como se muestra en la Lista 10-20, no se compilará.

Nombre de archivo: `src/main.rs`

```rust
fn longest(x: &str, y: &str) -> &str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

Lista 10-20: Una implementación de la función `longest` que devuelve la cadena más larga de dos trozos de cadena pero aún no se compila

En cambio, obtenemos el siguiente error que habla sobre lifetimes:

```bash
error[E0106]: missing lifetime specifier
 --> src/main.rs:9:33
  |
9 | fn longest(x: &str, y: &str) -> &str {
  |               ----     ----     ^ expected named lifetime parameter
  |
  = help: this function's return type contains a borrowed value,
but the signature does not say whether it is borrowed from `x` or `y`
help: consider introducing a named lifetime parameter
  |
9 | fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
  |           ++++     ++          ++          ++
```

El texto de ayuda revela que el tipo de retorno necesita un parámetro de lifetime genérico porque Rust no puede decir si la referencia que se devuelve se refiere a `x` o `y`. En realidad, nosotros tampoco sabemos, porque el bloque `if` en el cuerpo de esta función devuelve una referencia a `x` y el bloque `else` devuelve una referencia a `y` ¡

Cuando definimos esta función, no conocemos los valores concretos que se pasarán a esta función, por lo que no sabemos si el caso `if` o el caso `else` se ejecutará. Tampoco conocemos los lifetimes concretos de las referencias que se pasarán, por lo que no podemos mirar los ámbitos como lo hicimos en las Listas 10-17 y 10-18 para determinar si la referencia que devolvemos siempre será válida. El verificador de préstamos tampoco puede determinar esto, porque no sabe cómo los lifetimes de `x` e `y` se relacionan con el lifetime del valor de retorno. Para corregir este error, agregaremos parámetros de lifetime genéricos que definen la relación entre las referencias para que el verificador de préstamos pueda realizar su análisis.

# Concatenación con el operador + o la macro format!

A menudo, querrás combinar dos cadenas existentes. Una forma de hacerlo es usar el operador `+`, como se muestra en la Lista 8-18.

```rust
let s1 = String::from("Hello, ");
let s2 = String::from("world!");
let s3 = s1 + &s2; // nota que s1 se ha movido aquí y ya no se puede usar
```

Lista 8-18: Usando el operador `+` para combinar dos valores de `String` en un nuevo valor de `String`

La cadena `s3` contendrá `Hello, world!`. La razón por la cual `s1` ya no es válida después de la adición, y la razón por la cual usamos una referencia a `s2`, tiene que ver con la firma del método que se llama cuando usamos el operador `+`. El operador `+` usa el método `add`, cuya firma se ve así:

```rust
fn add(self, s: &str) -> String {
```

En la biblioteca estándar, verás que `add` está definido usando genéricos y tipos asociados. Aquí, hemos sustituido tipos concretos, que es lo que sucede cuando llamamos a este método con valores de `String`. Discutiremos genéricos en el Capítulo 10. Esta firma nos da las pistas que necesitamos para entender los aspectos complicados del operador `+`.

En primer lugar, `s2` tiene un `&`, lo que significa que estamos agregando una _referencia_ de la segunda cadena a la primera cadena. Esto se debe al parámetro `s` en la función `add`: solo podemos agregar un `&str` a una `String`; no podemos agregar dos valores de `String` juntos. Pero espera, el tipo de `&s2` es `&String`, no `&str`, como se especifica en el segundo parámetro de `add`. Entonces, ¿por qué la Lista 8-18 se compila?

La razón por la cual podemos usar `&s2` en la llamada a `add` es que el compilador puede _coaccionar_ el argumento `&String` en un `&str`. Cuando llamamos al método `add`, Rust usa una _coacción de dereferencia_, que aquí convierte `&s2` en `&s2[..]`. Discutiremos la coacción de dereferencia con más detalle en el Capítulo 15. Debido a que `add` no toma posesión del parámetro `s`, `s2` todavía será una `String` válida después de esta operación.

En segundo lugar, podemos ver en la firma que `add` toma posesión de `self` porque `self` no tiene un `&`. Esto significa que `s1` en la Lista 8-18 se moverá a la llamada a `add` y ya no será válida después de eso. Entonces, aunque `let s3 = s1 + &s2;` parece que copiará ambas cadenas y creará una nueva, esta declaración en realidad toma posesión de `s1`, anexa una copia del contenido de `s2` y luego devuelve la posesión del resultado. En otras palabras, parece que está haciendo muchas copias, pero no lo está; la implementación es más eficiente que la copia.

Si necesitamos concatenar múltiples cadenas, el comportamiento del operador `+` se vuelve complicado:

```rust
let s1 = String::from("tic");
let s2 = String::from("tac");
let s3 = String::from("toe");

let s = s1 + "-" + &s2 + "-" + &s3;
```

En este punto, `s` será `tic-tac-toe`. Con todos los caracteres `+` y `"`, es difícil ver lo que está sucediendo. Para combinar cadenas de maneras más complicadas, en cambio, podemos usar la macro `format!`:

```rust
let s1 = String::from("tic");
let s2 = String::from("tac");
let s3 = String::from("toe");

let s = format!("{s1}-{s2}-{s3}");
```

Este código también establece `s` en `tic-tac-toe`. La macro `format!` funciona como `println!`, pero en lugar de imprimir la salida en la pantalla, devuelve una `String` con el contenido. La versión del código que usa `format!` es mucho más fácil de leer, y el código generado por la macro `format!` usa referencias para que esta llamada no tome posesión de ninguno de sus parámetros.

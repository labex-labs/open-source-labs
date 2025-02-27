# Rebanadas de Cadena

Una _rebanada de cadena_ es una referencia a una parte de un `String`, y se ve así:

```rust
let s = String::from("hello world");

let hello = &s[0..5];
let world = &s[6..11];
```

En lugar de una referencia a todo el `String`, `hello` es una referencia a una parte del `String`, especificada en la parte adicional `[0..5]`. Creamos rebanadas usando un rango dentro de corchetes especificando `[índice_de_inicio..índice_de_fin]`, donde `índice_de_inicio` es la primera posición en la rebanada y `índice_de_fin` es uno más que la última posición en la rebanada. Internamente, la estructura de datos de la rebanada almacena la posición de inicio y la longitud de la rebanada, que corresponde a `índice_de_fin` menos `índice_de_inicio`. Entonces, en el caso de `let world = &s[6..11];`, `world` sería una rebanada que contiene un puntero al byte en el índice 6 de `s` con un valor de longitud de `5`.

La Figura 4-6 muestra esto en un diagrama.

Figura 4-6: Rebanada de cadena que se refiere a una parte de un `String`

Con la sintaxis de rango `..` de Rust, si quieres comenzar en el índice 0, puedes omitir el valor antes de los dos puntos. En otras palabras, estos son equivalentes:

```rust
let s = String::from("hello");

let slice = &s[0..2];
let slice = &s[..2];
```

Por el mismo motivo, si tu rebanada incluye el último byte del `String`, puedes omitir el número final. Eso significa que estos son equivalentes:

```rust
let s = String::from("hello");

let len = s.len();

let slice = &s[3..len];
let slice = &s[3..];
```

También puedes omitir ambos valores para tomar una rebanada de toda la cadena. Entonces estos son equivalentes:

```rust
let s = String::from("hello");

let len = s.len();

let slice = &s[0..len];
let slice = &s[..];
```

> Nota: Los índices de rango de rebanadas de cadena deben ocurrir en los límites válidos de caracteres UTF-8. Si intentas crear una rebanada de cadena en medio de un carácter de varios bytes, tu programa saldrá con un error. Con el propósito de introducir las rebanadas de cadena, estamos asumiendo solo ASCII en esta sección; una discusión más detallada del manejo de UTF-8 se encuentra en "Almacenar texto codificado en UTF-8 con cadenas".

Con toda esta información en mente, vamos a reescribir `first_word` para devolver una rebanada. El tipo que significa "rebanada de cadena" se escribe como `&str`:

Nombre del archivo: `src/main.rs`

```rust
fn first_word(s: &String) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
}
```

Obtenemos el índice para el final de la palabra de la misma manera que lo hicimos en la Lista 4-7, buscando la primera aparición de un espacio. Cuando encontramos un espacio, devolvemos una rebanada de cadena usando el inicio de la cadena y el índice del espacio como los índices de inicio y fin.

Ahora cuando llamamos a `first_word`, obtenemos un solo valor que está vinculado a los datos subyacentes. El valor está compuesto por una referencia al punto de inicio de la rebanada y el número de elementos en la rebanada.

Devolver una rebanada también funcionaría para una función `second_word`:

```rust
fn second_word(s: &String) -> &str {
```

Ahora tenemos una API directa que es mucho más difícil de desordenar porque el compilador asegurará que las referencias al `String` permanezcan válidas. Recuerda el error en el programa de la Lista 4-8, cuando obtuvimos el índice al final de la primera palabra pero luego limpiamos la cadena y nuestro índice quedó invalido? Ese código era lógicamente incorrecto pero no mostraba errores inmediatos. Los problemas aparecerían más tarde si seguíamos intentando usar el índice de la primera palabra con una cadena vaciada. Las rebanadas hacen imposible este error y nos permiten saber que tenemos un problema con nuestro código mucho antes. Usar la versión de rebanada de `first_word` generará un error de compilación:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    let mut s = String::from("hello world");

    let word = first_word(&s);

    s.clear(); // error!

    println!("the first word is: {word}");
}
```

Aquí está el error del compilador:

```bash
error[E0502]: cannot borrow `s` as mutable because it is also borrowed as
immutable
  --> src/main.rs:18:5
   |
16 |     let word = first_word(&s);
   |                           -- immutable borrow occurs here
17 |
18 |     s.clear(); // error!
   |     ^^^^^^^^^ mutable borrow occurs here
19 |
20 |     println!("the first word is: {word}");
   |                                   ---- immutable borrow later used here
```

Recuerda las reglas de préstamo de que si tenemos una referencia inmutable a algo, no podemos también tomar una referencia mutable. Debido a que `clear` necesita truncar el `String`, necesita obtener una referencia mutable. La llamada a `println!` después de la llamada a `clear` usa la referencia en `word`, por lo que la referencia inmutable debe todavía estar activa en ese momento. Rust no permite que la referencia mutable en `clear` y la referencia inmutable en `word` existan al mismo tiempo, y la compilación falla. No solo Rust ha hecho que nuestra API sea más fácil de usar, sino que también ha eliminado una clase completa de errores en tiempo de compilación.

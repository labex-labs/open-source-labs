# Estructuras Similares a la Unidad Sin Ningún Campo

También puedes definir estructuras que no tienen ningún campo. ¡Estas se llaman _estructuras similares a la unidad_ porque se comportan de manera similar a `()`, el tipo unidad que mencionamos en "El Tipo Tupla". Las estructuras similares a la unidad pueden ser útiles cuando necesitas implementar un trato en algún tipo pero no tienes ningún dato que desees almacenar en el tipo mismo. Discutiremos los tratados en el Capítulo 10. Aquí hay un ejemplo de declarar e instanciar una estructura unidad llamada `AlwaysEqual`:

Nombre del archivo: `src/main.rs`

```rust
struct AlwaysEqual;

fn main() {
    let subject = AlwaysEqual;
}
```

Para definir `AlwaysEqual`, usamos la palabra clave `struct`, el nombre que queremos y luego un punto y coma. ¡No es necesario usar llaves ni paréntesis! Luego podemos obtener una instancia de `AlwaysEqual` en la variable `subject` de manera similar: usando el nombre que definimos, sin ninguna llave ni paréntesis. Imagina que más adelante implementaremos un comportamiento para este tipo de manera que cada instancia de `AlwaysEqual` siempre sea igual a cada instancia de cualquier otro tipo, quizás para tener un resultado conocido con fines de prueba. ¡No necesitaríamos ningún dato para implementar ese comportamiento! Verás en el Capítulo 10 cómo definir tratados e implementarlos en cualquier tipo, incluyendo estructuras similares a la unidad.

> **Propiedad de los Datos de la Estructura**
>
> En la definición de la estructura `User` en la Lista 5-1, usamos el tipo `String` con propiedad en lugar del tipo de segmento de cadena `&str`. Esta es una elección deliberada porque queremos que cada instancia de esta estructura sea dueña de todos sus datos y que esos datos sean válidos durante todo el tiempo que la estructura completa sea válida.
>
> También es posible que las estructuras almacenen referencias a datos propiedad de algo más, pero para hacer eso se requiere el uso de _vidas de tiempo_, una característica de Rust que discutiremos en el Capítulo 10. Los períodos de vida aseguran que los datos referenciados por una estructura sean válidos durante todo el tiempo que la estructura lo sea. Digamos que intentas almacenar una referencia en una estructura sin especificar los períodos de vida, como lo siguiente en `src/main.rs`; esto no funcionará:
>
>     struct User {
>         active: bool,
>         username: &str,
>         email: &str,
>         sign_in_count: u64,
>     }
>
>     fn main() {
>         let user1 = User {
>             active: true,
>             username: "someusername123",
>             email: "someone@example.com",
>             sign_in_count: 1,
>         };
>     }
>
> El compilador se quejará de que necesita especificadores de períodos de vida:
>
>     $ `cargo run`
>        Compilando structs v0.1.0 (file:///projects/structs)
>     error[E0106]: missing lifetime specifier
>      --> src/main.rs:3:15
>       |
>     3 |     username: &str,
>       |               ^ expected named lifetime parameter
>       |
>     help: consider introducing a named lifetime parameter
>       |
>     1 ~ struct User<'a> {
>     2 |     active: bool,
>     3 ~     username: &'a str,
>       |
>
>     error[E0106]: missing lifetime specifier
>      --> src/main.rs:4:12
>       |
>     4 |     email: &str,
>       |            ^ expected named lifetime parameter
>       |
>     help: consider introducing a named lifetime parameter
>       |
>     1 ~ struct User<'a> {
>     2 |     active: bool,
>     3 |     username: &str,
>     4 ~     email: &'a str,
>       |
>
> En el Capítulo 10, discutiremos cómo corregir estos errores para que puedas almacenar referencias en estructuras, pero por ahora, corregiremos errores como estos usando tipos con propiedad como `String` en lugar de referencias como `&str`.

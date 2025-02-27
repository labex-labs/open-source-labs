# Acceder o modificar una variable estática mutable

En este libro, todavía no hemos hablado sobre variables globales, que Rust sí soporta pero puede ser problemático con las reglas de propiedad de Rust. Si dos hilos acceden a la misma variable global mutable, puede causar una carrera de datos.

En Rust, las variables globales se llaman _variables estáticas_. La Lista 19-9 muestra un ejemplo de declaración y uso de una variable estática con una rebanada de cadena como valor.

Nombre del archivo: `src/main.rs`

```rust
static HELLO_WORLD: &str = "Hello, world!";

fn main() {
    println!("value is: {HELLO_WORLD}");
}
```

Lista 19-9: Definir y usar una variable estática inmutable

Las variables estáticas son similares a las constantes, sobre las que hablamos en "Constantes". Las nombres de las variables estáticas por convención están en `SCREAMING_SNAKE_CASE`. Las variables estáticas solo pueden almacenar referencias con el período de vida `'static`, lo que significa que el compilador de Rust puede determinar el período de vida y no es necesario anotarlo explícitamente. Acceder a una variable estática inmutable es seguro.

Una diferencia sutil entre las constantes y las variables estáticas inmutables es que los valores en una variable estática tienen una dirección fija en la memoria. Usar el valor siempre accederá a los mismos datos. Las constantes, por otro lado, se permiten duplicar sus datos cada vez que se usan. Otra diferencia es que las variables estáticas pueden ser mutables. Acceder y modificar variables estáticas mutables es _inseguro_. La Lista 19-10 muestra cómo declarar, acceder y modificar una variable estática mutable llamada `COUNTER`.

Nombre del archivo: `src/main.rs`

```rust
static mut COUNTER: u32 = 0;

fn add_to_count(inc: u32) {
    unsafe {
        COUNTER += inc;
    }
}

fn main() {
    add_to_count(3);

    unsafe {
        println!("COUNTER: {COUNTER}");
    }
}
```

Lista 19-10: Leer o escribir en una variable estática mutable es inseguro.

Al igual que con las variables regulares, especificamos la mutabilidad usando la palabra clave `mut`. Cualquier código que lea o escriba en `COUNTER` debe estar dentro de un bloque `unsafe`. Este código se compila y muestra `COUNTER: 3` como esperamos porque es de un solo hilo. Tener múltiples hilos accediendo a `COUNTER` probablemente resultaría en carreras de datos.

Con datos mutables que son accesibles globalmente, es difícil garantizar que no haya carreras de datos, razón por la cual Rust considera que las variables estáticas mutables son inseguras. Donde sea posible, es preferible usar las técnicas de concurrencia y los punteros inteligentes seguros para hilos que discutimos en el Capítulo 16 para que el compilador verifique que el acceso a los datos desde diferentes hilos se realice de manera segura.

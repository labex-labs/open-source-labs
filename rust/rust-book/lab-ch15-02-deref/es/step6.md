# Coerciones de Deref Implícitas con Funciones y Métodos

La _coerción de Deref_ convierte una referencia a un tipo que implementa el trato `Deref` en una referencia a otro tipo. Por ejemplo, la coerción de Deref puede convertir `&String` en `&str` porque `String` implementa el trato `Deref` de manera que devuelve `&str`. La coerción de Deref es una facilidad que Rust realiza en los argumentos de funciones y métodos, y solo funciona en tipos que implementan el trato `Deref`. Ocurre automáticamente cuando pasamos una referencia al valor de un tipo particular como argumento a una función o método que no coincide con el tipo de parámetro en la definición de la función o método. Una secuencia de llamadas al método `deref` convierte el tipo que proporcionamos en el tipo que el parámetro necesita.

La coerción de Deref se agregó a Rust para que los programadores que escriben llamadas a funciones y métodos no necesiten agregar tantas referencias y desreferencias explícitas con `&` y `*`. La característica de coerción de Deref también nos permite escribir más código que puede funcionar tanto para referencias como para punteros inteligentes.

Para ver la coerción de Deref en acción, usemos el tipo `MyBox<T>` que definimos en la Lista 15-8, así como la implementación de `Deref` que agregamos en la Lista 15-10. La Lista 15-11 muestra la definición de una función que tiene un parámetro de tipo slice de cadena.

Nombre de archivo: `src/main.rs`

```rust
fn hello(name: &str) {
    println!("Hello, {name}!");
}
```

Lista 15-11: Una función `hello` que tiene el parámetro `name` de tipo `&str`

Podemos llamar a la función `hello` con un slice de cadena como argumento, como `hello("Rust");`, por ejemplo. La coerción de Deref hace posible llamar a `hello` con una referencia al valor de tipo `MyBox<String>`, como se muestra en la Lista 15-12.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let m = MyBox::new(String::from("Rust"));
    hello(&m);
}
```

Lista 15-12: Llamando a `hello` con una referencia a un valor `MyBox<String>`, lo que funciona debido a la coerción de Deref

Aquí estamos llamando a la función `hello` con el argumento `&m`, que es una referencia al valor de un `MyBox<String>`. Debido a que implementamos el trato `Deref` en `MyBox<T>` en la Lista 15-10, Rust puede convertir `&MyBox<String>` en `&String` llamando a `deref`. La biblioteca estándar proporciona una implementación de `Deref` en `String` que devuelve un slice de cadena, y esto está en la documentación de la API de `Deref`. Rust llama a `deref` nuevamente para convertir el `&String` en `&str`, lo que coincide con la definición de la función `hello`.

Si Rust no implementara la coerción de Deref, tendríamos que escribir el código de la Lista 15-13 en lugar del código de la Lista 15-12 para llamar a `hello` con un valor de tipo `&MyBox<String>`.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let m = MyBox::new(String::from("Rust"));
    hello(&(*m)[..]);
}
```

Lista 15-13: El código que tendríamos que escribir si Rust no tuviera coerción de Deref

La `(*m)` desreferencia el `MyBox<String>` en una `String`. Luego el `&` y `[..]` toman un slice de cadena de la `String` que es igual a toda la cadena para coincidir con la firma de `hello`. Este código sin coerción de Deref es más difícil de leer, escribir y entender con todos estos símbolos involucrados. La coerción de Deref permite que Rust maneje estas conversiones automáticamente para nosotros.

Cuando el trato `Deref` se define para los tipos involucrados, Rust analizará los tipos y usará `Deref::deref` tantas veces como sea necesario para obtener una referencia que coincida con el tipo del parámetro. El número de veces que se necesita insertar `Deref::deref` se resuelve en tiempo de compilación, por lo que no hay penalización en tiempo de ejecución para aprovechar la coerción de Deref.

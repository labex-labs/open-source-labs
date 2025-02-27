# Creación de sinónimos de tipo con alias de tipo

Rust permite declarar un _alias de tipo_ para dar a un tipo existente otro nombre. Para hacer esto, usamos la palabra clave `type`. Por ejemplo, podemos crear el alias `Kilómetros` para `i32` de la siguiente manera:

```rust
type Kilómetros = i32;
```

Ahora, el alias `Kilómetros` es un _sinónimo_ de `i32`; a diferencia de los tipos `Millímetros` y `Metros` que creamos en la Lista 19-15, `Kilómetros` no es un tipo separado y nuevo. Los valores que tienen el tipo `Kilómetros` se tratarán de la misma manera que los valores de tipo `i32`:

    type Kilómetros = i32;

    let x: i32 = 5;
    let y: Kilómetros = 5;

    println!("x + y = {}", x + y);

Debido a que `Kilómetros` e `i32` son el mismo tipo, podemos sumar valores de ambos tipos y podemos pasar valores de `Kilómetros` a funciones que tomen parámetros de tipo `i32`. Sin embargo, con este método, no obtenemos los beneficios de comprobación de tipos que obtenemos del patrón newtype discutido anteriormente. En otras palabras, si mezclamos valores de `Kilómetros` e `i32` en algún lugar, el compilador no nos dará un error.

El principal caso de uso de los sinónimos de tipo es reducir la repetición. Por ejemplo, podríamos tener un tipo largo como este:

```rust
Box<dyn Fn() + Send + 'static>
```

Escribir este tipo largo en firmas de funciones y como anotaciones de tipo en todo el código puede ser tedioso y propenso a errores. Imagina tener un proyecto lleno de código como el de la Lista 19-24.

```rust
let f: Box<dyn Fn() + Send + 'static> = Box::new(|| {
    println!("hi");
});

fn takes_long_type(f: Box<dyn Fn() + Send + 'static>) {
    --snip--
}

fn returns_long_type() -> Box<dyn Fn() + Send + 'static> {
    --snip--
}
```

Lista 19-24: Uso de un tipo largo en muchos lugares

Un alias de tipo hace que este código sea más manejable al reducir la repetición. En la Lista 19-25, hemos introducido un alias llamado `Thunk` para el tipo verboso y podemos reemplazar todos los usos del tipo con el alias más corto `Thunk`.

    type Thunk = Box<dyn Fn() + Send + 'static>;

    let f: Thunk = Box::new(|| println!("hi"));

    fn takes_long_type(f: Thunk) {
        --snip--
    }

    fn returns_long_type() -> Thunk {
        --snip--
    }

Lista 19-25: Introducción de un alias de tipo `Thunk` para reducir la repetición

¡Este código es mucho más fácil de leer y escribir! Elegir un nombre significativo para un alias de tipo también puede ayudar a comunicar tu intención (_thunk_ es una palabra para el código que se evaluará en un momento posterior, por lo que es un nombre adecuado para una clausura que se almacena).

Los alias de tipo también se usan comúnmente con el tipo `Result<T, E>` para reducir la repetición. Considere el módulo `std::io` de la biblioteca estándar. Las operaciones de E/S a menudo devuelven un `Result<T, E>` para manejar situaciones en las que las operaciones no funcionan correctamente. Esta biblioteca tiene una estructura `std::io::Error` que representa todos los posibles errores de E/S. Muchas de las funciones en `std::io` devolverán `Result<T, E>` donde el `E` es `std::io::Error`, como estas funciones en el trato `Write`:

```rust
use std::fmt;
use std::io::Error;

pub trait Write {
    fn write(&mut self, buf: &[u8]) -> Result<usize, Error>;
    fn flush(&mut self) -> Result<(), Error>;

    fn write_all(&mut self, buf: &[u8]) -> Result<(), Error>;
    fn write_fmt(
        &mut self,
        fmt: fmt::Arguments,
    ) -> Result<(), Error>;
}
```

El `Result<..., Error>` se repite mucho. Por lo tanto, `std::io` tiene esta declaración de alias de tipo:

```rust
type Result<T> = std::result::Result<T, std::io::Error>;
```

Debido a que esta declaración está en el módulo `std::io`, podemos usar el alias calificado `std::io::Result<T>`; es decir, un `Result<T, E>` con el `E` rellenado como `std::io::Error`. Las firmas de funciones del trato `Write` terminan siendo así:

```rust
pub trait Write {
    fn write(&mut self, buf: &[u8]) -> Result<usize>;
    fn flush(&mut self) -> Result<()>;

    fn write_all(&mut self, buf: &[u8]) -> Result<()>;
    fn write_fmt(&mut self, fmt: fmt::Arguments) -> Result<()>;
}
```

El alias de tipo ayuda de dos maneras: hace que el código sea más fácil de escribir _y_ nos da una interfaz consistente en todo `std::io`. Debido a que es un alias, es simplemente otro `Result<T, E>`, lo que significa que podemos usar cualquier método que funcione en `Result<T, E>` con él, así como la sintaxis especial como el operador `?`.

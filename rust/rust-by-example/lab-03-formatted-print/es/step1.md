# Impresión formateada

La impresión se maneja mediante una serie de `macros` definidas en `std::fmt`, algunas de las cuales son las siguientes:

- `format!`: escribe texto formateado en `String`.
- `print!`: es igual a `format!`, pero el texto se imprime en la consola (io::stdout).
- `println!`: es igual a `print!`, pero se agrega una nueva línea al final.
- `eprint!`: es igual a `print!`, pero el texto se imprime en el error estándar (io::stderr).
- `eprintln!`: es igual a `eprint!`, pero se agrega una nueva línea al final.

Todas analizan el texto de la misma manera. Además, Rust comprueba la corrección del formato en tiempo de compilación.

```rust
fn main() {
    // En general, `{}` se reemplazará automáticamente con cualquier
    // argumento. Estos se convertirán en cadenas.
    println!("{} días", 31);

    // Se pueden utilizar argumentos posicionales. Especificar un entero dentro de `{}`
    // determina qué argumento adicional se reemplazará. Los argumentos empiezan
    // en 0 inmediatamente después de la cadena de formato.
    println!("{0}, esto es {1}. {1}, esto es {0}", "Alice", "Bob");

    // También se pueden utilizar argumentos con nombre.
    println!("{subject} {verb} {object}",
             object="el perro perezoso",
             subject="el rápido zorro marrón",
             verb="salta sobre");

    // Se puede invocar un formato diferente especificando el carácter de formato
    // después de un `:`.
    println!("Base 10:               {}",   69420); // 69420
    println!("Base 2 (binaria):       {:b}", 69420); // 10000111100101100
    println!("Base 8 (octal):        {:o}", 69420); // 207454
    println!("Base 16 (hexadecimal): {:x}", 69420); // 10f2c
    println!("Base 16 (hexadecimal): {:X}", 69420); // 10F2C

    // Puedes justificar el texto a la derecha con un ancho especificado. Esto
    // imprimirá "    1". (Cuatro espacios en blanco y un "1", para un ancho total de 5.)
    println!("{number:>5}", number=1);

    // Puedes rellenar los números con ceros adicionales,
    println!("{number:0>5}", number=1); // 00001
    // y ajustar a la izquierda invirtiendo el signo. Esto imprimirá "10000".
    println!("{number:0<5}", number=1); // 10000

    // Puedes utilizar argumentos con nombre en el especificador de formato agregando un `$`.
    println!("{number:0>width$}", number=1, width=5);

    // Rust incluso comprueba para asegurarse de que se utilicen el número correcto de argumentos.
    println!("Mi nombre es {0}, {1} {0}", "Bond");
    // FIXME ^ Agrega el argumento faltante: "James"

    // Solo los tipos que implementan fmt::Display se pueden formatear con `{}`. Los tipos
    // definidos por el usuario no implementan fmt::Display por defecto.

    #[allow(dead_code)] // desactiva `dead_code` que advierte sobre el módulo no utilizado
    struct Structure(i32);

    // Esto no se compilará porque `Structure` no implementa
    // fmt::Display.
    // println!("Esta struct `{}` no se imprimirá...", Structure(3));
    // TODO ^ Intenta descomentar esta línea

    // Para Rust 1.58 y superior, puedes capturar directamente el argumento de una
    // variable circundante. Al igual que lo anterior, esto imprimirá
    // "    1", 4 espacios en blanco y un "1".
    let number: f64 = 1.0;
    let width: usize = 5;
    println!("{number:>width$}");
}
```

`std::fmt` contiene muchos `traits` que gobiernan la visualización del texto. A continuación, se enumeran las formas básicas de dos de los más importantes:

- `fmt::Debug`: utiliza el marcador `{:?}`. Formatea texto con fines de depuración.
- `fmt::Display`: utiliza el marcador `{}`. Formatea texto de manera más elegante y amigable para el usuario.

Aquí, usamos `fmt::Display` porque la biblioteca estándar de Rust proporciona implementaciones para estos tipos. Para imprimir texto de tipos personalizados, se requieren más pasos.

Implementar el trato `fmt::Display` implementa automáticamente el trato `ToString` que nos permite convertir el tipo a `String`.

En la _línea 43_, `#[allow(dead_code)]` es un \[atributo\] que solo se aplica al módulo posterior a él.

## Actividades

- Corrige el problema en el código anterior (ver FIXME) para que se ejecute sin errores.
- Intenta descomentar la línea que intenta formatear la struct `Structure` (ver TODO)
- Agrega una llamada a la macro `println!` que imprima: `Pi es aproximadamente 3.142` controlando el número de decimales mostrados. Con fines de este ejercicio, utiliza `let pi = 3.141592` como una estimación de pi. (Pista: es posible que necesites revisar la documentación de `std::fmt` para establecer el número de decimales a mostrar)

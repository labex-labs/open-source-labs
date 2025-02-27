# Ejecutar código en la limpieza con el trato Drop

El segundo trato importante para el patrón de puntero inteligente es `Drop`, que te permite personalizar lo que sucede cuando un valor está a punto de salir de ámbito. Puedes proporcionar una implementación para el trato `Drop` en cualquier tipo, y ese código se puede utilizar para liberar recursos como archivos o conexiones de red.

Estamos presentando `Drop` en el contexto de los punteros inteligentes porque la funcionalidad del trato `Drop` casi siempre se utiliza al implementar un puntero inteligente. Por ejemplo, cuando se elimina un `Box<T>`, se desasignará el espacio en el montón al que apunta la caja.

En algunos lenguajes, para algunos tipos, el programador debe llamar a código para liberar memoria o recursos cada vez que termina de usar una instancia de esos tipos. Ejemplos incluyen manejadores de archivos, sockets y candados. Si se olvidan, el sistema puede sobrecargarse y se puede bloquear. En Rust, puedes especificar que se ejecute un determinado código cada vez que un valor sale de ámbito, y el compilador insertará este código automáticamente. Como resultado, no tienes que preocuparte por colocar código de limpieza en todos los lugares de un programa donde se termina con una instancia de un tipo particular: ¡todavía no se perderán recursos!

Especifiques el código a ejecutar cuando un valor sale de ámbito implementando el trato `Drop`. El trato `Drop` requiere que implementes un método llamado `drop` que tome una referencia mutable a `self`. Para ver cuándo Rust llama a `drop`, implementemos `drop` con declaraciones `println!` por ahora.

La Lista 15-14 muestra una estructura `CustomSmartPointer` cuya única funcionalidad personalizada es que imprimirá `Dropping CustomSmartPointer!` cuando la instancia sale de ámbito, para mostrar cuándo Rust ejecuta el método `drop`.

Nombre de archivo: `src/main.rs`

```rust
struct CustomSmartPointer {
    data: String,
}

1 impl Drop for CustomSmartPointer {
    fn drop(&mut self) {
      2 println!(
            "Dropping CustomSmartPointer with data `{}`!",
            self.data
        );
    }
}

fn main() {
  3 let c = CustomSmartPointer {
        data: String::from("my stuff"),
    };
  4 let d = CustomSmartPointer {
        data: String::from("other stuff"),
    };
  5 println!("CustomSmartPointers created.");
6 }
```

Lista 15-14: Una estructura `CustomSmartPointer` que implementa el trato `Drop` donde pondríamos nuestro código de limpieza

El trato `Drop` está incluido en el preludio, por lo que no es necesario traerlo al ámbito. Implementamos el trato `Drop` en `CustomSmartPointer` \[1\] y proporcionamos una implementación para el método `drop` que llama a `println!` \[2\]. El cuerpo del método `drop` es donde colocarías cualquier lógica que quisieras ejecutar cuando una instancia de tu tipo sale de ámbito. Estamos imprimiendo algunos textos aquí para demostrar visualmente cuándo Rust llamará a `drop`.

En `main`, creamos dos instancias de `CustomSmartPointer` en \[3\] y \[4\] y luego imprimimos `CustomSmartPointers created` \[5\]. Al final de `main` \[6\], nuestras instancias de `CustomSmartPointer` saldrán de ámbito, y Rust llamará al código que pusimos en el método `drop` \[2\], imprimiendo nuestro mensaje final. Tenga en cuenta que no tuvimos que llamar explícitamente al método `drop`.

Cuando ejecutamos este programa, veremos la siguiente salida:

    CustomSmartPointers created.
    Dropping CustomSmartPointer with data `other stuff`!
    Dropping CustomSmartPointer with data `my stuff`!

Rust automáticamente llamó a `drop` por nosotros cuando nuestras instancias salieron de ámbito, llamando al código que especificamos. Las variables se eliminan en el orden inverso de su creación, por lo que `d` se eliminó antes que `c`. El propósito de este ejemplo es darte una guía visual de cómo funciona el método `drop`; por lo general, especificarías el código de limpieza que tu tipo necesita ejecutar en lugar de un mensaje de impresión.

Lamentablemente, no es sencillo deshabilitar la funcionalidad automática de `drop`. En general, no es necesario deshabilitar `drop`; el objetivo principal del trato `Drop` es que se cuide automáticamente. En ocasiones, sin embargo, es posible que desees limpiar un valor temprano. Un ejemplo es cuando se utilizan punteros inteligentes que administran candados: es posible que desees forzar el método `drop` que libera el candado para que otro código en el mismo ámbito pueda adquirir el candado. Rust no te permite llamar manualmente al método `drop` del trato `Drop`; en su lugar, debes llamar a la función `std::mem::drop` proporcionada por la biblioteca estándar si deseas forzar a que se elimine un valor antes del final de su ámbito.

Si intentamos llamar manualmente al método `drop` del trato `Drop` modificando la función `main` de la Lista 15-14, como se muestra en la Lista 15-15, obtendremos un error del compilador.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let c = CustomSmartPointer {
        data: String::from("some data"),
    };
    println!("CustomSmartPointer created.");
    c.drop();
    println!(
        "CustomSmartPointer dropped before the end of main."
    );
}
```

Lista 15-15: Intentando llamar al método `drop` del trato `Drop` manualmente para limpiar temprano

Cuando intentamos compilar este código, obtendremos este error:

```bash
error[E0040]: explicit use of destructor method
  --> src/main.rs:16:7
   |
16 |     c.drop();
   |     --^^^^--
   |     | |
   |     | explicit destructor calls not allowed
   |     help: consider using `drop` function: `drop(c)`
```

Este mensaje de error indica que no se permite llamar explícitamente a `drop`. El mensaje de error utiliza el término _destructor_, que es el término general de programación para una función que limpia una instancia. Un _destructor_ es análogo a un _constructor_, que crea una instancia. La función `drop` en Rust es un destructor en particular.

Rust no nos permite llamar a `drop` explícitamente porque Rust todavía llamará automáticamente a `drop` en el valor al final de `main`. Esto causaría un error de _doble liberación_ porque Rust intentaría limpiar el mismo valor dos veces.

No podemos deshabilitar la inserción automática de `drop` cuando un valor sale de ámbito, y no podemos llamar al método `drop` explícitamente. Entonces, si necesitamos forzar a que se limpie un valor temprano, usamos la función `std::mem::drop`.

La función `std::mem::drop` es diferente del método `drop` en el trato `Drop`. La llamamos pasando como argumento el valor que queremos forzar a eliminar. La función está en el preludio, por lo que podemos modificar `main` en la Lista 15-15 para llamar a la función `drop`, como se muestra en la Lista 15-16.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let c = CustomSmartPointer {
        data: String::from("some data"),
    };
    println!("CustomSmartPointer created.");
    drop(c);
    println!(
        "CustomSmartPointer dropped before the end of main."
    );
}
```

Lista 15-16: Llamando a `std::mem::drop` para eliminar explícitamente un valor antes de que salga de ámbito

Ejecutar este código imprimirá lo siguiente:

    CustomSmartPointer created.
    Dropping CustomSmartPointer with data `some data`!
    CustomSmartPointer dropped before the end of main.

El texto `Dropping CustomSmartPointer with data`some data`!` se imprime entre el texto `CustomSmartPointer created.` y `CustomSmartPointer dropped before the end of main.`, lo que muestra que se llama al código del método `drop` para eliminar `c` en ese momento.

Puedes usar el código especificado en una implementación del trato `Drop` de muchas maneras para hacer la limpieza conveniente y segura: por ejemplo, podrías usarla para crear tu propio asignador de memoria. Con el trato `Drop` y el sistema de propiedad de Rust, no tienes que recordar limpiar porque Rust lo hace automáticamente.

También no tienes que preocuparte por problemas que resulten de limpiar accidentalmente valores que todavía se están utilizando: el sistema de propiedad que asegura que las referencias siempre sean válidas también garantiza que `drop` se llame solo una vez cuando el valor ya no se está utilizando.

Ahora que hemos examinado `Box<T>` y algunas de las características de los punteros inteligentes, echemos un vistazo a algunos otros punteros inteligentes definidos en la biblioteca estándar.

# Recibiendo la entrada del usuario

Recuerda que incluimos la funcionalidad de entrada/salida de la librería estándar con `use std::io;` en la primera línea del programa. Ahora llamaremos a la función `stdin` del módulo `io`, que nos permitirá manejar la entrada del usuario:

```rust
io::stdin()
 .read_line(&mut guess)
```

Si no hubiéramos importado la librería `io` con `use std::io;` al principio del programa, todavía podríamos usar la función escribiendo esta llamada a la función como `std::io::stdin`. La función `stdin` devuelve una instancia de `std::io::Stdin`, que es un tipo que representa un controlador de la entrada estándar de tu terminal.

A continuación, la línea `.read_line(&mut guess)` llama al método `read_line` en el controlador de entrada estándar para obtener la entrada del usuario. También estamos pasando `&mut guess` como argumento a `read_line` para decirle en qué cadena almacenar la entrada del usuario. El trabajo completo de `read_line` es tomar lo que el usuario escribe en la entrada estándar y anexarlo a una cadena (sin sobrescribir su contenido), por lo que pasamos esa cadena como argumento. El argumento de cadena debe ser mutable para que el método pueda cambiar el contenido de la cadena.

El `&` indica que este argumento es una _referencia_, lo que te da una forma de permitir que múltiples partes de tu código accedan a un pedazo de datos sin necesidad de copiar ese dato en la memoria múltiples veces. Las referencias son una característica compleja, y una de las principales ventajas de Rust es lo segura y fácil que es usar referencias. No necesitas saber muchos detalles de eso para terminar este programa. Por ahora, todo lo que necesitas saber es que, al igual que las variables, las referencias son inmutables por defecto. Por lo tanto, debes escribir `&mut guess` en lugar de `&guess` para que sea mutable. (El Capítulo 4 explicará las referencias más detenidamente.)

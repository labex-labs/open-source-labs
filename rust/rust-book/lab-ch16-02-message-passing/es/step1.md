# Using Message Passing to Transfer Data Between Threads

Una forma cada vez más popular de garantizar una concurrencia segura es el _paso de mensajes_, donde los hilos o actores se comunican enviándose unos a otros mensajes que contienen datos. Aquí está la idea en un eslogan de la documentación de Go en *https://golang.org/doc/effective_go.html#concurrency*: "No comiences a comunicarte compartiendo memoria; en su lugar, comparte memoria comunicándote".

Para lograr una concurrencia de envío de mensajes, la biblioteca estándar de Rust proporciona una implementación de _canales_. Un canal es un concepto de programación general por el cual se envía datos de un hilo a otro.

Puedes imaginar un canal en programación como un canal direccional de agua, como un arroyo o un río. Si pones algo como un pato de goma en un río, viajará hacia abajo hasta el final del cauce.

Un canal tiene dos partes: un transmisor y un receptor. La parte del transmisor es la ubicación aguas arriba donde se coloca el pato de goma en el río, y la parte del receptor es donde termina el pato de goma aguas abajo. Una parte de tu código llama a métodos en el transmisor con los datos que quieres enviar, y otra parte revisa el extremo de recepción para los mensajes que llegan. Se dice que un canal está _cerrado_ si se elimina la parte del transmisor o del receptor.

Aquí, trabajaremos hasta un programa que tenga un hilo para generar valores y enviarlos a través de un canal, y otro hilo que recibirá los valores y los imprimirá. Enviaremos valores simples entre hilos usando un canal para ilustrar la característica. Una vez que estés familiarizado con la técnica, podrías usar canales para cualquier hilo que necesite comunicarse con otro, como un sistema de chat o un sistema donde muchos hilos realizan partes de un cálculo y envían las partes a un hilo que agrega los resultados.

Primero, en la Lista 16-6, crearemos un canal pero no haremos nada con él. Tenga en cuenta que esto no se compilará todavía porque Rust no puede determinar qué tipo de valores queremos enviar a través del canal.

Nombre de archivo: `src/main.rs`

```rust
use std::sync::mpsc;

fn main() {
    let (tx, rx) = mpsc::channel();
}
```

Lista 16-6: Creando un canal y asignando las dos partes a `tx` y `rx`

Creamos un nuevo canal usando la función `mpsc::channel`; `mpsc` significa _multiple producer, single consumer_. En resumen, la forma en que la biblioteca estándar de Rust implementa los canales significa que un canal puede tener múltiples _extremos de envío_ que producen valores pero solo un _extremo de recepción_ que consume esos valores. Imagina múltiples arroyos que fluyen juntos en un gran río: todo lo que se envía por cualquiera de los arroyos terminará en un solo río al final. Empezaremos con un solo productor por ahora, pero agregaremos múltiples productores cuando tengamos este ejemplo funcionando.

La función `mpsc::channel` devuelve un par, cuyo primer elemento es el extremo de envío, el transmisor, y cuyo segundo elemento es el extremo de recepción, el receptor. Las abreviaturas `tx` y `rx` se usan tradicionalmente en muchos campos para _transmisor_ y _receptor_, respectivamente, por lo que nombramos nuestras variables de esa manera para indicar cada extremo. Estamos usando una declaración `let` con un patrón que desestructura los pares; discutiremos el uso de patrones en declaraciones `let` y la desestructuración en el Capítulo 18. Por ahora, sabe que usar una declaración `let` de esta manera es un enfoque conveniente para extraer los fragmentos del par devuelto por `mpsc::channel`.

Movamos el extremo de transmisión a un hilo creado y que envíe una cadena para que el hilo creado se comunique con el hilo principal, como se muestra en la Lista 16-7. Esto es como poner un pato de goma en el río aguas arriba o enviar un mensaje de chat de un hilo a otro.

Nombre de archivo: `src/main.rs`

```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let val = String::from("hi");
        tx.send(val).unwrap();
    });
}
```

Lista 16-7: Moviendo `tx` a un hilo creado y enviando `"hi"`

Una vez más, estamos usando `thread::spawn` para crear un nuevo hilo y luego usando `move` para mover `tx` a la clausura para que el hilo creado sea dueño de `tx`. El hilo creado necesita ser dueño del transmisor para poder enviar mensajes a través del canal.

El transmisor tiene un método `send` que toma el valor que queremos enviar. El método `send` devuelve un tipo `Result<T, E>`, por lo que si el receptor ya ha sido eliminado y no hay ningún lugar donde enviar un valor, la operación de envío devolverá un error. En este ejemplo, estamos llamando a `unwrap` para generar un error en caso de error. Pero en una aplicación real, lo manejaríamos adecuadamente: regrese al Capítulo 9 para revisar las estrategias para el manejo adecuado de errores.

En la Lista 16-8, obtendremos el valor del receptor en el hilo principal. Esto es como recuperar el pato de goma del agua al final del río o recibir un mensaje de chat.

Nombre de archivo: `src/main.rs`

```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let val = String::from("hi");
        tx.send(val).unwrap();
    });

    let received = rx.recv().unwrap();
    println!("Got: {received}");
}
```

Lista 16-8: Recibiendo el valor `"hi"` en el hilo principal y lo imprimiendo

El receptor tiene dos métodos útiles: `recv` y `try_recv`. Estamos usando `recv`, abreviatura de _receive_, que bloqueará la ejecución del hilo principal y esperará hasta que se envíe un valor a través del canal. Una vez que se envía un valor, `recv` lo devolverá en un `Result<T, E>`. Cuando el transmisor se cierra, `recv` devolverá un error para indicar que ya no se enviarán más valores.

El método `try_recv` no bloquea, sino que devolverá inmediatamente un `Result<T, E>`: un valor `Ok` que contiene un mensaje si hay uno disponible y un valor `Err` si no hay mensajes en este momento. Usar `try_recv` es útil si este hilo tiene otras tareas que hacer mientras espera mensajes: podríamos escribir un bucle que llame a `try_recv` de vez en cuando, maneje un mensaje si hay uno disponible y, de lo contrario, haga otras tareas por un tiempo hasta comprobar de nuevo.

Hemos usado `recv` en este ejemplo por simplicidad; no tenemos ninguna otra tarea para que el hilo principal haga más que esperar mensajes, por lo que bloquear el hilo principal es apropiado.

Cuando ejecutamos el código de la Lista 16-8, veremos el valor impreso desde el hilo principal:

```rust
Got: hi
```

¡Perfecto!

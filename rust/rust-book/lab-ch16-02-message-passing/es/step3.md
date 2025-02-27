# Enviando múltiples valores y viendo al receptor esperando

El código de la Lista 16-8 se compiló y ejecutó, pero no nos mostró claramente que dos hilos separados estaban comunicándose entre sí a través del canal. En la Lista 16-10 hicimos algunos cambios que demostrarán que el código de la Lista 16-8 está ejecutándose de manera concurrente: el hilo creado ahora enviará múltiples mensajes y pausará durante un segundo entre cada mensaje.

Nombre de archivo: `src/main.rs`

```rust
use std::sync::mpsc;
use std::thread;
use std::time::Duration;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let vals = vec![
            String::from("hi"),
            String::from("from"),
            String::from("the"),
            String::from("thread"),
        ];

        for val in vals {
            tx.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });

    for received in rx {
        println!("Got: {received}");
    }
}
```

Lista 16-10: Enviando múltiples mensajes y pausando entre cada uno

Esta vez, el hilo creado tiene un vector de cadenas que queremos enviar al hilo principal. Iteramos sobre ellos, enviando cada uno individualmente, y pausamos entre cada uno llamando a la función `thread::sleep` con un valor `Duration` de un segundo.

En el hilo principal, ya no estamos llamando explícitamente a la función `recv`: en su lugar, estamos tratando a `rx` como un iterador. Para cada valor recibido, lo imprimimos. Cuando el canal se cierra, la iteración terminará.

Al ejecutar el código de la Lista 16-10, deberías ver la siguiente salida con una pausa de un segundo entre cada línea:

    Got: hi
    Got: from
    Got: the
    Got: thread

Debido a que no tenemos ningún código que pause o retrase en el `for` loop del hilo principal, podemos decir que el hilo principal está esperando a recibir valores del hilo creado.

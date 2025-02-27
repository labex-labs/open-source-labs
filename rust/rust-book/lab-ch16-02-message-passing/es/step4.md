# Creando múltiples productores mediante la clonación del transmisor

Antes mencionamos que `mpsc` era un acrónimo de _multiple producer, single consumer_. Vamos a poner en práctica `mpsc` y expandir el código de la Lista 16-10 para crear múltiples hilos que todos envíen valores al mismo receptor. Lo podemos hacer clonando el transmisor, como se muestra en la Lista 16-11.

Nombre de archivo: `src/main.rs`

```rust
--snip--

let (tx, rx) = mpsc::channel();

let tx1 = tx.clone();
thread::spawn(move || {
    let vals = vec![
        String::from("hi"),
        String::from("from"),
        String::from("the"),
        String::from("thread"),
    ];

    for val in vals {
        tx1.send(val).unwrap();
        thread::sleep(Duration::from_secs(1));
    }
});

thread::spawn(move || {
    let vals = vec![
        String::from("more"),
        String::from("messages"),
        String::from("for"),
        String::from("you"),
    ];

    for val in vals {
        tx.send(val).unwrap();
        thread::sleep(Duration::from_secs(1));
    }
});

for received in rx {
    println!("Got: {received}");
}

--snip--
```

Lista 16-11: Enviando múltiples mensajes de múltiples productores

Esta vez, antes de crear el primer hilo creado, llamamos a `clone` en el transmisor. Esto nos dará un nuevo transmisor que podemos pasar al primer hilo creado. Pasamos el transmisor original a un segundo hilo creado. Esto nos da dos hilos, cada uno enviando mensajes diferentes al mismo receptor.

Cuando ejecutes el código, tu salida debería verse así:

    Got: hi
    Got: more
    Got: from
    Got: messages
    Got: for
    Got: the
    Got: thread
    Got: you

Podrías ver los valores en otro orden, dependiendo de tu sistema. Esto es lo que hace que la concurrencia sea interesante y difícil al mismo tiempo. Si experimentas con `thread::sleep`, dándole diferentes valores en los diferentes hilos, cada ejecución será más indeterminista y creará una salida diferente cada vez.

Ahora que hemos visto cómo funcionan los canales, veamos un método diferente de concurrencia.

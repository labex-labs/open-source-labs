# Canales y transferencia de propiedad

Las reglas de propiedad juegan un papel fundamental en el envío de mensajes porque te ayudan a escribir código concurrente seguro. Prevenir errores en la programación concurrente es la ventaja de pensar en la propiedad en todo tu programa Rust. Hagamos un experimento para mostrar cómo los canales y la propiedad trabajan juntos para prevenir problemas: intentaremos usar un valor `val` en el hilo creado _después_ de haberlo enviado a través del canal. Intenta compilar el código de la Lista 16-9 para ver por qué este código no está permitido.

Nombre de archivo: `src/main.rs`

```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let val = String::from("hi");
        tx.send(val).unwrap();
        println!("val is {val}");
    });

    let received = rx.recv().unwrap();
    println!("Got: {received}");
}
```

Lista 16-9: Intentando usar `val` después de haberlo enviado a través del canal

Aquí, intentamos imprimir `val` después de haberlo enviado a través del canal mediante `tx.send`. Permitir esto sería una mala idea: una vez que el valor ha sido enviado a otro hilo, ese hilo podría modificarlo o eliminarlo antes de que intentemos usar el valor nuevamente. Potencialmente, las modificaciones del otro hilo podrían causar errores o resultados inesperados debido a datos inconsistentes o inexistentes. Sin embargo, Rust nos da un error si intentamos compilar el código de la Lista 16-9:

```bash
error[E0382]: borrow of moved value: `val`
  --> src/main.rs:10:31
   |
8  |         let val = String::from("hi");
   |             --- move occurs because `val` has type `String`, which does
not implement the `Copy` trait
9  |         tx.send(val).unwrap();
   |                 --- value moved here
10 |         println!("val is {val}");
   |                           ^^^ value borrowed here after move
```

Nuestro error de concurrencia ha causado un error de compilación. La función `send` toma la propiedad de su parámetro, y cuando el valor se mueve, el receptor toma la propiedad de él. Esto nos impide usar accidentalmente el valor nuevamente después de enviarlo; el sistema de propiedad comprueba que todo está bien.

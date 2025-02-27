# Waiting for All Threads to Finish Using join Handles

El código de la Lista 16-1 no solo detiene el hilo creado prematuramente la mayoría de las veces debido a que el hilo principal finaliza, sino que también, dado que no hay garantía sobre el orden en el que se ejecutan los hilos, no podemos garantizar que el hilo creado se ejecute en absoluto.

Podemos solucionar el problema de que el hilo creado no se ejecute o que finalice prematuramente guardando el valor de retorno de `thread::spawn` en una variable. El tipo de retorno de `thread::spawn` es `JoinHandle<T>`. Un `JoinHandle<T>` es un valor propiedad que, cuando llamamos al método `join` sobre él, esperará a que su hilo termine. La Lista 16-2 muestra cómo usar el `JoinHandle<T>` del hilo que creamos en la Lista 16-1 y llamar a `join` para asegurarnos de que el hilo creado finalice antes de que `main` salga.

Nombre de archivo: `src/main.rs`

```rust
use std::thread;
use std::time::Duration;

fn main() {
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {i} from the spawned thread!");
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("hi number {i} from the main thread!");
        thread::sleep(Duration::from_millis(1));
    }

    handle.join().unwrap();
}
```

Lista 16-2: Guardando un `JoinHandle<T>` de `thread::spawn` para garantizar que el hilo se ejecute hasta el final

Llamar a `join` en el manejador bloquea el hilo que está actualmente en ejecución hasta que el hilo representado por el manejador finaliza. _Bloquear_ un hilo significa que se impide que ese hilo realice trabajo o salga. Debido a que hemos colocado la llamada a `join` después del bucle `for` del hilo principal, al ejecutar la Lista 16-2 se debería producir una salida similar a esta:

    hi number 1 from the main thread!
    hi number 2 from the main thread!
    hi number 1 from the spawned thread!
    hi number 3 from the main thread!
    hi number 2 from the spawned thread!
    hi number 4 from the main thread!
    hi number 3 from the spawned thread!
    hi number 4 from the spawned thread!
    hi number 5 from the spawned thread!
    hi number 6 from the spawned thread!
    hi number 7 from the spawned thread!
    hi number 8 from the spawned thread!
    hi number 9 from the spawned thread!

Los dos hilos continúan alternando, pero el hilo principal espera debido a la llamada a `handle.join()` y no finaliza hasta que el hilo creado ha terminado.

Pero veamos qué pasa cuando en lugar de eso movemos `handle.join()` antes del bucle `for` en `main`, así:

Nombre de archivo: `src/main.rs`

```rust
use std::thread;
use std::time::Duration;

fn main() {
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {i} from the spawned thread!");
            thread::sleep(Duration::from_millis(1));
        }
    });

    handle.join().unwrap();

    for i in 1..5 {
        println!("hi number {i} from the main thread!");
        thread::sleep(Duration::from_millis(1));
    }
}
```

El hilo principal esperará a que el hilo creado termine y luego ejecutará su bucle `for`, por lo que la salida ya no se intercalará, como se muestra aquí:

    hi number 1 from the spawned thread!
    hi number 2 from the spawned thread!
    hi number 3 from the spawned thread!
    hi number 4 from the spawned thread!
    hi number 5 from the spawned thread!
    hi number 6 from the spawned thread!
    hi number 7 from the spawned thread!
    hi number 8 from the spawned thread!
    hi number 9 from the spawned thread!
    hi number 1 from the main thread!
    hi number 2 from the main thread!
    hi number 3 from the main thread!
    hi number 4 from the main thread!

Detalles tan pequeños como dónde se llama a `join` pueden afectar a si tus hilos se ejecutan al mismo tiempo o no.

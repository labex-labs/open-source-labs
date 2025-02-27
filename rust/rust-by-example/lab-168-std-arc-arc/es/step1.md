# Arc

Cuando se necesita propiedad compartida entre hilos, se puede usar `Arc`(Atomically Reference Counted). Esta estructura, a través de la implementación de `Clone`, puede crear un puntero de referencia a la ubicación de un valor en el montón de memoria mientras aumenta el contador de referencias. Como comparte la propiedad entre hilos, cuando el último puntero de referencia a un valor sale del ámbito, la variable se elimina.

```rust
use std::time::Duration;
use std::sync::Arc;
use std::thread;

fn main() {
    // Esta declaración de variable es donde se especifica su valor.
    let apple = Arc::new("the same apple");

    for _ in 0..10 {
        // Aquí no hay especificación de valor ya que es un puntero a una
        // referencia en el montón de memoria.
        let apple = Arc::clone(&apple);

        thread::spawn(move || {
            // Dado que se usó Arc, se pueden crear hilos usando el valor asignado
            // en la ubicación del puntero de variable Arc.
            println!("{:?}", apple);
        });
    }

    // Asegúrese de que todas las instancias de Arc se impriman desde los hilos creados.
    thread::sleep(Duration::from_secs(1));
}
```

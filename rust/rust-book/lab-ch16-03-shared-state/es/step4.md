# Compartiendo un Mutex`<T>` Entre Varios Hilos

Ahora intentemos compartir un valor entre varios hilos usando `Mutex<T>`. Iniciaremos 10 hilos y les pediremos que cada uno incremente en 1 un valor de contador, de modo que el contador pase de 0 a 10. El ejemplo de la Lista 16-13 tendrá un error de compilación, y usaremos ese error para aprender más sobre el uso de `Mutex<T>` y cómo Rust nos ayuda a usarlo correctamente.

Nombre de archivo: `src/main.rs`

```rust
use std::sync::Mutex;
use std::thread;

fn main() {
  1 let counter = Mutex::new(0);
    let mut handles = vec![];

  2 for _ in 0..10 {
      3 let handle = thread::spawn(move || {
          4 let mut num = counter.lock().unwrap();

          5 *num += 1;
        });
      6 handles.push(handle);
    }

    for handle in handles {
      7 handle.join().unwrap();
    }

  8 println!("Result: {}", *counter.lock().unwrap());
}
```

Lista 16-13: Diez hilos, cada uno incrementando un contador protegido por un `Mutex<T>`

Creamos una variable `counter` para almacenar un `i32` dentro de un `Mutex<T>` \[1\], como hicimos en la Lista 16-12. A continuación, creamos 10 hilos iterando sobre un rango de números \[2\]. Usamos `thread::spawn` y le damos a todos los hilos la misma clausura: una que mueve el contador al hilo \[3\], adquiere un cerrojo en el `Mutex<T>` llamando al método `lock` \[4\], y luego suma 1 al valor en el mutex \[5\]. Cuando un hilo termina de ejecutar su clausura, `num` saldrá del ámbito y liberará el cerrojo para que otro hilo pueda adquirirlo.

En el hilo principal, recolectamos todos los manejadores de unión \[6\]. Luego, como hicimos en la Lista 16-2, llamamos a `join` en cada manejador para asegurarnos de que todos los hilos terminen \[7\]. En ese momento, el hilo principal adquirirá el cerrojo y mostrará el resultado de este programa \[8\].

Indicamos que este ejemplo no se compilaría. Ahora averigüemos por qué.

```bash
error[E0382]: use of moved value: `counter`
  --> src/main.rs:9:36
   |
5  |     let counter = Mutex::new(0);
   |         ------- move occurs because `counter` has type `Mutex<i32>`, which
does not implement the `Copy` trait
...
9  |         let handle = thread::spawn(move || {
   |                                    ^^^^^^^ value moved into closure here,
in previous iteration of loop
10 |             let mut num = counter.lock().unwrap();
   |                           ------- use occurs due to use in closure
```

El mensaje de error indica que el valor `counter` se movió en la iteración anterior del bucle. Rust está diciéndonos que no podemos mover la propiedad del cerrojo `counter` a varios hilos. Vamos a corregir el error de compilación con el método de propiedad múltiple que discutimos en el Capítulo 15.

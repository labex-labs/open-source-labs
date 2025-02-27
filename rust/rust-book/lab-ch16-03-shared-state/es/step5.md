# Propiedad Múltiple con Varios Hilos

En el Capítulo 15, le dimos un valor a múltiples propietarios usando el puntero inteligente `Rc<T>` para crear un valor con referencia contada. Hagamos lo mismo aquí y veamos qué pasa. Envolveremos el `Mutex<T>` en `Rc<T>` en la Lista 16-14 y clonaremos el `Rc<T>` antes de transferir la propiedad al hilo.

Nombre de archivo: `src/main.rs`

```rust
use std::rc::Rc;
use std::sync::Mutex;
use std::thread;

fn main() {
    let counter = Rc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Rc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();

            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Result: {}", *counter.lock().unwrap());
}
```

Lista 16-14: Intentando usar `Rc<T>` para permitir que varios hilos posean el `Mutex<T>`

Una vez más, compilamos y obtenemos... errores diferentes. El compilador está enseñándonos mucho.

```bash
error[E0277]: `Rc<Mutex<i32>>` cannot be sent between threads safely 1
   --> src/main.rs:11:22
    |
11  |           let handle = thread::spawn(move || {
    |  ______________________^^^^^^^^^^^^^_-
    | |                      |
    | |                      `Rc<Mutex<i32>>` cannot be sent between threads
safely
12  | |             let mut num = counter.lock().unwrap();
13  | |
14  | |             *num += 1;
15  | |         });
    | |_________- within this `[closure@src/main.rs:11:36: 15:10]`
    |
= help: within `[closure@src/main.rs:11:36: 15:10]`, the trait `Send` is not
implemented for `Rc<Mutex<i32>>` 2
    = note: required because it appears within the type
`[closure@src/main.rs:11:36: 15:10]`
note: required by a bound in `spawn`
```

Wow, ese mensaje de error es muy largo. Aquí está la parte importante en la que centrarse: ``Rc<Mutex<i32>>` no se puede enviar entre hilos de forma segura` [1]. El compilador también nos está diciendo el por qué: `la característica `Send` no está implementada para `Rc<Mutex<i32>>`` \[2\]. Hablaremos de `Send` en la siguiente sección: es una de las características que garantiza que los tipos que usamos con los hilos son adecuados para su uso en situaciones concurrentes.

Lamentablemente, `Rc<T>` no es seguro para compartir entre hilos. Cuando `Rc<T>` gestiona la cuenta de referencias, aumenta la cuenta para cada llamada a `clone` y la disminuye cuando se elimina cada clon. Pero no utiliza ningún primitivo de concurrencia para asegurarse de que los cambios en la cuenta no puedan ser interrumpidos por otro hilo. Esto podría llevar a cuentas incorrectas, errores sutiles que a su vez podrían causar fugas de memoria o que un valor se elimine antes de que hayamos terminado con él. Lo que necesitamos es un tipo exactamente como `Rc<T>` pero que haga los cambios en la cuenta de referencias de manera segura para los hilos.

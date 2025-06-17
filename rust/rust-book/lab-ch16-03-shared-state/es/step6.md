# Conteo de Referencias Atómico con Arc`<T>`

Afortunadamente, `Arc<T>` _es_ un tipo como `Rc<T>` que es seguro de usar en situaciones concurrentes. La _a_ significa _atómico_, lo que significa que es un tipo _con conteo de referencias atómico_. Los atómicos son un tipo adicional de primitivos de concurrencia que no cubriremos en detalle aquí: consulte la documentación de la biblioteca estándar para `std::sync::atomic` para obtener más detalles. En este momento, solo necesita saber que los atómicos funcionan como los tipos primitivos pero son seguros para compartir entre hilos.

Entonces, puede preguntarse por qué no todos los tipos primitivos son atómicos y por qué los tipos de la biblioteca estándar no se implementan para usar `Arc<T>` por defecto. La razón es que la seguridad para los hilos tiene un costo de rendimiento que solo quieres pagar cuando realmente lo necesitas. Si solo estás realizando operaciones en valores dentro de un solo hilo, tu código puede ejecutarse más rápido si no tiene que cumplir con las garantías que proporcionan los atómicos.

Volvamos a nuestro ejemplo: `Arc<T>` y `Rc<T>` tienen la misma API, por lo que corregimos nuestro programa cambiando la línea `use`, la llamada a `new` y la llamada a `clone`. El código de la Lista 16-15 finalmente se compilará y ejecutará.

Nombre de archivo: `src/main.rs`

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Arc::clone(&counter);
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

Lista 16-15: Usando un `Arc<T>` para envolver el `Mutex<T>` para poder compartir la propiedad entre varios hilos

Este código imprimirá lo siguiente:

```rust
Result: 10
```

¡Lo hicimos! Contamos de 0 a 10, lo que puede no parecer muy impresionante, pero realmente nos enseñó mucho sobre `Mutex<T>` y la seguridad para los hilos. También podrías usar la estructura de este programa para hacer operaciones más complicadas que solo incrementar un contador. Usando esta estrategia, puedes dividir un cálculo en partes independientes, dividir esas partes entre hilos y luego usar un `Mutex<T>` para que cada hilo actualice el resultado final con su parte.

Tenga en cuenta que si está realizando operaciones numéricas simples, hay tipos más simples que los tipos `Mutex<T>` proporcionados por el módulo `std::sync::atomic` de la biblioteca estándar. Estos tipos proporcionan acceso seguro, concurrente y atómico a los tipos primitivos. Elegimos usar `Mutex<T>` con un tipo primitivo para este ejemplo para que pudiéramos concentrar nuestra atención en cómo funciona `Mutex<T>`.

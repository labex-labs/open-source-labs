# La API de Mutex`<T>`

Como ejemplo de cómo usar un mutex, comenzaremos por usarlo en un contexto de un solo hilo, como se muestra en la Lista 16-12.

Nombre de archivo: `src/main.rs`

```rust
use std::sync::Mutex;

fn main() {
  1 let m = Mutex::new(5);

    {
      2 let mut num = m.lock().unwrap();
      3 *num = 6;
  4 }

  5 println!("m = {:?}", m);
}
```

Lista 16-12: Explorando la API de `Mutex<T>` en un contexto de un solo hilo para mayor simplicidad

Como con muchos tipos, creamos un `Mutex<T>` usando la función asociada `new` \[1\]. Para acceder a los datos dentro del mutex, usamos el método `lock` para adquirir el cerrojo \[2\]. Esta llamada bloqueará el hilo actual, por lo que no podrá realizar ningún trabajo hasta que sea su turno para tener el cerrojo.

La llamada a `lock` fallaría si otro hilo que tiene el cerrojo se descontrolara. En ese caso, nadie podría obtener el cerrojo, por lo que hemos elegido `unwrap` y que este hilo se descontrolara si estamos en esa situación.

Después de haber adquirido el cerrojo, podemos tratar el valor devuelto, denominado `num` en este caso, como una referencia mutable a los datos dentro. El sistema de tipos garantiza que adquiramos un cerrojo antes de usar el valor en `m`. El tipo de `m` es `Mutex<i32>`, no `i32`, por lo que _debemos_ llamar a `lock` para poder usar el valor `i32`. No podemos olvidarlo; el sistema de tipos no nos permitirá acceder al `i32` interno de otra manera.

Como es de esperar, `Mutex<T>` es un puntero inteligente. Más precisamente, la llamada a `lock` _devuelve_ un puntero inteligente llamado `MutexGuard`, envuelto en un `LockResult` que manejamos con la llamada a `unwrap`. El puntero inteligente `MutexGuard` implementa `Deref` para apuntar a nuestros datos internos; el puntero inteligente también tiene una implementación de `Drop` que libera el cerrojo automáticamente cuando un `MutexGuard` sale del ámbito, lo que sucede al final del ámbito interno \[4\]. Como resultado, no corremos el riesgo de olvidar liberar el cerrojo y bloquear el mutex para que no pueda ser usado por otros hilos porque la liberación del cerrojo se produce automáticamente.

Después de liberar el cerrojo, podemos imprimir el valor del mutex y ver que pudimos cambiar el `i32` interno a `6` \[5\].

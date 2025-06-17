# Mantenimiento del Control de Préstamos en Tiempo de Ejecución con RefCell`<T>`

Al crear referencias inmutables y mutables, usamos la sintaxis `&` y `&mut`, respectivamente. Con `RefCell<T>`, usamos los métodos `borrow` y `borrow_mut`, que son parte de la API segura que pertenece a `RefCell<T>`. El método `borrow` devuelve el tipo de apuntador inteligente `Ref<T>`, y `borrow_mut` devuelve el tipo de apuntador inteligente `RefMut<T>`. Ambos tipos implementan `Deref`, por lo que podemos tratarlos como referencias normales.

`RefCell<T>` mantiene un control de cuántos apuntadores inteligentes `Ref<T>` y `RefMut<T>` están actualmente activos. Cada vez que llamamos a `borrow`, `RefCell<T>` incrementa su cuenta de cuántos préstamos inmutables están activos. Cuando un valor `Ref<T>` sale del ámbito, la cuenta de préstamos inmutables disminuye en 1. Al igual que las reglas de préstamo en tiempo de compilación, `RefCell<T>` nos permite tener muchos préstamos inmutables o un préstamo mutable en cualquier momento.

Si intentamos violar estas reglas, en lugar de obtener un error del compilador como lo haríamos con las referencias, la implementación de `RefCell<T>` se bloqueará en tiempo de ejecución. La Lista 15-23 muestra una modificación de la implementación de `send` en la Lista 15-22. Estamos deliberadamente intentando crear dos préstamos mutables activos para el mismo ámbito para ilustrar que `RefCell<T>` nos impide hacer esto en tiempo de ejecución.

Nombre de archivo: `src/lib.rs`

```rust
impl Messenger for MockMessenger {
    fn send(&self, message: &str) {
        let mut one_borrow = self.sent_messages.borrow_mut();
        let mut two_borrow = self.sent_messages.borrow_mut();

        one_borrow.push(String::from(message));
        two_borrow.push(String::from(message));
    }
}
```

Lista 15-23: Creando dos referencias mutables en el mismo ámbito para ver que `RefCell<T>` se bloqueará

Creamos una variable `one_borrow` para el apuntador inteligente `RefMut<T>` devuelto por `borrow_mut`. Luego creamos otro préstamo mutable de la misma manera en la variable `two_borrow`. Esto crea dos referencias mutables en el mismo ámbito, lo cual no está permitido. Cuando ejecutamos las pruebas de nuestra biblioteca, el código en la Lista 15-23 se compilará sin errores, pero la prueba fallará:

    ---- tests::it_sends_an_over_75_percent_warning_message stdout ----
    thread 'main' panicked at 'already borrowed: BorrowMutError', src/lib.rs:60:53
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

Observe que el código se bloqueó con el mensaje `already borrowed: BorrowMutError`. Así es como `RefCell<T>` maneja las violaciones de las reglas de préstamo en tiempo de ejecución.

Elegir capturar errores de préstamo en tiempo de ejecución en lugar de en tiempo de compilación, como lo hemos hecho aquí, significa que posiblemente estarías encontrando errores en tu código más adelante en el proceso de desarrollo: posiblemente no hasta que tu código se haya desplegado en producción. Además, tu código sufrirá una pequeña penalización de rendimiento en tiempo de ejecución como resultado de mantener el control de los préstamos en tiempo de ejecución en lugar de en tiempo de compilación. Sin embargo, usar `RefCell<T>` hace posible escribir un objeto de simulación que puede modificarse a sí mismo para registrar los mensajes que ha visto mientras lo estás usando en un contexto donde solo se permiten valores inmutables. Puedes usar `RefCell<T>` a pesar de sus compensaciones para obtener más funcionalidad que las referencias normales proporcionan.

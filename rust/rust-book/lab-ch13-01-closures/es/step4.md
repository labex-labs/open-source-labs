# Capturando Referencias o Transferiendo la Propiedad

Los closures pueden capturar valores de su entorno de tres maneras, lo cual se mapea directamente a las tres maneras en las que una función puede tomar un parámetro: prestar inmutablemente, prestar mutablemente y tomar la propiedad. El closure decidirá cuál de estas utilizará en función de lo que haga el cuerpo de la función con los valores capturados.

En la Lista 13-4, definimos un closure que captura una referencia inmutable al vector llamado `list` porque solo necesita una referencia inmutable para imprimir el valor.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let list = vec![1, 2, 3];
    println!("Before defining closure: {:?}", list);

  1 let only_borrows = || println!("From closure: {:?}", list);

    println!("Before calling closure: {:?}", list);
  2 only_borrows();
    println!("After calling closure: {:?}", list);
}
```

Lista 13-4: Definiendo y llamando un closure que captura una referencia inmutable

Este ejemplo también ilustra que una variable puede enlazarse a una definición de closure \[1\], y luego podemos llamar al closure usando el nombre de la variable y paréntesis como si el nombre de la variable fuera el nombre de una función \[2\].

Debido a que podemos tener múltiples referencias inmutables a `list` al mismo tiempo, `list` sigue siendo accesible desde el código antes de la definición del closure, después de la definición del closure pero antes de que se llame al closure y después de que se llame al closure. Este código se compila, ejecuta y muestra:

    Before defining closure: [1, 2, 3]
    Before calling closure: [1, 2, 3]
    From closure: [1, 2, 3]
    After calling closure: [1, 2, 3]

A continuación, en la Lista 13-5, cambiamos el cuerpo del closure para que agregue un elemento al vector `list`. El closure ahora captura una referencia mutable.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let mut list = vec![1, 2, 3];
    println!("Before defining closure: {:?}", list);

    let mut borrows_mutably = || list.push(7);

    borrows_mutably();
    println!("After calling closure: {:?}", list);
}
```

Lista 13-5: Definiendo y llamando un closure que captura una referencia mutable

Este código se compila, ejecuta y muestra:

```rust
Before defining closure: [1, 2, 3]
After calling closure: [1, 2, 3, 7]
```

Nota que ya no hay un `println!` entre la definición y la llamada del closure `borrows_mutably`: cuando se define `borrows_mutably`, captura una referencia mutable a `list`. No usamos el closure nuevamente después de que se llame al closure, por lo que el préstamo mutable finaliza. Entre la definición del closure y la llamada del closure, no se permite un préstamo inmutable para imprimir porque no se permiten otros préstamos cuando hay un préstamo mutable. Intenta agregar un `println!` allí para ver qué mensaje de error obtienes!

Si quieres forzar al closure a tomar la propiedad de los valores que utiliza en el entorno aunque el cuerpo del closure no necesite estrictamente la propiedad, puedes usar la palabra clave `move` antes de la lista de parámetros.

Esta técnica es útil principalmente cuando se pasa un closure a un nuevo hilo para mover los datos de modo que queden propiedad del nuevo hilo. Discutiremos los hilos y por qué quisieras usarlos en detalle en el Capítulo 16 cuando hablamos de concurrencia, pero por ahora, exploremos brevemente cómo crear un nuevo hilo usando un closure que necesita la palabra clave `move`. La Lista 13-6 muestra la Lista 13-4 modificada para imprimir el vector en un nuevo hilo en lugar del hilo principal.

Nombre de archivo: `src/main.rs`

```rust
use std::thread;

fn main() {
    let list = vec![1, 2, 3];
    println!("Before defining closure: {:?}", list);

  1 thread::spawn(move || {
      2 println!("From thread: {:?}", list)
    }).join().unwrap();
}
```

Lista 13-6: Usando `move` para forzar al closure del hilo a tomar la propiedad de `list`

Creamos un nuevo hilo, pasando al hilo un closure para que se ejecute como argumento. El cuerpo del closure imprime la lista. En la Lista 13-4, el closure solo capturó `list` usando una referencia inmutable porque esa es la menor cantidad de acceso a `list` necesaria para imprimirla. En este ejemplo, aunque el cuerpo del closure todavía solo necesita una referencia inmutable \[2\], necesitamos especificar que `list` debe ser movida al closure poniendo la palabra clave `move` \[1\] al principio de la definición del closure. El nuevo hilo podría terminar antes de que el resto del hilo principal termine, o el hilo principal podría terminar primero. Si el hilo principal mantiene la propiedad de `list` pero termina antes del nuevo hilo y libera `list`, la referencia inmutable en el hilo sería inválida. Por lo tanto, el compilador requiere que `list` sea movida al closure dado al nuevo hilo para que la referencia sea válida. Intenta quitar la palabra clave `move` o usar `list` en el hilo principal después de que se defina el closure para ver qué errores del compilador obtienes!

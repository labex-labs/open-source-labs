# Usando Rc`<T>`{=html} para compartir datos

Volvamos a nuestro ejemplo de lista enlazada en la Lista 15-5. Recuerde que la definimos usando `Box<T>`. Esta vez, crearemos dos listas que comparten la propiedad de una tercera lista. Conceptualmente, esto se parece a la Figura 15-3.

Figura 15-3: Dos listas, `b` y `c`, compartiendo la propiedad de una tercera lista, `a`

Crearemos la lista `a` que contiene `5` y luego `10`. Luego crearemos dos listas más: `b` que comienza con `3` y `c` que comienza con `4`. Ambas listas `b` y `c` luego continuarán con la primera lista `a` que contiene `5` y `10`. En otras palabras, ambas listas compartirán la primera lista que contiene `5` y `10`.

Intentar implementar este escenario usando nuestra definición de `List` con `Box<T>` no funcionará, como se muestra en la Lista 15-17.

Nombre de archivo: `src/main.rs`

```rust
enum List {
    Cons(i32, Box<List>),
    Nil,
}

use crate::List::{Cons, Nil};

fn main() {
    let a = Cons(5, Box::new(Cons(10, Box::new(Nil))));
  1 let b = Cons(3, Box::new(a));
  2 let c = Cons(4, Box::new(a));
}
```

Lista 15-17: Demostrando que no se permite tener dos listas usando `Box<T>` que intentan compartir la propiedad de una tercera lista

Cuando compilamos este código, obtenemos este error:

```bash
error[E0382]: use of moved value: `a`
  --> src/main.rs:11:30
   |
9  |     let a = Cons(5, Box::new(Cons(10, Box::new(Nil))));
   |         - move occurs because `a` has type `List`, which
does not implement the `Copy` trait
10 |     let b = Cons(3, Box::new(a));
   |                              - value moved here
11 |     let c = Cons(4, Box::new(a));
   |                              ^ value used here after move
```

Las variantes `Cons` poseen los datos que contienen, por lo que cuando creamos la lista `b` \[1\], `a` se mueve a `b` y `b` posee `a`. Luego, cuando intentamos usar `a` nuevamente al crear `c` \[2\], no se nos permite hacerlo porque `a` ha sido movido.

Podríamos cambiar la definición de `Cons` para que tenga referencias en lugar de valores, pero entonces tendríamos que especificar parámetros de vida. Al especificar parámetros de vida, estaríamos especificando que cada elemento de la lista vivirá al menos tanto tiempo como la lista completa. Este es el caso para los elementos y listas de la Lista 15-17, pero no en todos los escenarios.

En lugar de eso, cambiaremos nuestra definición de `List` para usar `Rc<T>` en lugar de `Box<T>`, como se muestra en la Lista 15-18. Cada variante `Cons` ahora contendrá un valor y un `Rc<T>` que apunta a una `List`. Cuando creamos `b`, en lugar de tomar posesión de `a`, clonaremos el `Rc<List>` que `a` está manteniendo, aumentando así el número de referencias de uno a dos y permitiendo que `a` y `b` compartan la propiedad de los datos en ese `Rc<List>`. También clonaremos `a` al crear `c`, aumentando el número de referencias de dos a tres. Cada vez que llamamos a `Rc::clone`, el recuento de referencias al data dentro del `Rc<List>` aumentará, y los datos no se limpiarán a menos que no haya referencias a ellos.

Nombre de archivo: `src/main.rs`

```rust
enum List {
    Cons(i32, Rc<List>),
    Nil,
}

use crate::List::{Cons, Nil};
1 use std::rc::Rc;

fn main() {
  2 let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
  3 let b = Cons(3, Rc::clone(&a));
  4 let c = Cons(4, Rc::clone(&a));
}
```

Lista 15-18: Una definición de `List` que usa `Rc<T>`

Necesitamos agregar una declaración `use` para traer `Rc<T>` al ámbito \[1\] porque no está en el preludio. En `main`, creamos la lista que contiene `5` y `10` y la almacenamos en un nuevo `Rc<List>` en `a` \[2\]. Luego, cuando creamos `b` \[3\] y `c` \[4\], llamamos a la función `Rc::clone` y pasamos una referencia al `Rc<List>` en `a` como argumento.

Podríamos haber llamado `a.clone()` en lugar de `Rc::clone(&a)`, pero la convención de Rust es usar `Rc::clone` en este caso. La implementación de `Rc::clone` no hace una copia profunda de todos los datos como lo hacen la mayoría de las implementaciones de `clone` de los tipos. La llamada a `Rc::clone` solo incrementa el recuento de referencias, lo que no lleva mucho tiempo. Las copias profundas de datos pueden llevar mucho tiempo. Al usar `Rc::clone` para el conteo de referencias, podemos distinguir visualmente entre los tipos de clonación de copia profunda y los tipos de clonación que aumentan el recuento de referencias. Al buscar problemas de rendimiento en el código, solo necesitamos considerar las clonaciones de copia profunda y podemos ignorar las llamadas a `Rc::clone`.

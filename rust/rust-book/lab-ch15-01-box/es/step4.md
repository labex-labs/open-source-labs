# Más información sobre la lista cons

Una _lista cons_ es una estructura de datos que proviene del lenguaje de programación Lisp y sus dialectos, está compuesta por pares anidados y es la versión de Lisp de una lista enlazada. Su nombre proviene de la función `cons` (abreviatura de _función constructora_) en Lisp que construye un nuevo par a partir de sus dos argumentos. Al llamar a `cons` en un par que consta de un valor y otro par, podemos construir listas cons compuestas por pares recursivos.

Por ejemplo, aquí está una representación en pseudocódigo de una lista cons que contiene la lista `1, 2, 3` con cada par en paréntesis:

```rust
(1, (2, (3, Nil)))
```

Cada elemento en una lista cons contiene dos elementos: el valor del elemento actual y el siguiente elemento. El último elemento de la lista contiene solo un valor llamado `Nil` sin un siguiente elemento. Una lista cons se produce llamando recursivamente a la función `cons`. El nombre canónico para denotar el caso base de la recursividad es `Nil`. Tenga en cuenta que esto no es lo mismo que el concepto de "nulo" o "nil" del Capítulo 6, que es un valor inválido o ausente.

La lista cons no es una estructura de datos comúnmente utilizada en Rust. En la mayoría de los casos, cuando tienes una lista de elementos en Rust, `Vec<T>` es una mejor opción para usar. Otros tipos de datos recursivos más complejos _son_ útiles en diversas situaciones, pero al comenzar con la lista cons en este capítulo, podemos explorar cómo las cajas nos permiten definir un tipo de datos recursivo sin muchas distracciones.

La Lista 15-2 contiene una definición de enumerado para una lista cons. Tenga en cuenta que este código no se compilará todavía porque el tipo `List` no tiene un tamaño conocido, lo que demostraremos.

Nombre de archivo: `src/main.rs`

```rust
enum List {
    Cons(i32, List),
    Nil,
}
```

Lista 15-2: El primer intento de definir un enumerado para representar una estructura de datos de lista cons de valores de `i32`

> Nota: Estamos implementando una lista cons que solo contiene valores de `i32` con fines de este ejemplo. Podríamos haberla implementado usando genéricos, como discutimos en el Capítulo 10, para definir un tipo de lista cons que podría almacenar valores de cualquier tipo.

Usar el tipo `List` para almacenar la lista `1, 2, 3` se vería como el código de la Lista 15-3.

Nombre de archivo: `src/main.rs`

```rust
--snip--

use crate::List::{Cons, Nil};

fn main() {
    let list = Cons(1, Cons(2, Cons(3, Nil)));
}
```

Lista 15-3: Usando el enumerado `List` para almacenar la lista `1, 2, 3`

El primer valor `Cons` contiene `1` y otro valor de tipo `List`. Este valor de tipo `List` es otro valor `Cons` que contiene `2` y otro valor de tipo `List`. Este valor de tipo `List` es otro valor `Cons` que contiene `3` y un valor de tipo `List`, que finalmente es `Nil`, la variante no recursiva que indica el final de la lista.

Si intentamos compilar el código de la Lista 15-3, obtenemos el error mostrado en la Lista 15-4.

```bash
error[E0072]: recursive type `List` has infinite size
 --> src/main.rs:1:1
  |
1 | enum List {
  | ^^^^^^^^^ recursive type has infinite size
2 |     Cons(i32, List),
  |               ---- recursive without indirection
  |
help: insert some indirection (e.g., a `Box`, `Rc`, or `&`) to make `List`
representable
  |
2 |     Cons(i32, Box<List>),
  |               ++++    +
```

Lista 15-4: El error que obtenemos al intentar definir un enumerado recursivo

El error muestra que este tipo "tiene un tamaño infinito". La razón es que hemos definido `List` con una variante que es recursiva: contiene directamente otro valor de sí mismo. Como resultado, Rust no puede determinar cuánto espacio necesita para almacenar un valor de tipo `List`. Vamos a analizar por qué obtenemos este error. Primero veremos cómo Rust decide cuánto espacio necesita para almacenar un valor de un tipo no recursivo.

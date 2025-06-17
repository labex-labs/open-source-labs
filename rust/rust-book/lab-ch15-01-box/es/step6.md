# Usando Box`<T>` para obtener un tipo recursivo con un tamaño conocido

Debido a que Rust no puede determinar cuánto espacio asignar para tipos definidos recursivamente, el compilador muestra un error con esta sugerencia útil:

    ayuda: insertar alguna indirección (por ejemplo, un `Box`, `Rc` o `&`) para que `List` sea representable
      |
    2 |     Cons(i32, Box<List>),
      |               ++++    +

En esta sugerencia, _indirección_ significa que en lugar de almacenar un valor directamente, debemos cambiar la estructura de datos para almacenar el valor indirectamente mediante el almacenamiento de un puntero al valor en lugar de hacerlo directamente.

Debido a que un `Box<T>` es un puntero, Rust siempre sabe cuánto espacio necesita un `Box<T>`: el tamaño de un puntero no cambia en función de la cantidad de datos a los que apunta. Esto significa que podemos poner un `Box<T>` dentro de la variante `Cons` en lugar de otro valor de tipo `List` directamente. El `Box<T>` apuntará al siguiente valor de tipo `List` que estará en el montón en lugar de estar dentro de la variante `Cons`. Conceptualmente, todavía tenemos una lista, creada con listas que contienen otras listas, pero esta implementación ahora es más como colocar los elementos uno al lado del otro en lugar de dentro de uno otro.

Podemos cambiar la definición del enumerado `List` en la Lista 15-2 y el uso del `List` en la Lista 15-3 al código de la Lista 15-5, que se compilará.

Nombre de archivo: `src/main.rs`

```rust
enum List {
    Cons(i32, Box<List>),
    Nil,
}

use crate::List::{Cons, Nil};

fn main() {
    let list = Cons(
        1,
        Box::new(Cons(
            2,
            Box::new(Cons(
                3,
                Box::new(Nil)
            ))
        ))
    );
}
```

Lista 15-5: Definición de `List` que utiliza `Box<T>` para tener un tamaño conocido

La variante `Cons` necesita el tamaño de un `i32` más el espacio para almacenar los datos del puntero de la caja. La variante `Nil` no almacena ningún valor, por lo que necesita menos espacio que la variante `Cons`. Ahora sabemos que cualquier valor de tipo `List` ocupará el tamaño de un `i32` más el tamaño de los datos del puntero de una caja. Al usar una caja, hemos roto la cadena infinita y recursiva, por lo que el compilador puede determinar el tamaño que necesita para almacenar un valor de tipo `List`. La Figura 15-2 muestra cómo se ve ahora la variante `Cons`.

Figura 15-2: Una `List` que no tiene un tamaño infinito, porque `Cons` contiene un `Box`

Las cajas solo proporcionan la indirección y la asignación de memoria en el montón; no tienen ninguna otra capacidad especial, como las que veremos con los otros tipos de punteros inteligentes. Tampoco tienen la sobrecarga de rendimiento que incurren estas capacidades especiales, por lo que pueden ser útiles en casos como la lista cons donde la indirección es la única característica que necesitamos. Veremos más casos de uso de cajas en el Capítulo 17.

El tipo `Box<T>` es un puntero inteligente porque implementa el trato `Deref`, que permite tratar los valores de `Box<T>` como referencias. Cuando un valor de `Box<T>` sale del ámbito, los datos del montón a los que apunta la caja también se limpian debido a la implementación del trato `Drop`. Estos dos tratados serán aún más importantes para la funcionalidad proporcionada por los otros tipos de punteros inteligentes que discutiremos en el resto de este capítulo. Exploremos estos dos tratados con más detalle.

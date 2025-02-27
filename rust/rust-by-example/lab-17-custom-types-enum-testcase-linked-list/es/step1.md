# Caso de prueba: lista enlazada

Una forma común de implementar una lista enlazada es a través de `enum`:

```rust
use crate::List::*;

enum List {
    // Cons: Estructura tupla que envuelve un elemento y un puntero al siguiente nodo
    Cons(u32, Box<List>),
    // Nil: Un nodo que significa el final de la lista enlazada
    Nil,
}

// Los métodos se pueden adjuntar a un enum
impl List {
    // Crea una lista vacía
    fn new() -> List {
        // `Nil` tiene tipo `List`
        Nil
    }

    // Consume una lista y devuelve la misma lista con un nuevo elemento al principio
    fn prepend(self, elem: u32) -> List {
        // `Cons` también tiene tipo List
        Cons(elem, Box::new(self))
    }

    // Devuelve la longitud de la lista
    fn len(&self) -> u32 {
        // `self` debe ser coincidido, porque el comportamiento de este método
        // depende de la variante de `self`
        // `self` tiene tipo `&List`, y `*self` tiene tipo `List`, coincidir en un
        // tipo concreto `T` es preferible sobre una coincidencia en una referencia `&T`
        // después de Rust 2018 también puede usar self aquí y tail (sin ref) a continuación,
        // rust inferirá &s y ref tail.
        // Ver https://doc.rust-lang.org/edition-guide/rust-2018/ownership-and-lifetimes/default-match-bindings.html
        match *self {
            // No se puede tomar posesión de la cola, porque `self` está prestada;
            // en cambio, tome una referencia a la cola
            Cons(_, ref tail) => 1 + tail.len(),
            // Caso base: Una lista vacía tiene longitud cero
            Nil => 0
        }
    }

    // Devuelve la representación de la lista como una cadena (asignada en el heap)
    fn stringify(&self) -> String {
        match *self {
            Cons(head, ref tail) => {
                // `format!` es similar a `print!`, pero devuelve una cadena
                // asignada en el heap en lugar de imprimir en la consola
                format!("{}, {}", head, tail.stringify())
            },
            Nil => {
                format!("Nil")
            },
        }
    }
}

fn main() {
    // Crea una lista enlazada vacía
    let mut list = List::new();

    // Agrega algunos elementos al principio
    list = list.prepend(1);
    list = list.prepend(2);
    list = list.prepend(3);

    // Muestra el estado final de la lista
    println!("la lista enlazada tiene longitud: {}", list.len());
    println!("{}", list.stringify());
}
```

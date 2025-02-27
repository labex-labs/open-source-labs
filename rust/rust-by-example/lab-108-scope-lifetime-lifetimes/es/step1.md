# Lifetimes

Un _lifetime_ es una construcción del compilador (o más específicamente, su _borrow checker_) que se utiliza para garantizar que todos los préstamos son válidos. Específicamente, el lifetime de una variable comienza cuando se crea y termina cuando se destruye. Si bien los lifetimes y los ámbitos a menudo se mencionan juntos, no son lo mismo.

Tomemos, por ejemplo, el caso en el que prestamos una variable a través de `&`. El préstamo tiene un lifetime que se determina por donde se declara. Como resultado, el préstamo es válido siempre y cuando termine antes de que el prestamista sea destruido. Sin embargo, el ámbito del préstamo se determina por donde se utiliza la referencia.

En el siguiente ejemplo y en el resto de esta sección, veremos cómo los lifetimes se relacionan con los ámbitos, así como cómo difieren los dos.

```rust
// Los lifetimes se anotan a continuación con líneas que indican la creación
// y la destrucción de cada variable.
// `i` tiene el lifetime más largo porque su ámbito encierra por completo
// tanto `borrow1` como `borrow2`. La duración de `borrow1` en comparación
// con `borrow2` es irrelevante ya que son disjuntos.
fn main() {
    let i = 3; // El lifetime para `i` comienza. ────────────────┐
    //                                                     │
    { //                                                   │
        let borrow1 = &i; // El lifetime de `borrow1` comienza. ──┐│
        //                                                ││
        println!("borrow1: {}", borrow1); //              ││
    } // El lifetime de `borrow1` termina. ─────────────────────────┘│
    //                                                     │
    //                                                     │
    { //                                                   │
        let borrow2 = &i; // El lifetime de `borrow2` comienza. ──┐│
        //                                                ││
        println!("borrow2: {}", borrow2); //              ││
    } // El lifetime de `borrow2` termina. ─────────────────────────┘│
    //                                                     │
}   // El lifetime termina. ─────────────────────────────────────┘
```

Tenga en cuenta que no se le asignan nombres o tipos para etiquetar los lifetimes. Esto restringe cómo se podrán utilizar los lifetimes, como veremos.

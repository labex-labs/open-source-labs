# Verwenden von `Box<T>` um einen rekursiven Typ mit bekannter Größe zu erhalten

Da Rust nicht herausfinden kann, wie viel Speicher für rekursiv definierte Typen zuzuweisen ist, gibt der Compiler einen Fehler mit diesem hilfreichen Tipp:

    help: insert some indirection (e.g., a `Box`, `Rc`, or `&`) to make `List`
    representable
      |
    2 |     Cons(i32, Box<List>),
      |               ++++    +

In diesem Tipp bedeutet _Indirektion_, dass wir statt eines Werts direkt zu speichern die Datenstruktur ändern sollten, um den Wert indirekt zu speichern, indem wir einen Zeiger auf den Wert speichern.

Da eine `Box<T>` ein Zeiger ist, weiß Rust immer, wie viel Speicher eine `Box<T>` benötigt: Die Größe eines Zeigers ändert sich nicht aufgrund der Menge der Daten, auf die er zeigt. Dies bedeutet, dass wir eine `Box<T>` in der `Cons`-Variante platzieren können, anstatt direkt einen anderen `List`-Wert. Die `Box<T>` wird auf den nächsten `List`-Wert zeigen, der auf dem Heap sein wird, anstatt innerhalb der `Cons`-Variante. Konzeptuell haben wir immer noch eine Liste, erstellt mit Listen, die andere Listen enthalten, aber diese Implementierung ist jetzt eher wie das Platzieren der Elemente nebeneinander, anstatt ineinander.

Wir können die Definition des `List`-Enums in Listing 15-2 und die Verwendung von `List` in Listing 15-3 in den Code in Listing 15-5 ändern, der kompilieren wird.

Dateiname: `src/main.rs`

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

Listing 15-5: Definition von `List`, die `Box<T>` verwendet, um eine bekannte Größe zu haben

Die `Cons`-Variante benötigt die Größe eines `i32` plus den Speicherplatz, um die Zeigerdaten der Box zu speichern. Die `Nil`-Variante speichert keine Werte, daher benötigt sie weniger Speicher als die `Cons`-Variante. Wir wissen jetzt, dass jeder `List`-Wert die Größe eines `i32` plus die Größe der Zeigerdaten einer Box einnehmen wird. Indem wir eine Box verwenden, haben wir die unendliche, rekursive Kette unterbrochen, so dass der Compiler herausfinden kann, die Größe, die er benötigt, um einen `List`-Wert zu speichern. Abbildung 15-2 zeigt, wie die `Cons`-Variante jetzt aussieht.

Abbildung 15-2: Eine `List`, die nicht unendlich groß ist, weil `Cons` eine `Box` enthält

Boxen bieten nur die Indirektion und die Heap-Allokation; sie haben keine anderen speziellen Funktionen, wie die, die wir bei den anderen Smart-Pointer-Typen sehen werden. Sie haben auch keine der Leistungsminderung, die diese speziellen Funktionen verursachen, daher können sie in Fällen wie der Cons-Liste nützlich sein, wo die Indirektion die einzige Funktion ist, die wir benötigen. Wir werden in Kapitel 17 weitere Anwendungsfälle für Boxen betrachten.

Der `Box<T>`-Typ ist ein Smart-Pointer, weil er das `Deref`-Trait implementiert, was es ermöglicht, `Box<T>`-Werte wie Referenzen zu behandeln. Wenn ein `Box<T>`-Wert außer Gültigkeitsbereich gelangt, wird auch die Heap-Daten, auf die die Box zeigt, aufgrund der `Drop`-Trait-Implementierung bereinigt. Diese beiden Traits werden noch wichtiger für die Funktionalität der anderen Smart-Pointer-Typen sein, die wir im Rest dieses Kapitels diskutieren werden. Lassen Sie uns diese beiden Traits genauer untersuchen.

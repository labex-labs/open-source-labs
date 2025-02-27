# Weitere Informationen über die Cons-Liste

Eine _Cons-Liste_ ist eine Datenstruktur, die aus der Lisp-Programmiersprache und ihren Dialekten stammt, aus geschachtelten Paaren besteht und die Lisp-Version einer verketteten Liste ist. Ihr Name stammt von der `cons`-Funktion (Abkürzung für _konstruktierende Funktion_) in Lisp, die ein neues Paar aus ihren zwei Argumenten konstruiert. Indem wir `cons` auf ein Paar, das aus einem Wert und einem anderen Paar besteht, aufrufen, können wir Cons-Listen aus rekursiven Paaren konstruieren.

Zum Beispiel ist hier eine Pseudocode-Darstellung einer Cons-Liste, die die Liste `1, 2, 3` enthält, wobei jedes Paar in Klammern steht:

```rust
(1, (2, (3, Nil)))
```

Jedes Element in einer Cons-Liste enthält zwei Elemente: den Wert des aktuellen Elements und das nächste Element. Das letzte Element in der Liste enthält nur einen Wert namens `Nil` ohne ein nächstes Element. Eine Cons-Liste wird durch rekursives Aufrufen der `cons`-Funktion erzeugt. Der kanonische Name, um den Basisfall der Rekursion zu bezeichnen, ist `Nil`. Beachten Sie, dass dies nicht dasselbe wie das "null" oder "nil"-Konzept im Kapitel 6 ist, das ein ungültiger oder fehlender Wert ist.

Die Cons-Liste ist keine häufig verwendete Datenstruktur in Rust. In den meisten Fällen, wenn Sie in Rust eine Liste von Elementen haben, ist `Vec<T>` eine bessere Wahl. Andere, komplexere rekursive Datentypen _sind_ in verschiedenen Situationen nützlich, aber indem wir in diesem Kapitel mit der Cons-Liste beginnen, können wir untersuchen, wie Boxen uns ermöglichen, einen rekursiven Datentyp zu definieren, ohne zu sehr abgelenkt zu werden.

Listing 15-2 enthält eine Enum-Definition für eine Cons-Liste. Beachten Sie, dass dieser Code noch nicht kompilieren wird, weil der `List`-Typ keine bekannte Größe hat, was wir demonstrieren werden.

Dateiname: `src/main.rs`

```rust
enum List {
    Cons(i32, List),
    Nil,
}
```

Listing 15-2: Der erste Versuch, eine Enum zu definieren, um eine Cons-Listen-Datenstruktur von `i32`-Werten darzustellen

> Hinweis: Wir implementieren eine Cons-Liste, die nur `i32`-Werte enthält, zum Zweck dieses Beispiels. Wir hätten es auch mit Generics implementieren können, wie wir im Kapitel 10 diskutiert haben, um einen Cons-Liste-Typ zu definieren, der Werte beliebigen Typs speichern kann.

Wenn wir den `List`-Typ verwenden, um die Liste `1, 2, 3` zu speichern, würde es wie der Code in Listing 15-3 aussehen.

Dateiname: `src/main.rs`

```rust
--snip--

use crate::List::{Cons, Nil};

fn main() {
    let list = Cons(1, Cons(2, Cons(3, Nil)));
}
```

Listing 15-3: Verwenden der `List`-Enum, um die Liste `1, 2, 3` zu speichern

Der erste `Cons`-Wert enthält `1` und einen anderen `List`-Wert. Dieser `List`-Wert ist ein weiterer `Cons`-Wert, der `2` und einen anderen `List`-Wert enthält. Dieser `List`-Wert ist noch ein weiterer `Cons`-Wert, der `3` und einen `List`-Wert enthält, der schließlich `Nil` ist, die nicht-rekursive Variante, die das Ende der Liste signalisiert.

Wenn wir versuchen, den Code in Listing 15-3 zu kompilieren, erhalten wir den Fehler, der in Listing 15-4 gezeigt wird.

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

Listing 15-4: Der Fehler, den wir erhalten, wenn wir versuchen, eine rekursive Enum zu definieren

Der Fehler zeigt an, dass dieser Typ "unendliche Größe hat". Der Grund ist, dass wir `List` mit einer Variante definiert haben, die rekursiv ist: sie enthält direkt einen anderen Wert von sich selbst. Folglich kann Rust nicht herausfinden, wie viel Speicher er für einen `List`-Wert benötigt. Lasst uns die Gründe für diesen Fehler aufteilen. Zunächst betrachten wir, wie Rust entscheidet, wie viel Speicher er für einen Wert eines nicht-rekursiven Typs benötigt.

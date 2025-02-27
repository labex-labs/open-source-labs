# Das Teilen von Daten mit Rc`<T>`{=html}

Lassen Sie uns zurückkehren zu unserem Beispiel mit der Cons-Liste in Listing 15-5. Erinnern Sie sich, dass wir es mit `Box<T>` definiert haben. Dieses Mal werden wir zwei Listen erstellen, die beide die Eigentumsgewalt über eine dritte Liste teilen. Konzeptionell sieht dies ähnlich wie in Abbildung 15-3 aus.

Abbildung 15-3: Zwei Listen, `b` und `c`, teilen die Eigentumsgewalt über eine dritte Liste, `a`

Wir werden die Liste `a` erstellen, die `5` und dann `10` enthält. Dann werden wir zwei weitere Listen erstellen: `b`, die mit `3` beginnt, und `c`, die mit `4` beginnt. Beide Listen `b` und `c` werden dann fortfahren mit der ersten Liste `a`, die `5` und `10` enthält. Mit anderen Worten, beide Listen werden die erste Liste, die `5` und `10` enthält, teilen.

Versuchen, dieses Szenario mit unserer Definition von `List` mit `Box<T>` umzusetzen, wird nicht funktionieren, wie in Listing 15-17 gezeigt.

Dateiname: `src/main.rs`

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

Listing 15-17: Demonstration, dass wir nicht zwei Listen mit `Box<T>` haben dürfen, die versuchen, die Eigentumsgewalt über eine dritte Liste zu teilen

Wenn wir diesen Code kompilieren, erhalten wir diesen Fehler:

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

Die `Cons`-Varianten besitzen die Daten, die sie enthalten, also wenn wir die Liste `b` erstellen \[1\], wird `a` in `b` bewegt und `b` besitzt `a`. Dann, wenn wir `a` erneut verwenden möchten, wenn wir `c` erstellen \[2\], dürfen wir es nicht, weil `a` bereits bewegt wurde.

Wir könnten die Definition von `Cons` ändern, um Referenzen zu halten, aber dann müssten wir Lebenszeitparameter angeben. Indem wir Lebenszeitparameter angeben, würden wir angeben, dass jedes Element in der Liste mindestens so lange existiert wie die gesamte Liste. Dies ist der Fall für die Elemente und Listen in Listing 15-17, aber nicht in jedem Szenario.

Stattdessen werden wir unsere Definition von `List` ändern, um `Rc<T>` anstelle von `Box<T>` zu verwenden, wie in Listing 15-18 gezeigt. Jede `Cons`-Variante wird jetzt einen Wert und einen `Rc<T>` enthalten, der auf eine `List` zeigt. Wenn wir `b` erstellen, werden wir statt der Eigentumsgewalt über `a` die `Rc<List>` klonen, die `a` hält, wodurch die Anzahl der Referenzen von eins auf zwei erhöht wird und `a` und `b` die Eigentumsgewalt über die Daten in dieser `Rc<List>` teilen. Wir werden `a` auch beim Erstellen von `c` klonen, was die Anzahl der Referenzen von zwei auf drei erhöht. Jedes Mal, wenn wir `Rc::clone` aufrufen, wird der Referenzzähler für die Daten innerhalb der `Rc<List>` erhöht, und die Daten werden nicht bereinigt, es sei denn, es gibt keine Referenzen mehr auf sie.

Dateiname: `src/main.rs`

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

Listing 15-18: Eine Definition von `List`, die `Rc<T>` verwendet

Wir müssen einen `use`-Befehl hinzufügen, um `Rc<T>` in den Gültigkeitsbereich zu bringen \[1\], da es nicht im Präambel ist. In `main` erstellen wir die Liste, die `5` und `10` enthält, und speichern sie in einer neuen `Rc<List>` in `a` \[2\]. Dann, wenn wir `b` \[3\] und `c` \[4\] erstellen, rufen wir die `Rc::clone`-Funktion auf und übergeben einen Verweis auf die `Rc<List>` in `a` als Argument.

Wir hätten `a.clone()` aufrufen können, anstatt `Rc::clone(&a)`, aber die Konvention in Rust ist, in diesem Fall `Rc::clone` zu verwenden. Die Implementierung von `Rc::clone` macht keine Tiefe-Kopie aller Daten, wie die Implementierungen von `clone` der meisten Typen es tun. Der Aufruf von `Rc::clone` erhöht nur den Referenzzähler, was nicht viel Zeit benötigt. Tiefe-Kopien von Daten können viel Zeit in Anspruch nehmen. Indem wir `Rc::clone` für die Referenzzählung verwenden, können wir zwischen den Tiefe-Kopie-Art von Klonen und den Klonen, die den Referenzzähler erhöhen, visuell unterscheiden. Wenn wir nach Leistungsproblemen im Code suchen, müssen wir nur die Tiefe-Kopie-Klone berücksichtigen und können Aufrufe von `Rc::clone` ignorieren.

# Ein Referenzzyklus erstellen

Schauen wir uns an, wie ein Referenzzyklus auftreten kann und wie man ihn vermeiden kann. Wir beginnen mit der Definition der `List`-Enumeration und einer `tail`-Methode in Listing 15-25.

Dateiname: `src/main.rs`

```rust
use crate::List::{Cons, Nil};
use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug)]
enum List {
  1 Cons(i32, RefCell<Rc<List>>),
    Nil,
}

impl List {
  2 fn tail(&self) -> Option<&RefCell<Rc<List>>> {
        match self {
            Cons(_, item) => Some(item),
            Nil => None,
        }
    }
}
```

Listing 15-25: Eine Definition einer Cons-Liste, die eine `RefCell<T>` enthält, um das zu verändern, auf das eine `Cons`-Variante zeigt

Wir verwenden eine andere Variation der `List`-Definition aus Listing 15-5. Das zweite Element in der `Cons`-Variante ist jetzt `RefCell<Rc<List>>` \[1\], was bedeutet, dass wir statt der Möglichkeit, den `i32`-Wert zu verändern, wie wir es in Listing 15-24 getan haben, den `List`-Wert verändern möchten, auf den eine `Cons`-Variante zeigt. Wir fügen auch eine `tail`-Methode hinzu \[2\], um es uns bequem zu machen, auf das zweite Element zuzugreifen, wenn wir eine `Cons`-Variante haben.

In Listing 15-26 fügen wir eine `main`-Funktion hinzu, die die Definitionen in Listing 15-25 verwendet. Dieser Code erstellt eine Liste in `a` und eine Liste in `b`, die auf die Liste in `a` zeigt. Anschließend ändert er die Liste in `a`, sodass sie auf `b` zeigt, was einen Referenzzyklus erzeugt. Es gibt `println!`-Anweisungen dazwischen, um anzuzeigen, was die Referenzzählungen zu verschiedenen Punkten in diesem Prozess sind.

Dateiname: `src/main.rs`

```rust
fn main() {
  1 let a = Rc::new(Cons(5, RefCell::new(Rc::new(Nil))));

    println!("a initial rc count = {}", Rc::strong_count(&a));
    println!("a next item = {:?}", a.tail());

  2 let b = Rc::new(Cons(10, RefCell::new(Rc::clone(&a))));

    println!(
        "a rc count after b creation = {}",
        Rc::strong_count(&a)
    );
    println!("b initial rc count = {}", Rc::strong_count(&b));
    println!("b next item = {:?}", b.tail());

  3 if let Some(link) = a.tail() {
      4 *link.borrow_mut() = Rc::clone(&b);
    }

    println!(
        "b rc count after changing a = {}",
        Rc::strong_count(&b)
    );
    println!(
        "a rc count after changing a = {}",
        Rc::strong_count(&a)
    );

    // Entkommentieren Sie die nächste Zeile, um zu sehen, dass wir einen Zyklus haben;
    // es wird den Stack überlaufen
    // println!("a next item = {:?}", a.tail());
}
```

Listing 15-26: Erstellen eines Referenzzyklus von zwei `List`-Werten, die sich aufeinander verweisen

Wir erstellen eine `Rc<List>`-Instanz, die einen `List`-Wert in der Variable `a` enthält, mit einer initialen Liste von `5, Nil` \[1\]. Anschließend erstellen wir eine `Rc<List>`-Instanz, die einen anderen `List`-Wert in der Variable `b` enthält, der den Wert `10` enthält und auf die Liste in `a` zeigt \[2\].

Wir ändern `a`, sodass es auf `b` statt auf `Nil` zeigt, was einen Zyklus erzeugt. Wir tun das, indem wir die `tail`-Methode verwenden, um auf die `RefCell<Rc<List>>` in `a` zu verweisen, die wir in die Variable `link` legen \[3\]. Anschließend verwenden wir die `borrow_mut`-Methode auf der `RefCell<Rc<List>>`, um den Wert darin von einer `Rc<List>`, die einen `Nil`-Wert enthält, zu einer `Rc<List>` in `b` zu ändern \[4\].

Wenn wir diesen Code ausführen und die letzte `println!`-Anweisung momentan kommentiert lassen, erhalten wir diese Ausgabe:

    a initial rc count = 1
    a next item = Some(RefCell { value: Nil })
    a rc count after b creation = 2
    b initial rc count = 1
    b next item = Some(RefCell { value: Cons(5, RefCell { value: Nil }) })
    b rc count after changing a = 2
    a rc count after changing a = 2

Die Referenzzählung der `Rc<List>`-Instanzen in sowohl `a` als auch `b` ist 2, nachdem wir die Liste in `a` geändert haben, sodass sie auf `b` zeigt. Am Ende von `main` verliert Rust die Variable `b`, was die Referenzzählung der `b` `Rc<List>`-Instanz von 2 auf 1 verringert. Der Arbeitsspeicher, den `Rc<List>` auf dem Heap hat, wird zu diesem Zeitpunkt nicht gelöscht, da seine Referenzzählung 1 und nicht 0 ist. Dann verliert Rust `a`, was auch die Referenzzählung der `a` `Rc<List>`-Instanz von 2 auf 1 verringert. Der Arbeitsspeicher dieser Instanz kann ebenfalls nicht gelöscht werden, da die andere `Rc<List>`-Instanz immer noch auf sie verweist. Der für die Liste zugewiesene Arbeitsspeicher bleibt für immer ungesammelt. Um diesen Referenzzyklus zu visualisieren, haben wir ein Diagramm in Abbildung 15-4 erstellt.

Abbildung 15-4: Ein Referenzzyklus von Listen `a` und `b`, die sich aufeinander verweisen

Wenn Sie die letzte `println!`-Anweisung entkommentieren und das Programm ausführen, wird Rust versuchen, diesen Zyklus mit `a` auf `b` auf `a` usw. anzuzeigen, bis der Stack überläuft.

Im Vergleich zu einem realen Programm sind die Folgen des Erstellens eines Referenzzyklus in diesem Beispiel nicht sehr schlimm: Kurz nachdem wir den Referenzzyklus erstellt haben, endet das Programm. Wenn jedoch ein komplexeres Programm in einem Zyklus viel Arbeitsspeicher allokiert und ihn lange Zeit hält, würde das Programm mehr Arbeitsspeicher verwenden, als es benötigt, und könnte das System überlasten, was dazu führen würde, dass es den verfügbaren Arbeitsspeicher erschöpft.

Das Erstellen von Referenzzyklen ist nicht leicht, aber es ist auch nicht unmöglich. Wenn Sie `RefCell<T>`-Werte haben, die `Rc<T>`-Werte enthalten oder ähnliche geschachtelte Kombinationen von Typen mit innerer Veränderbarkeit und Referenzzählung, müssen Sie sicherstellen, dass Sie keine Zyklen erzeugen; Sie können nicht darauf verlassen, dass Rust sie fängt. Das Erstellen eines Referenzzyklus wäre ein logischer Fehler in Ihrem Programm, den Sie mit automatisierten Tests, Code Reviews und anderen Softwareentwicklungspraktiken minimieren sollten.

Eine andere Möglichkeit, um Referenzzyklen zu vermeiden, besteht darin, Ihre Datenstrukturen umzuorganisieren, sodass einige Referenzen die Eigentumsbeziehung ausdrücken und einige Referenzen dies nicht tun. Dadurch können Sie Zyklen aus einigen Eigentumsbeziehungen und einigen Nicht-Eigentumsbeziehungen bilden, und nur die Eigentumsbeziehungen beeinflussen, ob ein Wert gelöscht werden kann. In Listing 15-25 möchten wir immer, dass `Cons`-Varianten ihre Liste besitzen, sodass eine Umorganisation der Datenstruktur nicht möglich ist. Schauen wir uns ein Beispiel mit Graphen aus Elternknoten und Kindknoten an, um zu sehen, wann Nicht-Eigentumsbeziehungen eine geeignete Möglichkeit sind, um Referenzzyklen zu vermeiden.

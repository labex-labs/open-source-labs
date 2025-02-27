# Visualisierung von Änderungen an strong_count und weak_count

Schauen wir uns an, wie sich die `strong_count`- und `weak_count`-Werte der `Rc<Node>`-Instanzen ändern, indem wir einen neuen inneren Bereich erstellen und das Erstellen von `branch` in diesen Bereich verschieben. Dadurch können wir sehen, was passiert, wenn `branch` erstellt wird und dann gelöscht wird, wenn es außerhalb des Bereichs geht. Die Änderungen sind in Listing 15-29 gezeigt.

Dateiname: `src/main.rs`

```rust
fn main() {
    let leaf = Rc::new(Node {
        value: 3,
        parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![]),
    });

  1 println!(
        "leaf strong = {}, weak = {}",
        Rc::strong_count(&leaf),
        Rc::weak_count(&leaf),
    );

  2 {
        let branch = Rc::new(Node {
            value: 5,
            parent: RefCell::new(Weak::new()),
            children: RefCell::new(vec![Rc::clone(&leaf)]),
        });

        *leaf.parent.borrow_mut() = Rc::downgrade(&branch);

      3 println!(
            "branch strong = {}, weak = {}",
            Rc::strong_count(&branch),
            Rc::weak_count(&branch),
        );

      4 println!(
            "leaf strong = {}, weak = {}",
            Rc::strong_count(&leaf),
            Rc::weak_count(&leaf),
        );
  5 }

  6 println!(
        "leaf parent = {:?}",
        leaf.parent.borrow().upgrade()
    );
  7 println!(
        "leaf strong = {}, weak = {}",
        Rc::strong_count(&leaf),
        Rc::weak_count(&leaf),
    );
}
```

Listing 15-29: Erstellen von `branch` in einem inneren Bereich und Untersuchung von starken und schwachen Referenzzählungen

Nachdem `leaf` erstellt wurde, hat seine `Rc<Node>` eine starke Referenzzählung von 1 und eine schwache Referenzzählung von 0 \[1\]. Im inneren Bereich \[2\] erstellen wir `branch` und verbinden es mit `leaf`. Zu diesem Zeitpunkt, wenn wir die Referenzzählungen ausgeben \[3\], hat die `Rc<Node>` in `branch` eine starke Referenzzählung von 1 und eine schwache Referenzzählung von 1 (für `leaf.parent`, das auf `branch` mit einer `Weak<Node>` verweist). Wenn wir die Referenzzählungen in `leaf` ausgeben \[4\], werden wir sehen, dass es eine starke Referenzzählung von 2 hat, da `branch` jetzt eine Kopie der `Rc<Node>` von `leaf` in `branch.children` gespeichert hat, aber immer noch eine schwache Referenzzählung von 0.

Wenn der innere Bereich endet \[5\], geht `branch` außerhalb des Bereichs und die starke Referenzzählung der `Rc<Node>` sinkt auf 0, sodass seine `Node` gelöscht wird. Die schwache Referenzzählung von 1 von `leaf.parent` hat keinen Einfluss darauf, ob die `Node` gelöscht wird oder nicht, daher erhalten wir keine Speicherlecks!

Wenn wir versuchen, auf den Elternteil von `leaf` nach dem Ende des Bereichs zuzugreifen, erhalten wir erneut `None` \[6\]. Am Ende des Programms \[7\] hat die `Rc<Node>` in `leaf` eine starke Referenzzählung von 1 und eine schwache Referenzzählung von 0, da die Variable `leaf` jetzt wieder die einzige Referenz auf die `Rc<Node>` ist.

Alle Logik, die die Referenzzählungen und das Löschen von Werten verwaltet, ist in `Rc<T>` und `Weak<T>` und deren Implementierungen des `Drop`-Traits eingebaut. Indem Sie in der Definition von `Node` angeben, dass die Beziehung von einem Kind zu seinem Elternteil eine `Weak<T>`-Referenz sein sollte, können Sie Elternknoten auf Kindknoten und umgekehrt verweisen, ohne einen Referenzzyklus und Speicherlecks zu erzeugen.

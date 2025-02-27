# Hinzufügen einer Referenz von einem Kind zu seinem Elternteil

Um das Kindknoten auf seinen Elternteil aufmerksam zu machen, müssen wir ein `parent`-Feld zu unserer `Node`-Strukturdefinition hinzufügen. Das Problem besteht darin, zu entscheiden, welchen Typ `parent` haben sollte. Wir wissen, dass es keinen `Rc<T>` enthalten kann, da dies einen Referenzzyklus mit `leaf.parent` auf `branch` und `branch.children` auf `leaf` erzeugen würde, was dazu führen würde, dass ihre `strong_count`-Werte niemals 0 werden.

Wenn wir die Beziehungen auf eine andere Weise betrachten, sollte ein Elternknoten seine Kinder besitzen: Wenn ein Elternknoten gelöscht wird, sollten auch seine Kindknoten gelöscht werden. Ein Kind sollte jedoch nicht seinen Elternteil besitzen: Wenn wir einen Kindknoten löschen, sollte der Elternteil weiterhin existieren. Dies ist ein Fall für schwache Referenzen!

Wir werden daher statt `Rc<T>` den Typ von `parent` auf `Weak<T>` setzen, speziell auf `RefCell<Weak<Node>>`. Unsere `Node`-Strukturdefinition sieht jetzt so aus:

Dateiname: `src/main.rs`

```rust
use std::cell::RefCell;
use std::rc::{Rc, Weak};

#[derive(Debug)]
struct Node {
    value: i32,
    parent: RefCell<Weak<Node>>,
    children: RefCell<Vec<Rc<Node>>>,
}
```

Ein Knoten wird in der Lage sein, auf seinen Elternknoten zu verweisen, aber er besitzt nicht seinen Elternteil. In Listing 15-28 aktualisieren wir `main`, um diese neue Definition zu verwenden, sodass der `leaf`-Knoten einen Weg hat, auf seinen Elternteil `branch` zu verweisen.

Dateiname: `src/main.rs`

```rust
fn main() {
    let leaf = Rc::new(Node {
        value: 3,
      1 parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![]),
    });

  2 println!(
        "leaf parent = {:?}",
        leaf.parent.borrow().upgrade()
    );

    let branch = Rc::new(Node {
        value: 5,
      3 parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![Rc::clone(&leaf)]),
    });

  4 *leaf.parent.borrow_mut() = Rc::downgrade(&branch);

  5 println!(
        "leaf parent = {:?}",
        leaf.parent.borrow().upgrade()
    );
}
```

Listing 15-28: Ein `leaf`-Knoten mit einer schwachen Referenz auf seinen Elternknoten, `branch`

Das Erstellen des `leaf`-Knotens sieht ähnlich aus wie in Listing 15-27, mit der Ausnahme des `parent`-Felds: `leaf` beginnt ohne Elternteil, daher erstellen wir eine neue, leere `Weak<Node>`-Referenzinstanz \[1\].

Zu diesem Zeitpunkt erhalten wir, wenn wir versuchen, eine Referenz auf den Elternteil von `leaf` mithilfe der `upgrade`-Methode zu erhalten, einen `None`-Wert. Wir sehen dies in der Ausgabe der ersten `println!`-Anweisung \[2\]:

```rust
leaf parent = None
```

Wenn wir den `branch`-Knoten erstellen, wird auch in seinem `parent`-Feld eine neue `Weak<Node>`-Referenz erstellt \[3\], da `branch` keinen Elternknoten hat. Wir haben immer noch `leaf` als eines der Kinder von `branch`. Sobald wir die `Node`-Instanz in `branch` haben, können wir `leaf` ändern, um ihm eine `Weak<Node>`-Referenz auf seinen Elternteil zu geben \[4\]. Wir verwenden die `borrow_mut`-Methode auf der `RefCell<Weak<Node>>` im `parent`-Feld von `leaf`, und dann verwenden wir die `Rc::downgrade`-Funktion, um eine `Weak<Node>`-Referenz auf `branch` aus der `Rc<Node>` in `branch` zu erstellen.

Wenn wir den Elternteil von `leaf` erneut ausgeben \[5\], erhalten wir diesmal eine `Some`-Variante, die `branch` enthält: jetzt kann `leaf` auf seinen Elternteil zugreifen! Wenn wir `leaf` ausgeben, vermeiden wir auch den Zyklus, der letztendlich in einem Stacküberlauf endete, wie wir es in Listing 15-26 hatten; die `Weak<Node>`-Referenzen werden als `(Weak)` ausgegeben:

    leaf parent = Some(Node { value: 5, parent: RefCell { value: (Weak) },
    children: RefCell { value: [Node { value: 3, parent: RefCell { value: (Weak) },
    children: RefCell { value: [] } }] } })

Das Fehlen einer unendlichen Ausgabe zeigt an, dass dieser Code keinen Referenzzyklus erzeugt hat. Wir können dies auch daran erkennen, indem wir uns die Werte ansehen, die wir von `Rc::strong_count` und `Rc::weak_count` erhalten.

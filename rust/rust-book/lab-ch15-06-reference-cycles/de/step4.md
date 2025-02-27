# Erstellen einer Baum-Datenstruktur: Ein Knoten mit Kindknoten

Zunächst werden wir einen Baum mit Knoten bauen, die über ihre Kindknoten wissen. Wir werden eine Struktur namens `Node` erstellen, die ihren eigenen `i32`-Wert sowie Referenzen auf ihre Kind-`Node`-Werte enthält:

Dateiname: `src/main.rs`

```rust
use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug)]
struct Node {
    value: i32,
    children: RefCell<Vec<Rc<Node>>>,
}
```

Wir möchten, dass ein `Node` seine Kinder besitzt und diese Eigentumsverteilung mit Variablen teilen kann, damit wir direkt auf jeden `Node` im Baum zugreifen können. Dazu definieren wir die `Vec<T>`-Elemente als Werte vom Typ `Rc<Node>`. Wir möchten auch ändern können, welche Knoten Kinder eines anderen Knotens sind, daher haben wir eine `RefCell<T>` in `children` um die `Vec<Rc<Node>>`.

Als nächstes werden wir unsere Strukturdefinition verwenden und eine `Node`-Instanz namens `leaf` mit dem Wert `3` und keinen Kindern sowie eine andere Instanz namens `branch` mit dem Wert `5` und `leaf` als einem seiner Kinder erstellen, wie in Listing 15-27 gezeigt.

Dateiname: `src/main.rs`

```rust
fn main() {
    let leaf = Rc::new(Node {
        value: 3,
        children: RefCell::new(vec![]),
    });

    let branch = Rc::new(Node {
        value: 5,
        children: RefCell::new(vec![Rc::clone(&leaf)]),
    });
}
```

Listing 15-27: Erstellen eines `leaf`-Knotens ohne Kinder und eines `branch`-Knotens mit `leaf` als einem seiner Kinder

Wir klonen die `Rc<Node>` in `leaf` und speichern sie in `branch`, was bedeutet, dass der `Node` in `leaf` jetzt zwei Besitzer hat: `leaf` und `branch`. Wir können von `branch` zu `leaf` über `branch.children` gelangen, aber es gibt keinen Weg, von `leaf` zu `branch` zu gelangen. Der Grund ist, dass `leaf` keine Referenz auf `branch` hat und nicht weiß, dass sie verwandt sind. Wir möchten, dass `leaf` weiß, dass `branch` sein Elternknoten ist. Wir werden das nächst tun.

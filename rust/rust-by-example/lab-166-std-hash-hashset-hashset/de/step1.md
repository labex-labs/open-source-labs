# HashSet

Denken Sie sich ein `HashSet` als eine `HashMap`, bei der wir uns nur um die Schlüssel kümmern ( `HashSet<T>` ist tatsächlich nur eine Umhüllung um `HashMap<T, ()>`).

"Was bringt das?" fragen Sie. "Ich könnte einfach die Schlüssel in einem `Vec` speichern."

Eine einzigartige Eigenschaft eines `HashSet` ist, dass gewährleistet ist, dass es keine doppelten Elemente enthält. Das ist das Vertragsverhältnis, das jede Mengen - Sammlung erfüllt. `HashSet` ist nur eine Implementierung. (siehe auch: `BTreeSet`)

Wenn Sie einen Wert einfügen, der bereits im `HashSet` vorhanden ist (d.h. der neue Wert ist gleich dem bestehenden und beide haben den gleichen Hash), dann wird der neue Wert den alten ersetzen.

Dies ist großartig, wenn Sie niemals mehr als eines von etwas haben möchten oder wenn Sie wissen möchten, ob Sie bereits etwas haben.

Aber Mengen können mehr leisten.

Mengen haben 4 primäre Operationen (alle folgenden Aufrufe geben einen Iterator zurück):

- `union`: erhalten Sie alle einzigartigen Elemente in beiden Mengen.

- `difference`: erhalten Sie alle Elemente, die in der ersten Menge, aber nicht in der zweiten Menge sind.

- `intersection`: erhalten Sie alle Elemente, die nur in _beiden_ Mengen sind.

- `symmetric_difference`: erhalten Sie alle Elemente, die in einer Menge oder der anderen sind, aber _nicht_ in beiden.

Versuchen Sie alle diese in folgendem Beispiel:

```rust
use std::collections::HashSet;

fn main() {
    let mut a: HashSet<i32> = vec![1i32, 2, 3].into_iter().collect();
    let mut b: HashSet<i32> = vec![2i32, 3, 4].into_iter().collect();

    assert!(a.insert(4));
    assert!(a.contains(&4));

    // `HashSet::insert()` gibt false zurück, wenn
    // bereits ein Wert vorhanden war.
    assert!(b.insert(4), "Wert 4 ist bereits in Menge B!");
    // FIXME ^ Kommentieren Sie diese Zeile aus

    b.insert(5);

    // Wenn der Elementtyp einer Sammlung `Debug` implementiert,
    // dann implementiert die Sammlung `Debug`.
    // Sie druckt normalerweise ihre Elemente im Format `[elem1, elem2,...]`
    println!("A: {:?}", a);
    println!("B: {:?}", b);

    // Druckt [1, 2, 3, 4, 5] in beliebiger Reihenfolge
    println!("Vereinigung: {:?}", a.union(&b).collect::<Vec<&i32>>());

    // Dies sollte [1] drucken
    println!("Differenz: {:?}", a.difference(&b).collect::<Vec<&i32>>());

    // Druckt [2, 3, 4] in beliebiger Reihenfolge.
    println!("Schnittmenge: {:?}", a.intersection(&b).collect::<Vec<&i32>>());

    // Druckt [1, 5]
    println!("Symmetrische Differenz: {:?}",
             a.symmetric_difference(&b).collect::<Vec<&i32>>());
}
```

(Beispiele sind aus der Dokumentation adaptiert.)

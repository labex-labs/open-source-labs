# Das Klonen von Rc`<T>` erhöht den Referenzzähler

Ändern wir unser funktionierendes Beispiel in Listing 15-18, so dass wir sehen können, wie sich die Referenzzähler ändern, wenn wir Referenzen auf die `Rc<List>` in `a` erstellen und fallen lassen.

In Listing 15-19 werden wir `main` ändern, sodass es einen inneren Gültigkeitsbereich um die Liste `c` hat; dann können wir sehen, wie sich die Referenzzähler ändert, wenn `c` außerhalb des Gültigkeitsbereichs fällt.

Dateiname: `src/main.rs`

```rust
--snip--

fn main() {
    let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
    println!(
        "count after creating a = {}",
        Rc::strong_count(&a)
    );
    let b = Cons(3, Rc::clone(&a));
    println!(
        "count after creating b = {}",
        Rc::strong_count(&a)
    );
    {
        let c = Cons(4, Rc::clone(&a));
        println!(
            "count after creating c = {}",
            Rc::strong_count(&a)
        );
    }
    println!(
        "count after c goes out of scope = {}",
        Rc::strong_count(&a)
    );
}
```

Listing 15-19: Ausgabe des Referenzzählers

An jeder Stelle im Programm, an der sich die Referenzzähler ändert, drucken wir die Referenzzähler, die wir erhalten, indem wir die `Rc::strong_count`-Funktion aufrufen. Diese Funktion heißt `strong_count` statt `count`, weil der Typ `Rc<T>` auch eine `weak_count` hat; wir werden sehen, wofür `weak_count` verwendet wird in "Verhinderung von Referenzzirkeln mit Weak`<T>`".

Dieser Code gibt Folgendes aus:

    count after creating a = 1
    count after creating b = 2
    count after creating c = 3
    count after c goes out of scope = 2

Wir können sehen, dass die `Rc<List>` in `a` einen anfänglichen Referenzzähler von 1 hat; dann erhöht sich der Zähler jedes Mal um 1, wenn wir `clone` aufrufen. Wenn `c` außerhalb des Gültigkeitsbereichs fällt, sinkt der Zähler um 1. Wir müssen keine Funktion aufrufen, um den Referenzzähler zu verringern, wie wir `Rc::clone` aufrufen müssen, um den Referenzzähler zu erhöhen: Die Implementierung des `Drop`-Traits verringert den Referenzzähler automatisch, wenn ein `Rc<T>`-Wert außerhalb des Gültigkeitsbereichs fällt.

Was wir in diesem Beispiel nicht sehen können, ist, dass wenn `b` und dann `a` am Ende von `main` außerhalb des Gültigkeitsbereichs fallen, der Zähler dann 0 ist und die `Rc<List>` vollständig bereinigt wird. Die Verwendung von `Rc<T>` ermöglicht es, dass ein einzelner Wert mehrere Besitzer hat, und der Zähler stellt sicher, dass der Wert solange gültig bleibt, wie irgendeiner der Besitzer noch existiert.

Über unveränderliche Referenzen ermöglicht `Rc<T>` es Ihnen, Daten zwischen mehreren Teilen Ihres Programms nur zum Lesen zu teilen. Wenn `Rc<T>` Ihnen auch mehrere veränderliche Referenzen erlauben würde, könnten Sie eine der in Kapitel 4 diskutierten Entleihregeln verletzen: mehrere veränderliche Entleihungen an die gleiche Stelle können zu Datenkonflikten und Inkonsistenzen führen. Aber das Ändern von Daten ist sehr nützlich! Im nächsten Abschnitt werden wir das Muster der inneren Veränderbarkeit und den Typ `RefCell<T>` diskutieren, den Sie in Verbindung mit einem `Rc<T>` verwenden können, um dieser Unveränderbarkeitsbeschränkung zu begegnen.

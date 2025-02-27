# Eigentum und Moves

Da Variablen sich um das Freigeben ihrer eigenen Ressourcen kümmern, **kann eine Ressource nur einen Besitzer haben**. Dadurch wird auch vermieden, dass Ressourcen mehrfach freigegeben werden. Beachten Sie, dass nicht alle Variablen Ressourcen besitzen (z.B. [Referenzen]).

Wenn Sie Zuweisungen durchführen (`let x = y`) oder Funktionsargumente per Wert übergeben (`foo(x)`), wird die _Eigentumsgewalt_ an die Ressourcen übertragen. In Rust-Sprache wird dies als _Move_ bezeichnet.

Nachdem die Ressourcen bewegt wurden, kann der vorherige Besitzer nicht mehr verwendet werden. Dadurch wird vermieden, dass fehlerhafte Zeiger erstellt werden.

```rust
// Diese Funktion erhält die Eigentumsgewalt an den auf dem Heap zugewiesenen Speicher
fn destroy_box(c: Box<i32>) {
    println!("Zerstöre eine Box, die enthält {}", c);

    // `c` wird zerstört und der Speicher freigegeben
}

fn main() {
    // _Stack_-zugewiesene Ganzzahl
    let x = 5u32;

    // *Kopiere* `x` in `y` - keine Ressourcen werden bewegt
    let y = x;

    // Beide Werte können unabhängig voneinander verwendet werden
    println!("x ist {}, und y ist {}", x, y);

    // `a` ist ein Zeiger auf eine _Heap_-zugewiesene Ganzzahl
    let a = Box::new(5i32);

    println!("a enthält: {}", a);

    // *Bewege* `a` in `b`
    let b = a;
    // Die Zeigeradresse von `a` wird in `b` kopiert (nicht die Daten).
    // Beide sind jetzt Zeiger auf die gleiche auf dem Heap zugewiesene Daten, aber
    // `b` besitzt sie jetzt.

    // Fehler! `a` kann die Daten nicht mehr zugreifen, da es die
    // Heap-Speicher nicht mehr besitzt
    //println!("a enthält: {}", a);
    // TODO ^ Versuchen Sie, diese Zeile auszulassen

    // Diese Funktion erhält die Eigentumsgewalt an den auf dem Heap zugewiesenen Speicher von `b`
    destroy_box(b);

    // Da der Heap-Speicher zu diesem Zeitpunkt bereits freigegeben wurde, würde diese Aktion
    // dazu führen, auf freien Speicher zu verweisen, was jedoch vom Compiler verboten ist
    // Fehler! Aus dem gleichen Grund wie der vorherige Fehler
    //println!("b enthält: {}", b);
    // TODO ^ Versuchen Sie, diese Zeile auszulassen
}
```

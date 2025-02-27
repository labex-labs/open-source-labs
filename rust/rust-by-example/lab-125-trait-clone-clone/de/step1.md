# Clone

Wenn es um Ressourcen geht, ist das Standardverhalten, sie während von Zuweisungen oder Funktionsaufrufen zu transferieren. Manchmal müssen wir jedoch auch eine Kopie der Ressource machen.

Das `Clone`-Trait hilft uns genau dabei. Am häufigsten können wir die von dem `Clone`-Trait definierte `.clone()`-Methode verwenden.

```rust
// Ein Unit-Struct ohne Ressourcen
#[derive(Debug, Clone, Copy)]
struct Unit;

// Ein Tuple-Struct mit Ressourcen, das das `Clone`-Trait implementiert
#[derive(Clone, Debug)]
struct Pair(Box<i32>, Box<i32>);

fn main() {
    // Instanziere `Unit`
    let unit = Unit;
    // Kopiere `Unit`, es gibt keine Ressourcen, die bewegt werden müssen
    let copied_unit = unit;

    // Beide `Unit`s können unabhängig voneinander verwendet werden
    println!("original: {:?}", unit);
    println!("Kopie: {:?}", copied_unit);

    // Instanziere `Pair`
    let pair = Pair(Box::new(1), Box::new(2));
    println!("original: {:?}", pair);

    // Bewege `pair` in `moved_pair`, bewegt die Ressourcen
    let moved_pair = pair;
    println!("bewegt: {:?}", moved_pair);

    // Fehler! `pair` hat seine Ressourcen verloren
    //println!("original: {:?}", pair);
    // TODO ^ Versuche, diese Zeile auszukommentieren

    // Klone `moved_pair` in `cloned_pair` (Ressourcen sind enthalten)
    let cloned_pair = moved_pair.clone();
    // Verwerfe das ursprüngliche Paar mit std::mem::drop
    drop(moved_pair);

    // Fehler! `moved_pair` wurde verworfen
    //println!("Kopie: {:?}", moved_pair);
    // TODO ^ Versuche, diese Zeile auszukommentieren

    // Das Ergebnis von.clone() kann immer noch verwendet werden!
    println!("Klon: {:?}", cloned_pair);
}
```

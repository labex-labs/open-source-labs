# Assoziierte Typen

Das Verwenden von "Assoziierten Typen" verbessert die Gesamtlesbarkeit des Codes, indem innere Typen lokal in ein Trait als _Ausgabetypen_ verschoben werden. Die Syntax für die `trait`-Definition lautet wie folgt:

```rust
// `A` und `B` werden im Trait über das `type`-Schlüsselwort definiert.
// (Hinweis: `type` hat in diesem Kontext eine andere Bedeutung als `type`,
// wenn es für Aliase verwendet wird).
trait Contains {
    type A;
    type B;

    // Aktualisierte Syntax, um generisch auf diese neuen Typen zu verweisen.
    fn contains(&self, _: &Self::A, _: &Self::B) -> bool;
}
```

Beachten Sie, dass Funktionen, die das `trait` `Contains` verwenden, überhaupt nicht mehr `A` oder `B` ausdrücken müssen:

```rust
// Ohne Verwendung assoziierter Typen
fn difference<A, B, C>(container: &C) -> i32 where
    C: Contains<A, B> {... }

// Mit Verwendung assoziierter Typen
fn difference<C: Contains>(container: &C) -> i32 {... }
```

Schreiben wir das Beispiel aus dem vorherigen Abschnitt mit assoziierten Typen um:

```rust
struct Container(i32, i32);

// Ein Trait, das überprüft, ob 2 Elemente im Container gespeichert sind.
// Ruft auch den ersten oder letzten Wert ab.
trait Contains {
    // Definieren Sie hier generische Typen, auf die Methoden zugreifen können.
    type A;
    type B;

    fn contains(&self, _: &Self::A, _: &Self::B) -> bool;
    fn first(&self) -> i32;
    fn last(&self) -> i32;
}

impl Contains for Container {
    // Geben Sie an, welche Typen `A` und `B` sind. Wenn der `input`-Typ
    // `Container(i32, i32)` ist, werden die `output`-Typen als `i32` und `i32`
    // bestimmt.
    type A = i32;
    type B = i32;

    // `&Self::A` und `&Self::B` sind hier ebenfalls gültig.
    fn contains(&self, number_1: &i32, number_2: &i32) -> bool {
        (&self.0 == number_1) && (&self.1 == number_2)
    }
    // Greifen Sie auf die erste Zahl zu.
    fn first(&self) -> i32 { self.0 }

    // Greifen Sie auf die letzte Zahl zu.
    fn last(&self) -> i32 { self.1 }
}

fn difference<C: Contains>(container: &C) -> i32 {
    container.last() - container.first()
}

fn main() {
    let number_1 = 3;
    let number_2 = 10;

    let container = Container(number_1, number_2);

    println!("Enthält der Container {} und {}: {}",
        &number_1, &number_2,
        container.contains(&number_1, &number_2));
    println!("Erste Zahl: {}", container.first());
    println!("Letzte Zahl: {}", container.last());

    println!("Der Unterschied ist: {}", difference(&container));
}
```

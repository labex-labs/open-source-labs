# Using Trait Bounds to Conditionally Implement Methods

Indem wir einen Trait Bound mit einem `impl`-Block verwenden, der generische Typparameter verwendet, können wir Methoden bedingt für Typen implementieren, die das angegebene Trait implementieren. Beispielsweise implementiert der Typ `Pair<T>` in Listing 10-15 immer die `new`-Funktion, um eine neue Instanz von `Pair<T>` zurückzugeben (denken Sie an "Defining Methods", dass `Self` ein Typalias für den Typ des `impl`-Blocks ist, was in diesem Fall `Pair<T>` ist). Aber im nächsten `impl`-Block implementiert `Pair<T>` nur die `cmp_display`-Methode, wenn sein innerer Typ `T` das `PartialOrd`-Trait implementiert, das das Vergleichen ermöglicht, _und_ das `Display`-Trait, das das Drucken ermöglicht.

Dateiname: `src/lib.rs`

```rust
use std::fmt::Display;

struct Pair<T> {
    x: T,
    y: T,
}

impl<T> Pair<T> {
    fn new(x: T, y: T) -> Self {
        Self { x, y }
    }
}

impl<T: Display + PartialOrd> Pair<T> {
    fn cmp_display(&self) {
        if self.x >= self.y {
            println!("The largest member is x = {}", self.x);
        } else {
            println!("The largest member is y = {}", self.y);
        }
    }
}
```

Listing 10-15: Bedingtes Implementieren von Methoden auf einem generischen Typ abhängig von Trait Bounds

Wir können auch bedingt ein Trait für jeden Typ implementieren, der ein anderes Trait implementiert. Implementierungen eines Traits für jeden Typ, der die Trait Bounds erfüllt, werden als _blanket implementations_ bezeichnet und werden in der Rust-Standardbibliothek weit verbreitet verwendet. Beispielsweise implementiert die Standardbibliothek das `ToString`-Trait für jeden Typ, der das `Display`-Trait implementiert. Der `impl`-Block in der Standardbibliothek sieht ähnlich wie dieser Code aus:

```rust
impl<T: Display> ToString for T {
    --snip--
}
```

Aufgrund dieser blanket implementation in der Standardbibliothek können wir die `to_string`-Methode, die durch das `ToString`-Trait definiert ist, auf jedem Typ aufrufen, der das `Display`-Trait implementiert. Beispielsweise können wir ganze Zahlen in ihre entsprechenden `String`-Werte umwandeln, wie dies hier geht, weil ganze Zahlen `Display` implementieren:

```rust
let s = 3.to_string();
```

Blanket Implementierungen erscheinen in der Dokumentation für das Trait im Abschnitt "Implementors".

Traits und Trait Bounds ermöglichen es uns, Code zu schreiben, der generische Typparameter verwendet, um die Duplizierung zu reduzieren, aber auch an den Compiler anzugeben, dass wir möchten, dass der generische Typ ein bestimmtes Verhalten hat. Der Compiler kann dann die Trait Bound-Informationen verwenden, um zu überprüfen, dass alle konkreten Typen, die mit unserem Code verwendet werden, das richtige Verhalten bieten. In dynamisch typisierten Sprachen würden wir bei der Ausführung eine Fehlermeldung erhalten, wenn wir eine Methode auf einem Typ aufrufen, der die Methode nicht definiert. Aber Rust verschiebt diese Fehler in die Kompilierzeit, sodass wir gezwungen sind, die Probleme zu beheben, bevor unser Code überhaupt ausgeführt werden kann. Darüber hinaus müssen wir keinen Code schreiben, der das Verhalten zur Laufzeit überprüft, weil wir es bereits zur Kompilierzeit überprüft haben. Dadurch wird die Leistung verbessert, ohne dass wir die Flexibilität der Generics aufgeben müssen.

# Testfall: List

Das Implementieren von `fmt::Display` für eine Struktur, bei der die Elemente sequentiell behandelt werden müssen, ist schwierig. Das Problem ist, dass jedes `write!` ein `fmt::Result` generiert. Die richtige Behandlung hiervon erfordert die Bearbeitung _aller_ Ergebnisse. Rust stellt genau zu diesem Zweck den `?`-Operator zur Verfügung.

Das Verwenden von `?` auf `write!` sieht so aus:

```rust
// Versuche `write!`, um zu sehen, ob es einen Fehler gibt. Wenn es einen Fehler gibt,
// gebe den Fehler zurück. Andernfalls fahre fort.
write!(f, "{}", value)?;
```

Mit `?` verfügbar ist die Implementierung von `fmt::Display` für ein `Vec` recht einfach:

```rust
use std::fmt; // Importiere das `fmt`-Modul.

// Definiere eine Struktur namens `List`, die ein `Vec` enthält.
struct List(Vec<i32>);

impl fmt::Display for List {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Extrahiere den Wert mithilfe von Tupel-Indexierung
        // und erstelle eine Referenz auf `vec`.
        let vec = &self.0;

        write!(f, "[")?;

        // Iteriere über `v` in `vec`, während du die Iterationszählung in `count`
        // aufzählst.
        for (count, v) in vec.iter().enumerate() {
            // Für jedes Element außer dem ersten füge einen Komma hinzu.
            // Verwende den?-Operator, um bei Fehlern zurückzugeben.
            if count!= 0 { write!(f, ", ")?; }
            write!(f, "{}", v)?;
        }

        // Schließe die geöffnete Klammer und gebe einen fmt::Result-Wert zurück.
        write!(f, "]")
    }
}

fn main() {
    let v = List(vec![1, 2, 3]);
    println!("{}", v);
}
```

## Aktivität

Versuche das Programm so zu ändern, dass auch der Index jedes Elements im Vektor ausgegeben wird. Die neue Ausgabe sollte so aussehen:

```rust
[0: 1, 1: 2, 2: 3]
```

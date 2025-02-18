# Erstellen einer neuen Hash-Tabelle (Hash Map)

Eine Möglichkeit, eine leere Hash-Tabelle zu erstellen, besteht darin, `new` zu verwenden und Elemente mit `insert` hinzuzufügen. In Listing 8-20 verfolgen wir die Punktzahlen von zwei Mannschaften, deren Namen _Blue_ und _Yellow_ sind. Die Blue-Mannschaft beginnt mit 10 Punkten, und die Yellow-Mannschaft beginnt mit 50 Punkten.

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);
```

Listing 8-20: Erstellen einer neuen Hash-Tabelle und Einfügen einiger Schlüssel und Werte

Beachten Sie, dass wir zunächst `HashMap` aus dem Abschnitt der Sammlungen (Collections) der Standardbibliothek `use` müssen. Von unseren drei gängigen Sammlungen wird diese am wenigsten verwendet, daher ist sie nicht in den Funktionen enthalten, die automatisch im Präambel in den Geltungsbereich gebracht werden. Hash-Tabellen werden auch von der Standardbibliothek weniger unterstützt; es gibt beispielsweise keine integrierte Makro, um sie zu konstruieren.

Genau wie Vektoren speichern Hash-Tabellen ihre Daten auf dem Heap. Diese `HashMap` hat Schlüssel vom Typ `String` und Werte vom Typ `i32`. Wie Vektoren sind Hash-Tabellen homogen: Alle Schlüssel müssen denselben Typ haben, und alle Werte müssen denselben Typ haben.

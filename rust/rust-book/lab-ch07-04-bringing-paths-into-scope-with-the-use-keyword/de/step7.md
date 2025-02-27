# Der Glob-Operator

Wenn wir alle öffentlichen Elemente, die in einem Pfad definiert sind, in den Gültigkeitsbereich bringen möchten, können wir diesen Pfad angeben, gefolgt vom `*`-Glob-Operator:

```rust
use std::collections::*;
```

Diese `use`-Anweisung bringt alle öffentlichen Elemente, die in `std::collections` definiert sind, in den aktuellen Gültigkeitsbereich. Seien Sie bei der Verwendung des Glob-Operators vorsichtig! Der Glob-Operator kann es schwieriger machen, zu erkennen, welche Namen im Gültigkeitsbereich sind und wo ein in Ihrem Programm verwendeter Name definiert wurde.

Der Glob-Operator wird häufig bei Tests verwendet, um alles, was getestet werden soll, in das `tests`-Modul zu bringen; wir werden darüber in "How to Write Tests" sprechen. Der Glob-Operator wird auch manchmal als Teil des Präambel-Musters verwendet; siehe die Standardbibliotheksdokumentation für weitere Informationen zu diesem Muster.

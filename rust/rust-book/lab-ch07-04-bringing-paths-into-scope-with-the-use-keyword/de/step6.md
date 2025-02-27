# Verwendung geschachtelter Pfade, um lange `use`-Listen zu vereinfachen

Wenn wir mehrere Elemente verwenden, die in demselben Crate oder demselben Modul definiert sind, kann das Auflisten jedes Elements auf einer eigenen Zeile viel vertikalen Platz in unseren Dateien beanspruchen. Beispielsweise bringen diese beiden `use`-Anweisungen, die wir im Zahlenratespiel in Listing 2-4 hatten, Elemente aus `std` in den Gültigkeitsbereich:

Dateiname: `src/main.rs`

```rust
--snip--
use std::cmp::Ordering;
use std::io;
--snip--
```

Stattdessen können wir geschachtelte Pfade verwenden, um die gleichen Elemente in einen einzigen Zeile in den Gültigkeitsbereich zu bringen. Dazu geben wir den gemeinsamen Teil des Pfads an, gefolgt von zwei Doppelpunkten, und dann geschweifte Klammern um eine Liste der unterschiedlichen Teile des Pfads, wie in Listing 7-18 gezeigt.

Dateiname: `src/main.rs`

```rust
--snip--
use std::{cmp::Ordering, io};
--snip--
```

Listing 7-18: Ein geschachtelter Pfad angeben, um mehrere Elemente mit demselben Präfix in den Gültigkeitsbereich zu bringen

In größeren Programmen kann das Einführen vieler Elemente aus demselben Crate oder Modul mithilfe geschachtelter Pfade die Anzahl der erforderlichen separaten `use`-Anweisungen erheblich reduzieren!

Wir können einen geschachtelten Pfad auf jeder Ebene eines Pfads verwenden, was nützlich ist, wenn zwei `use`-Anweisungen kombiniert werden, die einen gemeinsamen Unterpfad haben. Beispielsweise zeigt Listing 7-19 zwei `use`-Anweisungen: eine, die `std::io` in den Gültigkeitsbereich bringt, und eine, die `std::io::Write` in den Gültigkeitsbereich bringt.

Dateiname: `src/lib.rs`

```rust
use std::io;
use std::io::Write;
```

Listing 7-19: Zwei `use`-Anweisungen, wobei eine ein Unterpfad der anderen ist

Der gemeinsame Teil dieser beiden Pfade ist `std::io`, und das ist der vollständige erste Pfad. Um diese beiden Pfade zu einer einzigen `use`-Anweisung zu vereinigen, können wir `self` im geschachtelten Pfad verwenden, wie in Listing 7-20 gezeigt.

Dateiname: `src/lib.rs`

```rust
use std::io::{self, Write};
```

Listing 7-20: Die Pfade aus Listing 7-19 zu einer einzigen `use`-Anweisung kombinieren

Diese Zeile bringt `std::io` und `std::io::Write` in den Gültigkeitsbereich.

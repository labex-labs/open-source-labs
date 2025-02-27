# Slicen von Strings

Das Indizieren in einen String ist oft eine schlechte Idee, weil nicht klar ist, welchen Rückgabetyp die String-Indizierungsoperation haben sollte: einen Byte-Wert, ein Zeichen, einen Grapheme-Cluster oder einen String-Slice. Wenn Sie daher tatsächlich Indizes verwenden müssen, um String-Slices zu erstellen, fordert Rust Sie auf, sich genauer zu erklären.

Anstatt mit einer einzigen Zahl mit `[]` zu indizieren, können Sie mit einem Bereich `[]` verwenden, um einen String-Slice zu erstellen, der bestimmte Bytes enthält:

```rust
let hello = "Здравствуйте";

let s = &hello[0..4];
```

Hier wird `s` ein `&str` sein, der die ersten vier Bytes des Strings enthält. Früher haben wir erwähnt, dass jedes dieser Zeichen zwei Bytes lang war, was bedeutet, dass `s` `Зд` sein wird.

Wenn wir versuchen würden, nur einen Teil der Bytes eines Zeichens mit etwas wie `&hello[0..1]` zu slicen, würde Rust zur Laufzeit abstürzen, genauso wie wenn ein ungültiger Index in einem Vektor abgerufen wird:

```rust
thread 'main' panicked at 'byte index 1 is not a char boundary;
it is inside 'З' (bytes 0..2) of `Здравствуйте`', src/main.rs:4:14
```

Sie sollten Vorsicht walten lassen, wenn Sie String-Slices mit Bereichen erstellen, da dies Ihren Programm abstürzen kann.

# Aktualisieren eines Vektors

Um einen Vektor zu erstellen und dann Elemente hinzuzufügen, können wir die `push`-Methode verwenden, wie in Listing 8-3 gezeigt.

```rust
let mut v = Vec::new();

v.push(5);
v.push(6);
v.push(7);
v.push(8);
```

Listing 8-3: Verwenden der `push`-Methode, um Werte einem Vektor hinzuzufügen

Wie bei jeder Variable müssen wir sie, wenn wir ihren Wert ändern möchten, mithilfe des `mut`-Schlüsselworts als änderbar markieren, wie im Kapitel 3 besprochen. Die Zahlen, die wir hineinlegen, sind alle vom Typ `i32`, und Rust leitet dies aus den Daten ab, sodass wir die `Vec<i32>`-Annotation nicht benötigen.

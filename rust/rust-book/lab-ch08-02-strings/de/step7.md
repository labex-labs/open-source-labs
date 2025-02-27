# Indizieren von Strings

In vielen anderen Programmiersprachen ist das Abrufen einzelner Zeichen in einem String, indem man sie anhand eines Indexes referenziert, eine gültige und häufige Operation. In Rust jedoch wird ein Fehler auftreten, wenn Sie versuchen, Teile eines `Strings` mit der Indizierungssyntax zuzugreifen. Betrachten Sie den ungültigen Code in Listing 8-19.

```rust
let s1 = String::from("hello");
let h = s1[0];
```

Listing 8-19: Versuch, die Indizierungssyntax mit einem `String` zu verwenden

Dieser Code führt zu dem folgenden Fehler:

```bash
error[E0277]: der Typ `String` kann nicht mit `{integer}` indiziert werden
 --> src/main.rs:3:13
  |
3 |     let h = s1[0];
  |             ^^^^^ `String` kann nicht mit `{integer}` indiziert werden
  |
  = help: das Attribut `Index<{integer}>` ist für `String` nicht implementiert
```

Der Fehler und die Anmerkung erzählen die Geschichte: Rust-Strings unterstützen keine Indizierung. Aber warum nicht? Um diese Frage zu beantworten, müssen wir diskutieren, wie Rust Strings im Speicher speichert.

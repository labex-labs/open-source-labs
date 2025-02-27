# Datentypen

Jeder Wert in Rust hat einen bestimmten **Datentyp**, der Rust mitteilt, welche Art von Daten angegeben wird, damit es weiß, wie mit diesen Daten umgegangen werden soll. Wir werden zwei Datentypsubset betrachten: Skalare und zusammengesetzte Datentypen.

Denke daran, dass Rust eine **statisch typisierte** Sprache ist, was bedeutet, dass es die Typen aller Variablen zur Compile-Zeit kennen muss. Der Compiler kann normalerweise aufgrund des Werts und der Art, wie wir ihn verwenden, schließen, welchen Typ wir verwenden möchten. Wenn es mehrere Typen möglich sind, wie wenn wir in "Vergleichen der Vermutung mit der Geheimzahl" eine `String` in einen numerischen Typ umwandeln, indem wir `parse` verwenden, müssen wir eine Typbezeichnung hinzufügen, wie folgt:

```rust
let guess: u32 = "42".parse().expect("Not a number!");
```

Wenn wir die in obigem Code gezeigte Typbezeichnung `: u32` nicht hinzufügen, wird Rust den folgenden Fehler anzeigen, was bedeutet, dass der Compiler mehr Informationen von uns benötigt, um zu wissen, welchen Typ wir verwenden möchten:

```bash
$ cargo build
   Compiling no_type_annotations v0.1.0 (file:///projects/no_type_annotations)
error[E0282]: type annotations needed
 --> src/main.rs:2:9
  |
2 |     let guess = "42".parse().expect("Not a number!");
  |         ^^^^^ consider giving `guess` a type
```

Für andere Datentypen wirst du unterschiedliche Typbezeichnungen sehen.

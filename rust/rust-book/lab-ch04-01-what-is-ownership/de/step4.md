# Der String-Typ

Um die Besitzregeln zu veranschaulichen, benötigen wir einen Datentyp, der komplexer ist als diejenigen, die wir in "Datentypen" behandelt haben. Die zuvor behandelten Typen haben eine bekannte Größe, können auf dem Stapel gespeichert und beim Verlassen ihres Bereichs vom Stapel entfernt werden und können schnell und einfach kopiert werden, um eine neue, unabhängige Instanz zu erstellen, wenn ein anderer Teil des Codes denselben Wert in einem anderen Bereich verwenden muss. Wir möchten jedoch Daten betrachten, die auf dem Heap gespeichert sind, und untersuchen, wie Rust weiß, wann diese Daten bereinigt werden sollen, und der `String`-Typ ist ein ausgezeichnetes Beispiel.

Wir werden uns auf die Teile von `String` konzentrieren, die mit dem Besitz zusammenhängen. Diese Aspekte gelten auch für andere komplexe Datentypen, ob sie von der Standardbibliothek bereitgestellt werden oder von Ihnen erstellt werden. Wir werden `String` im Kapitel 8 im Detail diskutieren.

Wir haben bereits String-Literale gesehen, bei denen ein String-Wert in unserem Programm hartenkodiert ist. String-Literale sind praktisch, aber sie eignen sich nicht für jede Situation, in der wir möglicherweise Text verwenden möchten. Ein Grund dafür ist, dass sie unveränderlich sind. Ein weiterer Grund ist, dass nicht jeder String-Wert bekannt sein kann, wenn wir unseren Code schreiben: Was ist beispielsweise, wenn wir Benutzereingaben entgegennehmen und speichern möchten? Für diese Situationen hat Rust einen zweiten String-Typ, `String`. Dieser Typ verwaltet Daten, die auf dem Heap zugewiesen werden, und kann daher eine unbekannte Anzahl von Zeichen speichern, die uns zur Compile-Zeit unbekannt sind. Du kannst einen `String` aus einem String-Literal mit der `from`-Funktion erstellen, wie folgt:

```rust
let s = String::from("hello");
```

Der Doppelpunkt `::`-Operator ermöglicht es uns, diese bestimmte `from`-Funktion im Namensraum des `String`-Typs zu platzieren, anstatt einen Namen wie `string_from` zu verwenden. Wir werden diese Syntax im Abschnitt "Methodensyntax" und wenn wir über Namensräume mit Modulen im Abschnitt "Pfade zur Referenz auf ein Element im Modultree" diskutieren.

Dieser Art von String _kann_ verändert werden:

```rust
let mut s = String::from("hello");

s.push_str(", world!"); // push_str() fügt ein Literal an einen String an

println!("{s}"); // Dies wird `hello, world!` ausgeben
```

Was ist nun der Unterschied hier? Warum kann `String` verändert werden, aber Literale nicht? Der Unterschied liegt darin, wie diese beiden Typen mit dem Arbeitsspeicher umgehen.

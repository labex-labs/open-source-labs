# Werte mit Variablen speichern

Als nächstes erstellen wir eine _Variable_, um die Benutzer-Eingabe zu speichern, wie folgt:

```rust
let mut guess = String::new();
```

Jetzt wird das Programm interessant! In dieser kleinen Zeile passiert viel. Wir verwenden die `let`-Anweisung, um die Variable zu erstellen. Hier ist ein weiteres Beispiel:

```rust
let apples = 5;
```

Diese Zeile erstellt eine neue Variable namens `apples` und bindet sie an den Wert 5. In Rust sind Variablen standardmäßig unveränderlich, was bedeutet, dass der Wert, nachdem wir der Variable einen Wert zugewiesen haben, nicht mehr geändert werden kann. Wir werden dieses Konzept im Abschnitt "Variablen und Veränderbarkeit" im Detail diskutieren. Um eine Variable veränderlich zu machen, fügen wir `mut` vor den Variablennamen hinzu:

```rust
let apples = 5; // unveränderlich
let mut bananas = 5; // veränderlich
```

> Hinweis: Die `//`-Syntax startet einen Kommentar, der bis zum Ende der Zeile fortgesetzt wird. Rust ignoriert alles in Kommentaren. Wir werden Kommentare im dritten Kapitel im Detail diskutieren.

Wenn wir nun zurück zum Ratespielprogramm kommen, wissen Sie jetzt, dass `let mut guess` eine veränderliche Variable namens `guess` einführen wird. Das Gleichheitszeichen (`=`) sagt Rust, dass wir jetzt etwas an die Variable binden möchten. Rechts vom Gleichheitszeichen ist der Wert, an den `guess` gebunden ist, nämlich das Ergebnis des Aufrufs von `String::new`, einer Funktion, die eine neue Instanz eines `String` zurückgibt. `String` ist ein String-Typ, der von der Standardbibliothek bereitgestellt wird und der ein wächstes, UTF-8-kodiertes Textstück ist.

Die `::`-Syntax in der Zeile `::new` zeigt an, dass `new` eine assoziierte Funktion des `String`-Typs ist. Eine _assoziierte Funktion_ ist eine Funktion, die auf einem Typ implementiert ist, in diesem Fall `String`. Diese `new`-Funktion erstellt einen neuen, leeren String. Sie werden auf vielen Typen eine `new`-Funktion finden, da es ein üblicher Name für eine Funktion ist, die einen neuen Wert eines bestimmten Typs erstellt.

Insgesamt hat die Zeile `let mut guess = String::new();` eine veränderliche Variable erstellt, die derzeit an eine neue, leere Instanz eines `String` gebunden ist. Puh!

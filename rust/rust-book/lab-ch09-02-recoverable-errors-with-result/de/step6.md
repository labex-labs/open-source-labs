# Ein Schnellzugang zum Weiterreichen von Fehlern: Der?-Operator

Listing 9-7 zeigt eine Implementierung von `read_username_from_file`, die die gleiche Funktionalität wie in Listing 9-6 hat, aber diese Implementierung verwendet den `?`-Operator.

Dateiname: `src/main.rs`

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username_file = File::open("hello.txt")?;
    let mut username = String::new();
    username_file.read_to_string(&mut username)?;
    Ok(username)
}
```

Listing 9-7: Eine Funktion, die Fehler an den aufrufenden Code zurückgibt, indem sie den `?`-Operator verwendet

Der `?`, der nach einem `Result`-Wert platziert ist, ist so definiert, dass er fast auf die gleiche Weise funktioniert wie die `match`-Ausdrücke, die wir in Listing 9-6 definiert haben, um die `Result`-Werte zu behandeln. Wenn der Wert des `Result` ein `Ok` ist, wird der Wert innerhalb von `Ok` aus diesem Ausdruck zurückgegeben und das Programm wird fortgesetzt. Wenn der Wert ein `Err` ist, wird das `Err` aus der gesamten Funktion zurückgegeben, als hätten wir das `return`-Schlüsselwort verwendet, sodass der Fehlerwert an den aufrufenden Code weitergeleitet wird.

Es gibt einen Unterschied zwischen dem, was der `match`-Ausdruck aus Listing 9-6 tut, und dem, was der `?`-Operator tut: Fehlerwerte, auf denen der `?`-Operator aufgerufen wird, gehen durch die `from`-Funktion, die in dem `From`-Trait in der Standardbibliothek definiert ist, die verwendet wird, um Werte von einem Typ in einen anderen zu konvertieren. Wenn der `?`-Operator die `from`-Funktion aufruft, wird der empfangene Fehlertyp in den Fehlertyp konvertiert, der in dem Rückgabetyp der aktuellen Funktion definiert ist. Dies ist nützlich, wenn eine Funktion einen Fehlertyp zurückgibt, um alle Möglichkeiten zu repräsentieren, wie eine Funktion fehlschlagen kann, auch wenn Teile aus vielen verschiedenen Gründen fehlschlagen können.

Zum Beispiel könnten wir die `read_username_from_file`-Funktion in Listing 9-7 ändern, um einen benutzerdefinierten Fehlertyp namens `OurError` zurückzugeben, den wir definieren. Wenn wir auch `impl From<io::Error> for OurError` definieren, um eine Instanz von `OurError` aus einem `io::Error` zu konstruieren, dann werden die `?`-Operator-Aufrufe im Körper von `read_username_from_file` die `from`-Funktion aufrufen und die Fehlertypen konvertieren, ohne dass wir weitere Code in die Funktion hinzufügen müssen.

Im Kontext von Listing 9-7 wird der `?` am Ende des `File::open`-Aufrufs den Wert innerhalb eines `Ok` an die Variable `username_file` zurückgeben. Wenn ein Fehler auftritt, wird der `?`-Operator frühzeitig aus der gesamten Funktion heraus zurückgeben und jedem `Err`-Wert den aufrufenden Code geben. Dasselbe gilt für den `?` am Ende des `read_to_string`-Aufrufs.

Der `?`-Operator eliminiert viel Boilerplate-Code und vereinfacht die Implementierung dieser Funktion. Wir könnten diesen Code sogar noch weiter verkürzen, indem wir Methodenaufrufe direkt nach dem `?` verketten, wie in Listing 9-8 gezeigt.

Dateiname: `src/main.rs`

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username = String::new();

    File::open("hello.txt")?.read_to_string(&mut username)?;

    Ok(username)
}
```

Listing 9-8: Verkettung von Methodenaufrufen nach dem `?`-Operator

Wir haben die Erstellung der neuen `String` in `username` ans Anfang der Funktion verschoben; dieser Teil hat sich nicht geändert. Anstatt eine Variable `username_file` zu erstellen, haben wir den Aufruf von `read_to_string` direkt an das Ergebnis von `File::open("hello.txt")?` angehängt. Wir haben immer noch einen `?` am Ende des `read_to_string`-Aufrufs, und wir geben immer noch einen `Ok`-Wert, der `username` enthält, zurück, wenn sowohl `File::open` als auch `read_to_string` erfolgreich sind, anstatt Fehler zurückzugeben. Die Funktionalität ist wiederum die gleiche wie in Listing 9-6 und Listing 9-7; dies ist nur eine andere, ergonomischere Weise, ihn zu schreiben.

Listing 9-9 zeigt eine Möglichkeit, dies noch kürzer zu machen, indem `fs::read_to_string` verwendet wird.

Dateiname: `src/main.rs`

```rust
use std::fs;
use std::io;

fn read_username_from_file() -> Result<String, io::Error> {
    fs::read_to_string("hello.txt")
}
```

Listing 9-9: Verwenden von `fs::read_to_string` anstatt die Datei zu öffnen und dann zu lesen

Das Lesen einer Datei in einen String ist eine ziemlich häufige Operation, daher bietet die Standardbibliothek die bequeme `fs::read_to_string`-Funktion, die die Datei öffnet, eine neue `String` erstellt, den Inhalt der Datei liest, den Inhalt in diese `String` setzt und ihn zurückgibt. Natürlich gibt uns das Verwenden von `fs::read_to_string` keine Möglichkeit, alle Fehlerbehandlungen zu erklären, daher haben wir es zuerst auf die längere Weise gemacht.

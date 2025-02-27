# Wo der?-Operator verwendet werden kann

Der `?`-Operator kann nur in Funktionen verwendet werden, deren Rückgabetyp mit dem Wert kompatibel ist, auf dem der `?` verwendet wird. Dies liegt daran, dass der `?`-Operator definiert ist, um einen frühen Rückgabewert eines Werts aus der Funktion durchzuführen, auf die gleiche Weise wie der `match`-Ausdruck, den wir in Listing 9-6 definiert haben. In Listing 9-6 hat der `match` einen `Result`-Wert verwendet, und der frühe Rückgabebranch hat einen `Err(e)`-Wert zurückgegeben. Der Rückgabetyp der Funktion muss ein `Result` sein, damit er mit diesem `return` kompatibel ist.

In Listing 9-10 schauen wir uns den Fehler an, den wir erhalten, wenn wir den `?`-Operator in einer `main`-Funktion mit einem Rückgabetyp verwenden, der nicht kompatibel mit dem Typ des Werts ist, auf dem wir den `?` verwenden.

Dateiname: `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt")?;
}
```

Listing 9-10: Versuch, den `?` in der `main`-Funktion zu verwenden, die `()` zurückgibt, wird nicht kompilieren.

Dieser Code öffnet eine Datei, was fehlschlagen kann. Der `?`-Operator folgt dem `Result`-Wert, der von `File::open` zurückgegeben wird, aber diese `main`-Funktion hat den Rückgabetyp `()`, nicht `Result`. Wenn wir diesen Code kompilieren, erhalten wir die folgende Fehlermeldung:

```bash
error[E0277]: the `?` operator can only be used in a function that returns
`Result` or `Option` (or another type that implements `FromResidual`)
 --> src/main.rs:4:48
  |
3 | / fn main() {
4 | |     let greeting_file = File::open("hello.txt")?;
  | |                                                ^ cannot use the `?`
operator in a function that returns `()`
5 | | }
  | |_- this function should return `Result` or `Option` to accept `?`
  |
  = help: the trait `FromResidual<Result<Infallible, std::io::Error>>` is not
implemented for `()`
```

Diese Fehlermeldung zeigt an, dass wir nur erlaubt sind, den `?`-Operator in einer Funktion zu verwenden, die `Result`, `Option` oder einen anderen Typ zurückgibt, der `FromResidual` implementiert.

Um den Fehler zu beheben, haben Sie zwei Möglichkeiten. Eine Möglichkeit ist, den Rückgabetyp Ihrer Funktion zu ändern, um ihn mit dem Wert zu kompatibilisieren, auf dem Sie den `?`-Operator verwenden, solange Sie keine Einschränkungen haben, die dies verhindern. Die andere Möglichkeit ist, einen `match` oder eine der `Result<T, E>`-Methoden zu verwenden, um das `Result<T, E>` auf die passende Weise zu behandeln.

Die Fehlermeldung erwähnt auch, dass `?` auch mit `Option<T>`-Werten verwendet werden kann. Wie bei der Verwendung von `?` auf `Result` können Sie `?` nur auf `Option` in einer Funktion verwenden, die einen `Option` zurückgibt. Das Verhalten des `?`-Operators, wenn er auf einem `Option<T>` aufgerufen wird, ist ähnlich zu seinem Verhalten, wenn er auf einem `Result<T, E>` aufgerufen wird: Wenn der Wert `None` ist, wird das `None` zu diesem Zeitpunkt frühzeitig aus der Funktion zurückgegeben. Wenn der Wert `Some` ist, ist der Wert innerhalb von `Some` der resultierende Wert des Ausdrucks, und die Funktion setzt fort. Listing 9-11 hat ein Beispiel für eine Funktion, die das letzte Zeichen der ersten Zeile im angegebenen Text findet.

```rust
fn last_char_of_first_line(text: &str) -> Option<char> {
    text.lines().next()?.chars().last()
}
```

Listing 9-11: Verwendung des `?`-Operators auf einem `Option<T>`-Wert

Diese Funktion gibt `Option<char>` zurück, weil es möglich ist, dass dort ein Zeichen ist, aber es ist auch möglich, dass es keines gibt. Dieser Code nimmt das `text`-String-Slice-Argument und ruft die `lines`-Methode darauf auf, die einen Iterator über die Zeilen im String zurückgibt. Da diese Funktion die erste Zeile untersuchen möchte, ruft sie `next` auf dem Iterator auf, um den ersten Wert aus dem Iterator zu erhalten. Wenn `text` die leere Zeichenkette ist, wird dieser Aufruf von `next` `None` zurückgeben, in diesem Fall verwenden wir `?`, um zu stoppen und `None` aus `last_char_of_first_line` zurückzugeben. Wenn `text` nicht die leere Zeichenkette ist, wird `next` einen `Some`-Wert zurückgeben, der einen String-Slice der ersten Zeile in `text` enthält.

Der `?` extrahiert den String-Slice, und wir können `chars` auf diesem String-Slice aufrufen, um einen Iterator seiner Zeichen zu erhalten. Wir interessieren uns für das letzte Zeichen in dieser ersten Zeile, daher rufen wir `last` auf, um das letzte Element im Iterator zurückzugeben. Dies ist eine `Option`, weil es möglich ist, dass die erste Zeile die leere Zeichenkette ist; beispielsweise, wenn `text` mit einer leeren Zeile beginnt, aber auf anderen Zeilen Zeichen hat, wie in `"\nhi"`. Wenn es jedoch ein letztes Zeichen in der ersten Zeile gibt, wird es im `Some`-Variant zurückgegeben. Der `?`-Operator in der Mitte gibt uns eine präzise Möglichkeit, diese Logik auszudrücken, was uns ermöglicht, die Funktion in einer Zeile zu implementieren. Wenn wir den `?`-Operator nicht auf `Option` verwenden könnten, müssten wir diese Logik mit mehr Methodenaufrufen oder einem `match`-Ausdruck implementieren.

Beachten Sie, dass Sie den `?`-Operator auf einem `Result` in einer Funktion verwenden können, die `Result` zurückgibt, und Sie können den `?`-Operator auf einem `Option` in einer Funktion verwenden, die `Option` zurückgibt, aber Sie können nicht mischen und match. Der `?`-Operator konvertiert ein `Result` nicht automatisch in ein `Option` oder umgekehrt; in diesen Fällen können Sie Methoden wie die `ok`-Methode auf `Result` oder die `ok_or`-Methode auf `Option` verwenden, um die Konvertierung explizit durchzuführen.

Bisher haben alle `main`-Funktionen, die wir verwendet haben, `()` zurückgegeben. Die `main`-Funktion ist speziell, weil sie der Einstiegspunkt und Ausstiegspunkt eines ausführbaren Programms ist, und es gibt Einschränkungen für ihren Rückgabetyp, damit das Programm wie erwartet funktioniert.

Zum Glück kann `main` auch ein `Result<(), E>` zurückgeben. Listing 9-12 hat den Code aus Listing 9-10, aber wir haben den Rückgabetyp von `main` geändert, um `Result<(), Box<dyn Error>>` zu sein, und am Ende einen Rückgabewert `Ok(())` hinzugefügt. Dieser Code wird jetzt kompilieren.

Dateiname: `src/main.rs`

```rust
use std::error::Error;
use std::fs::File;

fn main() -> Result<(), Box<dyn Error>> {
    let greeting_file = File::open("hello.txt")?;

    Ok(())
}
```

Listing 9-12: Ändern von `main`, um `Result<(), E>` zurückzugeben, ermöglicht die Verwendung des `?`-Operators auf `Result`-Werten.

Der Typ `Box<dyn Error>` ist ein _Trait-Objekt_, über das wir in "Using Trait Objects That Allow for Values of Different Types" sprechen werden. Für jetzt können Sie `Box<dyn Error>` lesen als "irgendein Fehler". Das Verwenden von `?` auf einem `Result`-Wert in einer `main`-Funktion mit dem Fehlertyp `Box<dyn Error>` ist erlaubt, weil es ermöglicht, dass jeder `Err`-Wert frühzeitig zurückgegeben wird. Auch wenn der Körper dieser `main`-Funktion nur Fehler vom Typ `std::io::Error` zurückgeben wird, indem man `Box<dyn Error>` angibt, bleibt diese Signatur auch dann korrekt, wenn mehr Code hinzugefügt wird, der andere Fehler zurückgibt, in den Körper von `main`.

Wenn eine `main`-Funktion ein `Result<(), E>` zurückgibt, wird das ausführbare Programm mit einem Wert von `0` beendet, wenn `main` `Ok(())` zurückgibt, und wird mit einem nicht nullen Wert beendet, wenn `main` einen `Err`-Wert zurückgibt. Ausführbare Programme, die in C geschrieben sind, geben beim Beenden ganze Zahlen zurück: Programme, die erfolgreich beenden, geben die ganze Zahl `0` zurück, und Programme, die einen Fehler haben, geben eine andere ganze Zahl als `0` zurück. Rust gibt auch ganze Zahlen aus ausführbaren Programmen zurück, um mit dieser Konvention kompatibel zu sein.

Die `main`-Funktion kann beliebige Typen zurückgeben, die das `std::process::Termination`-Trait implementieren, das eine Funktion `report` enthält, die einen `ExitCode` zurückgibt. Lesen Sie die Standardbibliotheksdokumentation, um weitere Informationen zur Implementierung des `Termination`-Traits für Ihre eigenen Typen zu erhalten.

Jetzt, nachdem wir die Details des Aufrufs von `panic!` oder des Rückgebens von `Result` diskutiert haben, kehren wir zum Thema zurück, wie man entscheidet, welches in welchen Fällen geeignet ist.

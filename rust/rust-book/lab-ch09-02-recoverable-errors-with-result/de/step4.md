# Schnellzugänge für Panik bei Fehler: unwrap und expect

Das Verwenden von `match` funktioniert gut genug, kann aber etwas umständlich sein und kommuniziert die Absicht nicht immer gut. Der `Result<T, E>`-Typ hat viele Hilfsmethoden definiert, um verschiedene, spezifischere Aufgaben durchzuführen. Die `unwrap`-Methode ist eine Kurzschlussmethode, die genauso implementiert ist wie der `match`-Ausdruck, den wir in Listing 9-4 geschrieben haben. Wenn der `Result`-Wert die `Ok`-Variante ist, gibt `unwrap` den Wert innerhalb von `Ok` zurück. Wenn das `Result` die `Err`-Variante ist, ruft `unwrap` das `panic!`-Makro für uns auf. Hier ist ein Beispiel für das Funktionieren von `unwrap`:

Dateiname: `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt").unwrap();
}
```

Wenn wir diesen Code ausführen, ohne die Datei _hello.txt_ zu haben, werden wir eine Fehlermeldung aus dem `panic!`-Aufruf sehen, den die `unwrap`-Methode ausführt:

    thread 'main' panicked at 'called `Result::unwrap()` on an `Err` value: Os {
    code: 2, kind: NotFound, message: "No such file or directory" }',
    src/main.rs:4:49

Ähnlich gibt uns die `expect`-Methode die Möglichkeit, auch die `panic!`-Fehlermeldung zu wählen. Das Verwenden von `expect` anstelle von `unwrap` und das Angeben guter Fehlermeldungen kann Ihre Absicht vermitteln und das Auffinden der Quelle einer Panik einfacher machen. Die Syntax von `expect` sieht so aus:

Dateiname: `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt")
     .expect("hello.txt sollte in diesem Projekt enthalten sein");
}
```

Wir verwenden `expect` genauso wie `unwrap`: um den Dateihandle zurückzugeben oder das `panic!`-Makro aufzurufen. Die Fehlermeldung, die `expect` bei seinem Aufruf von `panic!` verwendet, wird der Parameter sein, den wir an `expect` übergeben, und nicht die Standard-`panic!`-Meldung, die `unwrap` verwendet. So sieht es aus:

    thread 'main' panicked at 'hello.txt sollte in diesem Projekt enthalten sein: Os {
    code: 2, kind: NotFound, message: "No such file or directory" }',
    src/main.rs:5:10

In produktionsreifer Code wählen die meisten Rustaceans `expect` statt `unwrap` und geben mehr Kontext darüber, warum die Operation immer erfolgreich sein sollte. Auf diese Weise haben Sie, wenn Ihre Annahmen jemals als falsch erwiesen werden, mehr Informationen, die Sie bei der Fehlersuche verwenden können.

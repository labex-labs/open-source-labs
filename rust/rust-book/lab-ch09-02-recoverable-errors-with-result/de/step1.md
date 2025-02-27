# Wiederherstellbare Fehler mit Result

Die meisten Fehler sind nicht so schwerwiegend, dass das Programm vollständig beendet werden muss. Manchmal scheitert eine Funktion aus einem Grund, den man leicht interpretieren und darauf reagieren kann. Beispielsweise, wenn Sie versuchen, eine Datei zu öffnen und diese Operation scheitert, weil die Datei nicht existiert, möchten Sie möglicherweise die Datei erstellen, anstatt den Prozess zu beenden.

Denken Sie sich aus "Handling Potential Failure with Result" zurück, dass die `Result`-Enumeration wie folgt definiert ist, mit zwei Varianten, `Ok` und `Err`:

```rust
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

Die `T` und `E` sind generische Typparameter: Wir werden Generics im Kapitel 10 genauer besprechen. Was Sie im Moment wissen müssen, ist, dass `T` den Typ des Werts darstellt, der im erfolgreichen Fall innerhalb der `Ok`-Variante zurückgegeben wird, und `E` den Typ des Fehlers darstellt, der im fehlerhaften Fall innerhalb der `Err`-Variante zurückgegeben wird. Da `Result` diese generischen Typparameter hat, können wir den `Result`-Typ und die auf ihm definierten Funktionen in vielen verschiedenen Situationen verwenden, in denen der Erfolgswert und der Fehlerwert, die wir zurückgeben möchten, unterschiedlich sein können.

Lassen Sie uns eine Funktion aufrufen, die einen `Result`-Wert zurückgibt, weil die Funktion fehlschlagen kann. In Listing 9-3 versuchen wir, eine Datei zu öffnen.

Dateiname: `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file_result = File::open("hello.txt");
}
```

Listing 9-3: Öffnen einer Datei

Der Rückgabetyp von `File::open` ist ein `Result<T, E>`. Der generische Parameter `T` wurde von der Implementierung von `File::open` mit dem Typ des Erfolgswerts, `std::fs::File`, das ein Dateihandle ist, ausgefüllt. Der Typ von `E`, der im Fehlerwert verwendet wird, ist `std::io::Error`. Dieser Rückgabetyp bedeutet, dass der Aufruf von `File::open` erfolgreich sein kann und einen Dateihandle zurückgeben kann, von dem wir lesen oder schreiben können. Der Funktionsaufruf kann auch fehlschlagen: Beispielsweise kann die Datei nicht existieren oder wir haben möglicherweise keine Berechtigung, auf die Datei zuzugreifen. Die `File::open`-Funktion muss einen Weg haben, uns mitzuteilen, ob es erfolgreich war oder nicht, und uns gleichzeitig entweder den Dateihandle oder die Fehlerinformationen geben. Genau diese Information vermittelt die `Result`-Enumeration.

Im Fall, dass `File::open` erfolgreich ist, wird der Wert in der Variable `greeting_file_result` eine Instanz von `Ok` sein, die einen Dateihandle enthält. Im Fall, dass es fehlschlägt, wird der Wert in `greeting_file_result` eine Instanz von `Err` sein, die weitere Informationen über die Art des aufgetretenen Fehlers enthält.

Wir müssen dem Code in Listing 9-3 hinzufügen, um unterschiedliche Aktionen zu unternehmen, je nachdem, welchen Wert `File::open` zurückgibt. Listing 9-4 zeigt eine Möglichkeit, das `Result` mit einem grundlegenden Werkzeug, dem `match`-Ausdruck, zu behandeln, den wir im Kapitel 6 besprochen haben.

Dateiname: `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => {
            panic!("Problem opening the file: {:?}", error);
        }
    };
}
```

Listing 9-4: Verwenden eines `match`-Ausdrucks, um die `Result`-Varianten zu behandeln, die möglicherweise zurückgegeben werden

Beachten Sie, dass wie bei der `Option`-Enumeration die `Result`-Enumeration und ihre Varianten durch den Präambel in den Gültigkeitsbereich gebracht wurden, so dass wir nicht `Result::` vor den `Ok`- und `Err`-Varianten im `match`-Arm angeben müssen.

Wenn das Ergebnis `Ok` ist, wird dieser Code den inneren `file`-Wert aus der `Ok`-Variante zurückgeben, und wir weisen dann diesen Dateihandle-Wert der Variablen `greeting_file` zu. Nach dem `match` können wir den Dateihandle zum Lesen oder Schreiben verwenden.

Der andere Arm des `match` behandelt den Fall, in dem wir einen `Err`-Wert von `File::open` erhalten. In diesem Beispiel haben wir uns entschieden, die `panic!`-Makro aufzurufen. Wenn es in unserem aktuellen Verzeichnis keine Datei namens _hello.txt_ gibt und wir diesen Code ausführen, werden wir die folgende Ausgabe des `panic!`-Makros sehen:

    thread 'main' panicked at 'Problem opening the file: Os { code:
     2, kind: NotFound, message: "No such file or directory" }',
    src/main.rs:8:23

Wie üblich gibt uns diese Ausgabe genau an, was schiefgelaufen ist.

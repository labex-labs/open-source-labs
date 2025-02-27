# Matching auf verschiedene Fehler

Der Code in Listing 9-4 wird `panic!` auslösen, unabhängig davon, warum `File::open` fehlschlägt. Wir möchten jedoch unterschiedliche Aktionen für verschiedene Fehlgründe unternehmen. Wenn `File::open` fehlschlägt, weil die Datei nicht existiert, möchten wir die Datei erstellen und den Handle für die neue Datei zurückgeben. Wenn `File::open` aus irgendeinem anderen Grund fehlschlägt - beispielsweise, weil wir keine Berechtigung hatten, die Datei zu öffnen - möchten wir, dass der Code auf die gleiche Weise `panic!` auslöst, wie er es in Listing 9-4 tat.为此，我们添加了一个内部的 `match` 表达式，如清单 9-5 所示。

Dateiname: `src/main.rs`

```rust
use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => {
                match File::create("hello.txt") {
                    Ok(fc) => fc,
                    Err(e) => panic!(
                        "Problem creating the file: {:?}",
                        e
                    ),
                }
            }
            other_error => {
                panic!(
                    "Problem opening the file: {:?}",
                    other_error
                );
            }
        },
    };
}
```

Listing 9-5: Behandeln unterschiedlicher Arten von Fehlern auf verschiedene Weise

Der Typ des Werts, den `File::open` innerhalb der `Err`-Variante zurückgibt, ist `io::Error`, eine Struktur, die von der Standardbibliothek bereitgestellt wird. Diese Struktur hat eine Methode `kind`, die wir aufrufen können, um einen `io::ErrorKind`-Wert zu erhalten. Die Enumeration `io::ErrorKind` wird von der Standardbibliothek bereitgestellt und hat Varianten, die die verschiedenen Arten von Fehlern repräsentieren, die aus einem `io`-Operation resultieren können. Die Variante, die wir verwenden möchten, ist `ErrorKind::NotFound`, die angibt, dass die Datei, die wir versuchen, zu öffnen, noch nicht existiert. Wir matchen daher auf `greeting_file_result`, aber wir haben auch eine innere Matches auf `error.kind()`.

Die Bedingung, die wir in der inneren Matches überprüfen möchten, ist, ob der Wert, der von `error.kind()` zurückgegeben wird, die `NotFound`-Variante der `ErrorKind`-Enumeration ist. Wenn dies der Fall ist, versuchen wir, die Datei mit `File::create` zu erstellen. Da `File::create` ebenfalls fehlschlagen kann, benötigen wir einen zweiten Arm im inneren `match`-Ausdruck. Wenn die Datei nicht erstellt werden kann, wird eine andere Fehlermeldung ausgegeben. Der zweite Arm der äußeren Matches bleibt gleich, sodass das Programm bei jedem Fehler außer dem Fehler aufgrund der fehlenden Datei `panic!` auslöst.

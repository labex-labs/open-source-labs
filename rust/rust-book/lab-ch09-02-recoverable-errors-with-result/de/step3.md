# Alternativen zu match mit Result\<T, E\>

Das sind wirklich viele `match`! Der `match`-Ausdruck ist sehr nützlich, aber auch ziemlich primitiv. Im Kapitel 13 lernen Sie über Closures, die mit vielen der auf `Result<T, E>` definierten Methoden verwendet werden. Diese Methoden können kürzer sein als die Verwendung von `match`, wenn Sie `Result<T, E>`-Werte in Ihrem Code behandeln.

Zum Beispiel ist hier eine andere Möglichkeit, die gleiche Logik wie in Listing 9-5 zu schreiben, diesmal mit Closures und der `unwrap_or_else`-Methode:

    // src/main.rs
    use std::fs::File;
    use std::io::ErrorKind;

    fn main() {
        let greeting_file = File::open("hello.txt").unwrap_or_else(|error| {
            if error.kind() == ErrorKind::NotFound {
                File::create("hello.txt").unwrap_or_else(|error| {
                    panic!("Problem creating the file: {:?}", error);
                })
            } else {
                panic!("Problem opening the file: {:?}", error);
            }
        });
    }

Obwohl dieser Code das gleiche Verhalten wie Listing 9-5 hat, enthält er keine `match`-Ausdrücke und ist lesbarer. Kommen Sie nach dem Lesen von Kapitel 13 zurück zu diesem Beispiel und suchen Sie die `unwrap_or_else`-Methode in der Standardbibliotheksdokumentation auf. Viele weitere dieser Methoden können riesige geschachtelte `match`-Ausdrücke aufräumen, wenn Sie mit Fehlern umgehen.

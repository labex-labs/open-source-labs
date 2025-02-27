# Hinzufügen benutzerdefinierter Fehlermeldungen

Sie können auch eine benutzerdefinierte Nachricht hinzufügen, die zusammen mit der Fehlermeldung als optionale Argumente an die `assert!`, `assert_eq!` und `assert_ne!`-Makros gedruckt wird. Alle nach den erforderlichen Argumenten angegebenen Argumente werden an das `format!`-Makro weitergeleitet (siehe "Concatenation with the + Operator or the format! Macro"), sodass Sie einen Formatstring übergeben können, der `{}`-Platzhalter enthält und die Werte, die in diese Platzhalter eingesetzt werden sollen. Benutzerdefinierte Nachrichten sind hilfreich, um zu dokumentieren, was eine Behauptung bedeutet; wenn ein Test fehlschlägt, haben Sie eine genauere Vorstellung davon, was das Problem mit dem Code ist.

Nehmen wir beispielsweise an, dass wir eine Funktion haben, die Menschen nach ihrem Namen begrüßt, und wir möchten testen, dass der Name, den wir in die Funktion übergeben, im Output erscheint:

Dateiname: `src/lib.rs`

```rust
pub fn greeting(name: &str) -> String {
    format!("Hello {name}!")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn greeting_contains_name() {
        let result = greeting("Carol");
        assert!(result.contains("Carol"));
    }
}
```

Die Anforderungen für dieses Programm sind noch nicht abgestimmt, und wir sind ziemlich sicher, dass der Text `Hello` am Anfang der Begrüßung sich ändern wird. Wir haben beschlossen, nicht gezwungen zu sein, den Test zu aktualisieren, wenn sich die Anforderungen ändern, daher überprüfen wir statt der genauen Gleichheit mit dem von der `greeting`-Funktion zurückgegebenen Wert nicht, sondern stellen nur sicher, dass der Output den Text des Eingabeparameters enthält.

Lassen Sie uns nun einen Fehler in diesem Code einführen, indem wir `greeting` ändern, um `name` auszuschließen, um zu sehen, wie die standardmäßige Testfehlermeldung aussieht:

```rust
pub fn greeting(name: &str) -> String {
    String::from("Hello!")
}
```

Das Ausführen dieses Tests liefert Folgendes:

    running 1 test
    test tests::greeting_contains_name... FAILED

    failures:

    ---- tests::greeting_contains_name stdout ----
    thread'main' panicked at 'assertion failed:
    result.contains(\"Carol\")', src/lib.rs:12:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace


    failures:
        tests::greeting_contains_name

Dieses Ergebnis zeigt nur an, dass die Behauptung fehlgeschlagen ist und auf welcher Zeile die Behauptung steht. Eine nützlichere Fehlermeldung würde den Wert aus der `greeting`-Funktion ausgeben. Fügen wir eine benutzerdefinierte Fehlermeldung hinzu, die aus einem Formatstring besteht, in dem ein Platzhalter mit dem tatsächlichen Wert ersetzt ist, den wir von der `greeting`-Funktion erhalten haben:

    #[test]
    fn greeting_contains_name() {
        let result = greeting("Carol");
        assert!(
            result.contains("Carol"),
            "Greeting did not contain name, value was `{result}`"
        );
    }

Wenn wir jetzt den Test ausführen, erhalten wir eine informativere Fehlermeldung:

    ---- tests::greeting_contains_name stdout ----
    thread'main' panicked at 'Greeting did not contain name, value
    was `Hello!`', src/lib.rs:12:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

Wir können den Wert sehen, den wir tatsächlich im Testoutput erhalten haben, was uns helfen würde, das Problem zu debuggen, was passiert ist, anstatt was wir erwartet haben.

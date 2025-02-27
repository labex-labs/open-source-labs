# Dokumentationstests

Die primäre Methode der Dokumentation eines Rust-Projekts ist die Annotation des Quellcodes. Dokumentationskommentare werden in der CommonMark Markdown-Spezifikation geschrieben und unterstützen darin Codeblöcke. Rust kümmert sich um die Korrektheit, sodass diese Codeblöcke kompiliert und als Dokumentationstests verwendet werden.

````rust
/// Die erste Zeile ist eine kurze Zusammenfassung, die die Funktion beschreibt.
///
/// Die nächsten Zeilen enthalten detaillierte Dokumentation. Codeblöcke beginnen mit
/// drei Anführungszeichen und haben implizit `fn main()` darin
/// und `extern crate <cratename>`. Nehmen wir an, dass wir das `doccomments`-Kratzer testen:
///
/// ```
/// let result = doccomments::add(2, 3);
/// assert_eq!(result, 5);
/// ```
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

/// Normalerweise können Dokumentationskommentare Abschnitte wie "Beispiele", "Panics" und "Fehlschläge" enthalten.
///
/// Die nächste Funktion teilt zwei Zahlen.
///
/// # Beispiele
///
/// ```
/// let result = doccomments::div(10, 2);
/// assert_eq!(result, 5);
/// ```
///
/// # Panics
///
/// Die Funktion stürzt ab, wenn der zweite Argument null ist.
///
/// ```rust
/// // stürzt bei Division durch null ab
/// doccomments::div(10, 0);
/// ```
pub fn div(a: i32, b: i32) -> i32 {
    if b == 0 {
        panic!("Divide-by-zero error");
    }

    a / b
}
````

Codeblöcke in der Dokumentation werden automatisch getestet, wenn der reguläre Befehl `cargo test` ausgeführt wird:

```shell
$ cargo test
running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out

   Doc-tests doccomments

running 3 tests
test src/lib.rs - add (line 7)... ok
test src/lib.rs - div (line 21)... ok
test src/lib.rs - div (line 31)... ok

test result: ok. 3 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
```

## Motivation hinter den Dokumentationstests

Der Hauptzweck von Dokumentationstests ist, als Beispiele zu dienen, die die Funktionalität testen, was eine der wichtigsten Richtlinien ist. Es ermöglicht, Beispiele aus der Dokumentation als vollständige Codeausschnitte zu verwenden. Aber das Verwenden von `?` führt zum Kompilierungsfehler, da `main` `unit` zurückgibt. Die Möglichkeit, einige Quellzeilen von der Dokumentation zu verstecken, kommt uns entgegen: Man kann `fn try_main() -> Result<(), ErrorType>` schreiben, es verstecken und es in verstecktem `main` `unwrap`en. Klingt kompliziert? Hier ist ein Beispiel:

````rust
/// Verwenden von verstecktem `try_main` in Dokumentationstests.
///
/// ```
/// # // versteckte Zeilen beginnen mit `#`-Symbol, aber sie sind dennoch compilierbar!
/// # fn try_main() -> Result<(), String> { // Zeile, die den im Dokument gezeigten Körper umschließt
/// let res = doccomments::try_div(10, 2)?;
/// # Ok(()) // Rückgabe von try_main
/// # }
/// # fn main() { // Beginn von main, das `unwrap()` aufruft
/// #    try_main().unwrap(); // Aufruf von try_main und Entpacken
/// #                         // sodass der Test bei einem Fehler abstürzt
/// # }
/// ```
pub fn try_div(a: i32, b: i32) -> Result<i32, String> {
    if b == 0 {
        Err(String::from("Divide-by-zero"))
    } else {
        Ok(a / b)
    }
}
````

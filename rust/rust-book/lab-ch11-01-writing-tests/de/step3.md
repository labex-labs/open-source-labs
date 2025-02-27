# Überprüfen von Ergebnissen mit dem assert!-Makro

Das `assert!`-Makro, das von der Standardbibliothek bereitgestellt wird, ist nützlich, wenn Sie sicherstellen möchten, dass eine bestimmte Bedingung in einem Test `true` auswertet. Wir geben dem `assert!`-Makro einen Ausdruck, der zu einem Boolean ausgewertet wird. Wenn der Wert `true` ist, passiert nichts und der Test wird bestanden. Wenn der Wert `false` ist, ruft das `assert!`-Makro `panic!` auf, um den Test als fehlgeschlagen zu markieren. Das Verwenden des `assert!`-Makros hilft uns zu überprüfen, ob unser Code auf die von uns beabsichtigte Weise funktioniert.

In Listing 5-15 haben wir eine `Rectangle`-Struktur und eine `can_hold`-Methode verwendet, die hier in Listing 11-5 wiedergegeben sind. Lassen Sie uns diesen Code in die `src/lib.rs`-Datei einfügen und dann einige Tests dafür schreiben, indem wir das `assert!`-Makro verwenden.

Dateiname: `src/lib.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
```

Listing 11-5: Verwendung der `Rectangle`-Struktur und ihrer `can_hold`-Methode aus Kapitel 5

Die `can_hold`-Methode gibt einen Boolean zurück, was bedeutet, dass es ein perfektes Anwendungsfall für das `assert!`-Makro ist. In Listing 11-6 schreiben wir einen Test, der die `can_hold`-Methode testet, indem wir eine `Rectangle`-Instanz mit einer Breite von 8 und einer Höhe von 7 erstellen und überprüfen, dass sie eine andere `Rectangle`-Instanz mit einer Breite von 5 und einer Höhe von 1 aufnehmen kann.

Dateiname: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
  1 use super::*;

    #[test]
  2 fn larger_can_hold_smaller() {
      3 let larger = Rectangle {
            width: 8,
            height: 7,
        };
        let smaller = Rectangle {
            width: 5,
            height: 1,
        };

      4 assert!(larger.can_hold(&smaller));
    }
}
```

Listing 11-6: Ein Test für `can_hold`, der überprüft, ob ein größerer Rechteck tatsächlich ein kleineres Rechteck aufnehmen kann

Beachten Sie, dass wir eine neue Zeile im `tests`-Modul hinzugefügt haben: `use super::*;` \[1\]. Das `tests`-Modul ist ein normales Modul, das den üblichen Sichtbarkeitsregeln folgt, die wir in "Paths for Referring to an Item in the Module Tree" behandelt haben. Da das `tests`-Modul ein inneres Modul ist, müssen wir den zu testenden Code im äußeren Modul in den Gültigkeitsbereich des inneren Moduls bringen. Wir verwenden hier ein Glob, sodass alles, was wir im äußeren Modul definieren, für dieses `tests`-Modul verfügbar ist.

Wir haben unseren Test `larger_can_hold_smaller` benannt \[2\], und wir haben die beiden erforderlichen `Rectangle`-Instanzen erstellt \[3\]. Dann haben wir das `assert!`-Makro aufgerufen und ihm das Ergebnis der Ausführung von `larger.can_hold(&smaller)` übergeben \[4\]. Dieser Ausdruck sollte `true` zurückgeben, sodass unser Test bestanden werden sollte. Finden wir heraus!

    running 1 test
    test tests::larger_can_hold_smaller... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Es besteht tatsächlich! Lassen Sie uns einen weiteren Test hinzufügen, diesmal überprüfend, dass ein kleineres Rechteck kein größeres Rechteck aufnehmen kann:

Dateiname: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn larger_can_hold_smaller() {
        --snip--
    }

    #[test]
    fn smaller_cannot_hold_larger() {
        let larger = Rectangle {
            width: 8,
            height: 7,
        };
        let smaller = Rectangle {
            width: 5,
            height: 1,
        };

        assert!(!smaller.can_hold(&larger));
    }
}
```

Da das korrekte Ergebnis der `can_hold`-Funktion in diesem Fall `false` ist, müssen wir das Ergebnis verneinen, bevor wir es an das `assert!`-Makro übergeben. Dadurch wird unser Test bestehen, wenn `can_hold` `false` zurückgibt:

    running 2 tests
    test tests::larger_can_hold_smaller... ok
    test tests::smaller_cannot_hold_larger... ok

    test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Zwei Tests, die bestehen! Jetzt sehen wir, was mit unseren Testresultaten passiert, wenn wir einen Fehler in unserem Code einführen. Wir ändern die Implementierung der `can_hold`-Methode, indem wir das größer-than-Zeichen durch ein kleiner-than-Zeichen ersetzen, wenn es die Breiten vergleicht:

    --snip--

    impl Rectangle {
        fn can_hold(&self, other: &Rectangle) -> bool {
            self.width < other.width && self.height > other.height
        }
    }

Das Ausführen der Tests liefert jetzt Folgendes:

    running 2 tests
    test tests::smaller_cannot_hold_larger... ok
    test tests::larger_can_hold_smaller... FAILED

    failures:

    ---- tests::larger_can_hold_smaller stdout ----
    thread'main' panicked at 'assertion failed:
    larger.can_hold(&smaller)', src/lib.rs:28:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace


    failures:
        tests::larger_can_hold_smaller

    test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Unsere Tests haben den Fehler erkannt! Da `larger.width` `8` ist und `smaller.width` `5` ist, liefert der Vergleich der Breiten in `can_hold` jetzt `false` zurück: 8 ist nicht kleiner als 5.

# Überprüfen auf Panik mit should_panic

Neben der Überprüfung von Rückgabewerten ist es wichtig, zu überprüfen, ob unser Code Fehlerbedingungen wie erwartet behandelt. Beispielsweise betrachten wir den `Guess`-Typ, den wir in Listing 9-13 erstellt haben. Anderer Code, der `Guess` verwendet, setzt sich darauf verlassen, dass `Guess`-Instanzen nur Werte zwischen 1 und 100 enthalten. Wir können einen Test schreiben, der sicherstellt, dass das Versuchen, eine `Guess`-Instanz mit einem Wert außerhalb dieses Bereichs zu erstellen, einen Fehler auslöst.

Wir tun dies, indem wir das Attribut `should_panic` zu unserer Testfunktion hinzufügen. Der Test besteht, wenn der Code innerhalb der Funktion einen Fehler auslöst; der Test scheitert, wenn der Code innerhalb der Funktion keinen Fehler auslöst.

Listing 11-8 zeigt einen Test, der überprüft, ob die Fehlerbedingungen von `Guess::new` auftreten, wenn wir erwarten, dass sie es tun.

    // src/lib.rs
    pub struct Guess {
        value: i32,
    }

    impl Guess {
        pub fn new(value: i32) -> Guess {
            if value < 1 || value > 100 {
                panic!(
                    "Guess value must be between 1 and 100, got {}.",
                    value
                );
            }

            Guess { value }
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        #[should_panic]
        fn greater_than_100() {
            Guess::new(200);
        }
    }

Listing 11-8: Testen, dass eine Bedingung einen Fehler auslöst!

Wir platzieren das Attribut `#[should_panic]` nach dem `#[test]`-Attribut und vor der Testfunktion, auf die es zutrifft. Schauen wir uns das Ergebnis an, wenn dieser Test besteht:

    running 1 test
    test tests::greater_than_100 - should panic... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Es sieht gut aus! Jetzt fügen wir einen Fehler in unseren Code ein, indem wir die Bedingung entfernen, dass die `new`-Funktion einen Fehler auslöst, wenn der Wert größer als 100 ist:

    // src/lib.rs
    --snip--

    impl Guess {
        pub fn new(value: i32) -> Guess {
            if value < 1 {
                panic!(
                    "Guess value must be between 1 and 100, got {}.",
                    value
                );
            }

            Guess { value }
        }
    }

Wenn wir den Test in Listing 11-8 ausführen, wird er fehlschlagen:

    running 1 test
    test tests::greater_than_100 - should panic... FAILED

    failures:

    ---- tests::greater_than_100 stdout ----
    note: test did not panic as expected

    failures:
        tests::greater_than_100

    test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Wir erhalten in diesem Fall keine sehr hilfreiche Meldung, aber wenn wir uns die Testfunktion ansehen, sehen wir, dass sie mit `#[should_panic]` annotiert ist. Der Fehler, den wir erhalten haben, bedeutet, dass der Code in der Testfunktion keinen Fehler ausgelöst hat.

Tests, die `should_panic` verwenden, können ungenau sein. Ein `should_panic`-Test würde bestehen, auch wenn der Test aus einem anderen Grund als dem, den wir erwarteten, einen Fehler auslöst. Um `should_panic`-Tests präziser zu machen, können wir einem optionalen `expected`-Parameter des `should_panic`-Attributs einen Wert hinzufügen. Der Testrunner wird sicherstellen, dass die Fehlermeldung den angegebenen Text enthält. Beispielsweise betrachten wir den modifizierten Code für `Guess` in Listing 11-9, in dem die `new`-Funktion je nachdem, ob der Wert zu klein oder zu groß ist, mit unterschiedlichen Nachrichten einen Fehler auslöst.

    // src/lib.rs
    --snip--

    impl Guess {
        pub fn new(value: i32) -> Guess {
            if value < 1 {
                panic!(
                    "Guess value must be greater than or equal to 1, got {}.",
                    value
                );
            } else if value > 100 {
                panic!(
                    "Guess value must be less than or equal to 100, got {}.",
                    value
                );
            }

            Guess { value }
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        #[should_panic(expected = "less than or equal to 100")]
        fn greater_than_100() {
            Guess::new(200);
        }
    }

Listing 11-9: Testen auf einen `panic!` mit einer Fehlermeldung, die einen bestimmten Teilstring enthält

Dieser Test wird bestehen, weil der Wert, den wir im `expected`-Parameter des `should_panic`-Attributs angegeben haben, ein Teilstring der Nachricht ist, mit der die `Guess::new`-Funktion einen Fehler auslöst. Wir hätten auch die gesamte erwartete Fehlermeldung angeben können, was in diesem Fall `Guess value must be less than or equal to 100, got 200` wäre. Was Sie wählen, um anzugeben, hängt davon ab, wie viel der Fehlermeldung einzigartig oder dynamisch ist und wie genau Sie Ihren Test möchten. In diesem Fall ist ein Teilstring der Fehlermeldung ausreichend, um sicherzustellen, dass der Code in der Testfunktion den `else if value > 100`-Fall ausführt.

Um zu sehen, was passiert, wenn ein `should_panic`-Test mit einer `expected`-Nachricht fehlschlägt, fügen wir erneut einen Fehler in unseren Code ein, indem wir die Körper der `if value < 1`- und der `else if value > 100`-Blöcke tauschen:

    // src/lib.rs
    --snip--
    if value < 1 {
        panic!(
            "Guess value must be less than or equal to 100, got {}.",
            value
        );
    } else if value > 100 {
        panic!(
            "Guess value must be greater than or equal to 1, got {}.",
            value
        );
    }
    --snip--

Diesmal wird der `should_panic`-Test fehlschlagen, wenn wir ihn ausführen:

    running 1 test
    test tests::greater_than_100 - should panic... FAILED

    failures:

    ---- tests::greater_than_100 stdout ----
    thread'main' panicked at 'Guess value must be greater than or equal to 1, got
    200.', src/lib.rs:13:13
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
    note: panic did not contain expected string
          panic message: `"Guess value must be greater than or equal to 1, got
    200."`,
     expected substring: `"less than or equal to 100"`

    failures:
        tests::greater_than_100

    test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out;
    finished in 0.00s

Die Fehlermeldung zeigt an, dass dieser Test tatsächlich wie erwartet einen Fehler ausgelöst hat, aber die Fehlermeldung enthielt nicht den erwarteten String `'Guess value must be less than or equal to 100'`. Die Fehlermeldung, die wir in diesem Fall erhalten haben, war `Guess value must be greater than or equal to 1, got 200`. Jetzt können wir anfangen, herauszufinden, wo unser Fehler ist!

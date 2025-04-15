# Die Struktur einer Testfunktion

Im einfachsten Fall ist ein Test in Rust eine Funktion, die mit dem `test`-Attribut annotiert ist. Attribute sind Metadaten zu Teilen von Rust-Code; ein Beispiel ist das `derive`-Attribut, das wir in Kapitel 5 mit Structs verwendet haben. Um eine Funktion in eine Testfunktion umzuwandeln, fügen Sie `#[test]` in der Zeile vor `fn` hinzu. Wenn Sie Ihre Tests mit dem Befehl `cargo test` ausführen, baut Rust einen Testrunner-Binär aus, der die annotierten Funktionen ausführt und meldet, ob jede Testfunktion erfolgreich abgeschlossen oder fehlschlägt.

Wenn wir mit Cargo ein neues Bibliotheksprojekt erstellen, wird automatisch ein Testmodul mit einer Testfunktion für uns erstellt. Dieses Modul gibt Ihnen ein Template zum Schreiben Ihrer Tests, sodass Sie nicht jedes Mal die genaue Struktur und Syntax recherchieren müssen, wenn Sie ein neues Projekt starten. Sie können so viele zusätzliche Testfunktionen und so viele Testmodule hinzufügen, wie Sie möchten!

Wir werden einige Aspekte der Funktionsweise von Tests erkunden, indem wir mit der Vorlage-Test experimentieren, bevor wir tatsächlich Code testen. Dann werden wir einige echte Tests schreiben, die auf Code zugreifen, den wir geschrieben haben, und überprüfen, ob sein Verhalten korrekt ist.

Lassen Sie uns ein neues Bibliotheksprojekt namens `adder` erstellen, das zwei Zahlen addiert:

```bash
$ cargo new adder --lib
Created library $(adder) project
$ cd adder
```

Der Inhalt der Datei `src/lib.rs` in Ihrer `adder`-Bibliothek sollte wie in Listing 11-1 aussehen.

Dateiname: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
  1 #[test]
    fn it_works() {
        let result = 2 + 2;
      2 assert_eq!(result, 4);
    }
}
```

Listing 11-1: Das automatisch von `cargo new` generierte Testmodul und -funktion

Lassen Sie uns für jetzt die obersten beiden Zeilen außer Acht und uns auf die Funktion konzentrieren. Beachten Sie die `#[test]`-Annotation \[1\]: Dieses Attribut gibt an, dass es sich um eine Testfunktion handelt, sodass der Testrunner weiß, diese Funktion als Test zu behandeln. Wir könnten auch nicht-Testfunktionen im `tests`-Modul haben, um allgemeine Szenarien einzurichten oder allgemeine Operationen durchzuführen, daher müssen wir immer angeben, welche Funktionen Tests sind.

Der Beispiel-Funktionskörper verwendet die `assert_eq!`-Makro \[2\], um zu überprüfen, dass `result`, das das Ergebnis der Addition von 2 und 2 enthält, gleich 4 ist. Diese Behauptung dient als Beispiel für das Format eines typischen Tests. Lassen Sie uns es ausführen, um zu sehen, dass dieser Test erfolgreich abgeschlossen wird.

Der Befehl `cargo test` führt alle Tests in unserem Projekt aus, wie in Listing 11-2 gezeigt.

```bash
[object Object]
```

Listing 11-2: Die Ausgabe bei der Ausführung des automatisch generierten Tests

Cargo hat die Tests kompiliert und ausgeführt. Wir sehen die Zeile `running 1 test` \[1\]. Die nächste Zeile zeigt den Namen der generierten Testfunktion, die `it_works` heißt, und dass das Ergebnis der Ausführung dieses Tests `ok` ist \[2\]. Die Gesamtübersicht `test result: ok.` \[3\] bedeutet, dass alle Tests erfolgreich abgeschlossen wurden, und der Teil, der `1 passed; 0 failed` liest, summiert die Anzahl der Tests, die erfolgreich abgeschlossen oder fehlgeschlagen sind.

Es ist möglich, einen Test als ignoriert zu markieren, sodass er in einem bestimmten Fall nicht ausgeführt wird; wir werden das in "Ignoring Some Tests Unless Specifically Requested" behandeln. Da wir das hier nicht getan haben, zeigt die Zusammenfassung `0 ignored`. Wir können auch einen Argument an den Befehl `cargo test` übergeben, um nur Tests auszuführen, deren Name einem String entspricht; dies wird als _Filterung_ bezeichnet, und wir werden es in "Running a Subset of Tests by Name" behandeln. Hier haben wir die ausgeführten Tests nicht gefiltert, daher zeigt das Ende der Zusammenfassung `0 filtered out`.

Die Statistik `0 measured` ist für Benchmark-Tests, die die Leistung messen. Benchmark-Tests sind wie beim Schreiben dieses Dokuments nur in der nightly-Version von Rust verfügbar. Siehe die Dokumentation zu Benchmark-Tests unter *https://doc.rust-lang.org/unstable-book/library-features/test.html*, um mehr zu erfahren.

Der nächste Teil der Testausgabe, der bei `Doc-tests adder` beginnt \[4\], bezieht sich auf die Ergebnisse beliebiger Dokumentationstests. Wir haben noch keine Dokumentationstests, aber Rust kann alle Codebeispiele kompilieren, die in unserer API-Dokumentation auftauchen. Diese Funktion hilft, Ihre Dokumentation und Ihren Code in Sync zu halten! Wir werden diskutieren, wie man Dokumentationstests schreibt, in "Documentation Comments as Tests". Für jetzt werden wir die `Doc-tests`-Ausgabe außer Acht lassen.

Lassen Sie uns den Test an unsere eigenen Bedürfnisse anpassen. Ändern Sie zunächst den Namen der `it_works`-Funktion in einen anderen Namen, wie `exploration`, so:

Dateiname: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn exploration() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
}
```

Führen Sie dann erneut `cargo test` aus. Die Ausgabe zeigt jetzt `exploration` anstelle von `it_works`:

    running 1 test
    test tests::exploration... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Jetzt fügen wir einen weiteren Test hinzu, aber diesmal einen Test, der fehlschlägt! Tests scheitern, wenn etwas in der Testfunktion einen Fehler auslöst. Jeder Test wird in einem neuen Thread ausgeführt, und wenn der Hauptthread sieht, dass ein Testthread abgestürzt ist, wird der Test als fehlgeschlagen markiert. Im Kapitel 9 haben wir darüber gesprochen, dass die einfachste Möglichkeit, einen Fehler auszulösen, der Aufruf der `panic!`-Makro ist. Geben Sie den neuen Test als Funktion namens `another` ein, sodass Ihre `src/lib.rs`-Datei wie in Listing 11-3 aussieht.

Dateiname: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn exploration() {
        assert_eq!(2 + 2, 4);
    }

    #[test]
    fn another() {
        panic!("Make this test fail");
    }
}
```

Listing 11-3: Hinzufügen eines zweiten Tests, der fehlschlägt, weil wir das `panic!`-Makro aufrufen

Führen Sie die Tests erneut mit `cargo test` aus. Die Ausgabe sollte wie in Listing 11-4 aussehen, was zeigt, dass unser `exploration`-Test erfolgreich abgeschlossen und `another` fehlgeschlagen ist.

    running 2 tests
    test tests::exploration... ok
    1 test tests::another... FAILED

    2 failures:

    ---- tests::another stdout ----
    thread'main' panicked at 'Make this test fail', src/lib.rs:10:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

    3 failures:
        tests::another

    4 test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

    error: test failed, to rerun pass '--lib'

Listing 11-4: Testresultate, wenn ein Test erfolgreich abgeschlossen und ein Test fehlschlägt

Anstelle von `ok` zeigt die Zeile `test tests::another` `FAILED` \[1\]. Zwei neue Abschnitte erscheinen zwischen den einzelnen Ergebnissen und der Zusammenfassung: Der erste \[2\] zeigt die detaillierten Gründe für jeden Testfehler an. In diesem Fall erhalten wir die Details, dass `another` fehlgeschlagen ist, weil es `panicked at 'Make this test fail'` in Zeile 10 in der `src/lib.rs`-Datei. Der nächste Abschnitt \[3\] listet nur die Namen aller fehlgeschlagenen Tests auf, was hilfreich ist, wenn es viele Tests und viel detaillierte fehlende Testausgabe gibt. Wir können den Namen eines fehlgeschlagenen Tests verwenden, um nur diesen Test auszuführen, um ihn leichter zu debuggen; wir werden mehr über Möglichkeiten zur Ausführung von Tests in "Controlling How Tests Are Run" sprechen.

Die Zusammenfassungzeile wird am Ende angezeigt \[4\]: Insgesamt ist unser Testresultat `FAILED`. Wir hatten einen Test, der erfolgreich abgeschlossen wurde, und einen Test, der fehlgeschlagen ist.

Jetzt, nachdem Sie gesehen haben, wie die Testresultate in verschiedenen Szenarien aussehen, werden wir uns einige Makros außer `panic!` ansehen, die in Tests nützlich sind.

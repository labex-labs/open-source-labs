# Rückgabewerte und Gültigkeitsbereich

Das Zurückgeben von Werten kann ebenfalls die Besitzübertragung bewirken. Listing 4-4 zeigt ein Beispiel einer Funktion, die einen Wert zurückgibt, mit ähnlichen Anmerkungen wie in Listing 4-3.

    // src/main.rs
    fn main() {
        let s1 = gives_ownership();         // gives_ownership verschiebt seinen
                                            // Rückgabewert in s1

        let s2 = String::from("hello");     // s2 tritt in den Gültigkeitsbereich

        let s3 = takes_and_gives_back(s2);  // s2 wird in
                                            // takes_and_gives_back verschoben,
                                            // das auch seinen Rückgabewert in s3
                                            // verschiebt
    } // Hier tritt s3 außerhalb seines Gültigkeitsbereichs und wird freigegeben.
      // s2 wurde verschoben, also passiert nichts. s1 tritt außerhalb seines
      // Gültigkeitsbereichs und wird freigegeben

    fn gives_ownership() -> String {             // gives_ownership wird seinen
                                                 // Rückgabewert in die Funktion
                                                 // verschieben, die es aufruft

        let some_string = String::from("yours"); // some_string tritt in den
                                                 // Gültigkeitsbereich

        some_string                              // some_string wird zurückgegeben
                                                 // und an die aufrufende Funktion
                                                 // verschoben
    }

    // Diese Funktion nimmt einen String entgegen und gibt einen String zurück
    fn takes_and_gives_back(a_string: String) -> String { // a_string tritt in den
                                                          // Gültigkeitsbereich

        a_string  // a_string wird zurückgegeben und an die aufrufende Funktion
                  // verschoben
    }

Listing 4-4: Übertragung der Besitzhaftung von Rückgabewerten

Die Besitzhaftung einer Variable folgt jedes Mal dem gleichen Muster: Das Zuweisen eines Werts an eine andere Variable verschiebt es. Wenn eine Variable, die Daten auf dem Heap enthält, außerhalb ihres Gültigkeitsbereichs fällt, wird der Wert durch `drop` aufgeräumt, es sei denn, die Besitzhaftung der Daten wurde an eine andere Variable übertragen.

Während dies funktioniert, ist es etwas lästig, bei jeder Funktion die Besitzhaftung zu übernehmen und dann wieder zurückzugeben. Was ist, wenn wir einer Funktion einen Wert zur Verfügung stellen möchten, aber die Besitzhaftung nicht übernehmen? Es ist ziemlich ärgerlich, dass alles, was wir übergeben, auch zurückgegeben werden muss, wenn wir es erneut verwenden möchten, zusätzlich zu allen Daten, die aus dem Funktionskörper resultieren und die wir möglicherweise auch zurückgeben möchten.

Rust erlaubt uns tatsächlich, mehrere Werte als Tupel zurückzugeben, wie in Listing 4-5 gezeigt.

Dateiname: `src/main.rs`

```rust
fn main() {
    let s1 = String::from("hello");

    let (s2, len) = calculate_length(s1);

    println!("The length of '{s2}' is {len}.");
}

fn calculate_length(s: String) -> (String, usize) {
    let length = s.len(); // len() gibt die Länge eines Strings zurück

    (s, length)
}
```

Listing 4-5: Rückgabe der Besitzhaftung von Parametern

Aber das ist zu aufwendig und erfordert viel Arbeit für einen Begriff, der eigentlich üblich sein sollte. Glücklicherweise hat Rust eine Funktion, um einen Wert zu verwenden, ohne die Besitzhaftung zu übertragen, nämlich _Referenzen_.

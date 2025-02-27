# Typenschluss

Der Typenschlussmotor ist ziemlich intelligent. Er macht mehr als nur auf den Typ des Wertausdrucks beim Initialisieren zu schauen. Er schaut auch, wie die Variable danach verwendet wird, um ihren Typ zu inferieren. Hier ist ein fortgeschrittenes Beispiel für Typenschluss:

```rust
fn main() {
    // Aufgrund der Annotation weiß der Compiler, dass `elem` vom Typ u8 ist.
    let elem = 5u8;

    // Erstellt einen leeren Vektor (ein wachsender Array).
    let mut vec = Vec::new();
    // Zu diesem Zeitpunkt weiß der Compiler nicht den genauen Typ von `vec`, er
    // weiß nur, dass es ein Vektor von etwas ist (`Vec<_>`).

    // Fügt `elem` in den Vektor ein.
    vec.push(elem);
    // Aha! Jetzt weiß der Compiler, dass `vec` ein Vektor von `u8`-Werten ist (`Vec<u8>`)
    // TODO ^ Versuchen Sie, die Zeile `vec.push(elem)` auszukommentieren

    println!("{:?}", vec);
}
```

Es war keine Typannotation der Variablen erforderlich, der Compiler ist zufrieden und auch der Programmierer!

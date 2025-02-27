# Ungültiger Zugriff auf Array-Elemente

Schauen wir uns an, was passiert, wenn Sie versuchen, auf ein Element eines Arrays zuzugreifen, das außerhalb des Arrays liegt. Stellen Sie sich vor, Sie führen diesen Code aus, der ähnlich dem Ratespiel im Kapitel 2 ist, um einen Array-Index von der Benutzerschaft zu erhalten:

Dateiname: `src/main.rs`

```rust
use std::io;

fn main() {
    let a = [1, 2, 3, 4, 5];

    println!("Bitte geben Sie einen Array-Index ein.");

    let mut index = String::new();

    io::stdin()
     .read_line(&mut index)
     .expect("Fehler beim Lesen der Zeile");

    let index: usize = index
     .trim()
     .parse()
     .expect("Der eingegebene Index war keine Zahl");

    let element = a[index];

    println!(
        "Der Wert des Elements an Index {index} ist: {element}"
    );
}
```

Dieser Code kompiliert erfolgreich. Wenn Sie diesen Code mit `cargo run` ausführen und `0`, `1`, `2`, `3` oder `4` eingeben, wird das Programm den entsprechenden Wert an diesem Index im Array ausgeben. Wenn Sie stattdessen eine Zahl außerhalb des Arrays eingeben, wie `10`, sehen Sie eine Ausgabe wie diese:

    thread 'main' panicked at 'index out of bounds: the len is 5 but the index is
    10', src/main.rs:19:19
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

Das Programm hat einen _Laufzeitfehler_ verursacht, als es einen ungültigen Wert bei der Indizierungsoperation verwendete. Das Programm ist mit einer Fehlermeldung beendet und hat den letzten `println!`-Ausdruck nicht ausgeführt. Wenn Sie versuchen, über die Indizierung auf ein Element zuzugreifen, überprüft Rust, ob der von Ihnen angegebene Index kleiner als die Arraylänge ist. Wenn der Index größer oder gleich der Länge ist, wird Rust in Panik versetzen. Diese Prüfung muss zur Laufzeit erfolgen, insbesondere in diesem Fall, weil der Compiler nicht möglicherweise weiß, welchen Wert ein Benutzer eingeben wird, wenn er den Code später ausführt.

Dies ist ein Beispiel für die Anwendung von Rusts Prinzipien der Arbeitsspeichersicherheit. In vielen niederen Programmiersprachen wird diese Art von Prüfung nicht durchgeführt, und wenn Sie einen falschen Index angeben, kann ungültiger Arbeitsspeicher zugegriffen werden. Rust schützt Sie vor diesem Fehler, indem es sofort beendet, anstatt den Arbeitsspeicherzugriff zuzulassen und fortzufahren. Kapitel 9 behandelt mehr über Rusts Fehlerbehandlung und wie Sie lesbares, sicheres Code schreiben können, der weder in Panik gerät noch ungültigen Arbeitsspeicherzugriff zulässt.

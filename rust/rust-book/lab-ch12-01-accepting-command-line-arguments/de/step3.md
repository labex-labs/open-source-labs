# Speichern der Argumentwerte in Variablen

Das Programm kann derzeit auf die als Befehlszeilenargumente angegebenen Werte zugreifen. Jetzt müssen wir die Werte der beiden Argumente in Variablen speichern, damit wir die Werte im Rest des Programms verwenden können. Wir tun das in Listing 12-2.

Dateiname: `src/main.rs`

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    let query = &args[1];
    let file_path = &args[2];

    println!("Searching for {}", query);
    println!("In file {}", file_path);
}
```

Listing 12-2: Erstellen von Variablen, um das Suchargument und den Dateipfadargument zu speichern

Wie wir gesehen haben, als wir den Vektor ausgegeben haben, nimmt der Programmname den ersten Wert im Vektor bei `args[0]` ein, daher beginnen wir die Argumente bei Index 1. Das erste Argument, das `minigrep` erhält, ist der String, nach dem wir suchen, daher legen wir eine Referenz auf das erste Argument in der Variable `query` ab. Das zweite Argument wird der Dateipfad sein, daher legen wir eine Referenz auf das zweite Argument in der Variable `file_path` ab.

Wir geben die Werte dieser Variablen vorübergehend aus, um zu beweisen, dass der Code wie gewünscht funktioniert. Führen wir dieses Programm erneut mit den Argumenten `test` und `sample.txt` aus:

```bash
$ cargo run -- test sample.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep test sample.txt`
Searching for test
In file sample.txt
```

Super, das Programm funktioniert! Die Werte der Argumente, die wir benötigen, werden in die richtigen Variablen gespeichert. Später werden wir einige Fehlerbehandlungen hinzufügen, um bestimmte potenzielle Fehlerfälle zu behandeln, wie wenn der Benutzer keine Argumente angibt; für jetzt ignorieren wir diese Situation und arbeiten stattdessen an der Hinzufügung von Datei-lesefähigkeiten.

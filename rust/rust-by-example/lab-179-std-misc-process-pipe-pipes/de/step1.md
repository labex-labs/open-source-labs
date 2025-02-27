# Rohre

Die `std::Child`-Struktur repräsentiert einen laufenden Kindprozess und bietet die `stdin`-, `stdout`- und `stderr`-Handles für die Interaktion mit dem zugrunde liegenden Prozess über Rohre an.

```rust
use std::io::prelude::*;
use std::process::{Command, Stdio};

static PANGRAM: &'static str =
"the quick brown fox jumped over the lazy dog\n";

fn main() {
    // Starte den Befehl `wc`
    let process = match Command::new("wc")
                              .stdin(Stdio::piped())
                              .stdout(Stdio::piped())
                              .spawn() {
        Err(why) => panic!("konnte wc nicht starten: {}", why),
        Ok(process) => process,
    };

    // Schreibe einen String in die `stdin` von `wc`.
    //
    // `stdin` hat den Typ `Option<ChildStdin>`, aber da wir wissen, dass diese Instanz
    // sicherlich einen Wert hat, können wir direkt `unwrap` verwenden.
    match process.stdin.unwrap().write_all(PANGRAM.as_bytes()) {
        Err(why) => panic!("konnte nicht in die wc stdin schreiben: {}", why),
        Ok(_) => println!("Pangramm an wc gesendet"),
    }

    // Da `stdin` nach den obigen Aufrufen nicht mehr existiert, wird sie `drop`ed
    // und das Rohr geschlossen.
    //
    // Dies ist sehr wichtig, andernfalls würde `wc` nicht mit der Verarbeitung
    // der von uns gerade gesendeten Eingabe beginnen.

    // Das `stdout`-Feld hat ebenfalls den Typ `Option<ChildStdout>` und muss daher unwrapped werden.
    let mut s = String::new();
    match process.stdout.unwrap().read_to_string(&mut s) {
        Err(why) => panic!("konnte die wc stdout nicht lesen: {}", why),
        Ok(_) => print!("wc hat geantwortet mit:\n{}", s),
    }
}
```

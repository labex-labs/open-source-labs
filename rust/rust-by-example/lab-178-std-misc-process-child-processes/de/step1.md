# Kindprozesse

Die `process::Output`-Struktur repräsentiert die Ausgabe eines abgeschlossenen Kindprozesses, und die `process::Command`-Struktur ist ein Prozessbauer.

```rust
use std::process::Command;

fn main() {
    let output = Command::new("rustc")
     .arg("--version")
     .output().unwrap_or_else(|e| {
            panic!("failed to execute process: {}", e)
    });

    if output.status.success() {
        let s = String::from_utf8_lossy(&output.stdout);

        print!("rustc succeeded and stdout was:\n{}", s);
    } else {
        let s = String::from_utf8_lossy(&output.stderr);

        print!("rustc failed and stderr was:\n{}", s);
    }
}
```

(Es wird empfohlen, das vorherige Beispiel mit einem falschen Flag für `rustc` auszuprobieren)

# Threads

Rust bietet einen Mechanismus zum Erzeugen von nativem Betriebssystem-Threads über die `spawn`-Funktion. Der Argument dieser Funktion ist eine verschiebende Closure.

```rust
use std::thread;

const NTHREADS: u32 = 10;

// Dies ist der `main`-Thread
fn main() {
    // Erzeuge einen Vektor, um die erzeugten Kinder-Threads zu speichern.
    let mut children = vec![];

    for i in 0..NTHREADS {
        // Starte einen weiteren Thread
        children.push(thread::spawn(move || {
            println!("dies ist Threadnummer {}", i);
        }));
    }

    for child in children {
        // Warte, bis der Thread abgeschlossen ist. Gibt ein Ergebnis zurück.
        let _ = child.join();
    }
}
```

Diese Threads werden vom Betriebssystem geplant.

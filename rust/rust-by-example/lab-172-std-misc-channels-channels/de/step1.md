# Kanäle

Rust bietet asynchrone `Kanäle` für die Kommunikation zwischen Threads. Kanäle ermöglichen einen einseitigen Informationsfluss zwischen zwei Endpunkten: dem `Sender` und dem `Receiver`.

```rust
use std::sync::mpsc::{Sender, Receiver};
use std::sync::mpsc;
use std::thread;

static NTHREADS: i32 = 3;

fn main() {
    // Kanäle haben zwei Endpunkte: den `Sender<T>` und den `Receiver<T>`,
    // wobei `T` der Typ der zu übertragenden Nachricht ist
    // (die Typangabe ist überflüssig)
    let (tx, rx): (Sender<i32>, Receiver<i32>) = mpsc::channel();
    let mut children = Vec::new();

    for id in 0..NTHREADS {
        // Der Sender-Endpunkt kann kopiert werden
        let thread_tx = tx.clone();

        // Jeder Thread wird seine ID über den Kanal senden
        let child = thread::spawn(move || {
            // Der Thread erhält die Eigentumsgewalt über `thread_tx`
            // Jeder Thread stellt eine Nachricht in den Kanal ein
            thread_tx.send(id).unwrap();

            // Senden ist eine nicht blockierende Operation, der Thread wird sofort fortfahren
            // nachdem er seine Nachricht gesendet hat
            println!("thread {} finished", id);
        });

        children.push(child);
    }

    // Hier werden alle Nachrichten gesammelt
    let mut ids = Vec::with_capacity(NTHREADS as usize);
    for _ in 0..NTHREADS {
        // Die `recv`-Methode wählt eine Nachricht aus dem Kanal aus
        // `recv` wird den aktuellen Thread blockieren, wenn keine Nachrichten verfügbar sind
        ids.push(rx.recv());
    }

    // Warte, bis die Threads alle verbleibende Arbeit beendet haben
    for child in children {
        child.join().expect("oops! the child thread panicked");
    }

    // Zeige die Reihenfolge, in der die Nachrichten gesendet wurden
    println!("{:?}", ids);
}
```

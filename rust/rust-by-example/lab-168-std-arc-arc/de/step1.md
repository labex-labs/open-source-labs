# Arc

Wenn die gemeinsame Besitzung zwischen Threads erforderlich ist, kann `Arc` (Atomically Reference Counted) verwendet werden. Diese Struktur kann über die `Clone`-Implementierung einen Verweiszeiger auf die Speicheradresse eines Werts im Speicherheap erstellen, während der Referenzzähler erhöht wird. Da sie die Besitzung zwischen Threads teilt, wird die Variable gelöscht, wenn der letzte Verweiszeiger auf einen Wert außerhalb des Gültigkeitsbereichs ist.

```rust
use std::time::Duration;
use std::sync::Arc;
use std::thread;

fn main() {
    // In dieser Variablendeklaration wird der Wert angegeben.
    let apple = Arc::new("the same apple");

    for _ in 0..10 {
        // Hier wird kein Wert angegeben, da es sich um einen Zeiger auf eine
        // Referenz im Speicherheap handelt.
        let apple = Arc::clone(&apple);

        thread::spawn(move || {
            // Da Arc verwendet wurde, können Threads mit dem in der Arc-Variablenzeigeradresse
            // zugewiesenen Wert erstellt werden.
            println!("{:?}", apple);
        });
    }

    // Stellen Sie sicher, dass alle Arc-Instanzen von den erstellten Threads ausgegeben werden.
    thread::sleep(Duration::from_secs(1));
}
```

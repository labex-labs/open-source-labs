# Senden mehrerer Werte und Beobachten des wartenden Empfängers

Der Code in Listing 16-8 hat sich kompiliert und ausgeführt, aber er hat uns nicht eindeutig gezeigt, dass zwei separate Threads über den Kanal miteinander kommunizieren. In Listing 16-10 haben wir einige Änderungen vorgenommen, die beweisen, dass der Code in Listing 16-8 parallel läuft: Der erzeugte Thread wird jetzt mehrere Nachrichten senden und zwischen jeder Nachricht eine Sekunde pausieren.

Dateiname: `src/main.rs`

```rust
use std::sync::mpsc;
use std::thread;
use std::time::Duration;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let vals = vec![
            String::from("hi"),
            String::from("from"),
            String::from("the"),
            String::from("thread"),
        ];

        for val in vals {
            tx.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });

    for received in rx {
        println!("Got: {received}");
    }
}
```

Listing 16-10: Senden mehrerer Nachrichten und Pausieren zwischen jeder

Diesmal hat der erzeugte Thread einen Vektor von Strings, die wir an den Hauptthread senden möchten. Wir iterieren über sie, senden jedes einzeln und pausieren zwischen jedem, indem wir die `thread::sleep`-Funktion mit einem `Duration`-Wert von einer Sekunde aufrufen.

Im Hauptthread rufen wir die `recv`-Funktion nicht mehr explizit auf: Stattdessen behandeln wir `rx` als Iterator. Für jeden empfangenen Wert drucken wir ihn aus. Wenn der Kanal geschlossen wird, endet die Iteration.

Wenn Sie den Code in Listing 16-10 ausführen, sollten Sie die folgende Ausgabe sehen, wobei zwischen jeder Zeile eine Sekunde Pause ist:

    Got: hi
    Got: from
    Got: the
    Got: thread

Da wir keinen Code haben, der in der `for`-Schleife im Hauptthread pausiert oder verzögert, können wir erkennen, dass der Hauptthread auf die Empfang von Werten vom erzeugten Thread wartet.

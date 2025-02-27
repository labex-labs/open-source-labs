# Erstellen eines neuen Threads mit spawn

Um einen neuen Thread zu erstellen, rufen wir die `thread::spawn`-Funktion auf und übergeben ihr eine Closure (wir haben uns in Kapitel 13 mit Closures beschäftigt), die den Code enthält, den wir in dem neuen Thread ausführen möchten. Das Beispiel in Listing 16-1 druckt einige Text aus einem Hauptthread und anderen Text aus einem neuen Thread.

Dateiname: `src/main.rs`

```rust
use std::thread;
use std::time::Duration;

fn main() {
    thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {i} from the spawned thread!");
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("hi number {i} from the main thread!");
        thread::sleep(Duration::from_millis(1));
    }
}
```

Listing 16-1: Erstellen eines neuen Threads, um etwas zu drucken, während der Hauptthread etwas anderes druckt

Beachten Sie, dass wenn der Hauptthread eines Rust-Programms abgeschlossen ist, alle erzeugten Threads beendet werden, unabhängig davon, ob sie fertig ausgeführt sind oder nicht. Die Ausgabe dieses Programms kann jedes Mal etwas anders sein, aber es wird ähnlich wie folgendes aussehen:

    hi number 1 from the main thread!
    hi number 1 from the spawned thread!
    hi number 2 from the main thread!
    hi number 2 from the spawned thread!
    hi number 3 from the main thread!
    hi number 3 from the spawned thread!
    hi number 4 from the main thread!
    hi number 4 from the spawned thread!
    hi number 5 from the spawned thread!

Die Aufrufe von `thread::sleep` zwingen einen Thread, seine Ausführung für eine kurze Zeit zu stoppen, um einen anderen Thread laufen zu lassen. Die Threads werden wahrscheinlich abwechselnd ausgeführt, aber das ist nicht gewährleistet: Es hängt davon ab, wie Ihr Betriebssystem die Threads planst. In dieser Ausführung hat der Hauptthread zuerst gedruckt, obwohl der Print-Befehl aus dem erzeugten Thread zuerst im Code erscheint. Und obwohl wir dem erzeugten Thread gesagt haben, bis `i` 9 zu drucken, hat er erst bis 5 gedruckt, bevor der Hauptthread beendet wurde.

Wenn Sie diesen Code ausführen und nur die Ausgabe des Hauptthreads sehen oder keine Überlappung sehen, versuchen Sie, die Zahlen in den Bereichen zu erhöhen, um mehr Möglichkeiten für das Betriebssystem zu schaffen, zwischen den Threads zu wechseln.

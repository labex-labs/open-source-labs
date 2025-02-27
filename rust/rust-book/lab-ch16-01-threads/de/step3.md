# Warten auf das Ende aller Threads mit join Handles

Der Code in Listing 16-1 stoppt den erzeugten Thread nicht nur meistens vorzeitig aufgrund des Endens des Hauptthreads, sondern auch, weil es keine Garantie gibt, in welcher Reihenfolge die Threads ausgeführt werden, können wir auch nicht garantieren, dass der erzeugte Thread überhaupt ausgeführt wird!

Wir können das Problem des nicht ausgeführten oder vorzeitigen Endens des erzeugten Threads beheben, indem wir den Rückgabewert von `thread::spawn` in einer Variable speichern. Der Rückgabetyp von `thread::spawn` ist `JoinHandle<T>`. Ein `JoinHandle<T>` ist ein eigenes Objekt, das, wenn wir die `join`-Methode darauf aufrufen, auf das Ende seines Threads warten wird. Listing 16-2 zeigt, wie man das `JoinHandle<T>` des Threads, den wir in Listing 16-1 erstellt haben, verwendet und `join` aufruft, um sicherzustellen, dass der erzeugte Thread vor dem Verlassen von `main` abgeschlossen ist.

Dateiname: `src/main.rs`

```rust
use std::thread;
use std::time::Duration;

fn main() {
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {i} from the spawned thread!");
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("hi number {i} from the main thread!");
        thread::sleep(Duration::from_millis(1));
    }

    handle.join().unwrap();
}
```

Listing 16-2: Speichern eines `JoinHandle<T>` von `thread::spawn`, um sicherzustellen, dass der Thread bis zum Abschluss ausgeführt wird

Das Aufrufen von `join` auf dem Handle blockiert den derzeit ausgeführten Thread, bis der von dem Handle dargestellte Thread terminiert. Ein Thread _blockieren_ bedeutet, dass dieser Thread daran gehindert wird, Arbeit auszuführen oder zu beenden. Da wir den Aufruf von `join` nach der `for`-Schleife des Hauptthreads platziert haben, sollte das Ausführen von Listing 16-2 eine Ausgabe ähnlich dieser erzeugen:

    hi number 1 from the main thread!
    hi number 2 from the main thread!
    hi number 1 from the spawned thread!
    hi number 3 from the main thread!
    hi number 2 from the spawned thread!
    hi number 4 from the main thread!
    hi number 3 from the spawned thread!
    hi number 4 from the spawned thread!
    hi number 5 from the spawned thread!
    hi number 6 from the spawned thread!
    hi number 7 from the spawned thread!
    hi number 8 from the spawned thread!
    hi number 9 from the spawned thread!

Die beiden Threads wechseln weiterhin abwechselnd, aber der Hauptthread wartet aufgrund des Aufrufs von `handle.join()` und endet erst, wenn der erzeugte Thread fertig ist.

Aber sehen wir uns an, was passiert, wenn wir `handle.join()` stattdessen vor der `for`-Schleife in `main` verschieben, wie folgt:

Dateiname: `src/main.rs`

```rust
use std::thread;
use std::time::Duration;

fn main() {
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {i} from the spawned thread!");
            thread::sleep(Duration::from_millis(1));
        }
    });

    handle.join().unwrap();

    for i in 1..5 {
        println!("hi number {i} from the main thread!");
        thread::sleep(Duration::from_millis(1));
    }
}
```

Der Hauptthread wird auf das Ende des erzeugten Threads warten und dann seine `for`-Schleife ausführen, sodass die Ausgabe nicht mehr verzahnt ist, wie hier gezeigt:

    hi number 1 from the spawned thread!
    hi number 2 from the spawned thread!
    hi number 3 from the spawned thread!
    hi number 4 from the spawned thread!
    hi number 5 from the spawned thread!
    hi number 6 from the spawned thread!
    hi number 7 from the spawned thread!
    hi number 8 from the spawned thread!
    hi number 9 from the spawned thread!
    hi number 1 from the main thread!
    hi number 2 from the main thread!
    hi number 3 from the main thread!
    hi number 4 from the main thread!

Kleine Details wie der Ort, an dem `join` aufgerufen wird, können sich darauf auswirken, ob Ihre Threads gleichzeitig ausgeführt werden.

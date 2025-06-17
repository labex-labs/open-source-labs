# Atomare Referenzzählung mit Arc`<T>`

Glücklicherweise ist `Arc<T>` ein Typ wie `Rc<T>`, der in konkurrierenden Situationen sicher zu verwenden ist. Der Buchstabe _a_ steht für _atomar_, was bedeutet, dass es ein _atomar referenzzählender_ Typ ist. Atomare Datentypen sind eine weitere Art von konkurrenzspezifischen Primitiven, die wir hier nicht im Detail behandeln werden: Siehe die Standardbibliothek-Dokumentation für `std::sync::atomic` für weitere Details. An diesem Punkt müssen Sie nur wissen, dass atomare Datentypen wie primitive Datentypen funktionieren, aber sicher über Threads hinweg zu teilen sind.

Sie könnten sich dann fragen, warum nicht alle primitiven Datentypen atomar sind und warum Standardbibliothekstypen standardmäßig nicht so implementiert sind, dass sie `Arc<T>` verwenden. Der Grund ist, dass die Threadsicherheit mit einem Leistungsverlust verbunden ist, den Sie nur zahlen möchten, wenn Sie ihn wirklich benötigen. Wenn Sie nur Operationen auf Werten innerhalb eines einzelnen Threads ausführen, kann Ihr Code schneller laufen, wenn er nicht die Garantien erfüllen muss, die atomare Datentypen bieten.

Lassen Sie uns zu unserem Beispiel zurückkehren: `Arc<T>` und `Rc<T>` haben die gleiche API, daher beheben wir unser Programm, indem wir die `use`-Zeile, den Aufruf von `new` und den Aufruf von `clone` ändern. Der Code in Listing 16-15 wird schließlich kompilieren und ausgeführt werden.

Dateiname: `src/main.rs`

```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();

            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Result: {}", *counter.lock().unwrap());
}
```

Listing 16-15: Verwenden eines `Arc<T>` zum Umhüllen des `Mutex<T>`, um die Eigentumsgewalt über mehrere Threads hinweg zu teilen

Dieser Code wird Folgendes ausgeben:

```rust
Result: 10
```

Wir haben es geschafft! Wir haben von 0 bis 10 gezählt, was vielleicht nicht sehr beeindruckend klingt, aber es hat uns viel über `Mutex<T>` und Threadsicherheit gelehrt. Sie könnten auch die Struktur dieses Programms verwenden, um komplexere Operationen durchzuführen, als nur einen Zähler zu erhöhen. Mit dieser Strategie können Sie eine Berechnung in unabhängige Teile unterteilen, diese Teile über Threads verteilen und dann einen `Mutex<T>` verwenden, um jeden Thread seinen Teil mit dem Endresultat zu aktualisieren.

Beachten Sie, dass wenn Sie einfache numerische Operationen durchführen, es Datentypen gibt, die einfacher sind als `Mutex<T>`-Typen, die vom `std::sync::atomic`-Modul der Standardbibliothek bereitgestellt werden. Diese Typen bieten sicheren, konkurrierenden, atomaren Zugang zu primitiven Datentypen. Wir haben für dieses Beispiel einen `Mutex<T>` mit einem primitiven Datentyp verwendet, damit wir uns auf die Funktionsweise von `Mutex<T>` konzentrieren konnten.

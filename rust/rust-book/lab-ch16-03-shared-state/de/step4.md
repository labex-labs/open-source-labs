# Teilen eines Mutex`<T>` Zwischen mehreren Threads

Lassen Sie uns nun versuchen, einen Wert zwischen mehreren Threads mithilfe von `Mutex<T>` zu teilen. Wir starten 10 Threads und lassen sie jeweils einen Zählerwert um 1 erhöhen, sodass der Zähler von 0 auf 10 geht. Das Beispiel in Listing 16-13 wird einen Compilerfehler haben, und wir werden diesen Fehler nutzen, um mehr über die Verwendung von `Mutex<T>` und wie Rust uns hilft, es richtig zu verwenden, zu lernen.

Dateiname: `src/main.rs`

```rust
use std::sync::Mutex;
use std::thread;

fn main() {
  1 let counter = Mutex::new(0);
    let mut handles = vec![];

  2 for _ in 0..10 {
      3 let handle = thread::spawn(move || {
          4 let mut num = counter.lock().unwrap();

          5 *num += 1;
        });
      6 handles.push(handle);
    }

    for handle in handles {
      7 handle.join().unwrap();
    }

  8 println!("Result: {}", *counter.lock().unwrap());
}
```

Listing 16-13: Zehn Threads, die jeweils einen von einem `Mutex<T>` bewachten Zähler um 1 erhöhen

Wir erstellen eine `counter`-Variable, um ein `i32` innerhalb eines `Mutex<T>` zu speichern \[1\], wie wir es in Listing 16-12 getan haben. Als nächstes erstellen wir 10 Threads, indem wir über einen Zahlenbereich iterieren \[2\]. Wir verwenden `thread::spawn` und geben allen Threads die gleiche Closure: eine, die den Zähler in den Thread verschiebt \[3\], einen Lock auf dem `Mutex<T>` erlangt, indem die `lock`-Methode aufgerufen wird \[4\], und dann 1 zum Wert im Mutex hinzufügt \[5\]. Wenn ein Thread mit der Ausführung seiner Closure fertig ist, wird `num` außer Gültigkeitsbereich gehen und den Lock freigeben, sodass ein anderer Thread ihn erwerben kann.

Im Hauptthread sammeln wir alle Join-Handles \[6\]. Dann, wie wir es in Listing 16-2 getan haben, rufen wir `join` auf jedem Handle auf, um sicherzustellen, dass alle Threads fertig sind \[7\]. Zu diesem Zeitpunkt wird der Hauptthread den Lock erwerben und das Ergebnis dieses Programms ausgeben \[8\].

Wir haben angedeutet, dass dieses Beispiel nicht kompilieren würde. Lassen Sie uns nun herausfinden, warum!

```bash
error[E0382]: use of moved value: `counter`
  --> src/main.rs:9:36
   |
5  |     let counter = Mutex::new(0);
   |         ------- move occurs because `counter` has type `Mutex<i32>`, which
does not implement the `Copy` trait
...
9  |         let handle = thread::spawn(move || {
   |                                    ^^^^^^^ value moved into closure here,
in previous iteration of loop
10 |             let mut num = counter.lock().unwrap();
   |                           ------- use occurs due to use in closure
```

Die Fehlermeldung besagt, dass der `counter`-Wert in der vorherigen Iteration der Schleife verschoben wurde. Rust sagt uns, dass wir die Eigentumsgewalt des Locks `counter` nicht in mehrere Threads verschieben können. Lassen Sie uns den Compilerfehler mit der Mehrfach-Eigentumsmethode beheben, die wir im Kapitel 15 diskutiert haben.

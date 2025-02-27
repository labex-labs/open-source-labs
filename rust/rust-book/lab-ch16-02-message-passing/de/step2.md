# Kanäle und Eigentumsübertragung

Die Eigentumsregeln spielen eine entscheidende Rolle bei der Nachrichtenübertragung, da sie Ihnen helfen, sicheres, konkurrierendes Code zu schreiben. Das Vermeiden von Fehlern bei der konkurrierenden Programmierung ist der Vorteil, wenn Sie sich bei der gesamten Rust-Programmierung um das Eigentum kümmern. Lassen Sie uns ein Experiment durchführen, um zu zeigen, wie Kanäle und Eigentum zusammenarbeiten, um Probleme zu vermeiden: wir werden versuchen, einen `val`-Wert im erzeugten Thread _nachdem_ wir ihn über den Kanal gesendet haben, zu verwenden. Versuchen Sie, den Code in Listing 16-9 zu kompilieren, um zu sehen, warum dieser Code nicht zugelassen wird.

Dateiname: `src/main.rs`

```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let val = String::from("hi");
        tx.send(val).unwrap();
        println!("val is {val}");
    });

    let received = rx.recv().unwrap();
    println!("Got: {received}");
}
```

Listing 16-9: Versuch, `val` nach dem Senden über den Kanal zu verwenden

Hier versuchen wir, `val` auszugeben, nachdem wir es über `tx.send` über den Kanal gesendet haben. Dies zuzulassen wäre ein schlechter Gedanke: sobald der Wert an einen anderen Thread gesendet wurde, könnte dieser Thread ihn modifizieren oder löschen, bevor wir versuchen, den Wert erneut zu verwenden. Möglicherweise könnten die Änderungen des anderen Threads aufgrund inkonsistenter oder nicht vorhandener Daten Fehler oder unerwartete Ergebnisse verursachen. Rust gibt uns jedoch einen Fehler, wenn wir versuchen, den Code in Listing 16-9 zu kompilieren:

```bash
error[E0382]: borrow of moved value: `val`
  --> src/main.rs:10:31
   |
8  |         let val = String::from("hi");
   |             --- move occurs because `val` has type `String`, which does
not implement the `Copy` trait
9  |         tx.send(val).unwrap();
   |                 --- value moved here
10 |         println!("val is {val}");
   |                           ^^^ value borrowed here after move
```

Unser konkurrierender Fehler hat einen Kompilierungsfehler verursacht. Die `send`-Funktion übernimmt die Eigentumsgewalt über ihren Parameter, und wenn der Wert verschoben wird, übernimmt der Empfänger die Eigentumsgewalt darüber. Dies verhindert, dass wir versehentlich den Wert erneut verwenden, nachdem wir ihn gesendet haben; das Eigentumssystem überprüft, dass alles in Ordnung ist.

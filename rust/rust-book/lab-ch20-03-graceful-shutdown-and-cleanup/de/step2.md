# Implementieren des Drop-Traits für ThreadPool

Lassen Sie uns beginnen, indem wir `Drop` für unseren Threadpool implementieren. Wenn der Pool gelöscht wird, sollten alle unsere Threads `join` aufrufen, um sicherzustellen, dass sie ihre Arbeit beenden. Listing 20-22 zeigt einen ersten Versuch einer `Drop`-Implementierung; dieser Code funktioniert noch nicht ganz.

Dateiname: `src/lib.rs`

```rust
impl Drop for ThreadPool {
    fn drop(&mut self) {
      1 for worker in &mut self.workers {
          2 println!("Shutting down worker {}", worker.id);

          3 worker.thread.join().unwrap();
        }
    }
}
```

Listing 20-22: Joinen jedes Threads, wenn der Threadpool außerhalb des Gültigkeitsbereichs geht

Zunächst durchlaufen wir jeden `Worker` im Threadpool \[1\]. Wir verwenden `&mut` dafür, weil `self` eine mutable Referenz ist und wir auch `worker` mutieren müssen. Für jeden `Worker` drucken wir eine Nachricht, die besagt, dass diese bestimmte `Worker`-Instanz heruntergefahren wird \[2\], und rufen dann `join` auf dem Thread dieser `Worker`-Instanz auf \[3\]. Wenn der Aufruf von `join` fehlschlägt, verwenden wir `unwrap`, um Rust zu einem Panik zu bringen und in einen ungracefulen Shutdown zu gehen.

Hier ist der Fehler, den wir erhalten, wenn wir diesen Code kompilieren:

```bash
error[E0507]: cannot move out of `worker.thread` which is behind a mutable
reference
    --> src/lib.rs:52:13
     |
52   |             worker.thread.join().unwrap();
     |             ^^^^^^^^^^^^^ ------ `worker.thread` moved due to this
method call
     |             |
     |             move occurs because `worker.thread` has type
`JoinHandle<()>`, which does not implement the `Copy` trait
     |
note: this function takes ownership of the receiver `self`, which moves
`worker.thread`
```

Der Fehler sagt uns, dass wir `join` nicht aufrufen können, weil wir nur eine mutable Referenz auf jeden `worker` haben und `join` die Eigentumsgewalt über seinen Argument nimmt. Um dieses Problem zu lösen, müssen wir den Thread aus der `Worker`-Instanz, die `thread` besitzt, herausbewegen, damit `join` den Thread konsumieren kann. Wir haben das in Listing 17-15 gemacht: Wenn `Worker` ein `Option<thread::JoinHandle<()>>` hält, können wir die `take`-Methode auf dem `Option` aufrufen, um den Wert aus der `Some`-Variante herauszubewegen und an seiner Stelle eine `None`-Variante zu hinterlassen. Mit anderen Worten, ein laufender `Worker` wird in `thread` eine `Some`-Variante haben, und wenn wir einen `Worker` bereinigen möchten, ersetzen wir `Some` mit `None`, sodass der `Worker` keinen Thread mehr zum Ausführen hat.

Wir wissen also, dass wir die Definition von `Worker` so aktualisieren möchten:

Dateiname: `src/lib.rs`

```rust
struct Worker {
    id: usize,
    thread: Option<thread::JoinHandle<()>>,
}
```

Lassen Sie uns jetzt auf den Compiler vertrauen, um die anderen Stellen zu finden, die geändert werden müssen. Wenn wir diesen Code überprüfen, erhalten wir zwei Fehler:

```bash
error[E0599]: no method named `join` found for enum `Option` in the current
scope
  --> src/lib.rs:52:27
   |
52 |             worker.thread.join().unwrap();
   |                           ^^^^ method not found in
`Option<JoinHandle<()>>`

error[E0308]: mismatched types
  --> src/lib.rs:72:22
   |
72 |         Worker { id, thread }
   |                      ^^^^^^ expected enum `Option`, found struct
`JoinHandle`
   |
   = note: expected enum `Option<JoinHandle<()>>`
            found struct `JoinHandle<_>`
help: try wrapping the expression in `Some`
   |
72 |         Worker { id, thread: Some(thread) }
   |                      +++++++++++++      +
```

Lassen Sie uns uns zunächst den zweiten Fehler ansehen, der auf den Code am Ende von `Worker::new` zeigt; wir müssen den `thread`-Wert in `Some` umschließen, wenn wir eine neue `Worker` erstellen. Machen Sie die folgenden Änderungen, um diesen Fehler zu beheben:

Dateiname: `src/lib.rs`

```rust
impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        --snip--

        Worker {
            id,
            thread: Some(thread),
        }
    }
}
```

Der erste Fehler befindet sich in unserer `Drop`-Implementierung. Wir haben zuvor erwähnt, dass wir die `take`-Methode auf dem `Option`-Wert aufrufen möchten, um `thread` aus `worker` herauszubewegen. Die folgenden Änderungen werden dies tun:

Dateiname: `src/lib.rs`

```rust
impl Drop for ThreadPool {
    fn drop(&mut self) {
        for worker in &mut self.workers {
            println!("Shutting down worker {}", worker.id);

          1 if let Some(thread) = worker.thread.take() {
              2 thread.join().unwrap();
            }
        }
    }
}
```

Wie in Kapitel 17 diskutiert, nimmt die `take`-Methode auf `Option` die `Some`-Variante heraus und lässt `None` an ihrer Stelle. Wir verwenden `if let`, um die `Some` zu zerlegen und den Thread zu erhalten \[1\]; dann rufen wir `join` auf dem Thread auf \[2\]. Wenn der Thread einer `Worker`-Instanz bereits `None` ist, wissen wir, dass der Thread von `Worker` bereits bereinigt wurde, sodass in diesem Fall nichts passiert.

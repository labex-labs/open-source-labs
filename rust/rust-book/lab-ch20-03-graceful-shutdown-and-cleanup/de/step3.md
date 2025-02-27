# Signalieren an die Threads, dass sie auf Jobs warten sollen

Mit all den Änderungen, die wir vorgenommen haben, compiliert unser Code ohne Warnungen. Die schlechte Nachricht ist jedoch, dass dieser Code noch nicht so funktioniert, wie wir es möchten. Der Schlüssel liegt in der Logik in den Closures, die von den Threads der `Worker`-Instanzen ausgeführt werden: Momentan rufen wir `join` auf, aber das wird die Threads nicht herunterfahren, weil sie in einer Endlosschleife `loop` laufen, um Jobs zu suchen. Wenn wir versuchen, unseren `ThreadPool` mit unserer aktuellen `drop`-Implementierung zu löschen, wird der Hauptthread für immer blockieren und auf den ersten Thread warten, bis er fertig ist.

Um dieses Problem zu beheben, müssen wir eine Änderung in der `ThreadPool`-`drop`-Implementierung vornehmen und dann eine Änderung in der `Worker`-Schleife.

Zunächst ändern wir die `ThreadPool`-`drop`-Implementierung, um `sender` explizit zu löschen, bevor wir auf die Threads warten, bis sie fertig sind. Listing 20-23 zeigt die Änderungen an `ThreadPool`, um `sender` explizit zu löschen. Wir verwenden die gleiche `Option`- und `take`-Technik wie bei dem Thread, um `sender` aus `ThreadPool` herausbewegen zu können.

Dateiname: `src/lib.rs`

```rust
pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: Option<mpsc::Sender<Job>>,
}
--snip--
impl ThreadPool {
    pub fn new(size: usize) -> ThreadPool {
        --snip--

        ThreadPool {
            workers,
            sender: Some(sender),
        }
    }

    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() + Send + 'static,
    {
        let job = Box::new(f);

        self.sender
           .as_ref()
           .unwrap()
           .send(job)
           .unwrap();
    }
}

impl Drop for ThreadPool {
    fn drop(&mut self) {
      1 drop(self.sender.take());

        for worker in &mut self.workers {
            println!("Shutting down worker {}", worker.id);

            if let Some(thread) = worker.thread.take() {
                thread.join().unwrap();
            }
        }
    }
}
```

Listing 20-23: Explizites Löschen von `sender` vor dem Joinen der `Worker`-Threads

Das Löschen von `sender` \[1\] schließt den Kanal, was bedeutet, dass keine weiteren Nachrichten gesendet werden. Wenn das passiert, werden alle Aufrufe von `recv`, die die `Worker`-Instanzen in der Endlosschleife ausführen, einen Fehler zurückgeben. In Listing 20-24 ändern wir die `Worker`-Schleife, um in diesem Fall die Schleife elegant zu verlassen, was bedeutet, dass die Threads beendet werden, wenn die `ThreadPool`-`drop`-Implementierung `join` auf sie aufruft.

Dateiname: `src/lib.rs`

```rust
impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        let thread = thread::spawn(move || loop {
            let message = receiver.lock().unwrap().recv();

            match message {
                Ok(job) => {
                    println!(
                        "Worker {id} got a job; executing."
                    );

                    job();
                }
                Err(_) => {
                    println!(
                        "Worker {id} shutting down."
                    );
                    break;
                }
            }
        });

        Worker {
            id,
            thread: Some(thread),
        }
    }
}
```

Listing 20-24: Explizites Beenden der Schleife, wenn `recv` einen Fehler zurückgibt

Um diesen Code in Aktion zu sehen, ändern wir `main`, um nur zwei Anfragen zu akzeptieren, bevor wir den Server gracefully herunterfahren, wie in Listing 20-25 gezeigt.

Dateiname: `src/main.rs`

```rust
fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
    let pool = ThreadPool::new(4);

    for stream in listener.incoming().take(2) {
        let stream = stream.unwrap();

        pool.execute(|| {
            handle_connection(stream);
        });
    }

    println!("Shutting down.");
}
```

Listing 20-25: Herunterfahren des Servers nach der Verarbeitung von zwei Anfragen, indem die Schleife verlassen wird

Ein echter Webserver würde sicherlich nicht nach nur zwei Anfragen herunterfahren. Dieser Code demonstriert nur, dass der gracefull Shutdown und die Bereinigung funktionieren.

Die `take`-Methode ist in dem `Iterator`-Trait definiert und begrenzt die Iteration auf höchstens die ersten zwei Elemente. Der `ThreadPool` wird am Ende von `main` außerhalb des Gültigkeitsbereichs gehen, und die `drop`-Implementierung wird ausgeführt.

Starten Sie den Server mit `cargo run` und machen Sie drei Anfragen. Die dritte Anfrage sollte einen Fehler ergeben, und in Ihrem Terminal sollten Sie eine Ausgabe ähnlich der folgenden sehen:

```bash
$ cargo run
   Compiling hello v0.1.0 (file:///projects/hello)
    Finished dev [unoptimized + debuginfo] target(s) in 1.0s
     Running `target/debug/hello`
Worker 0 got a job; executing.
Shutting down.
Shutting down worker 0
Worker 3 got a job; executing.
Worker 1 disconnected; shutting down.
Worker 2 disconnected; shutting down.
Worker 3 disconnected; shutting down.
Worker 0 disconnected; shutting down.
Shutting down worker 1
Shutting down worker 2
Shutting down worker 3
```

Sie könnten eine andere Reihenfolge von `Worker`-IDs und gedruckten Nachrichten sehen. Wir können sehen, wie dieser Code funktioniert, anhand der Nachrichten: Die `Worker`-Instanzen 0 und 3 erhielten die ersten zwei Anfragen. Der Server hat nach der zweiten Verbindung aufgehört, neue Verbindungen anzunehmen, und die `Drop`-Implementierung auf `ThreadPool` beginnt, bevor `Worker` 3 seine Aufgabe einmal gestartet hat, auszuführen. Das Löschen von `sender` trennt alle `Worker`-Instanzen und sagt ihnen, sich herunterzufahren. Die `Worker`-Instanzen drucken jeweils eine Nachricht, wenn sie getrennt werden, und dann ruft der Threadpool `join` auf, um auf jeden `Worker`-Thread zu warten, bis er fertig ist.

Bemerken Sie einen interessanten Aspekt dieser speziellen Ausführung: Der `ThreadPool` hat `sender` gelöscht, und bevor eine `Worker` einen Fehler erhalten hat, haben wir versucht, `Worker` 0 zu joinen. `Worker` 0 hatte noch keinen Fehler von `recv` erhalten, also blockierte der Hauptthread und wartete auf `Worker` 0, bis er fertig war. Inzwischen hat `Worker` 3 einen Job erhalten, und dann haben alle Threads einen Fehler erhalten. Wenn `Worker` 0 fertig war, hat der Hauptthread auf die restlichen `Worker`-Instanzen gewartet, bis sie fertig waren. Zu diesem Zeitpunkt waren sie alle aus ihrer Schleife herausgekommen und gestoppt.

Glückwunsch! Wir haben jetzt unser Projekt abgeschlossen; wir haben einen einfachen Webserver, der einen Threadpool verwendet, um asynchron zu reagieren. Wir können den Server gracefully herunterfahren, was alle Threads im Pool bereinigt. Siehe *https://www.nostarch.com/Rust2021*, um den vollständigen Code für dieses Kapitel herunterzuladen, um ihn als Referenz zu verwenden.

Wir könnten hier noch mehr tun! Wenn Sie das Projekt weiter verbessern möchten, hier sind einige Ideen:

- Fügen Sie mehr Dokumentation zu `ThreadPool` und seinen öffentlichen Methoden hinzu.
- Fügen Sie Tests der Funktionalität der Bibliothek hinzu.
- Ändern Sie die Aufrufe von `unwrap` zu einem robusteren Fehlerhandling.
- Verwenden Sie `ThreadPool`, um eine andere Aufgabe als das Beantworten von Webanfragen auszuführen.
- Suchen Sie auf *https://crates.io* einen Threadpool-Crate und implementieren Sie einen ähnlichen Webserver mit dem Crate. Vergleichen Sie dann seine API und Robustheit mit dem von unserem Threadpool.

# Implementierung der execute-Methode

Implementieren wir endlich die `execute`-Methode auf `ThreadPool`. Wir ändern auch `Job` von einer Struktur zu einem Typalias für ein Traitobjekt, das den Typ der Closure enthält, die `execute` erhält. Wie in "Erstellen von Typbezeichnungen mit Typaliasen" diskutiert, ermöglichen Typaliasen es uns, lange Typen zu verkürzen, um die Verwendung zu erleichtern. Schauen Sie sich Listing 20-19 an.

Dateiname: `src/lib.rs`

```rust
--snip--

type Job = Box<dyn FnOnce() + Send + 'static>;

impl ThreadPool {
    --snip--

    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() + Send + 'static,
    {
      1 let job = Box::new(f);

      2 self.sender.send(job).unwrap();
    }
}

--snip--
```

Listing 20-19: Erstellen eines `Job`-Typaliases für eine `Box`, die jede Closure enthält, und das Senden der Aufgabe über den Kanal

Nachdem wir eine neue `Job`-Instanz mit der Closure erstellt haben, die wir in `execute` erhalten \[1\], senden wir diese Aufgabe über das sendende Ende des Kanals \[2\]. Wir rufen `unwrap` auf `send` für den Fall, dass das Senden fehlschlägt. Dies kann z. B. passieren, wenn wir alle unsere Threads davon abhalten, auszuführen, was bedeutet, dass das empfangende Ende aufhört, neue Nachrichten zu empfangen. Momentan können wir unsere Threads nicht davon abhalten, auszuführen: unsere Threads führen fort, solange der Pool existiert. Der Grund, warum wir `unwrap` verwenden, ist, dass wir wissen, dass der Fehlerfall nicht auftreten wird, aber der Compiler weiß das nicht.

Aber wir sind noch nicht fertig! Im `Worker` verweist die von uns an `thread::spawn` übergebene Closure immer noch nur auf das empfangende Ende des Kanals. Stattdessen müssen wir die Closure so gestalten, dass sie für immer in einer Schleife läuft, das empfangende Ende des Kanals nach einer Aufgabe fragt und die Aufgabe ausführt, wenn sie eine erhält. Lassen Sie uns die in Listing 20-20 gezeigten Änderungen an `Worker::new` vornehmen.

Dateiname: `src/lib.rs`

```rust
--snip--

impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        let thread = thread::spawn(move || loop {
            let job = receiver
              1.lock()
              2.unwrap()
              3.recv()
              4.unwrap();

            println!("Worker {id} got a job; executing.");

            job();
        });

        Worker { id, thread }
    }
}
```

Listing 20-20: Empfangen und Ausführen der Aufgaben im Thread der `Worker`-Instanz

Hier rufen wir zunächst `lock` auf dem `receiver` auf, um den Mutex zu erwerben \[1\], und rufen dann `unwrap` auf, um bei jedem Fehler abzustürzen \[2\]. Das Erwerben eines Locks kann fehlschlagen, wenn der Mutex in einem _vergifteten_ Zustand ist, was passieren kann, wenn ein anderer Thread während des Halten des Locks abgestürzt ist, anstatt den Lock freizugeben. In dieser Situation ist es die richtige Aktion, `unwrap` aufzurufen, um diesen Thread abzustürzen. Sie können diese `unwrap` gerne in ein `expect` mit einer Ihnen sinnvollen Fehlermeldung umwandeln.

Wenn wir den Lock am Mutex erhalten, rufen wir `recv` auf, um eine `Job` aus dem Kanal zu empfangen \[3\]. Ein abschließendes `unwrap` überspringt auch hier alle Fehler \[4\], die auftreten können, wenn der Thread, der den Sender hält, heruntergefahren ist, ähnlich wie die `send`-Methode `Err` zurückgibt, wenn der Empfänger heruntergefahren ist.

Der Aufruf von `recv` blockiert, sodass der aktuelle Thread warten wird, wenn noch keine Aufgabe vorhanden ist, bis eine Aufgabe verfügbar wird. Das `Mutex<T>` stellt sicher, dass nur ein `Worker`-Thread zu einem Zeitpunkt versucht, eine Aufgabe anzufordern.

Unser Threadpool ist jetzt im funktionierenden Zustand! Geben Sie `cargo run` aus und stellen Sie einige Anfragen:

```bash
[object Object]
```

Erfolg! Wir haben jetzt einen Threadpool, der Verbindungen asynchron ausführt. Es werden nie mehr als vier Threads erstellt, sodass unser System nicht überlastet wird, wenn der Server viele Anfragen erhält. Wenn wir eine Anfrage an _/sleep_ stellen, kann der Server andere Anfragen bedienen, indem ein anderer Thread sie ausführt.

> Hinweis: Wenn Sie _/sleep_ gleichzeitig in mehreren Browserfenstern öffnen, können sie möglicherweise mit fünf-sekündigen Intervallen nacheinander geladen werden. Einige Webbrowser führen mehrere Instanzen derselben Anfrage sequentiell aus, um die Caching-Effizienz zu erhöhen. Diese Einschränkung wird nicht von unserem Webserver verursacht.

Nachdem Sie in Kapitel 18 über die `while let`-Schleife gelernt haben, könnten Sie sich fragen, warum wir den `Worker`-Thread-Code nicht wie in Listing 20-21 geschrieben haben.

Dateiname: `src/lib.rs`

```rust
--snip--

impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        let thread = thread::spawn(move || {
            while let Ok(job) = receiver.lock().unwrap().recv() {
                println!("Worker {id} got a job; executing.");

                job();
            }
        });

        Worker { id, thread }
    }
}
```

Listing 20-21: Eine alternative Implementierung von `Worker::new` mit `while let`

Dieser Code kompiliert und läuft, führt jedoch nicht das gewünschte Threadverhalten aus: Ein langsamer Request wird immer noch andere Requests dazu bringen, zu warten, bis sie verarbeitet werden. Der Grund ist etwas subtil: Die `Mutex`-Struktur hat keine öffentliche `unlock`-Methode, weil die Eigentumsgewalt am Lock von der Lebensdauer des `MutexGuard<T>` innerhalb des `LockResult<MutexGuard<T>>` abhängt, das die `lock`-Methode zurückgibt. Zur Compile-Zeit kann der Entleihensprüfer dann die Regel erzwingen, dass eine von einem `Mutex` geschützte Ressource nicht zugegriffen werden kann, es sei denn, wir halten den Lock. Allerdings kann diese Implementierung auch dazu führen, dass der Lock länger gehalten wird, als intendiert, wenn wir nicht auf die Lebensdauer des `MutexGuard<T>` achten.

Der Code in Listing 20-20, der `let job = receiver.lock().unwrap().recv().unwrap();` verwendet, funktioniert, weil mit `let` alle temporären Werte, die im Ausdruck auf der rechten Seite des Gleichheitszeichens verwendet werden, sofort verworfen werden, wenn die `let`-Anweisung endet. `while let` (und `if let` und `match`) hingegen verwirft temporäre Werte erst am Ende des zugehörigen Blocks. In Listing 20-21 bleibt der Lock während des Aufrufs von `job()` gehalten, was bedeutet, dass andere `Worker`-Instanzen keine Jobs empfangen können.

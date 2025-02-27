# Senden von Anfragen an Threads über Kanäle

Das nächste Problem, das wir angehen werden, ist, dass die Closures, die an `thread::spawn` übergeben werden, absolut nichts tun. Derzeit erhalten wir die Closure, die wir ausführen möchten, in der `execute`-Methode. Aber wir müssen `thread::spawn` eine Closure geben, die beim Erstellen jedes `Worker` während der Erstellung des `ThreadPool` ausgeführt wird.

Wir möchten, dass die von uns gerade erstellten `Worker`-Strukturen den Code, der ausgeführt werden soll, aus einer Warteschlange im `ThreadPool` abrufen und diesen Code an ihren Thread senden, um ausgeführt zu werden.

Die Kanäle, über die wir in Kapitel 16 gelernt haben - eine einfache Möglichkeit, zwischen zwei Threads zu kommunizieren - wären für diesen Anwendungsfall perfekt. Wir werden einen Kanal verwenden, um als Warteschlange für die Aufgaben zu fungieren, und `execute` wird eine Aufgabe vom `ThreadPool` an die `Worker`-Instanzen senden, die die Aufgabe an ihren Thread senden werden. Hier ist der Plan:

1. Der `ThreadPool` wird einen Kanal erstellen und den Sender beibehalten.
2. Jeder `Worker` wird den Empfänger beibehalten.
3. Wir werden eine neue `Job`-Struktur erstellen, die die Closures enthält, die wir über den Kanal senden möchten.
4. Die `execute`-Methode wird die Aufgabe, die sie ausführen möchte, über den Sender senden.
5. In seinem Thread wird der `Worker` in einer Schleife über seinen Empfänger iterieren und die Closures aller empfangenen Aufgaben ausführen.

Lassen Sie uns beginnen, indem wir in `ThreadPool::new` einen Kanal erstellen und den Sender im `ThreadPool`-Instanz beibehalten, wie in Listing 20-16 gezeigt. Die `Job`-Struktur enthält für jetzt nichts, wird aber der Typ der Elemente sein, die wir über den Kanal senden.

Dateiname: `src/lib.rs`

```rust
use std::{sync::mpsc, thread};

pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: mpsc::Sender<Job>,
}

struct Job;

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

      1 let (sender, receiver) = mpsc::channel();

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(Worker::new(id));
        }

        ThreadPool { workers, 2 sender }
    }
    --snip--
}
```

Listing 20-16: Ändern von `ThreadPool`, um den Sender eines Kanals zu speichern, der `Job`-Instanzen überträgt

In `ThreadPool::new` erstellen wir unseren neuen Kanal \[1\] und lassen den Pool den Sender beibehalten \[2\]. Dies wird erfolgreich kompilieren.

Lassen Sie uns versuchen, einen Empfänger des Kanals an jedes `Worker` zu übergeben, wenn der Threadpool den Kanal erstellt. Wir wissen, dass wir den Empfänger im Thread verwenden möchten, den die `Worker`-Instanzen erzeugen, daher werden wir auf den `receiver`-Parameter in der Closure verweisen. Der Code in Listing 20-17 wird noch nicht ganz kompilieren.

Dateiname: `src/lib.rs`

```rust
impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
          1 workers.push(Worker::new(id, receiver));
        }

        ThreadPool { workers, sender }
    }
    --snip--
}

--snip--

impl Worker {
    fn new(id: usize, receiver: mpsc::Receiver<Job>) -> Worker {
        let thread = thread::spawn(|| {
          2 receiver;
        });

        Worker { id, thread }
    }
}
```

Listing 20-17: Übergeben des Empfängers an jedes `Worker`

Wir haben einige kleine und einfache Änderungen vorgenommen: wir übergeben den Empfänger an `Worker::new` \[1\], und verwenden ihn dann innerhalb der Closure \[2\].

Wenn wir diesen Code überprüfen möchten, erhalten wir diesen Fehler:

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0382]: use of moved value: `receiver`
  --> src/lib.rs:26:42
   |
21 |         let (sender, receiver) = mpsc::channel();
   |                      -------- move occurs because `receiver` has type
`std::sync::mpsc::Receiver<Job>`, which does not implement the `Copy` trait
...
26 |             workers.push(Worker::new(id, receiver));
   |                                          ^^^^^^^^ value moved here, in
previous iteration of loop
```

Der Code versucht, `receiver` an mehrere `Worker`-Instanzen zu übergeben. Dies wird nicht funktionieren, wie Sie sich aus Kapitel 16 erinnern werden: Die von Rust bereitgestellte Kanalimplementierung ist ein Mehrfach-_Produzent_, Einzel-_Verbraucher_. Dies bedeutet, dass wir den konsumierenden Endpunkt des Kanals nicht einfach klonen können, um diesen Code zu beheben. Wir möchten auch keine Nachricht mehrfach an mehrere Konsumenten senden; wir möchten eine Liste von Nachrichten mit mehreren `Worker`-Instanzen haben, sodass jede Nachricht einmal verarbeitet wird.

Zusätzlich erfordert das Entnehmen einer Aufgabe aus der Kanalwarteschlange die Veränderung des `Empfängers`, daher müssen die Threads eine sichere Möglichkeit haben, `Empfänger` zu teilen und zu verändern; andernfalls könnten wir Wettlaufbedingungen erhalten (wie in Kapitel 16 behandelt).

Denken Sie an die in Kapitel 16 diskutierten thread-sicheren Smart-Pointer: um die Eigentumsgewalt über mehrere Threads zu teilen und den Threads die Möglichkeit zu geben, den Wert zu verändern, müssen wir `Arc<Mutex<T>>` verwenden. Der `Arc`-Typ wird es mehreren `Worker`-Instanzen ermöglichen, den Empfänger zu besitzen, und `Mutex` wird sicherstellen, dass nur ein `Worker` zu einem Zeitpunkt eine Aufgabe aus dem Empfänger bekommt. Listing 20-18 zeigt die Änderungen, die wir vornehmen müssen.

Dateiname: `src/lib.rs`

```rust
use std::{
    sync::{mpsc, Arc, Mutex},
    thread,
};
--snip--

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

      1 let receiver = Arc::new(Mutex::new(receiver));

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(
                Worker::new(id, Arc::clone(& 2 receiver))
            );
        }

        ThreadPool { workers, sender }
    }

    --snip--
}

--snip--

impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        --snip--
    }
}
```

Listing 20-18: Teilen des Empfängers unter den `Worker`-Instanzen mit `Arc` und `Mutex`

In `ThreadPool::new` legen wir den Empfänger in einen `Arc` und ein `Mutex` \[1\]. Für jeden neuen `Worker` klonen wir den `Arc`, um den Verweiszähler zu erhöhen, sodass die `Worker`-Instanzen die Eigentumsgewalt am Empfänger teilen können \[2\].

Mit diesen Änderungen kompiliert der Code! Wir kommen immer näher!

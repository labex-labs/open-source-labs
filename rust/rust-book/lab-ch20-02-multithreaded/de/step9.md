# Übermitteln von Code aus dem ThreadPool an einen Thread

Wir haben in der `for`-Schleife in Listing 20-14 einen Kommentar zu der Erstellung von Threads hinterlassen. Hier werden wir uns ansehen, wie wir tatsächlich Threads erstellen. Die Standardbibliothek bietet `thread::spawn` als Möglichkeit zum Erstellen von Threads an, und `thread::spawn` erwartet, dass es Code bekommt, den der Thread sofort ausführen soll, sobald er erstellt wurde. Im unseren Fall möchten wir jedoch die Threads erstellen und sie _warten_ auf Code, den wir später senden werden. Die Implementierung der Threads in der Standardbibliothek bietet keine Möglichkeit dazu; wir müssen es manuell implementieren.

Wir werden dieses Verhalten implementieren, indem wir eine neue Datenstruktur zwischen dem `ThreadPool` und den Threads einführen, die dieses neue Verhalten verwalten wird. Wir werden diese Datenstruktur _Worker_ nennen, was ein üblicher Begriff in Poolimplementierungen ist. Der `Worker` nimmt Code auf, der ausgeführt werden muss, und führt ihn in seinem Thread aus.

Denken Sie an Menschen, die in der Küche eines Restaurants arbeiten: Die Mitarbeiter warten, bis Bestellungen von Kunden eintreffen, und sind dann für die Aufnahme und Erfüllung dieser Bestellungen verantwortlich.

Anstatt einen Vektor von `JoinHandle<()>`-Instanzen im Threadpool zu speichern, werden wir Instanzen der `Worker`-Struktur speichern. Jeder `Worker` wird eine einzelne `JoinHandle<()>`-Instanz speichern. Dann implementieren wir eine Methode auf `Worker`, die eine Closure mit Code zum Ausführen aufnimmt und sie an den bereits laufenden Thread sendet, um ausgeführt zu werden. Wir geben auch jedem `Worker` eine `id`, damit wir zwischen den verschiedenen Instanzen von `Worker` im Pool unterscheiden können, wenn wir protokollieren oder debuggen.

Hier ist der neue Prozess, der stattfinden wird, wenn wir einen `ThreadPool` erstellen. Wir werden den Code implementieren, der die Closure an den Thread sendet, nachdem wir `Worker` auf diese Weise eingerichtet haben:

1. Definieren Sie eine `Worker`-Struktur, die eine `id` und ein `JoinHandle<()>` enthält.
2. Ändern Sie `ThreadPool`, um einen Vektor von `Worker`-Instanzen zu speichern.
3. Definieren Sie eine `Worker::new`-Funktion, die eine `id`-Nummer annimmt und eine `Worker`-Instanz zurückgibt, die die `id` und einen mit einer leeren Closure erzeugten Thread enthält.
4. In `ThreadPool::new` verwenden Sie den `for`-Schleifen-Zähler, um eine `id` zu generieren, erstellen Sie einen neuen `Worker` mit dieser `id` und speichern Sie den `Worker` im Vektor.

Wenn Sie sich für eine Herausforderung interessieren, versuchen Sie, diese Änderungen selbst zu implementieren, bevor Sie sich den Code in Listing 20-15 ansehen.

Bereit? Hier ist Listing 20-15 mit einer Möglichkeit, die vorangegangenen Änderungen vorzunehmen.

Dateiname: `src/lib.rs`

```rust
use std::thread;

pub struct ThreadPool {
  1 workers: Vec<Worker>,
}

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let mut workers = Vec::with_capacity(size);

      2 for id in 0..size {
          3 workers.push(Worker::new(id));
        }

        ThreadPool { workers }
    }
    --snip--
}

4 struct Worker {
    id: usize,
    thread: thread::JoinHandle<()>,
}

impl Worker {
  5 fn new(id: usize) -> Worker {
      6 let thread = thread::spawn(|| {});

        Worker { 7 id, 8 thread }
    }
}
```

Listing 20-15: Ändern von `ThreadPool`, um `Worker`-Instanzen zu speichern, anstatt Threads direkt zu speichern

Wir haben den Namen des Felds in `ThreadPool` von `threads` in `workers` geändert, weil es jetzt `Worker`-Instanzen statt `JoinHandle<()>`-Instanzen speichert \[1\]. Wir verwenden den Zähler in der `for`-Schleife \[2\] als Argument für `Worker::new` und speichern jede neue `Worker` im Vektor namens `workers` \[3\].

Externer Code (wie unser Server in `src/main.rs`) muss nicht die Implementierungsdetails kennen, die bei der Verwendung einer `Worker`-Struktur innerhalb von `ThreadPool` auftreten, daher machen wir die `Worker`-Struktur \[4\] und ihre `new`-Funktion \[5\] privat. Die `Worker::new`-Funktion verwendet die `id`, die wir ihr geben \[7\], und speichert eine `JoinHandle<()>`-Instanz \[8\], die durch das Erzeugen eines neuen Threads mit einer leeren Closure erstellt wird \[6\].

> Hinweis: Wenn das Betriebssystem keinen Thread erstellen kann, weil es nicht genug Systemressourcen hat, wird `thread::spawn` abstürzen. Dadurch wird unser ganzer Server abstürzen, auch wenn die Erstellung einiger Threads erfolgreich sein mag. Aus Gründen der Einfachheit ist dieses Verhalten in Ordnung, aber in einer produktiven Threadpool-Implementierung würden Sie wahrscheinlich `std::thread::Builder` und seine `spawn`-Methode verwenden, die `Result` zurückgibt.

Dieser Code wird kompilieren und die Anzahl der `Worker`-Instanzen speichern, die wir als Argument für `ThreadPool::new` angegeben haben. Aber wir verarbeiten _noch_ immer nicht die Closure, die wir in `execute` erhalten. Schauen wir uns an, wie das geht, im nächsten Schritt.

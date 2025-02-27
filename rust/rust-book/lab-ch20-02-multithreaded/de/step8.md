# Platz zum Speichern der Threads erstellen

Jetzt, da wir eine Möglichkeit haben, zu wissen, dass wir eine gültige Anzahl von Threads im Pool speichern können, können wir diese Threads erstellen und im `ThreadPool`-Struktur speichern, bevor wir die Struktur zurückgeben. Aber wie "speichern" wir einen Thread? Schauen wir uns erneut die `thread::spawn`-Signatur an:

```rust
pub fn spawn<F, T>(f: F) -> JoinHandle<T>
    where
        F: FnOnce() -> T,
        F: Send + 'static,
        T: Send + 'static,
```

Die `spawn`-Funktion gibt ein `JoinHandle<T>` zurück, wobei `T` der Typ ist, den die Closure zurückgibt. Versuchen wir auch `JoinHandle` zu verwenden und sehen, was passiert. Im unseren Fall werden die Closures, die wir an den Threadpool übergeben, die Verbindung verarbeiten und nichts zurückgeben, also wird `T` der Einheitstyp `()` sein.

Der Code in Listing 20-14 wird kompilieren, erstellt aber noch keine Threads. Wir haben die Definition von `ThreadPool` geändert, um einen Vektor von `thread::JoinHandle<()>`-Instanzen zu speichern, initialisiert den Vektor mit einer Kapazität von `size`, eingerichtet eine `for`-Schleife, die einige Code ausführt, um die Threads zu erstellen, und gibt eine `ThreadPool`-Instanz zurück, die sie enthält.

Dateiname: `src/lib.rs`

```rust
1 use std::thread;

pub struct ThreadPool {
  2 threads: Vec<thread::JoinHandle<()>>,
}

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

      3 let mut threads = Vec::with_capacity(size);

        for _ in 0..size {
            // create some threads and store them in the vector
        }

        ThreadPool { threads }
    }
    --snip--
}
```

Listing 20-14: Erstellen eines Vektors für `ThreadPool`, um die Threads zu speichern

Wir haben `std::thread` in den Gültigkeitsbereich des Bibliothekskrats gebracht \[1\], weil wir `thread::JoinHandle` als Typ der Elemente im Vektor in `ThreadPool` verwenden \[2\].

Sobald eine gültige Größe empfangen wird, erstellt unser `ThreadPool` einen neuen Vektor, der `size` Elemente aufnehmen kann \[3\]. Die `with_capacity`-Funktion führt die gleiche Aufgabe wie `Vec::new` aus, aber mit einem wichtigen Unterschied: sie reserviert vorab Speicherplatz im Vektor. Da wir wissen, dass wir `size` Elemente im Vektor speichern müssen, ist diese Voreinrichtung etwas effizienter als die Verwendung von `Vec::new`, das sich selbst anpasst, wenn Elemente eingefügt werden.

Wenn Sie `cargo check` erneut ausführen, sollte es erfolgreich sein.

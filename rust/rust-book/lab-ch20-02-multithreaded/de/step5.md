# Ein endliches Anzahl von Threads erstellen

Wir möchten, dass unser Threadpool auf eine ähnliche, vertraute Weise funktioniert, so dass der Wechsel von Threads zu einem Threadpool keine großen Änderungen am Code erfordert, der unsere Schnittstelle verwendet. Listing 20-12 zeigt die hypothetische Schnittstelle für eine `ThreadPool`-Struktur, die wir anstelle von `thread::spawn` verwenden möchten.

Dateiname: `src/main.rs`

```rust
fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
  1 let pool = ThreadPool::new(4);

    for stream in listener.incoming() {
        let stream = stream.unwrap();

      2 pool.execute(|| {
            handle_connection(stream);
        });
    }
}
```

Listing 20-12: Unsere ideale `ThreadPool`-Schnittstelle

Wir verwenden `ThreadPool::new`, um einen neuen Threadpool mit einer konfigurierbaren Anzahl von Threads zu erstellen, in diesem Fall vier \[1\]. Dann, in der `for`-Schleife, hat `pool.execute` eine ähnliche Schnittstelle wie `thread::spawn`, in dem es eine Closure annimmt, die der Pool für jeden Stream ausführen soll \[2\]. Wir müssen `pool.execute` implementieren, so dass es die Closure annimmt und an einen Thread im Pool gibt, um auszuführen. Dieser Code wird noch nicht kompilieren, aber wir werden versuchen, damit uns der Compiler bei der Fehlerbehebung helfen kann.

# Die Entwicklung von ThreadPool mit compilergetriebener Entwicklung

Machen Sie die Änderungen aus Listing 20-12 in `src/main.rs` und verwenden Sie dann die Compilerfehler von `cargo check`, um unsere Entwicklung zu steuern. Hier ist der erste Fehler, den wir erhalten:

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0433]: failed to resolve: use of undeclared type `ThreadPool`
  --> src/main.rs:11:16
   |
11 |     let pool = ThreadPool::new(4);
   |                ^^^^^^^^^^ use of undeclared type `ThreadPool`
```

Super! Dieser Fehler sagt uns, dass wir einen `ThreadPool`-Typ oder -Modul benötigen, also werden wir einen jetzt erstellen. Unsere `ThreadPool`-Implementierung wird unabhängig von der Art der Arbeit sein, die unser Webserver ausführt. Wechseln wir daher das `hello`-Krat aus einem binären Krat in ein Bibliothekskrat, um unsere `ThreadPool`-Implementierung zu speichern. Nachdem wir in ein Bibliothekskrat gewechselt haben, könnten wir auch die separate Threadpool-Bibliothek für jede Arbeit verwenden, die wir mit einem Threadpool durchführen möchten, nicht nur für das Servieren von Webanfragen.

Erstellen Sie eine Datei `src/lib.rs`, die Folgendes enthält, was die einfachste Definition einer `ThreadPool`-Struktur ist, die wir momentan haben können:

Dateiname: `src/lib.rs`

```rust
pub struct ThreadPool;
```

Ändern Sie dann die Datei `main.rs`, um `ThreadPool` aus dem Bibliothekskrat in den Gültigkeitsbereich zu bringen, indem Sie den folgenden Code am Anfang von `src/main.rs` hinzufügen:

Dateiname: `src/main.rs`

```rust
use hello::ThreadPool;
```

Dieser Code funktioniert immer noch nicht, aber lassen Sie uns ihn erneut überprüfen, um den nächsten Fehler zu erhalten, den wir beheben müssen:

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0599]: no function or associated item named `new` found for struct
`ThreadPool` in the current scope
  --> src/main.rs:12:28
   |
12 |     let pool = ThreadPool::new(4);
   |                            ^^^ function or associated item not found in
`ThreadPool`
```

Dieser Fehler zeigt an, dass wir als nächstes eine assoziierte Funktion namens `new` für `ThreadPool` erstellen müssen. Wir wissen auch, dass `new` einen Parameter haben muss, der `4` als Argument akzeptieren kann und eine `ThreadPool`-Instanz zurückgeben sollte. Implementieren wir die einfachste `new`-Funktion, die diese Eigenschaften hat:

Dateiname: `src/lib.rs`

```rust
pub struct ThreadPool;

impl ThreadPool {
    pub fn new(size: usize) -> ThreadPool {
        ThreadPool
    }
}
```

Wir haben `usize` als Typ des `size`-Parameters gewählt, weil wir wissen, dass eine negative Anzahl von Threads keinen Sinn macht. Wir wissen auch, dass wir dieses `4` als Anzahl der Elemente in einer Sammlung von Threads verwenden werden, was der `usize`-Typ ist, wie in "Ganzzahltypen" diskutiert.

Lassen Sie uns den Code erneut überprüfen:

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0599]: no method named `execute` found for struct `ThreadPool` in the
current scope
  --> src/main.rs:17:14
   |
17 |         pool.execute(|| {
   |              ^^^^^^^ method not found in `ThreadPool`
```

Jetzt tritt der Fehler auf, weil wir keine `execute`-Methode auf `ThreadPool` haben. Erinnern Sie sich aus "Ein endliches Anzahl von Threads erstellen", dass wir beschlossen haben, dass unser Threadpool eine Schnittstelle haben sollte, die ähnlich zu `thread::spawn` ist. Darüber hinaus werden wir die `execute`-Funktion implementieren, so dass sie die übergebene Closure annimmt und an einen inaktiven Thread im Pool gibt, um auszuführen.

Wir werden die `execute`-Methode auf `ThreadPool` definieren, um eine Closure als Parameter zu nehmen. Erinnern Sie sich aus "Werte, die in Closures eingefangen werden, aus Closures und den Fn-Traits entfernen", dass wir Closures als Parameter mit drei verschiedenen Traits verwenden können: `Fn`, `FnMut` und `FnOnce`. Wir müssen entscheiden, welchen Typ von Closure wir hier verwenden möchten. Wir wissen, dass wir am Ende ähnliches tun wie die Standardbibliothek-Implementierung von `thread::spawn`, also können wir schauen, welche Grenzen die Signatur von `thread::spawn` für ihren Parameter hat. Die Dokumentation zeigt uns Folgendes:

```rust
pub fn spawn<F, T>(f: F) -> JoinHandle<T>
    where
        F: FnOnce() -> T,
        F: Send + 'static,
        T: Send + 'static,
```

Der `F`-Typparameter ist derjenige, an dem wir uns hier interessieren; der `T`-Typparameter bezieht sich auf den Rückgabewert, und wir interessieren uns nicht dafür. Wir können sehen, dass `spawn` `FnOnce` als Trait-Bound für `F` verwendet. Dies ist wahrscheinlich auch das, was wir wollen, weil wir schließlich das Argument, das wir in `execute` erhalten, an `spawn` übergeben werden. Wir können uns auch sicher sein, dass `FnOnce` das Trait ist, das wir verwenden möchten, weil der Thread zum Ausführen einer Anfrage die Closure dieser Anfrage nur einmal ausführen wird, was mit dem `Once` in `FnOnce` übereinstimmt.

Der `F`-Typparameter hat auch das Trait-Bound `Send` und die Lebensdauer-Bound `'static`, die in unserer Situation nützlich sind: wir brauchen `Send`, um die Closure von einem Thread zu einem anderen zu übertragen, und `'static`, weil wir nicht wissen, wie lange der Thread zum Ausführen dauern wird. Erstellen wir eine `execute`-Methode auf `ThreadPool`, die einen generischen Parameter vom Typ `F` mit diesen Grenzen akzeptiert:

Dateiname: `src/lib.rs`

```rust
impl ThreadPool {
    --snip--
    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() 1 + Send + 'static,
    {
    }
}
```

Wir verwenden immer noch die `()` nach `FnOnce` \[1\], weil diese `FnOnce` eine Closure darstellt, die keine Parameter nimmt und den Einheitstyp `()` zurückgibt. Genau wie bei Funktionsdefinitionen kann der Rückgabetyp aus der Signatur weggelassen werden, aber selbst wenn wir keine Parameter haben, brauchen wir immer noch die Klammern.

Dies ist wiederum die einfachste Implementierung der `execute`-Methode: Sie tut nichts, aber wir versuchen nur, unseren Code zu kompilieren. Lassen Sie uns ihn erneut überprüfen:

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
    Finished dev [unoptimized + debuginfo] target(s) in 0.24s
```

Es kompiliert! Beachten Sie jedoch, dass, wenn Sie `cargo run` ausprobieren und eine Anfrage im Browser tätigen, Sie die Fehler im Browser sehen werden, die wir am Anfang des Kapitels gesehen haben. Unsere Bibliothek ruft tatsächlich die an `execute` übergebene Closure noch nicht auf!

> Hinweis: Ein Sprichwort, das Sie vielleicht von Sprachen mit strengen Compilern wie Haskell und Rust hören, lautet: "Wenn der Code kompiliert, funktioniert er." Aber dieses Sprichwort stimmt nicht immer. Unser Projekt kompiliert, tut aber absolut nichts! Wenn wir ein echtes, vollständiges Projekt bauen würden, wäre dies ein guter Zeitpunkt, um mit der Schreiben von Unit-Tests zu beginnen, um zu überprüfen, dass der Code kompiliert _und_ das Verhalten hat, das wir wollen.

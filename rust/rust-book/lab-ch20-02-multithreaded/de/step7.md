# Überprüfung der Anzahl der Threads in new

Wir machen nichts mit den Parametern von `new` und `execute`. Implementieren wir die Körper dieser Funktionen mit dem Verhalten, das wir möchten. Zunächst denken wir an `new`. Früher haben wir einen unsigned-Typ für den `size`-Parameter gewählt, weil ein Pool mit einer negativen Anzahl von Threads keinen Sinn macht. Ein Pool mit null Threads macht jedoch auch keinen Sinn, aber null ist ein völlig gültiger `usize`. Wir werden Code hinzufügen, um zu überprüfen, dass `size` größer als null ist, bevor wir eine `ThreadPool`-Instanz zurückgeben, und lassen das Programm mit `assert!` abstürzen, wenn es null erhält, wie in Listing 20-13 gezeigt.

Dateiname: `src/lib.rs`

```rust
impl ThreadPool {
    /// Erstellt einen neuen ThreadPool.
    ///
    /// Die Größe ist die Anzahl der Threads im Pool.
    ///
  1 /// # Panics
    ///
    /// Die `new`-Funktion wird abstürzen, wenn die Größe null ist.
    pub fn new(size: usize) -> ThreadPool {
      2 assert!(size > 0);

        ThreadPool
    }

    --snip--
}
```

Listing 20-13: Implementierung von `ThreadPool::new`, um abzustürzen, wenn `size` null ist

Wir haben auch einige Dokumentation für unsere `ThreadPool` mit Doc-Kommentaren hinzugefügt. Beachten Sie, dass wir gute Dokumentationspraktiken befolgt haben, indem wir einen Abschnitt hinzugefügt haben, in dem die Situationen aufgeführt werden, in denen unsere Funktion abstürzen kann \[1\], wie in Kapitel 14 diskutiert. Versuchen Sie, `cargo doc --open` auszuführen und auf die `ThreadPool`-Struktur zu klicken, um zu sehen, wie die generierten Docs für `new` aussehen!

Anstatt den `assert!`-Makro wie hier zu verwenden \[2\], könnten wir `new` in `build` umwandeln und ein `Result` zurückgeben, wie wir es in Listing 12-9 im I/O-Projekt mit `Config::build` getan haben. Wir haben jedoch in diesem Fall entschieden, dass das Versuchen, einen ThreadPool ohne Threads zu erstellen, ein nicht wiederherstellbarer Fehler sein sollte. Wenn Sie sich wagemutig fühlen, versuchen Sie, eine Funktion namens `build` mit der folgenden Signatur zu schreiben, um mit der `new`-Funktion zu vergleichen:

```rust
pub fn build(
    size: usize
) -> Result<ThreadPool, PoolCreationError> {
```

# Verwenden von move Closures mit Threads

Wir werden oft das `move`-Schlüsselwort mit Closures verwenden, die an `thread::spawn` übergeben werden, weil das Closure dann die Werte, die es aus der Umgebung verwendet, in Besitz nimmt und so die Besitzübertragung dieser Werte von einem Thread an einen anderen ermöglicht. In "Capturing the Environment with Closures" haben wir `move` im Zusammenhang mit Closures diskutiert. Jetzt werden wir uns stärker auf die Wechselwirkung zwischen `move` und `thread::spawn` konzentrieren.

Beachten Sie in Listing 16-1, dass das Closure, das wir an `thread::spawn` übergeben, keine Argumente nimmt: Wir verwenden keine Daten aus dem Hauptthread im Code des erzeugten Threads. Um Daten aus dem Hauptthread im erzeugten Thread zu verwenden, muss das Closure des erzeugten Threads die Werte, die es benötigt, aufnehmen. Listing 16-3 zeigt einen Versuch, einen Vektor im Hauptthread zu erstellen und ihn im erzeugten Thread zu verwenden. Dies wird jedoch noch nicht funktionieren, wie Sie gleich sehen werden.

Dateiname: `src/main.rs`

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    let handle = thread::spawn(|| {
        println!("Here's a vector: {:?}", v);
    });

    handle.join().unwrap();
}
```

Listing 16-3: Versuch, einen von Hauptthread erstellten Vektor in einem anderen Thread zu verwenden

Das Closure verwendet `v`, also wird `v` aufgenommen und zu Teil der Umgebung des Closures. Da `thread::spawn` dieses Closure in einem neuen Thread ausführt, sollten wir in diesem neuen Thread auf `v` zugreifen können. Wenn wir jedoch dieses Beispiel kompilieren, erhalten wir folgenden Fehler:

```bash
error[E0373]: closure may outlive the current function, but it borrows `v`,
which is owned by the current function
 --> src/main.rs:6:32
  |
6 |     let handle = thread::spawn(|| {
  |                                ^^ may outlive borrowed value `v`
7 |         println!("Here's a vector: {:?}", v);
  |                                           - `v` is borrowed here
  |
note: function requires argument type to outlive `'static`
 --> src/main.rs:6:18
  |
6 |       let handle = thread::spawn(|| {
  |  __________________^
7 | |         println!("Here's a vector: {:?}", v);
8 | |     });
  | |______^
help: to force the closure to take ownership of `v` (and any other referenced
variables), use the `move` keyword
  |
6 |     let handle = thread::spawn(move || {
  |                                ++++
```

Rust _schließt_ daraus, wie `v` aufgenommen werden soll, und da `println!` nur eine Referenz auf `v` benötigt, versucht das Closure, `v` zu entleihen. Es gibt jedoch ein Problem: Rust kann nicht wissen, wie lange der erzeugte Thread läuft, daher weiß es auch nicht, ob die Referenz auf `v` immer gültig sein wird.

Listing 16-4 stellt einen Szenario vor, in dem es wahrscheinlicher ist, dass eine Referenz auf `v` ungültig wird.

Dateiname: `src/main.rs`

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    let handle = thread::spawn(|| {
        println!("Here's a vector: {:?}", v);
    });

    drop(v); // oh no!

    handle.join().unwrap();
}
```

Listing 16-4: Ein Thread mit einem Closure, das versucht, eine Referenz auf `v` aus einem Hauptthread zu erfassen, der `v` löscht

Wenn Rust uns erlaubte, diesen Code auszuführen, gäbe es die Möglichkeit, dass der erzeugte Thread sofort in den Hintergrund gesetzt wird und überhaupt nicht ausgeführt wird. Der erzeugte Thread hat eine Referenz auf `v` drin, aber der Hauptthread löst sofort `v` mit der `drop`-Funktion, die wir in Kapitel 15 diskutiert haben. Dann, wenn der erzeugte Thread beginnt, auszuführen, ist `v` nicht mehr gültig, daher ist auch eine Referenz darauf ungültig. Oh nein!

Um den Compilerfehler in Listing 16-3 zu beheben, können wir den Tipp aus der Fehlermeldung verwenden:

    help: to force the closure to take ownership of `v` (and any other referenced
    variables), use the `move` keyword
      |
    6 |     let handle = thread::spawn(move || {
      |                                ++++

Indem wir das `move`-Schlüsselwort vor das Closure hinzufügen, zwingen wir das Closure, die Werte, die es verwendet, in Besitz zu nehmen, anstatt Rust zu erlauben, zu schließen, dass es die Werte entleihen sollte. Die in Listing 16-5 gezeigte Änderung von Listing 16-3 wird wie gewünscht kompilieren und ausgeführt.

Dateiname: `src/main.rs`

```rust
use std::thread;

fn main() {
    let v = vec![1, 2, 3];

    let handle = thread::spawn(move || {
        println!("Here's a vector: {:?}", v);
    });

    handle.join().unwrap();
}
```

Listing 16-5: Verwenden des `move`-Schlüsselworts, um ein Closure dazu zu zwingen, die Werte, die es verwendet, in Besitz zu nehmen

Wir könnten versucht sein, das gleiche zu tun, um den Code in Listing 16-4 zu beheben, in dem der Hauptthread `drop` aufgerufen hat, indem wir ein `move`-Closure verwenden. Dieser Fix funktioniert jedoch nicht, weil das, was Listing 16-4 versucht zu tun, aus einem anderen Grund nicht zugelassen wird. Wenn wir `move` zum Closure hinzufügen würden, würden wir `v` in die Umgebung des Closures verschieben, und wir könnten es dann nicht mehr in dem Hauptthread mit `drop` aufrufen. Stattdessen würden wir folgenden Compilerfehler erhalten:

```bash
error[E0382]: use of moved value: `v`
  --> src/main.rs:10:10
   |
4  |     let v = vec![1, 2, 3];
   |         - move occurs because `v` has type `Vec<i32>`, which does not
implement the `Copy` trait
5  |
6  |     let handle = thread::spawn(move || {
   |                                ------- value moved into closure here
7  |         println!("Here's a vector: {:?}", v);
   |                                           - variable moved due to use in
closure
...
10 |     drop(v); // oh no!
   |          ^ value used here after move
```

Rusts Besitzregeln haben uns wieder gerettet! Wir haben einen Fehler aus dem Code in Listing 16-3 erhalten, weil Rust konservativ ist und nur `v` für den Thread entleiht, was bedeutet, dass der Hauptthread theoretisch die Referenz des erzeugten Threads ungültig machen könnte. Indem wir Rust sagen, die Besitzübertragung von `v` an den erzeugten Thread zu machen, gewährleisten wir Rust, dass der Hauptthread `v` nicht mehr verwenden wird. Wenn wir Listing 16-4 auf die gleiche Weise ändern, verletzen wir dann die Besitzregeln, wenn wir versuchen, `v` im Hauptthread zu verwenden. Das `move`-Schlüsselwort überschreibt Rusts konservativen Standard der Entleihe; es lässt uns die Besitzregeln nicht verletzen.

Jetzt, nachdem wir gesehen haben, was Threads sind und welche Methoden die Thread-API zur Verfügung stellt, schauen wir uns einige Situationen an, in denen wir Threads verwenden können.

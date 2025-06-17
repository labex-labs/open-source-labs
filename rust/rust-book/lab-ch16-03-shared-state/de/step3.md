# Die API von Mutex`<T>`

Als Beispiel für die Verwendung eines Mutex starten wir mit der Verwendung eines Mutex in einem ein-threadigen Kontext, wie in Listing 16-12 gezeigt.

Dateiname: `src/main.rs`

```rust
use std::sync::Mutex;

fn main() {
  1 let m = Mutex::new(5);

    {
      2 let mut num = m.lock().unwrap();
      3 *num = 6;
  4 }

  5 println!("m = {:?}", m);
}
```

Listing 16-12: Erkundung der API von `Mutex<T>` in einem ein-threadigen Kontext zur Vereinfachung

Wie bei vielen Typen erstellen wir einen `Mutex<T>` mit der assoziierten Funktion `new` \[1\]. Um auf die Daten innerhalb des Mutex zuzugreifen, verwenden wir die `lock`-Methode, um den Lock zu erwerben \[2\]. Dieser Aufruf blockiert den aktuellen Thread, sodass er keine Arbeit machen kann, bis es an unserem Zug ist, den Lock zu erwerben.

Der Aufruf von `lock` würde fehlschlagen, wenn ein anderer Thread, der den Lock hält, in Panik gerät. In diesem Fall würde niemals jemand den Lock erhalten, daher haben wir entschieden, `unwrap` aufzurufen und diesen Thread in Panik zu versetzen, wenn wir in dieser Situation sind.

Nachdem wir den Lock erworben haben, können wir den Rückgabewert, in diesem Fall `num` genannt, als mutablen Verweis auf die Daten innerhalb betrachten. Das Typsystem stellt sicher, dass wir einen Lock erwerben, bevor wir den Wert in `m` verwenden. Der Typ von `m` ist `Mutex<i32>`, nicht `i32`, daher _müssen_ wir `lock` aufrufen, um den `i32`-Wert verwenden zu können. Wir können nicht vergessen; das Typsystem wird uns nicht zugelassen, auf das innere `i32` zuzugreifen, anders als so.

Wie Sie vermuten könnten, ist `Mutex<T>` ein Smart-Pointer. Genauer gesagt gibt der Aufruf von `lock` _einen_ Smart-Pointer namens `MutexGuard` zurück, der in einem `LockResult` verpackt ist, das wir mit dem Aufruf von `unwrap` behandelt haben. Der Smart-Pointer `MutexGuard` implementiert `Deref`, um auf unsere inneren Daten zu verweisen; der Smart-Pointer hat auch eine `Drop`-Implementierung, die den Lock automatisch freigibt, wenn ein `MutexGuard` außer Gültigkeitsbereich geht, was am Ende des inneren Bereichs passiert \[4\]. Dadurch riskieren wir nicht, den Lock zu vergessen und den Mutex für andere Threads zu blockieren, da die Lockfreigabe automatisch erfolgt.

Nachdem wir den Lock fallen lassen, können wir den Mutex-Wert ausgeben und sehen, dass wir das innere `i32` auf `6` ändern konnten \[5\].

# Das Einfangen von Referenzen oder die Übergabe der Eigentumsgewalt

Closures können Werte aus ihrer Umgebung auf drei Arten einfangen, was direkt auf die drei Arten abbildet, auf denen eine Funktion einen Parameter entgegennehmen kann: unveränderliche Referenzübernahme, veränderliche Referenzübernahme und die Übernahme der Eigentumsgewalt. Der Closure wird entscheiden, welche dieser Methoden verwendet werden soll, basierend darauf, was der Funktionskörper mit den eingefangenen Werten macht.

In Listing 13-4 definieren wir einen Closure, der eine unveränderliche Referenz auf den Vektor namens `list` einfangt, da es nur eine unveränderliche Referenz benötigt, um den Wert auszugeben.

Dateiname: `src/main.rs`

```rust
fn main() {
    let list = vec![1, 2, 3];
    println!("Before defining closure: {:?}", list);

  1 let only_borrows = || println!("From closure: {:?}", list);

    println!("Before calling closure: {:?}", list);
  2 only_borrows();
    println!("After calling closure: {:?}", list);
}
```

Listing 13-4: Definieren und Aufrufen eines Closures, das eine unveränderliche Referenz einfangt

Dieses Beispiel veranschaulicht auch, dass eine Variable an eine Closure-Definition gebunden werden kann \[1\], und wir können den Closure später aufrufen, indem wir den Variablennamen und Klammern verwenden, als wäre der Variablennamen ein Funktionsname \[2\].

Da wir gleichzeitig mehrere unveränderliche Referenzen auf `list` haben können, ist `list` auch von dem Code vor der Closure-Definition, nach der Closure-Definition aber vor dem Aufruf des Closures und nach dem Aufruf des Closures noch zugänglich. Dieser Code kompiliert, läuft und gibt aus:

    Before defining closure: [1, 2, 3]
    Before calling closure: [1, 2, 3]
    From closure: [1, 2, 3]
    After calling closure: [1, 2, 3]

Als nächstes ändern wir in Listing 13-5 den Closure-Körper, sodass er ein Element zum `list`-Vektor hinzufügt. Der Closure fängt jetzt eine veränderliche Referenz ein.

Dateiname: `src/main.rs`

```rust
fn main() {
    let mut list = vec![1, 2, 3];
    println!("Before defining closure: {:?}", list);

    let mut borrows_mutably = || list.push(7);

    borrows_mutably();
    println!("After calling closure: {:?}", list);
}
```

Listing 13-5: Definieren und Aufrufen eines Closures, das eine veränderliche Referenz einfangt

Dieser Code kompiliert, läuft und gibt aus:

```rust
Before defining closure: [1, 2, 3]
After calling closure: [1, 2, 3, 7]
```

Beachten Sie, dass es zwischen der Definition und dem Aufruf des `borrows_mutably`-Closures keine `println!` mehr gibt: Wenn `borrows_mutably` definiert wird, fängt es eine veränderliche Referenz auf `list` ein. Wir verwenden den Closure nicht mehr nach dem Aufruf des Closures, sodass die veränderliche Referenzende. Zwischen der Closure-Definition und dem Closure-Aufruf ist eine unveränderliche Referenz zum Ausgeben nicht erlaubt, da keine anderen Referenzen erlaubt sind, wenn es eine veränderliche Referenz gibt. Versuchen Sie, eine `println!` dort hinzuzufügen, um zu sehen, welche Fehlermeldung Sie erhalten!

Wenn Sie den Closure erzwingen möchten, die Werte in der Umgebung, die es verwendet, in die Eigentumsgewalt zu übernehmen, auch wenn der Funktionskörper die Eigentumsgewalt nicht streng benötigt, können Sie das Schlüsselwort `move` vor der Parameterliste verwenden.

Diese Technik ist hauptsächlich nützlich, wenn ein Closure an einen neuen Thread übergeben wird, um die Daten zu verschieben, sodass sie vom neuen Thread besessen werden. Wir werden in Kapitel 16 im Detail über Threads und warum Sie sie verwenden möchten sprechen, wenn wir über Konkurrenz sprechen, aber für jetzt wollen wir kurz untersuchen, wie ein neuer Thread mit einem Closure erzeugt wird, das das `move`-Schlüsselwort benötigt. Listing 13-6 zeigt Listing 13-4 modifiziert, um den Vektor in einem neuen Thread statt im Hauptthread auszugeben.

Dateiname: `src/main.rs`

```rust
use std::thread;

fn main() {
    let list = vec![1, 2, 3];
    println!("Before defining closure: {:?}", list);

  1 thread::spawn(move || {
      2 println!("From thread: {:?}", list)
    }).join().unwrap();
}
```

Listing 13-6: Verwenden von `move`, um zu erzwingen, dass der Closure für den Thread die Eigentumsgewalt an `list` übernimmt

Wir erzeugen einen neuen Thread und übergeben dem Thread ein Closure, das als Argument ausgeführt werden soll. Der Closure-Körper gibt die Liste aus. In Listing 13-4 hat der Closure nur `list` mit einer unveränderlichen Referenz eingefangen, da das die geringste Zugangsmöglichkeit zu `list` ist, die zum Ausgeben erforderlich ist. In diesem Beispiel muss der Closure-Körper zwar immer noch nur eine unveränderliche Referenz benötigen \[2\], aber wir müssen angeben, dass `list` in den Closure verschoben werden soll, indem wir das `move`-Schlüsselwort \[1\] am Anfang der Closure-Definition setzen. Der neue Thread kann vor dem Rest des Hauptthreads fertig sein, oder der Hauptthread kann zuerst fertig werden. Wenn der Hauptthread die Eigentumsgewalt an `list` behält, aber vor dem neuen Thread endet und `list` freigibt, wäre die unveränderliche Referenz im Thread ungültig. Daher erfordert der Compiler, dass `list` in den an den neuen Thread übergebenen Closure verschoben wird, damit die Referenz gültig ist. Versuchen Sie, das `move`-Schlüsselwort zu entfernen oder `list` im Hauptthread nach der Closure-Definition zu verwenden, um zu sehen, welche Compilerfehler Sie erhalten!

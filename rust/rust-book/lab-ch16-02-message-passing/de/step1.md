# Verwenden von Nachrichtenübertragung zum Übertragen von Daten zwischen Threads

Ein zunehmend beliebter Ansatz zur Sicherstellung einer sicheren Konkurrenz ist die _Nachrichtenübertragung_, bei der Threads oder Akteure miteinander kommunizieren, indem sie sich Nachrichten mit Daten senden. Hier ist die Idee in einem Slogan aus der Go-Sprachen-Dokumentation unter *https://golang.org/doc/effective_go.html#concurrency*: "Kommunizieren Sie nicht, indem Sie den Speicher teilen; teilen Sie stattdessen den Speicher, indem Sie kommunizieren."

Um eine Nachrichtenübertragungskonkurrenz zu erreichen, bietet die Standardbibliothek von Rust eine Implementierung von _Kanälen_. Ein Kanal ist ein allgemeines Programmierkonzept, über den Daten von einem Thread an einen anderen gesendet werden.

Sie können sich einen Kanal in der Programmierung wie einen gerichteten Wasserkanal vorstellen, wie einen Bach oder einen Fluss. Wenn Sie etwas wie eine Gummitüte in einen Fluss legen, wird sie den Fluss hinunter bis zum Ende des Wasserkreislaufs fließen.

Ein Kanal hat zwei Hälften: einen Sender und einen Empfänger. Die Senderhälfte ist der obere Flussabschnitt, an dem Sie die Gummitüte in den Fluss legen, und die Empfängerhälfte ist der Punkt, an dem die Gummitüte am Ende des Flusses landet. Ein Teil Ihres Codes ruft Methoden am Sender mit den Daten auf, die Sie senden möchten, und ein anderer Teil prüft die Empfangsseite auf ankommende Nachrichten. Ein Kanal wird als _geschlossen_ bezeichnet, wenn entweder die Sender- oder die Empfängerhälfte gelöscht wird.

Hier werden wir ein Programm entwickeln, das einen Thread verwendet, um Werte zu generieren und über einen Kanal zu senden, und einen anderen Thread, der die Werte empfängt und ausgibt. Wir werden einfache Werte zwischen Threads über einen Kanal senden, um das Feature zu veranschaulichen. Sobald Sie mit der Technik vertraut sind, können Sie Kanäle für alle Threads verwenden, die miteinander kommunizieren müssen, wie z. B. ein Chat-System oder ein System, in dem viele Threads Teile einer Berechnung durchführen und die Teile an einen Thread senden, der die Ergebnisse aggregiert.

Zunächst erstellen wir in Listing 16-6 einen Kanal, aber wir machen nichts damit. Beachten Sie, dass dies noch nicht kompilieren wird, da Rust nicht weiß, welchen Wertetyp wir über den Kanal senden möchten.

Dateiname: `src/main.rs`

```rust
use std::sync::mpsc;

fn main() {
    let (tx, rx) = mpsc::channel();
}
```

Listing 16-6: Erstellen eines Kanals und Zuweisen der beiden Hälften zu `tx` und `rx`

Wir erstellen einen neuen Kanal mit der `mpsc::channel`-Funktion; `mpsc` steht für _multiple producer, single consumer_. Kurz gesagt bedeutet die Art, wie die Standardbibliothek von Rust Kanäle implementiert, dass ein Kanal mehrere \_Sende_enden haben kann, die Werte erzeugen, aber nur ein \_Empfangs_ende, das diese Werte konsumiert. Stellen Sie sich mehrere Ströme vor, die zusammen in einen großen Fluss münden: Alles, was in einen der Ströme gesendet wird, wird am Ende in einem Fluss landen. Wir beginnen zunächst mit einem einzelnen Produzenten, aber wir werden mehrere Produzenten hinzufügen, wenn dieses Beispiel funktioniert.

Die `mpsc::channel`-Funktion gibt ein Tupel zurück, dessen erstes Element der Sendeende - der Sender - und das zweite Element der Empfangsende - der Empfänger - ist. Die Abkürzungen `tx` und `rx` werden in vielen Bereichen traditionell für _Sender_ und _Empfänger_ verwendet, daher benennen wir unsere Variablen so, um jedes Ende anzuzeigen. Wir verwenden eine `let`-Anweisung mit einem Muster, das das Tupel aufspaltet; wir werden die Verwendung von Mustern in `let`-Anweisungen und das Aufspalten in Kapitel 18 besprechen. Für jetzt wissen Sie, dass das Verwenden einer `let`-Anweisung auf diese Weise ein bequemer Ansatz ist, um die Teile des von `mpsc::channel` zurückgegebenen Tupels zu extrahieren.

Lassen Sie uns die Sendeende in einen neu erzeugten Thread verschieben und einen String senden, sodass der neu erzeugte Thread mit dem Hauptthread kommuniziert, wie in Listing 16-7 gezeigt. Dies ist wie das Legen einer Gummitüte in den Fluss upstream oder das Senden einer Chatnachricht von einem Thread an einen anderen.

Dateiname: `src/main.rs`

```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let val = String::from("hi");
        tx.send(val).unwrap();
    });
}
```

Listing 16-7: Verschieben von `tx` in einen neu erzeugten Thread und Senden von `"hi"`

Wir verwenden erneut `thread::spawn`, um einen neuen Thread zu erstellen, und dann `move`, um `tx` in die Closure zu verschieben, sodass der neu erzeugte Thread `tx` besitzt. Der neu erzeugte Thread muss den Sender besitzen, um Nachrichten über den Kanal senden zu können.

Der Sender hat eine `send`-Methode, die den Wert annimmt, den wir senden möchten. Die `send`-Methode gibt einen `Result<T, E>`-Typ zurück, sodass die Sendoperation einen Fehler zurückgeben wird, wenn der Empfänger bereits gelöscht wurde und es keinen Ort gibt, an den ein Wert gesendet werden kann. In diesem Beispiel rufen wir `unwrap` auf, um im Falle eines Fehlers einen Fehler auszulösen. In einer echten Anwendung würden wir dies jedoch richtig behandeln: kehren Sie zu Kapitel 9 zurück, um Strategien zur richtigen Fehlerbehandlung zu überprüfen.

In Listing 16-8 werden wir den Wert aus dem Empfänger im Hauptthread abrufen. Dies ist wie das Abholen der Gummitüte aus dem Wasser am Ende des Flusses oder das Empfangen einer Chatnachricht.

Dateiname: `src/main.rs`

```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let val = String::from("hi");
        tx.send(val).unwrap();
    });

    let received = rx.recv().unwrap();
    println!("Got: {received}");
}
```

Listing 16-8: Empfangen des Werts `"hi"` im Hauptthread und Ausgeben

Der Empfänger hat zwei nützliche Methoden: `recv` und `try_recv`. Wir verwenden `recv`, das Abkürzung für _receive_ ist, das die Ausführung des Hauptthreads blockieren und bis zu einem Wert warten wird, der über den Kanal gesendet wird. Wenn ein Wert gesendet wird, wird `recv` ihn in einem `Result<T, E>` zurückgeben. Wenn der Sender geschlossen wird, wird `recv` einen Fehler zurückgeben, um anzuzeigen, dass keine weiteren Werte mehr kommen werden.

Die `try_recv`-Methode blockiert nicht, sondern gibt stattdessen sofort ein `Result<T, E>` zurück: einen `Ok`-Wert, der eine Nachricht enthält, wenn eine verfügbar ist, und einen `Err`-Wert, wenn keine Nachrichten vorhanden sind. Das Verwenden von `try_recv` ist nützlich, wenn dieser Thread andere Arbeit zu erledigen hat, während er auf Nachrichten wartet: wir könnten eine Schleife schreiben, die `try_recv` regelmäßig aufruft, eine Nachricht behandelt, wenn eine verfügbar ist, und andernfalls für eine Weile andere Arbeit erledigt, bis wir erneut prüfen.

Wir haben `recv` in diesem Beispiel aus Einfachheit verwendet; wir haben keine andere Arbeit für den Hauptthread, als auf Nachrichten zu warten, daher ist es angemessen, den Hauptthread zu blockieren.

Wenn wir den Code in Listing 16-8 ausführen, werden wir den Wert aus dem Hauptthread sehen:

```rust
Got: hi
```

Perfekt!

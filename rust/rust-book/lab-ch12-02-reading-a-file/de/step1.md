# Datei lesen

Jetzt fügen wir Funktionalität hinzu, um die Datei zu lesen, die im `file_path`-Argument angegeben ist. Zunächst benötigen wir eine Beispiel-Datei, um sie zu testen: wir verwenden eine Datei mit wenig Text über mehrere Zeilen mit einigen wiederholten Wörtern. Listing 12-3 enthält einen Gedicht von Emily Dickinson, das gut geeignet ist! Erstellen Sie eine Datei namens _poem.txt_ im Stammverzeichnis Ihres Projekts und geben Sie das Gedicht "I'm Nobody! Who are you?" ein.

Dateiname: poem.txt

    I'm nobody! Who are you?
    Are you nobody, too?
    Then there's a pair of us - don't tell!
    They'd banish us, you know.

    How dreary to be somebody!
    How public, like a frog
    To tell your name the livelong day
    To an admiring bog!

Listing 12-3: Ein Gedicht von Emily Dickinson ist ein guter Testfall.

Mit dem Text in der Datei bearbeiten Sie `src/main.rs` und fügen Sie Code hinzu, um die Datei zu lesen, wie in Listing 12-4 gezeigt.

Dateiname: `src/main.rs`

```rust
use std::env;
1 use std::fs;

fn main() {
    --snip--
    println!("In file {}", file_path);

  2 let contents = fs::read_to_string(file_path)
       .expect("Should have been able to read the file");

  3 println!("With text:\n{contents}");
}
```

Listing 12-4: Lesen des Inhalts der von dem zweiten Argument angegebenen Datei

Zunächst bringen wir einen relevanten Teil der Standardbibliothek mit einem `use`-Statement ein: wir benötigen `std::fs`, um Dateien zu verarbeiten \[1\].

In `main` nimmt der neue Ausdruck `fs::read_to_string` den `file_path`, öffnet diese Datei und gibt ein `std::io::Result<String>` des Dateiinhalts zurück \[2\].

Danach fügen wir erneut einen temporären `println!`-Ausdruck hinzu, der den Wert von `contents` nach dem Lesen der Datei ausgibt, damit wir überprüfen können, ob das Programm bisher funktioniert \[3\].

Lassen Sie uns diesen Code mit einem beliebigen String als erstes Kommandozeilenargument (weil wir den Suchteil noch nicht implementiert haben) und der _poem.txt_-Datei als zweites Argument ausführen:

```bash
$ cargo run -- the poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep the poem.txt`
Searching for the
In file poem.txt
With text:
I'm nobody! Who are you?
Are you nobody, too?
Then there's a pair of us - don't tell!
They'd banish us, you know.

How dreary to be somebody!
How public, like a frog
To tell your name the livelong day
To an admiring bog!
```

Super! Der Code hat die Datei gelesen und dann den Inhalt ausgegeben. Aber der Code hat einige Mängel. Momentan hat die `main`-Funktion mehrere Verantwortlichkeiten: Im Allgemeinen sind Funktionen deutlicher und leichter wartbar, wenn jede Funktion nur eine Idee vertritt. Das andere Problem ist, dass wir Fehler nicht so gut wie möglich behandeln. Das Programm ist noch klein, also sind diese Mängel kein großes Problem, aber wenn das Programm wächst, wird es schwieriger, sie sauber zu beheben. Es ist eine gute Praxis, frühzeitig beim Entwicklung eines Programms mit der Refactoring zu beginnen, weil es viel einfacher ist, kleinere Codemengen umzugestalten. Wir werden das nächste tun.

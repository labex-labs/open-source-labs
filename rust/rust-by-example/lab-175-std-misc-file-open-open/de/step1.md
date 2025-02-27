# `open`

Die `open`-Funktion kann verwendet werden, um eine Datei im schreibgeschützten Modus zu öffnen.

Ein `File` besitzt eine Ressource, den Dateidescriptor, und kümmert sich um das Schließen der Datei, wenn es `drop`ed wird.

```rust
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

fn main() {
    // Erzeuge einen Pfad zur gewünschten Datei
    let path = Path::new("hello.txt");
    let display = path.display();

    // Öffne den Pfad im schreibgeschützten Modus, gibt `io::Result<File>` zurück
    let mut file = match File::open(&path) {
        Err(why) => panic!("konnte {} nicht öffnen: {}", display, why),
        Ok(file) => file,
    };

    // Lies den Dateiinhalt in einen String, gibt `io::Result<usize>` zurück
    let mut s = String::new();
    match file.read_to_string(&mut s) {
        Err(why) => panic!("konnte {} nicht lesen: {}", display, why),
        Ok(_) => print!("{} enthält:\n{}", display, s),
    }

    // `file` verlässt den Gültigkeitsbereich, und die Datei "hello.txt" wird geschlossen
}
```

Hier ist die erwartete erfolgreiche Ausgabe:

```shell
$ echo "Hello World!" > hello.txt
$ rustc open.rs && ./open
hello.txt enthält:
Hello World!
```

(Es wird empfohlen, das vorherige Beispiel unter verschiedenen Fehlbedingungen zu testen: `hello.txt` existiert nicht oder `hello.txt` ist nicht lesbar usw.)

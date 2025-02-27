# `create`

Die `create`-Funktion öffnet eine Datei im schreibgeschützten Modus. Wenn die Datei bereits existierte, wird der alte Inhalt zerstört. Andernfalls wird eine neue Datei erstellt.

```rust
static LOREM_IPSUM: &str =
    "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
";

use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

fn main() {
    let path = Path::new("lorem_ipsum.txt");
    let display = path.display();

    // Öffnet eine Datei im schreibgeschützten Modus, gibt `io::Result<File>` zurück
    let mut file = match File::create(&path) {
        Err(why) => panic!("konnte {} nicht erstellen: {}", display, why),
        Ok(file) => file,
    };

    // Schreibt die `LOREM_IPSUM`-Zeichenfolge in `file`, gibt `io::Result<()>` zurück
    match file.write_all(LOREM_IPSUM.as_bytes()) {
        Err(why) => panic!("konnte nicht in {} schreiben: {}", display, why),
        Ok(_) => println!("erfolgreich in {} geschrieben", display),
    }
}
```

Hier ist die erwartete erfolgreiche Ausgabe:

```shell
$ rustc create.rs && ./create
erfolgreich in lorem_ipsum.txt geschrieben
$ cat lorem_ipsum.txt
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
```

(Wie im vorherigen Beispiel wird Ihnen empfohlen, dieses Beispiel unter Fehlbedingungen zu testen.)

Die \[`OpenOptions`\]-Struktur kann verwendet werden, um zu konfigurieren, wie eine Datei geöffnet wird.

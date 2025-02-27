# `read_lines`

## Ein naive Ansatz

Dies könnte ein vernünftiger erster Versuch für die erste Implementierung eines Anfängers zum Lesen von Zeilen aus einer Datei.

```rust
use std::fs::read_to_string;

fn read_lines(filename: &str) -> Vec<String> {
    let mut result = Vec::new();

    for line in read_to_string(filename).unwrap().lines() {
        result.push(line.to_string())
    }

    result
}
```

Da die Methode `lines()` einen Iterator über die Zeilen in der Datei zurückgibt, können wir auch eine Map-Inline-Ausführung durchführen und die Ergebnisse sammeln, was zu einem präziseren und flüssigeren Ausdruck führt.

```rust
use std::fs::read_to_string;

fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename)
     .unwrap()  // Panik bei möglichen Dateilesefehler
     .lines()  // Teilt die Zeichenfolge in einen Iterator von Zeichenfolgen-Slices auf
     .map(String::from)  // Macht jeden Slice zu einer Zeichenfolge
     .collect()  // Sammelt sie zu einem Vektor zusammen
}
```

Beachten Sie, dass in beiden obigen Beispielen wir die `&str`-Referenz, die von `lines()` zurückgegeben wird, in den eigenen Typ `String` umwandeln müssen, indem wir jeweils `.to_string()` und `String::from` verwenden.

## Ein effizienterer Ansatz

Hier übergeben wir die Besitzerschaft der geöffneten `File` an eine `BufReader`-Struktur. `BufReader` verwendet einen internen Puffer, um Zwischenzuweisungen zu reduzieren.

Wir aktualisieren auch `read_lines`, um einen Iterator zurückzugeben, anstatt für jede Zeile neue `String`-Objekte im Speicher zuzuweisen.

```rust
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    // Die Datei hosts.txt muss im aktuellen Pfad existieren
    if let Ok(lines) = read_lines("./hosts.txt") {
        // Verbraucht den Iterator, gibt eine (Optional) Zeichenfolge zurück
        for line in lines {
            if let Ok(ip) = line {
                println!("{}", ip);
            }
        }
    }
}

// Die Ausgabe ist in einem Result verpackt, um auf Fehler zu prüfen
// Gibt einen Iterator zum Reader der Zeilen der Datei zurück.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
```

Das Ausführen dieses Programms druckt einfach die Zeilen einzeln aus.

```shell
$ echo -e "127.0.0.1\n192.168.0.1\n" > hosts.txt
$ rustc read_lines.rs && ./read_lines
127.0.0.1
192.168.0.1
```

(Beachten Sie, dass da `File::open` ein generisches `AsRef<Path>` als Argument erwartet, definieren wir unsere generische `read_lines()`-Methode mit derselben generischen Einschränkung, indem wir das `where`-Schlüsselwort verwenden.)

Dieser Prozess ist effizienter als das Erstellen eines `String` im Speicher mit allen Inhalten der Datei. Dies kann insbesondere bei der Arbeit mit größeren Dateien zu Leistungsproblemen führen.

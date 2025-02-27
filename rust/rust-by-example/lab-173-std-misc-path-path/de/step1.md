# Pfad

Die `Path`-Struktur repräsentiert Dateipfade im zugrunde liegenden Dateisystem. Es gibt zwei Varianten von `Path`: `posix::Path` für UNIX-ähnliche Systeme und `windows::Path` für Windows. Der Präambel exportiert die passende plattformspezifische `Path`-Variante.

Ein `Path` kann aus einem `OsStr` erstellt werden und bietet mehrere Methoden, um Informationen aus der Datei/des Verzeichnisses zu erhalten, auf das der Pfad zeigt.

Ein `Path` ist unveränderlich. Die eigene Version von `Path` ist `PathBuf`. Die Beziehung zwischen `Path` und `PathBuf` ist ähnlich der von `str` und `String`: Ein `PathBuf` kann in-place verändert werden und kann auf einen `Path` dereferenziert werden.

Beachten Sie, dass ein `Path` intern _nicht_ als UTF-8-Zeichenfolge dargestellt wird, sondern als `OsString` gespeichert ist. Daher ist die Umwandlung eines `Paths` in einen `&str` _nicht_ kostenlos und kann fehlschlagen (es wird eine `Option` zurückgegeben). Ein `Path` kann jedoch mit `into_os_string` bzw. `as_os_str` frei in einen `OsString` oder `&OsStr` umgewandelt werden.

```rust
use std::path::Path;

fn main() {
    // Erstellen Sie einen `Path` aus einem `&'static str`
    let path = Path::new(".");

    // Die `display`-Methode gibt eine `Display`-fähige Struktur zurück
    let _display = path.display();

    // `join` vereinigt einen Pfad mit einem Byte-Container unter Verwendung des
    // Betriebssystem-spezifischen Separators und gibt ein `PathBuf` zurück
    let mut new_path = path.join("a").join("b");

    // `push` erweitert das `PathBuf` um einen `&Path`
    new_path.push("c");
    new_path.push("myfile.tar.gz");

    // `set_file_name` aktualisiert den Dateinamen des `PathBuf`
    new_path.set_file_name("package.tgz");

    // Konvertieren Sie das `PathBuf` in einen String-Slice
    match new_path.to_str() {
        None => panic!("new path is not a valid UTF-8 sequence"),
        Some(s) => println!("new path is {}", s),
    }
}
```

Vergewissern Sie sich, andere `Path`-Methoden (`posix::Path` oder `windows::Path`) und die `Metadata`-Struktur zu überprüfen.

# Formatierter Druck

Der Druck wird durch eine Reihe von `Makros` behandelt, die in `std::fmt` definiert sind, darunter einige:

- `format!`: formatierten Text in eine `String` schreiben.
- `print!`: wie `format!`, aber der Text wird auf der Konsole (io::stdout) gedruckt.
- `println!`: wie `print!`, aber ein Zeilenumbruch wird angehängt.
- `eprint!`: wie `print!`, aber der Text wird auf die Standardfehlerausgabe (io::stderr) gedruckt.
- `eprintln!`: wie `eprint!`, aber ein Zeilenumbruch wird angehängt.

Alle analysieren den Text auf die gleiche Weise. Als Plus prüft Rust die Formatierkorrektheit zur Compile-Zeit.

```rust
fn main() {
    // Im Allgemeinen wird `{}` automatisch durch beliebige
    // Argumente ersetzt. Diese werden in einen String umgewandelt.
    println!("{} Tage", 31);

    // Es können positionale Argumente verwendet werden. Die Angabe einer ganzen Zahl innerhalb von `{}`
    // bestimmt, welches zusätzliche Argument ersetzt werden soll. Die Argumente beginnen
    // bei 0 direkt nach der Formatzeichenfolge.
    println!("{0}, dies ist {1}. {1}, dies ist {0}", "Alice", "Bob");

    // Ebenso können benannte Argumente verwendet werden.
    println!("{subject} {verb} {object}",
             object="der faulige Hund",
             subject="der schnelle braune Fuchs",
             verb="springt über");

    // Verschiedene Formatierungen können durch Angabe des Formatzeichens
    // nach einem `:` aufgerufen werden.
    println!("Base 10:               {}",   69420); // 69420
    println!("Base 2 (binär):       {:b}", 69420); // 10000111100101100
    println!("Base 8 (oktal):        {:o}", 69420); // 207454
    println!("Base 16 (hexadezimal): {:x}", 69420); // 10f2c
    println!("Base 16 (hexadezimal): {:X}", 69420); // 10F2C

    // Sie können Text rechtsbündig mit einer angegebenen Breite ausrichten. Dies wird
    // "    1" ausgeben. (Vier Leerzeichen und eine "1", für eine Gesamtbreite von 5.)
    println!("{number:>5}", number=1);

    // Sie können Zahlen mit zusätzlichen Nullen auffüllen,
    println!("{number:0>5}", number=1); // 00001
    // und linksbündig durch Umschreiben des Zeichens. Dies wird "10000" ausgeben.
    println!("{number:0<5}", number=1); // 10000

    // Sie können benannte Argumente im Formatangaben durch Anhängen eines `$` verwenden.
    println!("{number:0>width$}", number=1, width=5);

    // Rust prüft sogar, ob die richtige Anzahl von Argumenten verwendet wird.
    println!("Mein Name ist {0}, {1} {0}", "Bond");
    // FIXME ^ Fügen Sie das fehlende Argument hinzu: "James"

    // Nur Typen, die fmt::Display implementieren, können mit `{}` formatiert werden. Benutzerdefinierte
    // Typen implementieren fmt::Display standardmäßig nicht.

    #[allow(dead_code)] // deaktiviert `dead_code`, das Warnungen vor nicht verwendeten Modulen ausgibt
    struct Structure(i32);

    // Dies wird nicht kompilieren, da `Structure` fmt::Display nicht implementiert.
    // println!("Dieses Struct `{}` wird nicht gedruckt...", Structure(3));
    // TODO ^ Versuchen Sie, diese Zeile zu entsperren

    // Ab Rust 1.58 können Sie das Argument direkt aus einer umgebenden Variable erfassen. Genau wie oben wird dies
    // "    1" ausgeben, 4 Leerzeichen und eine "1".
    let number: f64 = 1.0;
    let width: usize = 5;
    println!("{number:>width$}");
}
```

`std::fmt` enthält viele `Attribute`, die die Darstellung von Text steuern. Die grundlegenden Formen zweier wichtiger Attribute werden unten aufgeführt:

- `fmt::Debug`: Verwenden des `{:?}`-Markers. Text für Debugging-Zwecke formatieren.
- `fmt::Display`: Verwenden des `{}`-Markers. Text auf eine elegantere, benutzerfreundlichere Weise formatieren.

Hier haben wir `fmt::Display` verwendet, da die std-Bibliothek Implementierungen für diese Typen bereitstellt. Um Text für benutzerdefinierte Typen zu drucken, sind weitere Schritte erforderlich.

Das Implementieren des `fmt::Display`-Attributs implementiert automatisch das `ToString`-Attribut, das uns ermöglicht, den Typ in eine `String` umzuwandeln.

In _Zeile 43_ ist `#[allow(dead_code)]` ein \[Attribut\], das nur auf das nachfolgende Modul anwendbar ist.

## Aktivitäten

- Beheben Sie das Problem im obigen Code (siehe FIXME), so dass er ohne Fehler läuft.
- Versuchen Sie, die Zeile zu entsperren, in der versucht wird, das `Structure`-Struct zu formatieren (siehe TODO)
- Fügen Sie einen `println!`-Makros-Aufruf hinzu, der ausgibt: `Pi ist ungefähr 3.142`, indem Sie die Anzahl der angezeigten Dezimalstellen steuern. Zu Zwecken dieses Übungs verwenden Sie `let pi = 3.141592` als Schätzung für Pi. (Hinweis: Sie müssen möglicherweise die `std::fmt`-Dokumentation überprüfen, um die Anzahl der anzuzeigenden Dezimalstellen festzulegen)

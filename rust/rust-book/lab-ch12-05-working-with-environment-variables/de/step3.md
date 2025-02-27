# Implementierung der search_case_insensitive-Funktion

Die `search_case_insensitive`-Funktion, wie in Listing 12-21 gezeigt, wird fast identisch zur `search`-Funktion sein. Der einzige Unterschied besteht darin, dass wir die `query` und jede `line` in Kleinbuchstaben umwandeln, so dass unabhängig von der Groß-/Kleinschreibung der Eingabeargumente sie in der gleichen Groß-/Kleinschreibung übereinstimmen, wenn wir überprüfen, ob die Zeile die Abfrage enthält.

Dateiname: `src/lib.rs`

```rust
pub fn search_case_insensitive<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
  1 let query = query.to_lowercase();
    let mut results = Vec::new();

    for line in contents.lines() {
        if 2 line.to_lowercase().contains(3 &query) {
            results.push(line);
        }
    }

    results
}
```

Listing 12-21: Definition der `search_case_insensitive`-Funktion, um die Abfrage und die Zeile in Kleinbuchstaben zu konvertieren, bevor sie verglichen werden

Zunächst konvertieren wir die `query`-Zeichenfolge in Kleinbuchstaben und speichern sie in einer neu deklarierten Variable mit dem gleichen Namen \[1\]. Es ist erforderlich, `to_lowercase` auf der Abfrage aufzurufen, damit unabhängig davon, ob die Abfrage des Benutzers `"rust"`, `"RUST"`, `"Rust"` oder `"rUsT"` lautet, wir die Abfrage als ob es `"rust"` wäre behandeln und die Groß-/Kleinschreibung ignorieren. Während `to_lowercase` die grundlegenden Unicode-Zeichen behandeln wird, wird es nicht 100% genau sein. Wenn wir eine echte Anwendung schreiben würden, müssten wir hier etwas mehr Arbeit leisten, aber dieser Abschnitt geht um Umgebungsvariablen, nicht um Unicode, daher belassen wir es hier bei diesem Stand.

Beachten Sie, dass `query` jetzt ein `String` ist, statt eine Zeichenfolgen-Slice, da das Aufrufen von `to_lowercase` neue Daten erzeugt, anstatt vorhandene Daten zu referenzieren. Nehmen wir beispielsweise an, die Abfrage lautet `"rUsT"`: Diese Zeichenfolgen-Slice enthält keine Kleinbuchstaben `u` oder `t`, die wir verwenden könnten, daher müssen wir einen neuen `String` mit dem Inhalt `"rust"` zuweisen. Wenn wir `query` jetzt als Argument an die `contains`-Methode übergeben, müssen wir ein Ampersand hinzufügen \[3\], da die Signatur von `contains` definiert ist, um eine Zeichenfolgen-Slice zu akzeptieren.

Als Nächstes fügen wir einen Aufruf von `to_lowercase` für jede `line` hinzu, um alle Zeichen in Kleinbuchstaben zu konvertieren \[2\]. Jetzt, nachdem wir `line` und `query` in Kleinbuchstaben umgewandelt haben, werden wir Treffer finden, unabhängig von der Groß-/Kleinschreibung der Abfrage.

Lassen Sie uns sehen, ob diese Implementierung die Tests besteht:

    running 2 tests
    test tests::case_insensitive... ok
    test tests::case_sensitive... ok

    test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Super! Die Tests haben bestanden. Jetzt rufen wir die neue `search_case_insensitive`-Funktion aus der `run`-Funktion auf. Zunächst fügen wir eine Konfigurationsoption zur `Config`-Struktur hinzu, um zwischen case-sensitive und case-insensitive Suche umzuschalten. Das Hinzufügen dieses Felds verursacht Compilerfehler, da wir dieses Feld noch nirgends initialisieren:

Dateiname: `src/lib.rs`

```rust
pub struct Config {
    pub query: String,
    pub file_path: String,
    pub ignore_case: bool,
}
```

Wir haben das `ignore_case`-Feld hinzugefügt, das einen Boolean speichert. Als Nächstes müssen wir die `run`-Funktion dazu bringen, den Wert des `ignore_case`-Felds zu überprüfen und daraus zu entscheiden, ob die `search`-Funktion oder die `search_case_insensitive`-Funktion aufgerufen werden soll, wie in Listing 12-22 gezeigt. Dies wird noch nicht kompilieren.

Dateiname: `src/lib.rs`

```rust
pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)?;

    let results = if config.ignore_case {
        search_case_insensitive(&config.query, &contents)
    } else {
        search(&config.query, &contents)
    };

    for line in results {
        println!("{line}");
    }

    Ok(())
}
```

Listing 12-22: Aufrufen von entweder `search` oder `search_case_insensitive` basierend auf dem Wert in `config.ignore_case`

Schließlich müssen wir nach der Umgebungsvariable suchen. Die Funktionen zum Umgang mit Umgebungsvariablen befinden sich im `env`-Modul der Standardbibliothek, daher importieren wir dieses Modul am Anfang von `src/lib.rs` in den Geltungsbereich. Dann verwenden wir die `var`-Funktion aus dem `env`-Modul, um zu überprüfen, ob ein Wert für eine Umgebungsvariable namens `IGNORE_CASE` gesetzt wurde, wie in Listing 12-23 gezeigt.

Dateiname: `src/lib.rs`

```rust
use std::env;
--snip--

impl Config {
    pub fn build(
        args: &[String]
    ) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("not enough arguments");
        }

        let query = args[1].clone();
        let file_path = args[2].clone();

        let ignore_case = env::var("IGNORE_CASE").is_ok();

        Ok(Config {
            query,
            file_path,
            ignore_case,
        })
    }
}
```

Listing 12-23: Prüfen, ob ein Wert in einer Umgebungsvariable namens `IGNORE_CASE` vorhanden ist

Hier erstellen wir eine neue Variable, `ignore_case`. Um ihren Wert zu setzen, rufen wir die `env::var`-Funktion auf und übergeben ihr den Namen der `IGNORE_CASE`-Umgebungsvariable. Die `env::var`-Funktion gibt ein `Result` zurück, das die erfolgreiche `Ok`-Variante sein wird, die den Wert der Umgebungsvariable enthält, wenn die Umgebungsvariable auf einen beliebigen Wert gesetzt ist. Sie wird die `Err`-Variante zurückgeben, wenn die Umgebungsvariable nicht gesetzt ist.

Wir verwenden die `is_ok`-Methode auf dem `Result`, um zu überprüfen, ob die Umgebungsvariable gesetzt ist, was bedeutet, dass das Programm eine case-insensitive Suche durchführen sollte. Wenn die `IGNORE_CASE`-Umgebungsvariable nicht auf etwas gesetzt ist, wird `is_ok` `false` zurückgeben und das Programm wird eine case-sensitive Suche durchführen. Wir interessieren uns nicht für den _Wert_ der Umgebungsvariable, sondern nur für den Umstand, ob sie gesetzt oder nicht gesetzt ist, daher überprüfen wir `is_ok` anstatt `unwrap`, `expect` oder eine der anderen Methoden, die wir auf `Result` gesehen haben, zu verwenden.

Wir übergeben den Wert in der `ignore_case`-Variable an die `Config`-Instanz, damit die `run`-Funktion diesen Wert lesen und entscheiden kann, ob `search_case_insensitive` oder `search` aufgerufen werden soll, wie wir in Listing 12-22 implementiert haben.

Lassen Sie uns es ausprobieren! Zunächst führen wir unser Programm ohne die Umgebungsvariable gesetzt und mit der Abfrage `to` aus, die alle Zeilen, die das Wort _to_ in Kleinbuchstaben enthalten, finden sollte:

```bash
$ cargo run -- to poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep to poem.txt`
Are you nobody, too?
How dreary to be somebody!
```

Es sieht so aus, als würde das immer noch funktionieren! Jetzt führen wir das Programm mit `IGNORE_CASE` auf `1` und der gleichen Abfrage `to` aus:

```bash
IGNORE_CASE=1 cargo run -- to poem.txt
```

Wenn Sie PowerShell verwenden, müssen Sie die Umgebungsvariable setzen und das Programm als separate Befehle ausführen:

```rust
PS> $Env:IGNORE_CASE=1; cargo run -- to poem.txt
```

Dadurch wird `IGNORE_CASE` für die restliche Zeit Ihrer Shell-Sitzung bestehen bleiben. Es kann mit dem `Remove-Item`-Cmdlet gelöscht werden:

```rust
PS> Remove-Item Env:IGNORE_CASE
```

Wir sollten Zeilen erhalten, die _to_ enthalten und möglicherweise auch Großbuchstaben haben:

    Are you nobody, too?
    How dreary to be somebody!
    To tell your name the livelong day
    To an admiring bog!

Toller! Wir haben auch Zeilen erhalten, die _To_ enthalten! Unser `minigrep`-Programm kann jetzt eine case-insensitive Suche durchführen, die durch eine Umgebungsvariable gesteuert wird. Jetzt wissen Sie, wie Sie Optionen verwalten, die entweder über Befehlszeilenargumente oder Umgebungsvariablen festgelegt werden.

Einige Programme erlauben sowohl Argumente _als auch_ Umgebungsvariablen für die gleiche Konfiguration. In diesen Fällen entscheiden die Programme, dass das eine oder das andere Vorrang hat. Als weitere Übung können Sie versuchen, die Groß-/Kleinschreibung über einen Befehlszeilenargument oder eine Umgebungsvariable zu steuern. Entscheiden Sie, ob das Befehlszeilenargument oder die Umgebungsvariable Vorrang haben sollte, wenn das Programm mit einem auf case-sensitive und einem auf ignore case gesetzt wird.

Das `std::env`-Modul enthält noch viele weitere nützliche Funktionen zum Umgang mit Umgebungsvariablen: Schauen Sie sich seine Dokumentation an, um zu sehen, was verfügbar ist.

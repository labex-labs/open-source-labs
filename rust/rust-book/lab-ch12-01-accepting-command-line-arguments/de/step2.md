# Lesen der Argumentwerte

Um es `minigrep` zu ermöglichen, die Werte der Befehlszeilenargumente zu lesen, die wir ihm übergeben, benötigen wir die `std::env::args`-Funktion, die in der Standardbibliothek von Rust zur Verfügung steht. Diese Funktion gibt einen Iterator über die an `minigrep` übergebenen Befehlszeilenargumente zurück. Wir werden Iteratoren im Kapitel 13 ausführlicher behandeln. Für jetzt müssen Sie nur zwei Details zu Iteratoren wissen: Iteratoren erzeugen eine Reihe von Werten, und wir können die `collect`-Methode auf einem Iterator aufrufen, um ihn in eine Sammlung wie einen Vektor zu verwandeln, der alle Elemente enthält, die der Iterator erzeugt.

Der Code in Listing 12-1 ermöglicht es Ihrem `minigrep`-Programm, alle an ihn übergebenen Befehlszeilenargumente zu lesen und die Werte dann in einen Vektor zu sammeln.

Dateiname: `src/main.rs`

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    dbg!(args);
}
```

Listing 12-1: Sammeln der Befehlszeilenargumente in einen Vektor und Ausgeben derselben

Zuerst bringen wir das `std::env`-Modul in den Gültigkeitsbereich mit einem `use`-Statement, damit wir seine `args`-Funktion verwenden können. Beachten Sie, dass die `std::env::args`-Funktion in zwei Ebenen von Modulen geschachtelt ist. Wie wir im Kapitel 7 diskutiert haben, wählen wir im Falle einer gewünschten Funktion, die in mehr als einem Modul geschachtelt ist, das übergeordnete Modul in den Gültigkeitsbereich, statt die Funktion. Dadurch können wir leicht andere Funktionen aus `std::env` verwenden. Es ist auch weniger zweideutig als das Hinzufügen von `use std::env::args` und dann das Aufrufen der Funktion nur mit `args`, da `args` leicht für eine Funktion verwechselt werden könnte, die in dem aktuellen Modul definiert ist.

> **Die args-Funktion und ungültiges Unicode**
>
> Beachten Sie, dass `std::env::args` einen Fehler auslösen wird, wenn irgendein Argument ungültiges Unicode enthält. Wenn Ihr Programm Argumente mit ungültigem Unicode akzeptieren muss, verwenden Sie stattdessen `std::env::args_os`. Diese Funktion gibt einen Iterator zurück, der `OsString`-Werte statt `String`-Werte erzeugt. Wir haben hier aus Einfachheit `std::env::args` gewählt, weil `OsString`-Werte je nach Plattform unterschiedlich sind und mit `String`-Werten umzugehen komplexer ist.

In der ersten Zeile von `main` rufen wir `env::args` auf und verwenden sofort `collect`, um den Iterator in einen Vektor zu verwandeln, der alle von dem Iterator erzeugten Werte enthält. Wir können die `collect`-Funktion verwenden, um viele Arten von Sammlungen zu erstellen, daher annotieren wir explizit den Typ von `args`, um anzugeben, dass wir einen Vektor von Strings möchten. Obwohl Sie in Rust sehr selten Typen annotieren müssen, ist `collect` eine Funktion, für die Sie es oft tun müssen, weil Rust nicht in der Lage ist, die Art der Sammlung zu inferieren, die Sie möchten.

Schließlich drucken wir den Vektor mit der Debug-Makro. Versuchen wir zuerst den Code ohne Argumente und dann mit zwei Argumenten auszuführen:

```bash
$ cargo run
--snip--
[src/main.rs:5] args = [
"target/debug/minigrep",
]
$ cargo run -- needle haystack
--snip--
[src/main.rs:5] args = [
"target/debug/minigrep",
"needle",
"haystack",
]
```

Beachten Sie, dass der erste Wert im Vektor `"target/debug/minigrep"` ist, was der Name unseres Binärprogramms ist. Dies stimmt mit dem Verhalten der Argumentliste in C überein und ermöglicht es Programmen, den Namen, unter dem sie aufgerufen wurden, in ihrer Ausführung zu verwenden. Es ist oft praktisch, auf den Programmnamen zugreifen zu können, falls Sie ihn in Nachrichten ausgeben möchten oder das Verhalten des Programms basierend auf dem Befehlszeilenalias ändern möchten, mit dem das Programm aufgerufen wurde. Aber für die Zwecke dieses Kapitels werden wir ihn ignorieren und nur die zwei benötigten Argumente speichern.

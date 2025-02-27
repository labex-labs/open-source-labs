# Splitting Code into a Library Crate

Unser `minigrep`-Projekt sieht bisher gut aus! Jetzt werden wir die Datei `src/main.rs` aufteilen und einige Code in die Datei `src/lib.rs` verschieben. Auf diese Weise können wir den Code testen und eine `src/main.rs`-Datei mit weniger Verantwortungen haben.

Lassen Sie uns all den Code verschieben, der nicht in der `main`-Funktion von `src/main.rs` in `src/lib.rs` ist:

- Die `run`-Funktionsdefinition
- Die relevanten `use`-Anweisungen
- Die Definition von `Config`
- Die `Config::build`-Funktionsdefinition

Der Inhalt von `src/lib.rs` sollte die Signaturen haben, wie in Listing 12-13 gezeigt (wir haben die Körper der Funktionen aus Gründen der Kürze weggelassen). Beachten Sie, dass dies erst kompilieren wird, wenn wir `src/main.rs` in Listing 12-14 ändern.

Dateiname: `src/lib.rs`

```rust
use std::error::Error;
use std::fs;

pub struct Config {
    pub query: String,
    pub file_path: String,
}

impl Config {
    pub fn build(
        args: &[String],
    ) -> Result<Config, &'static str> {
        --snip--
    }
}

pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    --snip--
}
```

Listing 12-13: Moving `Config` and `run` into `src/lib.rs`

Wir haben liberal das `pub`-Schlüsselwort verwendet: auf `Config`, auf seine Felder und seine `build`-Methode und auf die `run`-Funktion. Wir haben jetzt einen Bibliothekskasten, der eine öffentliche API hat, die wir testen können!

Jetzt müssen wir den Code, den wir in `src/lib.rs` verschoben haben, in den Gültigkeitsbereich des Binärkastens in `src/main.rs` bringen, wie in Listing 12-14 gezeigt.

Dateiname: `src/main.rs`

```rust
use std::env;
use std::process;

use minigrep::Config;

fn main() {
    --snip--
    if let Err(e) = minigrep::run(config) {
        --snip--
    }
}
```

Listing 12-14: Using the `minigrep` library crate in `src/main.rs`

Wir fügen eine `use minigrep::Config`-Zeile hinzu, um den `Config`-Typ aus dem Bibliothekskasten in den Gültigkeitsbereich des Binärkastens zu bringen, und wir präfixieren die `run`-Funktion mit unserem Kastennamen. Jetzt sollten alle Funktionalitäten verbunden sein und funktionieren. Führen Sie das Programm mit `cargo run` aus und stellen Sie sicher, dass alles korrekt funktioniert.

Puh! Das war eine Menge Arbeit, aber wir haben uns für den Erfolg in der Zukunft gerüstet. Jetzt ist es viel einfacher, Fehler zu behandeln, und wir haben den Code modularer gemacht. Fast all unsere Arbeit wird von hier aus in `src/lib.rs` erledigt werden.

Lassen Sie uns von dieser neuen Modularität profitieren, indem wir etwas tun, was mit dem alten Code schwierig gewesen wäre, aber mit dem neuen Code einfach ist: wir werden einige Tests schreiben!

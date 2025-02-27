# Returning a Result Instead of Calling panic!

Stattdessen können wir einen `Result`-Wert zurückgeben, der in einem erfolgreichen Fall eine `Config`-Instanz enthalten wird und das Problem im Fehlerfall beschreiben wird. Wir werden auch den Funktionsnamen von `new` in `build` ändern, da viele Programmierer erwarten, dass `new`-Funktionen niemals fehlschlagen. Wenn `Config::build` mit `main` kommuniziert, können wir den `Result`-Typ verwenden, um anzuzeigen, dass ein Problem aufgetreten ist. Dann können wir `main` ändern, um eine `Err`-Variante in einen für unsere Benutzer praktikableren Fehler umzuwandeln, ohne den umgebenden Text über `thread'main'` und `RUST_BACKTRACE`, den ein Aufruf von `panic!` verursacht.

Listing 12-9 zeigt die Änderungen, die wir am Rückgabewert der Funktion vornehmen müssen, die wir jetzt `Config::build` nennen, und den Funktionskörper, um einen `Result` zurückzugeben. Beachten Sie, dass dies erst kompiliert, wenn wir auch `main` aktualisieren, was wir im nächsten Listing tun werden.

Dateiname: `src/main.rs`

```rust
impl Config {
    fn build(args: &[String]) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("not enough arguments");
        }

        let query = args[1].clone();
        let file_path = args[2].clone();

        Ok(Config { query, file_path })
    }
}
```

Listing 12-9: Returning a `Result` from `Config::build`

Unsere `build`-Funktion gibt ein `Result` zurück, das in einem erfolgreichen Fall eine `Config`-Instanz und im Fehlerfall einen `&'static str` enthält. Unsere Fehlerwerte werden immer Stringliterale sein, die die `'static`-Lebensdauer haben.

Wir haben zwei Änderungen im Funktionskörper vorgenommen: anstatt `panic!` aufzurufen, wenn der Benutzer nicht genug Argumente übergibt, geben wir jetzt einen `Err`-Wert zurück, und wir haben den `Config`-Rückgabewert in einem `Ok` eingeschlossen. Diese Änderungen machen die Funktion kompatibel mit ihrer neuen Typsignatur.

Das Zurückgeben eines `Err`-Werts von `Config::build` ermöglicht es der `main`-Funktion, den `Result`-Wert, der von der `build`-Funktion zurückgegeben wird, zu verarbeiten und im Fehlerfall den Prozess sauberer zu beenden.

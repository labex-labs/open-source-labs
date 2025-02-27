# Verwendung von Iterator-Trait-Methoden anstelle von Indizierung

Als nächstes werden wir den Körper von `Config::build` beheben. Da `args` das `Iterator`-Trait implementiert, wissen wir, dass wir die `next`-Methode darauf aufrufen können! Listing 13-20 aktualisiert den Code aus Listing 12-23, um die `next`-Methode zu verwenden.

Dateiname: `src/lib.rs`

```rust
impl Config {
    pub fn build(
        mut args: impl Iterator<Item = String>,
    ) -> Result<Config, &'static str> {
        args.next();

        let query = match args.next() {
            Some(arg) => arg,
            None => return Err("Didn't get a query string"),
        };

        let file_path = match args.next() {
            Some(arg) => arg,
            None => return Err("Didn't get a file path"),
        };

        let ignore_case = env::var("IGNORE_CASE").is_ok();

        Ok(Config {
            query,
            file_path,
            ignore_case,
        })
    }
}
```

Listing 13-20: Änderung des Körpers von `Config::build`, um Iterator-Methoden zu verwenden

Denken Sie daran, dass der erste Wert im Rückgabewert von `env::args` der Name des Programms ist. Wir möchten diesen ignorieren und zum nächsten Wert gelangen, daher rufen wir zuerst `next` auf und tun nichts mit dem Rückgabewert. Dann rufen wir `next` auf, um den Wert zu erhalten, den wir in das `query`-Feld von `Config` einfügen möchten. Wenn `next` `Some` zurückgibt, verwenden wir eine `match`, um den Wert zu extrahieren. Wenn es `None` zurückgibt, bedeutet das, dass nicht genug Argumente angegeben wurden, und wir geben frühzeitig einen `Err`-Wert zurück. Wir tun das Gleiche für den `filename`-Wert.

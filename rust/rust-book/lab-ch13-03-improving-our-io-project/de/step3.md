# Direkte Verwendung des zurückgegebenen Iterators

Öffnen Sie die Datei `src/main.rs` Ihres I/O-Projekts, die ungefähr so aussehen sollte:

Dateiname: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::build(&args).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {err}");
        process::exit(1);
    });

    --snip--
}
```

Wir werden zunächst den Anfang der `main`-Funktion, wie er in Listing 12-24 war, in den Code von Listing 13-18 umändern, der diesmal einen Iterator verwendet. Dies wird nicht kompilieren, bis wir auch `Config::build` aktualisieren.

Dateiname: `src/main.rs`

```rust
fn main() {
    let config =
        Config::build(env::args()).unwrap_or_else(|err| {
            eprintln!("Problem parsing arguments: {err}");
            process::exit(1);
        });

    --snip--
}
```

Listing 13-18: Übergeben des Rückgabewerts von `env::args` an `Config::build`

Die `env::args`-Funktion gibt einen Iterator zurück! Anstatt die Iteratorwerte in einem Vektor zu sammeln und dann einen Slice an `Config::build` zu übergeben, geben wir jetzt die Eigentumsgewalt des von `env::args` zurückgegebenen Iterators direkt an `Config::build` weiter.

Als nächstes müssen wir die Definition von `Config::build` aktualisieren. In der Datei `src/lib.rs` Ihres I/O-Projekts ändern wir die Signatur von `Config::build` so, dass sie wie in Listing 13-19 aussieht. Dies wird immer noch nicht kompilieren, weil wir den Funktionskörper aktualisieren müssen.

Dateiname: `src/lib.rs`

```rust
impl Config {
    pub fn build(
        mut args: impl Iterator<Item = String>,
    ) -> Result<Config, &'static str> {
        --snip--
```

Listing 13-19: Aktualisierung der Signatur von `Config::build`, um einen Iterator zu erwarten

Die Standardbibliothekdokumentation zur `env::args`-Funktion zeigt, dass der Typ des Iterators, den sie zurückgibt, `std::env::Args` ist und dass dieser Typ das `Iterator`-Trait implementiert und `String`-Werte zurückgibt.

Wir haben die Signatur der `Config::build`-Funktion aktualisiert, sodass der Parameter `args` einen generischen Typ mit den Trait-Bounds `impl Iterator<Item = String>` anstelle von `&[String]` hat. Dieses Verwendungsszenario der `impl Trait`-Syntax, über die wir in "Traits as Parameters" diskutiert haben, bedeutet, dass `args` irgendein Typ sein kann, der das `Iterator`-Typ implementiert und `String`-Elemente zurückgibt.

Da wir die Eigentumsgewalt von `args` übernehmen und `args` durch das Iterieren darüber mutieren werden, können wir das `mut`-Schlüsselwort in die Spezifikation des `args`-Parameters hinzufügen, um es mutierbar zu machen.

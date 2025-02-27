# Entfernen eines Klons mithilfe eines Iterators

In Listing 12-6 haben wir Code hinzugefügt, der einen Slice von `String`-Werten nahm und eine Instanz der `Config`-Struktur erzeugte, indem er in den Slice indizierte und die Werte klonierte, was es der `Config`-Struktur ermöglichte, diese Werte zu besitzen. In Listing 13-17 haben wir die Implementierung der `Config::build`-Funktion wiedergegeben, wie sie in Listing 12-23 war.

Dateiname: `src/lib.rs`

```rust
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

Listing 13-17: Wiederholung der `Config::build`-Funktion aus Listing 12-23

Damals sagten wir, dass wir uns nicht um die ineffizienten `clone`-Aufrufe kümmern müssen, da wir sie später entfernen würden. Nun ist diese Zeit gekommen!

Wir brauchten hier `clone`, weil wir in dem Parameter `args` einen Slice mit `String`-Elementen haben, aber die `build`-Funktion besitzt `args` nicht. Um die Eigentumsgewalt einer `Config`-Instanz zurückzugeben, mussten wir die Werte aus den `query`- und `filename`-Feldern von `Config` klonen, damit die `Config`-Instanz ihre Werte besitzen kann.

Mit unseren neuen Kenntnissen über Iteratoren können wir die `build`-Funktion ändern, um die Eigentumsgewalt eines Iterators als Argument zu übernehmen, anstatt einen Slice zu entleihen. Wir werden die Iteratorfunktionalität verwenden, anstatt den Code, der die Länge des Slices überprüft und in bestimmte Positionen indiziert. Dies wird klären, was die `Config::build`-Funktion tut, da der Iterator die Werte zugreifen wird.

Sobald `Config::build` die Eigentumsgewalt des Iterators übernimmt und auf Indexoperationen verzichtet, die etwas entleihen, können wir die `String`-Werte aus dem Iterator in `Config` verschieben, anstatt `clone` aufzurufen und eine neue Allokation zu machen.

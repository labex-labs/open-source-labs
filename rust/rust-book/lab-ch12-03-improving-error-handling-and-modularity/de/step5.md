# Creating a Constructor for Config

Bisher haben wir die Logik, die für die Analyse der Befehlszeilenargumente verantwortlich ist, aus `main` extrahiert und in die `parse_config`-Funktion gelegt. Dadurch konnten wir erkennen, dass die `query`- und `file_path`-Werte zusammenhängen, und diese Beziehung sollte in unserem Code vermittelt werden. Anschließend haben wir eine `Config`-Struktur hinzugefügt, um den zusammenhängenden Zweck von `query` und `file_path` zu benennen und um die Werte als Strukturfeldnamen zurückgeben zu können, wenn die `parse_config`-Funktion aufgerufen wird.

Da der Zweck der `parse_config`-Funktion jetzt darin besteht, eine `Config`-Instanz zu erstellen, können wir `parse_config` von einer einfachen Funktion in eine Funktion namens `new` umwandeln, die mit der `Config`-Struktur assoziiert ist. Diese Änderung wird den Code idiomatischer machen. Wir können Instanzen von Typen in der Standardbibliothek, wie `String`, erstellen, indem wir `String::new` aufrufen. Ähnlich können wir `parse_config` in eine mit `Config` assoziierte `new`-Funktion umwandeln, sodass wir Instanzen von `Config` erstellen können, indem wir `Config::new` aufrufen. Listing 12-7 zeigt die erforderlichen Änderungen.

Dateiname: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

  1 let config = Config::new(&args);

    --snip--
}

--snip--

2 impl Config {
  3 fn new(args: &[String]) -> Config {
        let query = args[1].clone();
        let file_path = args[2].clone();

        Config { query, file_path }
    }
}
```

Listing 12-7: Changing `parse_config` into `Config::new`

Wir haben `main` aktualisiert, wo wir zuvor `parse_config` aufruften, um stattdessen `Config::new` aufzurufen \[1\]. Wir haben den Namen von `parse_config` in `new` geändert \[3\] und ihn innerhalb eines `impl`-Blocks verschoben \[2\], was die `new`-Funktion mit `Config` assoziiert. Versuchen Sie, diesen Code erneut zu kompilieren, um sicherzustellen, dass er funktioniert.

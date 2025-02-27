# Handling Errors Returned from run in main

Wir werden nach Fehlern suchen und sie mit einer Technik behandeln, die ähnlich der ist, die wir in Listing 12-10 mit `Config::build` verwendet haben, aber mit einem kleinen Unterschied:

Dateiname: `src/main.rs`

```rust
fn main() {
    --snip--

    println!("Searching for {}", config.query);
    println!("In file {}", config.file_path);

    if let Err(e) = run(config) {
        println!("Application error: {e}");
        process::exit(1);
    }
}
```

Wir verwenden `if let` anstatt `unwrap_or_else`, um zu überprüfen, ob `run` einen `Err`-Wert zurückgibt und `process::exit(1)` aufzurufen, wenn dies der Fall ist. Die `run`-Funktion gibt keinen Wert zurück, den wir auf die gleiche Weise `unwrap` möchten, wie `Config::build` die `Config`-Instanz zurückgibt. Da `run` im Erfolgfall `()` zurückgibt, interessieren wir uns nur für das Entdecken eines Fehlers, daher brauchen wir nicht `unwrap_or_else`, um den entpackten Wert zurückzugeben, der nur `()` sein würde.

Der Körper der `if let`- und der `unwrap_or_else`-Funktionen ist in beiden Fällen gleich: wir drucken den Fehler und beenden das Programm.

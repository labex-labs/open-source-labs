# Returning Errors from the run Function

Mit der verbleibenden Programmlogik in die `run`-Funktion aufgeteilt, können wir die Fehlerbehandlung verbessern, wie wir es in Listing 12-9 mit `Config::build` getan haben. Anstatt das Programm zu einem Absturz zu bringen, indem wir `expect` aufrufen, wird die `run`-Funktion ein `Result<T, E>` zurückgeben, wenn etwas schief geht. Dies wird uns ermöglichen, die Logik um die Fehlerbehandlung weiter in `main` auf eine benutzerfreundliche Weise zusammenzufassen. Listing 12-12 zeigt die Änderungen, die wir am Signatur und am Körper von `run` vornehmen müssen.

Dateiname: `src/main.rs`

```rust
1 use std::error::Error;

--snip--

2 fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)3?;

    println!("With text:\n{contents}");

  4 Ok(())
}
```

Listing 12-12: Changing the `run` function to return `Result`

Wir haben hier drei bedeutende Änderungen vorgenommen. Erstens haben wir den Rückgabetyp der `run`-Funktion in `Result<(), Box<dyn Error>>` geändert \[2\]. Diese Funktion hat zuvor den Einheitstyp `()` zurückgegeben, und wir behalten diesen als den Wert bei, der im `Ok`-Fall zurückgegeben wird.

Für den Fehlertyp haben wir das _Trait-Objekt_ `Box<dyn Error>` verwendet (und wir haben `std::error::Error` mit einem `use`-Statement am Anfang in den Gültigkeitsbereich gebracht \[1\]). Wir werden Trait-Objekte im Kapitel 17 behandeln. Für jetzt wissen Sie einfach, dass `Box<dyn Error>` bedeutet, dass die Funktion einen Typ zurückgeben wird, der das `Error`-Trait implementiert, aber wir müssen nicht angeben, welchen bestimmten Typ der Rückgabewert sein wird. Dies gibt uns die Flexibilität, Fehlerwerte zurückzugeben, die in verschiedenen Fehlerfällen möglicherweise unterschiedlicher Typen sein können. Das `dyn`-Schlüsselwort ist die Abkürzung für _dynamisch_.

Zweitens haben wir den Aufruf von `expect` entfernt und stattdessen den `?`-Operator verwendet \[3\], wie wir es im Kapitel 9 besprochen haben. Anstatt bei einem Fehler `panic!` aufzurufen, wird `?` den Fehlerwert aus der aktuellen Funktion zurückgeben, damit der Aufrufer ihn behandeln kann.

Drittens gibt die `run`-Funktion jetzt im Erfolgfall einen `Ok`-Wert zurück \[4\]. Wir haben im Signatur den Erfolgstyp der `run`-Funktion als `()` deklariert, was bedeutet, dass wir den Einheitstyp-Wert in den `Ok`-Wert einpacken müssen. Diese `Ok(())`-Syntax mag zunächst ein wenig seltsam aussehen, aber das Verwenden von `()` auf diese Weise ist die übliche Methode, um anzuzeigen, dass wir `run` nur wegen seiner Nebeneffekte aufrufen; es gibt keinen Wert zurück, den wir benötigen.

Wenn Sie diesen Code ausführen, wird er kompilieren, aber es wird eine Warnung angezeigt:

    warning: unused `Result` that must be used
      --> src/main.rs:19:5
       |
    19 |     run(config);
       |     ^^^^^^^^^^^^
       |
       = note: `#[warn(unused_must_use)]` on by default
       = note: this `Result` may be an `Err` variant, which should be
    handled

Rust sagt uns, dass unser Code den `Result`-Wert ignoriert hat und der `Result`-Wert möglicherweise anzeigt, dass ein Fehler aufgetreten ist. Aber wir überprüfen nicht, ob ein Fehler aufgetreten ist, und der Compiler erinnert uns daran, dass wir wahrscheinlich hier irgendeinen Fehlerbehandlungs-Code haben sollten! Lassen Sie uns dieses Problem jetzt beheben.

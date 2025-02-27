# Speichern von übereinstimmenden Zeilen

Um diese Funktion abzuschließen, benötigen wir eine Möglichkeit, die übereinstimmenden Zeilen zu speichern, die wir zurückgeben möchten. Dazu können wir ein mutables Vektor vor der `for`-Schleife erstellen und die `push`-Methode aufrufen, um eine `line` im Vektor zu speichern. Nach der `for`-Schleife geben wir den Vektor zurück, wie in Listing 12-19 gezeigt.

Dateiname: `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    let mut results = Vec::new();

    for line in contents.lines() {
        if line.contains(query) {
            results.push(line);
        }
    }

    results
}
```

Listing 12-19: Speichern der übereinstimmenden Zeilen, damit wir sie zurückgeben können

Jetzt sollte die `search`-Funktion nur die Zeilen zurückgeben, die `query` enthalten, und unser Test sollte bestanden werden. Lassen Sie uns den Test ausführen:

```bash
$ cargo test
--snip--
running 1 test
test tests::one_result... ok

test result: ok. 1 passed
0 failed
0 ignored
0 measured
0
filtered out
finished in 0.00s
```

Unser Test ist bestanden, so dass wir wissen, dass es funktioniert!

An diesem Punkt könnten wir Möglichkeiten zur Umgestaltung der Implementierung der `search`-Funktion erwägen, während wir die Tests bestehen lassen, um die gleiche Funktionalität beizubehalten. Der Code in der `search`-Funktion ist nicht schlecht, aber er nutzt einige nützliche Funktionen von Iteratoren nicht aus. Wir werden in Kapitel 13 auf dieses Beispiel zurückkommen, wo wir Iteratoren im Detail untersuchen und sehen, wie wir es verbessern können.

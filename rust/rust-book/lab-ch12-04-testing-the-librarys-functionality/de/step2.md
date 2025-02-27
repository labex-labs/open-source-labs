# Schreiben eines fehlschlagenden Tests

Da wir sie nicht mehr benötigen, entfernen wir die `println!`-Anweisungen aus `src/lib.rs` und `src/main.rs`, die wir früher verwendet haben, um das Verhalten des Programms zu überprüfen. Dann fügen wir in `src/lib.rs` ein `tests`-Modul mit einer Testfunktion hinzu, wie wir es im Kapitel 11 getan haben. Die Testfunktion definiert das Verhalten, das wir von der `search`-Funktion erwarten: Sie nimmt eine Abfrage und den Text, in dem gesucht werden soll, und gibt nur die Zeilen aus dem Text zurück, die die Abfrage enthalten. Listing 12-15 zeigt diesen Test, der noch nicht kompilieren wird.

Dateiname: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn one_result() {
        let query = "duct";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.";

        assert_eq!(
            vec!["safe, fast, productive."],
            search(query, contents)
        );
    }
}
```

Listing 12-15: Erstellen eines fehlschlagenden Tests für die `search`-Funktion, die wir haben möchten

Dieser Test sucht nach dem String `"duct"`. Der Text, in dem wir suchen, besteht aus drei Zeilen, von denen nur eine `"duct"` enthält (beachten Sie, dass der Backslash nach der öffnenden Anführungszeichen Rust mitteilt, keine Zeilenumbrüche am Anfang des Inhalts dieses Stringliterals zu platzieren). Wir überprüfen, dass der von der `search`-Funktion zurückgegebene Wert nur die Zeile enthält, die wir erwarten.

Wir können diesen Test noch nicht ausführen und beobachten, wie er fehlschlägt, da der Test noch nicht einmal kompiliert: Die `search`-Funktion existiert noch nicht! In Übereinstimmung mit den TDD-Prinzipien fügen wir nur so viel Code hinzu, um den Test zu kompilieren und auszuführen, indem wir eine Definition der `search`-Funktion hinzufügen, die immer einen leeren Vektor zurückgibt, wie in Listing 12-16 gezeigt. Dann sollte der Test kompilieren und fehlschlagen, da ein leerer Vektor nicht mit einem Vektor übereinstimmt, der die Zeile `"safe, fast, productive."` enthält.

Dateiname: `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    vec![]
}
```

Listing 12-16: Definieren Sie nur so viel der `search`-Funktion, dass Ihr Test kompiliert

Beachten Sie, dass wir in der Signatur von `search` ein explizites Lebenszeitparametername `'a` definieren müssen und dieses Lebenszeitparametername mit dem `contents`-Argument und dem Rückgabewert verwenden. Erinnern Sie sich aus Kapitel 10, dass die Lebenszeitparameter bestimmen, welches Argumentlebenszeit mit der Lebenszeit des Rückgabewerts verbunden ist. Im Falle von `search` geben wir an, dass der zurückgegebene Vektor String-Slices enthalten soll, die Slices des `contents`-Arguments referenzieren (statt des `query`-Arguments).

Mit anderen Worten, wir sagen Rust, dass die Daten, die von der `search`-Funktion zurückgegeben werden, so lange leben wie die Daten, die als `contents`-Argument an die `search`-Funktion übergeben werden. Dies ist wichtig! Die Daten, auf die ein Slice verweist, müssen gültig sein, damit die Referenz gültig ist; wenn der Compiler annimmt, dass wir String-Slices von `query` statt von `contents` erstellen, wird er seine Sicherheitsüberprüfungen falsch durchführen.

Wenn wir die Lebenszeitangaben vergessen und versuchen, diese Funktion zu kompilieren, erhalten wir diesen Fehler:

```bash
error[E0106]: missing lifetime specifier
  --> src/lib.rs:31:10
   |
29 |     query: &str,
   |            ----
30 |     contents: &str,
   |               ----
31 | ) -> Vec<&str> {
   |          ^ expected named lifetime parameter
   |
   = help: this function's return type contains a borrowed value, but the
signature does not say whether it is borrowed from `query` or `contents`
help: consider introducing a named lifetime parameter
   |
28 ~ pub fn search<'a>(
29 ~     query: &'a str,
30 ~     contents: &'a str,
31 ~ ) -> Vec<&'a str> {
   |
```

Rust kann nicht wissen, welches der beiden Argumente wir benötigen, daher müssen wir es ihm explizit sagen. Da `contents` das Argument ist, das alle unseren Text enthält und wir die Teile dieses Texts zurückgeben möchten, die übereinstimmen, wissen wir, dass `contents` das Argument ist, das mit dem Rückgabewert mithilfe der Lebenszeitsyntax verbunden werden sollte.

Andere Programmiersprachen erfordern es nicht, Argumente mit Rückgabewerten in der Signatur zu verbinden, aber diese Praxis wird mit der Zeit einfacher. Sie können diesen Beispiel mit den Beispielen in "Validating References with Lifetimes" vergleichen.

Lassen Sie uns jetzt den Test ausführen:

```bash
$ cargo test
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished test [unoptimized + debuginfo] target(s) in 0.97s
     Running unittests src/lib.rs (target/debug/deps/minigrep-9cd200e5fac0fc94)

running 1 test
test tests::one_result... FAILED

failures:

---- tests::one_result stdout ----
thread 'tests::one_result' panicked at 'assertion failed: `(left == right)`
  left: `["safe, fast, productive."]`,
 right: `[]`', src/lib.rs:47:9
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace


failures:
    tests::one_result

test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out;
finished in 0.00s

error: test failed, to rerun pass '--lib'
```

Super, der Test fehlschlägt, genau wie wir es erwartet haben. Lassen Sie uns den Test erfolgreich machen!

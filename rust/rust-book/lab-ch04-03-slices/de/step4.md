# String-Slices als Parameter

Das Wissen, dass Sie Slices von Literalen und `String`-Werten nehmen können, führt uns zu einer weiteren Verbesserung von `first_word`, und das ist seine Signatur:

```rust
fn first_word(s: &String) -> &str {
```

Ein erfahrener Rust-Programmierer würde stattdessen die in Listing 4-9 gezeigte Signatur schreiben, da es uns ermöglicht, die gleiche Funktion sowohl auf `&String`-Werten als auch auf `&str`-Werten zu verwenden.

```rust
fn first_word(s: &str) -> &str {
```

Listing 4-9: Verbessern der `first_word`-Funktion, indem ein String-Slice für den Typ des `s`-Parameters verwendet wird

Wenn wir einen String-Slice haben, können wir diesen direkt übergeben. Wenn wir einen `String` haben, können wir einen Slice des `String` oder eine Referenz auf den `String` übergeben. Diese Flexibilität nutzt _Deref-Koerzions_, ein Feature, das wir in "Implizite Deref-Koerzions mit Funktionen und Methoden" behandeln werden.

Das Definieren einer Funktion, die einen String-Slice statt einer Referenz auf einen `String` nimmt, macht unsere API allgemeiner und nützlicher, ohne dass dabei irgend eine Funktionalität verloren geht:

Dateiname: `src/main.rs`

```rust
fn main() {
    let my_string = String::from("hello world");

    // `first_word` funktioniert auf Slices von `String`s, ob partiell
    // oder ganz
    let word = first_word(&my_string[0..6]);
    let word = first_word(&my_string[..]);
    // `first_word` funktioniert auch auf Referenzen auf `String`s, die
    // äquivalent zu ganzen Slices von `String`s sind
    let word = first_word(&my_string);

    let my_string_literal = "hello world";

    // `first_word` funktioniert auf Slices von String-Literalen,
    // ob partiell oder ganz
    let word = first_word(&my_string_literal[0..6]);
    let word = first_word(&my_string_literal[..]);

    // Da String-Literale *selbst* bereits String-Slices sind,
    // funktioniert dies auch ohne die Slice-Syntax!
    let word = first_word(my_string_literal);
}
```

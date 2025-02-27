# Rohe Bezeichner

Rust hat wie viele Programmiersprachen das Konzept der "Schlüsselwörter". Diese Bezeichner haben eine Bedeutung für die Sprache und können daher nicht an Stellen wie Variablennamen, Funktionsnamen und anderen Orten verwendet werden. Rohe Bezeichner ermöglichen es Ihnen, Schlüsselwörter an Orten zu verwenden, an denen sie normalerweise nicht erlaubt sind. Dies ist besonders nützlich, wenn Rust neue Schlüsselwörter einführt und eine Bibliothek, die eine ältere Edition von Rust verwendet, eine Variable oder Funktion mit dem gleichen Namen wie ein in einer neueren Edition eingeführtes Schlüsselwort hat.

Nehmen wir beispielsweise eine Bibliothek `foo`, die mit der 2015-Edition von Rust kompiliert wurde und eine Funktion namens `try` exportiert. Dieses Schlüsselwort ist für eine neue Funktion in der 2018-Edition reserviert, so dass wir ohne rohe Bezeichner keine Möglichkeit hätten, die Funktion zu benennen.

```rust
extern crate foo;

fn main() {
    foo::try();
}
```

Sie erhalten folgende Fehlermeldung:

```plaintext
error: expected identifier, found keyword `try`
 --> src/main.rs:4:4
  |
4 | foo::try();
  |      ^^^ expected identifier, found keyword
```

Sie können dies mit einem rohen Bezeichner schreiben:

```rust
extern crate foo;

fn main() {
    foo::r#try();
}
```

# Anweisungen und Ausdrücke

Funktionskörper bestehen aus einer Reihe von Anweisungen, die optional mit einem Ausdruck enden. Bislang haben die Funktionen, die wir behandelt haben, keinen abschließenden Ausdruck, aber du hast einen Ausdruck als Teil einer Anweisung gesehen. Da Rust eine ausdrucksbasiertes Sprach ist, ist dies eine wichtige Unterscheidung, die zu verstehen ist. Andere Sprachen haben keine gleichen Unterscheidungen, also schauen wir uns an, was Anweisungen und Ausdrücke sind und wie ihre Unterschiede die Funktionskörper beeinflussen.

- **Anweisungen**: sind Anweisungen, die eine Aktion ausführen und keinen Wert zurückgeben.
- **Ausdrücke**: evaluieren zu einem Ergebniswert. Schauen wir uns einige Beispiele an.

Wir haben tatsächlich bereits Anweisungen und Ausdrücke verwendet. Das Erstellen einer Variable und das Zuweisen eines Werts mit dem `let`-Schlüsselwort ist eine Anweisung. In Listing 3-1 ist `let y = 6;` eine Anweisung.

Dateiname: `src/main.rs`

```rust
fn main() {
    let y = 6;
}
```

Listing 3-1: Eine `main`-Funktionsdeklaration mit einer Anweisung

Funktionsdefinitionen sind ebenfalls Anweisungen; das gesamte vorherige Beispiel ist in sich eine Anweisung.

Anweisungen geben keine Werte zurück. Daher kannst du eine `let`-Anweisung nicht an eine andere Variable zuweisen, wie im folgenden Code versucht wird; du bekommst einen Fehler:

Dateiname: `src/main.rs`

```rust
fn main() {
    let x = (let y = 6);
}
```

Wenn du dieses Programm ausführst, siehst du einen Fehler wie diesen:

```bash
$ cargo run
   Compiling functions v0.1.0 (file:///projects/functions)
error: expected expression, found statement (`let`)
 --> src/main.rs:2:14
  |
2 |     let x = (let y = 6);
  |              ^^^^^^^^^
  |
  = note: variable declaration using `let` is a statement

error[E0658]: `let` expressions in this position are unstable
 --> src/main.rs:2:14
  |
2 |     let x = (let y = 6);
  |              ^^^^^^^^^
  |
  = note: see issue #53667 <https://github.com/rust-lang/rust/issues/53667> for
more information
```

Die Anweisung `let y = 6` gibt keinen Wert zurück, sodass es nichts gibt, an das `x` gebunden werden kann. Dies unterscheidet sich von anderen Sprachen wie C und Ruby, in denen die Zuweisung den Wert der Zuweisung zurückgibt. In diesen Sprachen kannst du `x = y = 6` schreiben und sowohl `x` als auch `y` den Wert `6` zuweisen; das ist in Rust nicht der Fall.

Ausdrücke evaluieren zu einem Wert und machen den größten Teil des restlichen Codes aus, den du in Rust schreiben wirst. Betrachte eine mathematische Operation wie `5 + 6`, die ein Ausdruck ist, der den Wert `11` ergibt. Ausdrücke können Teil von Anweisungen sein: In Listing 3-1 ist die `6` in der Anweisung `let y = 6;` ein Ausdruck, der den Wert `6` ergibt. Ein Funktionsaufruf ist ein Ausdruck. Ein Makroaufruf ist ein Ausdruck. Ein neuer Bereichsblock, der mit geschweiften Klammern erstellt wird, ist ein Ausdruck, z.B.:

Dateiname: `src/main.rs`

```rust
fn main() {
  1 let y = {2
        let x = 3;
      3 x + 1
    };

    println!("The value of y is: {y}");
}
```

Der Ausdruck \[2\] ist ein Block, der in diesem Fall den Wert `4` ergibt. Dieser Wert wird als Teil der `let`-Anweisung \[1\] an `y` gebunden. Beachte die Zeile ohne Semikolon am Ende \[3\], die anders als die meisten Zeilen ist, die du bisher gesehen hast. Ausdrücke enthalten keine abschließenden Semikolons. Wenn du ein Semikolon am Ende eines Ausdrucks hinzufügst, verwandelst du ihn in eine Anweisung, und er wird dann keinen Wert zurückgeben. Halte dies im Hinterkopf, wenn du im nächsten Schritt die Funktionsrückgabewerte und Ausdrücke erkundest.

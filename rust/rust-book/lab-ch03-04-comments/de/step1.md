# Kommentare

Alle Programmierer streben danach, ihren Code so einfach wie möglich zu verstehen, aber manchmal ist zusätzliche Erklärung erforderlich. In diesen Fällen hinterlassen Programmierer _Kommentare_ in ihrem Quellcode, die der Compiler ignorieren wird, aber die für Menschen, die den Quellcode lesen, nützlich sein können.

Hier ist ein einfacher Kommentar:

```rust
// hallo, Welt
```

In Rust beginnt der übliche Kommentarstil mit zwei Schrägstrichen, und der Kommentar geht bis zum Ende der Zeile. Für Kommentare, die über eine Zeile hinausgehen, musst du in jeder Zeile `//` hinzufügen, wie folgt:

    // Wir machen hier etwas Kompliziertes, so kompliziert, dass wir mehrere
    // Zeilen Kommentar benötigen, um es zu erklären! Puh! Hoffentlich erklärt
    // dieser Kommentar, was passiert.

Kommentare können auch am Ende von Zeilen mit Code platziert werden:

Dateiname: `src/main.rs`

```rust
fn main() {
    let lucky_number = 7; // Ich fühle mich heute glücklich
}
```

Aber du wirst sie öfter in diesem Format sehen, mit dem Kommentar in einer separaten Zeile über dem Code, den er kommentiert:

Dateiname: `src/main.rs`

```rust
fn main() {
    // Ich fühle mich heute glücklich
    let lucky_number = 7;
}
```

Rust hat auch eine andere Art von Kommentaren, die Dokumentationskommentare, über die wir in "Veröffentlichen eines Crates auf Crates.io" sprechen werden.

# Kommentare

Jedes Programm erfordert Kommentare, und Rust unterstützt einige verschiedene Arten:

- _Reguläre Kommentare_, die vom Compiler ignoriert werden:
  - `// Zeilenkommentare, die bis zum Ende der Zeile gehen.`
  - `/* Blockkommentare, die bis zum schließenden Trennzeichen gehen. */`
- _Dok-Kommentare_, die in HTML-Bibliothekdokumentation analysiert werden:
  - `/// Generiere Bibliothekdokumentation für das folgende Element.`
  - `//! Generiere Bibliothekdokumentation für das umgebende Element.`

```rust
fn main() {
    // Dies ist ein Beispiel für einen Zeilenkommentar.
    // Es gibt zwei Schrägstriche am Anfang der Zeile.
    // Und nichts, was nach diesen geschrieben wird, wird vom Compiler gelesen.

    // println!("Hello, world!");

    // Führe es aus. Siehe? Versuche jetzt, die beiden Schrägstriche zu löschen und es erneut auszuführen.

    /*
     * Dies ist ein anderer Typ von Kommentar, ein Blockkommentar. Im Allgemeinen
     * werden Zeilenkommentare als empfohlene Kommentarstil angesehen. Aber Blockkommentare
     * sind extrem nützlich, um Teile des Codes vorübergehend zu deaktivieren.
     * /* Blockkommentare können /* geschachtelt */ */ werden, sodass es nur wenige
     * Tastatureingaben benötigt, um alles in dieser main()-Funktion auszukommentieren.
     * /*/*/* Probieren Sie es selbst aus! */*/*/
     */

    /*
    Hinweis: Die vorherige Spalte von `*` war ausschließlich für den Stil. Es besteht
    keine tatsächliche Notwendigkeit dafür.
    */

    // Sie können Ausdrücke leichter mit Blockkommentaren manipulieren
    // als mit Zeilenkommentaren. Versuchen Sie, die Kommentartrennzeichen zu löschen,
    // um das Ergebnis zu ändern:
    let x = 5 + /* 90 + */ 5;
    println!("Ist `x` 10 oder 100? x = {}", x);
}
```

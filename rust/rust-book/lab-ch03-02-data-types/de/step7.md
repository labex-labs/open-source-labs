# Der Zeichentyp

Rusts `char`-Typ ist der ursprünglichste alphabetische Typ der Sprache. Hier sind einige Beispiele für die Deklaration von `char`-Werten:

Dateiname: `src/main.rs`

```rust
fn main() {
    let c = 'z';
    let z: char = 'ℤ'; // mit expliziter Typangabe
    let heart_eyed_cat = '😻';
}
```

Beachten Sie, dass wir `char`-Literale mit einfachen Anführungszeichen angeben, im Gegensatz zu String-Literalen, die doppelte Anführungszeichen verwenden. Rusts `char`-Typ hat eine Größe von vier Bytes und repräsentiert einen Unicode-Skalarnwert, was bedeutet, dass er viel mehr als nur ASCII repräsentieren kann. Akzentierte Buchstaben; chinesische, japanische und koreanische Zeichen; Emojis; und Leerzeichen mit null Breite sind alle gültige `char`-Werte in Rust. Unicode-Skalarnwerte reichen von `U+0000` bis `U+D7FF` und `U+E000` bis `U+10FFFF` eingeschlossen. Ein "Zeichen" ist jedoch kein echtes Konzept in Unicode, sodass Ihre menschliche Intuition für das, was ein "Zeichen" ist, möglicherweise nicht mit dem übereinstimmt, was ein `char` in Rust ist. Wir werden dieses Thema im Abschnitt "Speichern von UTF-8-kodiertem Text mit Strings" im Detail besprechen.

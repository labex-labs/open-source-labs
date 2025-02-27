# Lifetime Annotations in Struct Definitions

Bisher haben alle von uns definierten Structs nur eigene Typen gespeichert. Wir können Structs definieren, um Referenzen zu speichern, aber in diesem Fall müssten wir eine Lebenszeitannotation für jede Referenz in der Struct-Definition hinzufügen. Listing 10-24 hat einen Struct namens `ImportantExcerpt`, der einen String-Slice speichert.

Dateiname: `src/main.rs`

```rust
1 struct ImportantExcerpt<'a> {
  2 part: &'a str,
}

fn main() {
  3 let novel = String::from(
        "Call me Ishmael. Some years ago..."
    );
  4 let first_sentence = novel
       .split('.')
       .next()
       .expect("Could not find a '.'");
  5 let i = ImportantExcerpt {
        part: first_sentence,
    };
}
```

Listing 10-24: Ein Struct, der eine Referenz speichert und eine Lebenszeitannotation erfordert

Dieser Struct hat das einzelne Feld `part`, das einen String-Slice speichert, der eine Referenz ist \[2\]. Wie bei generischen Datentypen deklarieren wir den Namen des generischen Lebenszeitparameters innerhalb von spitzen Klammern nach dem Namen des Structs, damit wir den Lebenszeitparameter im Körper der Struct-Definition verwenden können \[1\]. Diese Annotation bedeutet, dass eine Instanz von `ImportantExcerpt` nicht länger existieren kann als die Referenz, die sie in ihrem `part`-Feld hält.

Die `main`-Funktion hier erstellt eine Instanz des `ImportantExcerpt`-Structs \[5\], der eine Referenz auf den ersten Satz der von der Variable `novel` \[3\] besitzten `String` \[4\] hält. Die Daten in `novel` existieren vor der Erstellung der `ImportantExcerpt`-Instanz. Darüber hinaus geht `novel` erst außer Gültigkeitsbereich, nachdem die `ImportantExcerpt` außer Gültigkeitsbereich ist, sodass die Referenz in der `ImportantExcerpt`-Instanz gültig ist.

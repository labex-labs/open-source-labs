# Unsichere Operationen

Als Einführung in diesen Abschnitt, um von den offiziellen Dokumentationen zu zitieren: "Man sollte versuchen, die Menge an unsicherem Code in einer Codebasis zu minimieren." Im Licht dessen, fangen wir an! Unsichere Anmerkungen in Rust werden verwendet, um die von dem Compiler eingeführten Schutzmechanismen zu umgehen; genauer gesagt, gibt es vier Hauptsachen, für die `unsafe` verwendet wird:

- Dereferenzieren von rohen Zeigern
- Aufrufen von Funktionen oder Methoden, die `unsafe` sind (einschließlich des Aufrufs einer Funktion über FFI, siehe [einem vorherigen Kapitel des Buches])
- Zugreifen auf oder Ändern von statischen veränderlichen Variablen
- Implementieren unsicherer Traits

## Rohzeiger

Rohzeiger `*` und Referenzen `&T` verhalten sich ähnlich, aber Referenzen sind immer sicher, da aufgrund des Borrow-Checkers garantiert ist, dass sie auf gültige Daten verweisen. Das Dereferenzieren eines rohen Zeigers kann nur innerhalb eines unsicheren Blocks erfolgen.

```rust
fn main() {
    let raw_p: *const u32 = &10;

    unsafe {
        assert!(*raw_p == 10);
    }
}
```

## Aufrufen unsicherer Funktionen

Einige Funktionen können als `unsafe` deklariert werden, was bedeutet, dass es die Verantwortung des Programmierers ist, die Korrektheit zu gewährleisten, anstatt des Compilers. Ein Beispiel dafür ist \[`std::slice::from_raw_parts`\], das einen Slice erstellt, wenn ein Zeiger auf das erste Element und eine Länge angegeben werden.

```rust
use std::slice;

fn main() {
    let some_vector = vec![1, 2, 3, 4];

    let pointer = some_vector.as_ptr();
    let length = some_vector.len();

    unsafe {
        let my_slice: &[u32] = slice::from_raw_parts(pointer, length);

        assert_eq!(some_vector.as_slice(), my_slice);
    }
}
```

Für `slice::from_raw_parts` ist eine der Annahmen, die _erhalten_ werden _muss_, dass der übergebene Zeiger auf gültigen Speicher zeigt und dass der daraufhin angezeigte Speicher vom richtigen Typ ist. Wenn diese Invarianten nicht eingehalten werden, ist das Verhalten des Programms undefiniert und es ist nicht vorhersehbar, was passieren wird.

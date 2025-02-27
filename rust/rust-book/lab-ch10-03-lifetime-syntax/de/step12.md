# Generic Type Parameters, Trait Bounds, and Lifetimes Together

Schauen wir uns kurz die Syntax an, um generische Typparameter, Trait-Bounds und Lebenszeiten in einer Funktion anzugeben!

```rust
use std::fmt::Display;

fn longest_with_an_announcement<'a, T>(
    x: &'a str,
    y: &'a str,
    ann: T,
) -> &'a str
where
    T: Display,
{
    println!("Announcement! {ann}");
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

Dies ist die `longest`-Funktion aus Listing 10-21, die die längere von zwei String-Slices zurückgibt. Aber jetzt hat es einen zusätzlichen Parameter namens `ann` vom generischen Typ `T`, der mit jedem Typ ausgefüllt werden kann, der das `Display`-Trait implementiert, wie in der `where`-Klausel angegeben. Dieser zusätzliche Parameter wird mit `{}` gedruckt, weshalb die `Display`-Trait-Bound erforderlich ist. Da Lebenszeiten eine Art von Generics sind, werden die Deklarationen des Lebenszeitparameters `'a` und des generischen Typparameters `T` in derselben Liste innerhalb der spitzen Klammern nach dem Funktionsnamen angegeben.

# Lifetime Annotations in Method Definitions

Wenn wir Methoden für einen Struct mit Lebenszeiten implementieren, verwenden wir die gleiche Syntax wie für generische Typparameter, wie in Listing 10-11 gezeigt. Wo wir die Lebenszeitparameter deklarieren und verwenden, hängt davon ab, ob sie mit den Struct-Feldern oder den Methodenparametern und Rückgabewerten zusammenhängen.

Lebenszeitsnamen für Struct-Felder müssen immer nach dem `impl`-Schlüsselwort deklariert und dann nach dem Struct-Namen verwendet werden, weil diese Lebenszeiten Teil des Struct-Typs sind.

In Methodensignaturen innerhalb des `impl`-Blocks können Referenzen entweder an die Lebenszeit von Referenzen in den Struct-Feldern gebunden sein oder unabhängig davon sein. Darüber hinaus machen die Lebenszeitelisionsregeln oftmals so, dass Lebenszeitannotationen in Methodensignaturen nicht erforderlich sind. Schauen wir uns einige Beispiele an, die den in Listing 10-24 definierten Struct namens `ImportantExcerpt` verwenden.

Zunächst verwenden wir eine Methode namens `level`, deren einziger Parameter eine Referenz auf `self` ist und deren Rückgabewert ein `i32` ist, was keine Referenz auf etwas ist:

```rust
impl<'a> ImportantExcerpt<'a> {
    fn level(&self) -> i32 {
        3
    }
}
```

Die Lebenszeitparameterdeklaration nach `impl` und ihre Verwendung nach dem Typnamen sind erforderlich, aber wir müssen die Lebenszeit der Referenz auf `self` nicht annotieren, weil die erste Elisionsregel gilt.

Hier ist ein Beispiel, in dem die dritte Lebenszeitelisionsregel zutrifft:

```rust
impl<'a> ImportantExcerpt<'a> {
    fn announce_and_return_part(&self, announcement: &str) -> &str {
        println!("Attention please: {announcement}");
        self.part
    }
}
```

Es gibt zwei Eingangslebenszeiten, daher wendet Rust die erste Lebenszeitelisionsregel an und gibt sowohl `&self` als auch `announcement` ihre eigenen Lebenszeiten. Dann, weil einer der Parameter `&self` ist, erhält der Rückgabetyp die Lebenszeit von `&self`, und alle Lebenszeiten sind berücksichtigt.

# Literale

Numerische Literale können durch Hinzufügen des Typs als Suffix typannotiert werden. Als Beispiel, um anzugeben, dass das Literal `42` den Typ `i32` haben soll, schreiben Sie `42i32`.

Der Typ von unsuffixed numerischen Literalen hängt davon ab, wie sie verwendet werden. Wenn keine Einschränkung besteht, verwendet der Compiler `i32` für Ganzzahlen und `f64` für Gleitkommazahlen.

```rust
fn main() {
    // Suffixed Literale, ihre Typen sind bei der Initialisierung bekannt
    let x = 1u8;
    let y = 2u32;
    let z = 3f32;

    // Unsuffixed Literale, ihre Typen hängen davon ab, wie sie verwendet werden
    let i = 1;
    let f = 1.0;

    // `size_of_val` gibt die Größe einer Variable in Bytes zurück
    println!("Größe von `x` in Bytes: {}", std::mem::size_of_val(&x));
    println!("Größe von `y` in Bytes: {}", std::mem::size_of_val(&y));
    println!("Größe von `z` in Bytes: {}", std::mem::size_of_val(&z));
    println!("Größe von `i` in Bytes: {}", std::mem::size_of_val(&i));
    println!("Größe von `f` in Bytes: {}", std::mem::size_of_val(&f));
}
```

Es gibt einige Konzepte im vorherigen Code, die noch nicht erklärt wurden. Hier ist eine kurze Erklärung für die ungeduldigen Leser:

- `std::mem::size_of_val` ist eine Funktion, aber mit ihrem _vollen Pfad_ aufgerufen. Code kann in logische Einheiten namens _Module_ aufgeteilt werden. In diesem Fall ist die `size_of_val`-Funktion im `mem`-Modul definiert, und das `mem`-Modul ist im `std`-_Kasten_ definiert. Weitere Details finden Sie unter Modulen und Kasten.

# Funktionen

Wenn man \[Elision\] ignoriert, haben Funktionssignaturen mit Lebensdauern einige Einschränkungen:

- Jede Referenz _muss_ eine annotierte Lebensdauer haben.
- Jede zurückgegebene Referenz _muss_ die gleiche Lebensdauer wie eine Eingabe haben oder `static` sein.

Zusätzlich ist zu beachten, dass das Zurückgeben von Referenzen ohne Eingabe verboten ist, wenn dies zu einem Zurückgeben von Referenzen auf ungültige Daten führen würde. Das folgende Beispiel zeigt einige gültige Formen von Funktionen mit Lebensdauern:

```rust
// Eine Eingabereferenz mit der Lebensdauer `'a`, die mindestens so lange
// existieren muss wie die Funktion.
fn print_one<'a>(x: &'a i32) {
    println!("`print_one`: x ist {}", x);
}

// Mutabele Referenzen sind auch mit Lebensdauern möglich.
fn add_one<'a>(x: &'a mut i32) {
    *x += 1;
}

// Mehrere Elemente mit unterschiedlicher Lebensdauer. Im diesem Fall
// wäre es auch in Ordnung, wenn beide die gleiche Lebensdauer `'a` hätten,
// aber in komplexeren Fällen können unterschiedliche Lebensdauern erforderlich sein.
fn print_multi<'a, 'b>(x: &'a i32, y: &'b i32) {
    println!("`print_multi`: x ist {}, y ist {}", x, y);
}

// Das Zurückgeben von Referenzen, die als Parameter übergeben wurden, ist akzeptabel.
// Allerdings muss die richtige Lebensdauer zurückgegeben werden.
fn pass_x<'a, 'b>(x: &'a i32, _: &'b i32) -> &'a i32 { x }

//fn invalid_output<'a>() -> &'a String { &String::from("foo") }
// Das obige ist ungültig: `'a` muss länger als die Funktion existieren.
// Hier würde `&String::from("foo")` ein `String` erstellen, gefolgt von einer
// Referenz. Dann wird das Datenobjekt beim Verlassen des Bereichs gelöscht,
// sodass eine Referenz auf ungültige Daten zurückgegeben wird.

fn main() {
    let x = 7;
    let y = 9;

    print_one(&x);
    print_multi(&x, &y);

    let z = pass_x(&x, &y);
    print_one(z);

    let mut t = 3;
    add_one(&mut t);
    print_one(&t);
}
```

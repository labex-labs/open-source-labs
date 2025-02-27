# Arrays und Slices

Ein Array ist eine Sammlung von Objekten vom gleichen Typ `T`, die in zusammenhängender Speicherstelle gespeichert sind. Arrays werden mit eckigen Klammern `[]` erstellt, und ihre Länge, die zur Compile-Zeit bekannt ist, ist Teil ihrer Typsignatur `[T; length]`.

Slices ähneln sich Arrays, aber ihre Länge ist zur Compile-Zeit nicht bekannt. Stattdessen ist ein Slice ein zweigeteiltes Objekt; das erste Wort ist ein Zeiger auf die Daten, das zweite Wort die Länge des Slices. Die Wortgröße ist die gleiche wie usize, bestimmt durch die Prozessorarchitektur, z.B. 64 Bit auf einem x86-64. Slices können verwendet werden, um einen Abschnitt eines Arrays zu entleihen und haben die Typsignatur `&[T]`.

```rust
use std::mem;

// Diese Funktion entleiht einen Slice.
fn analyze_slice(slice: &[i32]) {
    println!("Erstes Element des Slices: {}", slice[0]);
    println!("Der Slice hat {} Elemente", slice.len());
}

fn main() {
    // Fixgrößen-Array (Typsignatur überflüssig).
    let xs: [i32; 5] = [1, 2, 3, 4, 5];

    // Alle Elemente können auf den gleichen Wert initialisiert werden.
    let ys: [i32; 500] = [0; 500];

    // Der Index beginnt bei 0.
    println!("Erstes Element des Arrays: {}", xs[0]);
    println!("Zweites Element des Arrays: {}", xs[1]);

    // `len` gibt die Anzahl der Elemente im Array zurück.
    println!("Anzahl der Elemente im Array: {}", xs.len());

    // Arrays werden auf dem Stack zugewiesen.
    println!("Array nimmt {} Bytes ein", mem::size_of_val(&xs));

    // Arrays können automatisch als Slices entliehen werden.
    println!("Entleihe das gesamte Array als Slice.");
    analyze_slice(&xs);

    // Slices können auf einen Abschnitt eines Arrays zeigen.
    // Sie haben die Form [starting_index..ending_index].
    // `starting_index` ist die erste Position im Slice.
    // `ending_index` ist um eins größer als die letzte Position im Slice.
    println!("Entleihe einen Abschnitt des Arrays als Slice.");
    analyze_slice(&ys[1.. 4]);

    // Beispiel für einen leeren Slice `&[]`:
    let empty_array: [u32; 0] = [];
    assert_eq!(&empty_array, &[]);
    assert_eq!(&empty_array, &[][..]); // Identisch, aber ausführlicher

    // Arrays können sicher mit `.get` zugegriffen werden, was ein
    // `Option` zurückgibt. Dies kann wie unten gezeigt abgeglichen werden,
    // oder mit `.expect()` verwendet werden, wenn Sie möchten, dass das
    // Programm mit einer netten Nachricht beendet wird, anstatt glücklich
    // fortzufahren.
    for i in 0..xs.len() + 1 { // Ups, ein Element zu weit!
        match xs.get(i) {
            Some(xval) => println!("{}: {}", i, xval),
            None => println!("Langsam! {} ist zu weit!", i),
        }
    }

    // Ein Index außerhalb der Grenzen des Arrays verursacht einen
    // Compile-Zeitfehler.
    //println!("{}", xs[5]);
    // Ein Index außerhalb der Grenzen eines Slices verursacht einen
    // Laufzeitfehler.
    //println!("{}", xs[..][5]);
}
```

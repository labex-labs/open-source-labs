# Zeiger/Ref

Beim Umgang mit Zeigern muss zwischen Destrukturierung und Dereferenzierung unterschieden werden, da es sich um verschiedene Konzepte handelt, die anders verwendet werden als in Sprachen wie C/C++.

- Die Dereferenzierung verwendet `*`
- Die Destrukturierung verwendet `&`, `ref` und `ref mut`

```rust
fn main() {
    // Weisen Sie eine Referenz vom Typ `i32` zu. Das `&` signalisiert,
    // dass eine Referenz zugewiesen wird.
    let reference = &4;

    match reference {
        // Wenn `reference` mit `&val` muster-matched wird, ergibt das
        // einen Vergleich wie:
        // `&i32`
        // `&val`
        // ^ Wir sehen, dass wenn die entsprechenden `&` entfernt werden,
        // dann sollte der `i32` an `val` zugewiesen werden.
        &val => println!("Got a value via destructuring: {:?}", val),
    }

    // Um das `&` zu vermeiden, dereferenzieren Sie vor dem Matching.
    match *reference {
        val => println!("Got a value via dereferencing: {:?}", val),
    }

    // Was passiert, wenn Sie nicht mit einer Referenz beginnen? `reference`
    // war ein `&`, weil die rechte Seite bereits eine Referenz war. Dies
    // ist keine Referenz, weil die rechte Seite keine ist.
    let _not_a_reference = 3;

    // Rust stellt `ref` genau zu diesem Zweck zur Verfügung. Es modifiziert
    // die Zuweisung, sodass für das Element eine Referenz erstellt wird;
    // diese Referenz wird zugewiesen.
    let ref _is_a_reference = 3;

    // Entsprechend können Sie, indem Sie 2 Werte ohne Referenzen definieren,
    // Referenzen über `ref` und `ref mut` abrufen.
    let value = 5;
    let mut mut_value = 6;

    // Verwenden Sie das `ref`-Schlüsselwort, um eine Referenz zu erstellen.
    match value {
        ref r => println!("Got a reference to a value: {:?}", r),
    }

    // Verwenden Sie `ref mut` ähnlich.
    match mut_value {
        ref mut m => {
            // Es wurde eine Referenz erhalten. Wir müssen sie dereferenzieren,
            // bevor wir ihr etwas hinzufügen können.
            *m += 10;
            println!("We added 10. `mut_value`: {:?}", m);
        },
    }
}
```

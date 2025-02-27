# `Option`

Manchmal ist es wünschenswert, das Versagen bestimmter Teile eines Programms zu fangen, anstatt `panic!` aufzurufen; dies kann mit der `Option`-Enumeration erreicht werden.

Die `Option<T>`-Enumeration hat zwei Varianten:

- `None`, um das Versagen oder das Fehlen eines Werts anzuzeigen, und
- `Some(value)`, eine Tuple-Struktur, die einen `value` vom Typ `T` umschließt.

```rust
// Eine Ganzzahldivision, die nicht `panic!` aufruft
fn checked_division(dividend: i32, divisor: i32) -> Option<i32> {
    if divisor == 0 {
        // Das Versagen wird als die `None`-Variant dargestellt
        None
    } else {
        // Das Ergebnis wird in einer `Some`-Variant eingeschlossen
        Some(dividend / divisor)
    }
}

// Diese Funktion behandelt eine Division, die möglicherweise fehlschlägt
fn try_division(dividend: i32, divisor: i32) {
    // `Option`-Werte können wie andere Enumerationen mit Mustern abgeglichen werden
    match checked_division(dividend, divisor) {
        None => println!("{} / {} ist fehlgeschlagen!", dividend, divisor),
        Some(quotient) => {
            println!("{} / {} = {}", dividend, divisor, quotient)
        },
    }
}

fn main() {
    try_division(4, 2);
    try_division(1, 0);

    // Das Binden von `None` an eine Variable erfordert eine Typangabe
    let none: Option<i32> = None;
    let _equivalent_none = None::<i32>;

    let optional_float = Some(0f32);

    // Das Entpacken einer `Some`-Variant extrahiert den eingeschlossenen Wert.
    println!("{:?} entpackt zu {:?}", optional_float, optional_float.unwrap());

    // Das Entpacken einer `None`-Variant wird `panic!` auslösen
    println!("{:?} entpackt zu {:?}", none, none.unwrap());
}
```

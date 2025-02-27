# Zuerst deklarieren

Es ist möglich, Variable Bindungen zuerst zu deklarieren und sie später zu initialisieren. Diese Form wird jedoch selten verwendet, da es zu Verwendung von nicht initialisierten Variablen führen kann.

```rust
fn main() {
    // Deklariere eine Variable Bindung
    let a_binding;

    {
        let x = 2;

        // Initialisiere die Bindung
        a_binding = x * x;
    }

    println!("a binding: {}", a_binding);

    let another_binding;

    // Fehler! Verwendung von nicht initialisierter Bindung
    println!("another binding: {}", another_binding);
    // FIXME ^ Kommentiere diese Zeile aus

    another_binding = 1;

    println!("another binding: {}", another_binding);
}
```

Der Compiler verbietet die Verwendung von nicht initialisierten Variablen, da dies zu undefiniertem Verhalten führen würde.

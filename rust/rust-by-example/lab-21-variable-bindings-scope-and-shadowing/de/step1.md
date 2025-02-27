# Gültigkeitsbereich und Shadowing

Variable Bindungen haben einen Gültigkeitsbereich und sind darauf beschränkt, in einem _Block_ zu existieren. Ein Block ist eine Sammlung von Anweisungen, die in geschweiften Klammern `{}` eingeschlossen sind.

```rust
fn main() {
    // Diese Bindung existiert in der main-Funktion
    let long_lived_binding = 1;

    // Dies ist ein Block und hat einen kleineren Gültigkeitsbereich als die main-Funktion
    {
        // Diese Bindung existiert nur in diesem Block
        let short_lived_binding = 2;

        println!("inner short: {}", short_lived_binding);
    }
    // Ende des Blocks

    // Fehler! `short_lived_binding` existiert in diesem Gültigkeitsbereich nicht
    println!("outer short: {}", short_lived_binding);
    // FIXME ^ Kommentieren Sie diese Zeile aus

    println!("outer long: {}", long_lived_binding);
}
```

Außerdem ist das Variable Shadowing erlaubt.

```rust
fn main() {
    let shadowed_binding = 1;

    {
        println!("before being shadowed: {}", shadowed_binding);

        // Diese Bindung *überdeckt* die äußere
        let shadowed_binding = "abc";

        println!("shadowed in inner block: {}", shadowed_binding);
    }
    println!("outside inner block: {}", shadowed_binding);

    // Diese Bindung *überdeckt* die vorherige Bindung
    let shadowed_binding = 2;
    println!("shadowed in outer block: {}", shadowed_binding);
}
```

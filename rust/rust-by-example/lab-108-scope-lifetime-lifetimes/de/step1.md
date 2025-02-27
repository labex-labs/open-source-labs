# Lebenszeiten

Eine _Lebenszeit_ ist ein Konstrukt des Compilers (oder genauer gesagt, seiner _Entleihprüfung_) und wird verwendet, um sicherzustellen, dass alle Entleihungen gültig sind. Genauer gesagt beginnt die Lebenszeit einer Variable bei ihrer Erstellung und endet bei ihrer Zerstörung. Obwohl Lebenszeiten und Gültigkeitsbereiche oft zusammen erwähnt werden, sind sie nicht identisch.

Nehmen wir beispielsweise den Fall, in dem wir eine Variable via `&` entleihen. Die Entleihung hat eine Lebenszeit, die durch ihren Deklarationsort bestimmt wird. Folglich ist die Entleihung gültig, solange sie vor dem Zerstören des Verleiher endet. Der Gültigkeitsbereich der Entleihung wird jedoch durch den Ort bestimmt, an dem die Referenz verwendet wird.

Im folgenden Beispiel und im Rest dieses Abschnitts werden wir sehen, wie Lebenszeiten mit Gültigkeitsbereichen zusammenhängen und wie sich die beiden unterscheiden.

```rust
// Lebenszeiten werden unten mit Linien annotiert, die das Erstellen
// und Zerstören jeder Variable anzeigen.
// `i` hat die längste Lebenszeit, da ihr Gültigkeitsbereich vollständig
// beide `Entleihungen1` und `Entleihungen2` umschließt. Die Lebensdauer von
// `Entleihungen1` im Vergleich zu `Entleihungen2` ist unerheblich, da sie disjunkt sind.
fn main() {
    let i = 3; // Lebenszeit für `i` beginnt. ────────────────┐
    //                                                     │
    { //                                                   │
        let borrow1 = &i; // `Entleihungen1` Lebenszeit beginnt. ──┐│
        //                                                ││
        println!("Entleihungen1: {}", borrow1); //              ││
    } // `Entleihungen1` endet. ─────────────────────────────────┘│
    //                                                     │
    //                                                     │
    { //                                                   │
        let borrow2 = &i; // `Entleihungen2` Lebenszeit beginnt. ──┐│
        //                                                ││
        println!("Entleihungen2: {}", borrow2); //              ││
    } // `Entleihungen2` endet. ─────────────────────────────────┘│
    //                                                     │
}   // Lebenszeit endet. ─────────────────────────────────────┘
```

Beachten Sie, dass keine Namen oder Typen den Lebenszeiten zugewiesen werden. Dies begrenzt die Verwendung der Lebenszeiten, wie wir sehen werden.

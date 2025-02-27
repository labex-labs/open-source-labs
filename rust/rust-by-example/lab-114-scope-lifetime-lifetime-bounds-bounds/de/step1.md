# Begrenzungen

Genau wie generische Typen begrenzt werden können, verwenden auch Lebensdauern (selbst generisch) Begrenzungen. Das Zeichen `:` hat hier eine etwas andere Bedeutung, aber `+` ist das gleiche. Beachten Sie, wie die folgenden Lesarten lauten:

1.  `T: 'a`: _Alle_ Referenzen in `T` müssen die Lebensdauer `'a` überdauern.
2.  `T: Trait + 'a`: Der Typ `T` muss das Trait `Trait` implementieren und _alle_ Referenzen in `T` müssen `'a` überdauern.

Das folgende Beispiel zeigt die obige Syntax im Einsatz, die nach dem Schlüsselwort `where` verwendet wird:

```rust
use std::fmt::Debug; // Trait, mit dem begrenzend gearbeitet wird.

#[derive(Debug)]
struct Ref<'a, T: 'a>(&'a T);
// `Ref` enthält eine Referenz auf einen generischen Typ `T`, der
// eine unbekannte Lebensdauer `'a` hat. `T` ist so begrenzt, dass alle
// *Referenzen* in `T` die Lebensdauer `'a` überdauern müssen. Darüber hinaus
// darf die Lebensdauer von `Ref` nicht die Lebensdauer `'a` überschreiten.

// Eine generische Funktion, die mit dem `Debug`-Trait ausgibt.
fn print<T>(t: T) where
    T: Debug {
    println!("`print`: t ist {:?}", t);
}

// Hier wird eine Referenz auf `T` genommen, wobei `T`
// das `Debug`-Trait implementiert und alle *Referenzen* in `T`
// die Lebensdauer `'a` überdauern. Darüber hinaus muss
// die Lebensdauer `'a` die Lebensdauer der Funktion überdauern.
fn print_ref<'a, T>(t: &'a T) where
    T: Debug + 'a {
    println!("`print_ref`: t ist {:?}", t);
}

fn main() {
    let x = 7;
    let ref_x = Ref(&x);

    print_ref(&ref_x);
    print(ref_x);
}
```

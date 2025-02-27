# Testfall: Einheitsklärung

Ein nützliches Verfahren für die Einheitenumrechnung kann durch die Implementierung von `Add` mit einem Phantom-Typ-Parameter untersucht werden. Das `Add`-`Trait` wird unten untersucht:

```rust
// Diese Konstruktion würde verlangen: `Self + RHS = Output`
// wobei RHS standardmäßig auf Self gesetzt ist, wenn nicht in der Implementierung angegeben.
pub trait Add<RHS = Self> {
    type Output;

    fn add(self, rhs: RHS) -> Self::Output;
}

// `Output` muss `T<U>` sein, damit `T<U> + T<U> = T<U>`.
impl<U> Add for T<U> {
    type Output = T<U>;
  ...
}
```

Die gesamte Implementierung:

```rust
use std::ops::Add;
use std::marker::PhantomData;

/// Erstellen Sie leere Enumerationen, um Einheitstypen zu definieren.
#[derive(Debug, Clone, Copy)]
enum Inch {}
#[derive(Debug, Clone, Copy)]
enum Mm {}

/// `Length` ist ein Typ mit Phantom-Typ-Parameter `Unit`,
/// und ist nicht generisch über den Längen-Typ (das ist `f64`).
///
/// `f64` implementiert bereits die `Clone`- und `Copy`-Traits.
#[derive(Debug, Clone, Copy)]
struct Length<Unit>(f64, PhantomData<Unit>);

/// Das `Add`-Trait definiert das Verhalten des `+`-Operators.
impl<Unit> Add for Length<Unit> {
    type Output = Length<Unit>;

    // add() gibt eine neue `Length`-Struktur zurück, die die Summe enthält.
    fn add(self, rhs: Length<Unit>) -> Length<Unit> {
        // `+` ruft die `Add`-Implementierung für `f64` auf.
        Length(self.0 + rhs.0, PhantomData)
    }
}

fn main() {
    // Gibt an, dass `one_foot` den Phantom-Typ-Parameter `Inch` hat.
    let one_foot:  Length<Inch> = Length(12.0, PhantomData);
    // `one_meter` hat den Phantom-Typ-Parameter `Mm`.
    let one_meter: Length<Mm>   = Length(1000.0, PhantomData);

    // `+` ruft die `add()`-Methode auf, die wir für `Length<Unit>` implementiert haben.
    //
    // Da `Length` `Copy` implementiert, wird `add()` nicht `one_foot` und `one_meter`
    // konsumiert, sondern kopiert sie in `self` und `rhs`.
    let two_feet = one_foot + one_foot;
    let two_meters = one_meter + one_meter;

    // Die Addition funktioniert.
    println!("one foot + one_foot = {:?} in", two_feet.0);
    println!("one meter + one_meter = {:?} mm", two_meters.0);

    // Unsinnige Operationen scheitern wie erwartet:
    // Kompilierfehler: Typen stimmen nicht überein.
    //let one_feter = one_foot + one_meter;
}
```

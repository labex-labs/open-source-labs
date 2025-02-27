# structs

Ähnlich kann ein `struct` wie folgt zerlegt werden:

```rust
fn main() {
    struct Foo {
        x: (u32, u32),
        y: u32,
    }

    // Versuche, die Werte im Struct zu ändern, um zu sehen, was passiert
    let foo = Foo { x: (1, 2), y: 3 };

    match foo {
        Foo { x: (1, b), y } => println!("Das erste von x ist 1, b = {},  y = {} ", b, y),

        // Du kannst Structs zerlegen und die Variablen umbenennen,
        // Die Reihenfolge ist nicht wichtig
        Foo { y: 2, x: i } => println!("y ist 2, i = {:?}", i),

        // und du kannst auch einige Variablen ignorieren:
        Foo { y,.. } => println!("y = {}, wir interessieren uns nicht für x", y),
        // Dies wird einen Fehler geben: Muster erwähnt kein Feld `x`
        //Foo { y } => println!("y = {}", y),
    }

    let faa = Foo { x: (1, 2), y: 3 };

    // Du brauchst keinen match-Block, um Structs zu zerlegen:
    let Foo { x : x0, y: y0 } = faa;
    println!("Außerhalb: x0 = {x0:?}, y0 = {y0}");
}
```

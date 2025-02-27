# Iterator::any

`Iterator::any` ist eine Funktion, die wenn ihr eine Iterator übergeben wird, `true` zurückgibt, wenn irgendein Element das Prädikat erfüllt. Ansonsten `false`. Ihre Signatur:

```rust
pub trait Iterator {
    // Der Typ, über den iteriert wird.
    type Item;

    // `any` nimmt `&mut self` an, was bedeutet, dass der Aufrufer
    // entliehen und modifiziert werden kann, aber nicht konsumiert.
    fn any<F>(&mut self, f: F) -> bool where
        // `FnMut` bedeutet, dass jede erfasste Variable höchstens
        // modifiziert, nicht konsumiert werden darf. `Self::Item`
        // gibt an, dass sie die Argumente an die Closure per Wert
        // erhält.
        F: FnMut(Self::Item) -> bool;
}
```

```rust
fn main() {
    let vec1 = vec![1, 2, 3];
    let vec2 = vec![4, 5, 6];

    // `iter()` für Vecs liefert `&i32`. Entpacken zu `i32`.
    println!("2 in vec1: {}", vec1.iter()    .any(|&x| x == 2));
    // `into_iter()` für Vecs liefert `i32`. Keine Entpackung erforderlich.
    println!("2 in vec2: {}", vec2.into_iter().any(|x| x == 2));

    // `iter()` entleiht nur `vec1` und seine Elemente, sodass sie
    // nochmals verwendet werden können
    println!("vec1 len: {}", vec1.len());
    println!("First element of vec1 is: {}", vec1[0]);
    // `into_iter()` bewegt `vec2` und seine Elemente, sodass sie
    // nicht mehr verwendet werden können
    // println!("First element of vec2 is: {}", vec2[0]);
    // println!("vec2 len: {}", vec2.len());
    // TODO: Entkommentieren Sie die beiden Zeilen oben und sehen Sie sich die Compilerfehler an.

    let array1 = [1, 2, 3];
    let array2 = [4, 5, 6];

    // `iter()` für Arrays liefert `&i32`.
    println!("2 in array1: {}", array1.iter()    .any(|&x| x == 2));
    // `into_iter()` für Arrays liefert `i32`.
    println!("2 in array2: {}", array2.into_iter().any(|x| x == 2));
}
```

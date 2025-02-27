# Suchen durch Iteratoren

`Iterator::find` ist eine Funktion, die über einen Iterator iteriert und nach dem ersten Wert sucht, der eine bestimmte Bedingung erfüllt. Wenn keiner der Werte die Bedingung erfüllt, wird `None` zurückgegeben. Seine Signatur:

```rust
pub trait Iterator {
    // Der Typ, über den iteriert wird.
    type Item;

    // `find` nimmt `&mut self` an, was bedeutet, dass der Aufrufer
    // entliehen und modifiziert werden kann, aber nicht konsumiert.
    fn find<P>(&mut self, predicate: P) -> Option<Self::Item> where
        // `FnMut` bedeutet, dass jede eingefangene Variable höchstens
        // modifiziert, nicht konsumiert werden darf. `&Self::Item`
        // gibt an, dass es die Argumente für die Closure per Referenz
        // annimmt.
        P: FnMut(&Self::Item) -> bool;
}
```

```rust
fn main() {
    let vec1 = vec![1, 2, 3];
    let vec2 = vec![4, 5, 6];

    // `iter()` für Vecs liefert `&i32`.
    let mut iter = vec1.iter();
    // `into_iter()` für Vecs liefert `i32`.
    let mut into_iter = vec2.into_iter();

    // `iter()` für Vecs liefert `&i32`, und wir möchten auf eines seiner
    // Elemente verweisen, also müssen wir `&&i32` in `i32` zerlegen
    println!("Find 2 in vec1: {:?}", iter.find(|&&x| x == 2));
    // `into_iter()` für Vecs liefert `i32`, und wir möchten auf eines seiner
    // Elemente verweisen, also müssen wir `&i32` in `i32` zerlegen
    println!("Find 2 in vec2: {:?}", into_iter.find(| &x| x == 2));

    let array1 = [1, 2, 3];
    let array2 = [4, 5, 6];

    // `iter()` für Arrays liefert `&&i32`
    println!("Find 2 in array1: {:?}", array1.iter().find(|&&x| x == 2));
    // `into_iter()` für Arrays liefert `&i32`
    println!("Find 2 in array2: {:?}", array2.into_iter().find(|&x| x == 2));
}
```

`Iterator::find` gibt Ihnen eine Referenz auf das Element. Wenn Sie jedoch den _Index_ des Elements möchten, verwenden Sie `Iterator::position`.

```rust
fn main() {
    let vec = vec![1, 9, 3, 3, 13, 2];

    // `iter()` für Vecs liefert `&i32` und `position()` nimmt keine Referenz an, also
    // müssen wir `&i32` in `i32` zerlegen
    let index_of_first_even_number = vec.iter().position(|&x| x % 2 == 0);
    assert_eq!(index_of_first_even_number, Some(5));

    // `into_iter()` für Vecs liefert `i32` und `position()` nimmt keine Referenz an, also
    // müssen wir nicht zerlegen
    let index_of_first_negative_number = vec.into_iter().position(|x| x < 0);
    assert_eq!(index_of_first_negative_number, None);
}
```

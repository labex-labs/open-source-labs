# Búsqueda a través de iteradores

`Iterator::find` es una función que itera sobre un iterador y busca el primer valor que satisface una cierta condición. Si ninguno de los valores satisface la condición, devuelve `None`. Su firma:

```rust
pub trait Iterator {
    // El tipo que se está iterando.
    type Item;

    // `find` toma `&mut self`, lo que significa que el llamador puede ser prestado
    // y modificado, pero no consumido.
    fn find<P>(&mut self, predicate: P) -> Option<Self::Item> where
        // `FnMut` significa que cualquier variable capturada puede ser, como máximo,
        // modificada, no consumida. `&Self::Item` indica que toma
        // argumentos para la clausura por referencia.
        P: FnMut(&Self::Item) -> bool;
}
```

```rust
fn main() {
    let vec1 = vec![1, 2, 3];
    let vec2 = vec![4, 5, 6];

    // `iter()` para vectores produce `&i32`.
    let mut iter = vec1.iter();
    // `into_iter()` para vectores produce `i32`.
    let mut into_iter = vec2.into_iter();

    // `iter()` para vectores produce `&i32`, y queremos referirnos a uno de sus
    // elementos, por lo que tenemos que desestructurar `&&i32` a `i32`
    println!("Encontrar 2 en vec1: {:?}", iter    .find(|&&x| x == 2));
    // `into_iter()` para vectores produce `i32`, y queremos referirnos a uno de
    // sus elementos, por lo que tenemos que desestructurar `&i32` a `i32`
    println!("Encontrar 2 en vec2: {:?}", into_iter.find(| &x| x == 2));

    let array1 = [1, 2, 3];
    let array2 = [4, 5, 6];

    // `iter()` para arrays produce `&&i32`
    println!("Encontrar 2 en array1: {:?}", array1.iter()    .find(|&&x| x == 2));
    // `into_iter()` para arrays produce `&i32`
    println!("Encontrar 2 en array2: {:?}", array2.into_iter().find(|&x| x == 2));
}
```

`Iterator::find` te da una referencia al elemento. Pero si quieres el _índice_ del elemento, utiliza `Iterator::position`.

```rust
fn main() {
    let vec = vec![1, 9, 3, 3, 13, 2];

    // `iter()` para vectores produce `&i32` y `position()` no toma una referencia, por lo que
    // tenemos que desestructurar `&i32` a `i32`
    let index_of_first_even_number = vec.iter().position(|&x| x % 2 == 0);
    assert_eq!(index_of_first_even_number, Some(5));

    // `into_iter()` para vectores produce `i32` y `position()` no toma una referencia, por lo que
    // no tenemos que desestructurar
    let index_of_first_negative_number = vec.into_iter().position(|x| x < 0);
    assert_eq!(index_of_first_negative_number, None);
}
```

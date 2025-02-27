# Iterator::any

`Iterator::any` es una función que, cuando se le pasa un iterador, devolverá `true` si algún elemento satisface el predicado. En caso contrario, devolverá `false`. Su firma es la siguiente:

```rust
pub trait Iterator {
    // El tipo sobre el que se está iterando.
    type Item;

    // `any` toma `&mut self`, lo que significa que el llamador puede ser prestado
    // y modificado, pero no consumido.
    fn any<F>(&mut self, f: F) -> bool where
        // `FnMut` significa que cualquier variable capturada puede ser, como
        // máximo, modificada, no consumida. `Self::Item` indica que toma
        // argumentos para la clausura por valor.
        F: FnMut(Self::Item) -> bool;
}
```

```rust
fn main() {
    let vec1 = vec![1, 2, 3];
    let vec2 = vec![4, 5, 6];

    // `iter()` para vectores produce `&i32`. Desestructura a `i32`.
    println!("2 en vec1: {}", vec1.iter()    .any(|&x| x == 2));
    // `into_iter()` para vectores produce `i32`. No es necesario desestructurar.
    println!("2 en vec2: {}", vec2.into_iter().any(|x| x == 2));

    // `iter()` solo presta `vec1` y sus elementos, por lo que se pueden usar de nuevo
    println!("Longitud de vec1: {}", vec1.len());
    println!("El primer elemento de vec1 es: {}", vec1[0]);
    // `into_iter()` mueve `vec2` y sus elementos, por lo que ya no se pueden usar
    // println!("El primer elemento de vec2 es: {}", vec2[0]);
    // println!("Longitud de vec2: {}", vec2.len());
    // TODO: descomenta las dos líneas anteriores y observa los errores del compilador.

    let array1 = [1, 2, 3];
    let array2 = [4, 5, 6];

    // `iter()` para arrays produce `&i32`.
    println!("2 en array1: {}", array1.iter()    .any(|&x| x == 2));
    // `into_iter()` para arrays produce `i32`.
    println!("2 en array2: {}", array2.into_iter().any(|x| x == 2));
}
```

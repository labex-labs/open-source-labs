# Coerción

Una vida útil más larga puede ser forzada a convertirse en una más corta para que funcione dentro de un ámbito en el que normalmente no funcionaría. Esto se presenta en forma de coerción inferida por el compilador de Rust, y también en forma de declarar una diferencia de vida útil:

```rust
// Aquí, Rust infiere una vida útil lo más corta posible.
// Las dos referencias se ven luego forzadas a esa vida útil.
fn multiply<'a>(first: &'a i32, second: &'a i32) -> i32 {
    first * second
}

// `<'a: 'b, 'b>` se lee como la vida útil `'a` es al menos tan larga como `'b`.
// Aquí, tomamos un `&'a i32` y devolvemos un `&'b i32` como resultado de la coerción.
fn choose_first<'a: 'b, 'b>(first: &'a i32, _: &'b i32) -> &'b i32 {
    first
}

fn main() {
    let first = 2; // Vida útil más larga

    {
        let second = 3; // Vida útil más corta

        println!("El producto es {}", multiply(&first, &second));
        println!("{} es el primero", choose_first(&first, &second));
    };
}
```

# Literales

Los literales numéricos pueden ser anotados con su tipo agregando el tipo como sufijo. Por ejemplo, para especificar que el literal `42` debe tener el tipo `i32`, escriba `42i32`.

El tipo de los literales numéricos sin sufijo dependerá de cómo se usen. Si no existe ninguna restricción, el compilador usará `i32` para enteros y `f64` para números de punto flotante.

```rust
fn main() {
    // Literales con sufijo, sus tipos son conocidos en la inicialización
    let x = 1u8;
    let y = 2u32;
    let z = 3f32;

    // Literales sin sufijo, sus tipos dependen de cómo se usan
    let i = 1;
    let f = 1.0;

    // `size_of_val` devuelve el tamaño de una variable en bytes
    println!("tamaño de `x` en bytes: {}", std::mem::size_of_val(&x));
    println!("tamaño de `y` en bytes: {}", std::mem::size_of_val(&y));
    println!("tamaño de `z` en bytes: {}", std::mem::size_of_val(&z));
    println!("tamaño de `i` en bytes: {}", std::mem::size_of_val(&i));
    println!("tamaño de `f` en bytes: {}", std::mem::size_of_val(&f));
}
```

Hay algunos conceptos usados en el código anterior que no se han explicado todavía, aquí está una breve explicación para los lectores impacientes:

- `std::mem::size_of_val` es una función, pero se llama con su _ruta completa_. El código se puede dividir en unidades lógicas llamadas _módulos_. En este caso, la función `size_of_val` está definida en el módulo `mem`, y el módulo `mem` está definido en el _crate_ `std`. Para obtener más detalles, consulte módulos y crates.

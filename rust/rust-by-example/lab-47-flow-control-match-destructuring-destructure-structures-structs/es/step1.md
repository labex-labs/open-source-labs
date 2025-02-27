# structs

De manera similar, un `struct` se puede desestructurar como se muestra:

```rust
fn main() {
    struct Foo {
        x: (u32, u32),
        y: u32,
    }

    // Intente cambiar los valores en el struct para ver qué pasa
    let foo = Foo { x: (1, 2), y: 3 };

    match foo {
        Foo { x: (1, b), y } => println!("El primer valor de x es 1, b = {},  y = {} ", b, y),

        // se puede desestructurar structs y renombrar las variables,
        // el orden no es importante
        Foo { y: 2, x: i } => println!("y es 2, i = {:?}", i),

        // y también se puede ignorar algunas variables:
        Foo { y,.. } => println!("y = {}, no nos importa x", y),
        // esto generará un error: el patrón no menciona el campo `x`
        //Foo { y } => println!("y = {}", y),
    }

    let faa = Foo { x: (1, 2), y: 3 };

    // No es necesario un bloque match para desestructurar structs:
    let Foo { x : x0, y: y0 } = faa;
    println!("Fuera: x0 = {x0:?}, y0 = {y0}");
}
```

# `panic`

El mecanismo de manejo de errores más simple que veremos es `panic`. Imprime un mensaje de error, comienza a deshacer la pila y generalmente sale del programa. Aquí, llamamos explícitamente a `panic` en nuestra condición de error:

```rust
fn drink(beverage: &str) {
    // No deberías beber demasiadas bebidas azucaradas.
    if beverage == "lemonade" { panic!("AAAaaaaa!!!!"); }

    println!("Some refreshing {} is all I need.", beverage);
}

fn main() {
    drink("water");
    drink("lemonade");
}
```

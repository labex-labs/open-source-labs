# Declarar primero

Es posible declarar enlaces de variables primero y luego inicializarlos. Sin embargo, esta forma se usa raramente, ya que puede llevar a la utilización de variables no inicializadas.

```rust
fn main() {
    // Declarar un enlace de variable
    let a_binding;

    {
        let x = 2;

        // Inicializar el enlace
        a_binding = x * x;
    }

    println!("a binding: {}", a_binding);

    let another_binding;

    // Error: Uso de un enlace no inicializado
    println!("another binding: {}", another_binding);
    // FIXME ^ Comentar esta línea

    another_binding = 1;

    println!("another binding: {}", another_binding);
}
```

El compilador prohíbe el uso de variables no inicializadas, ya que esto llevaría a un comportamiento indefinido.

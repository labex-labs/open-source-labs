# Declarar primeiro

É possível declarar ligações de variáveis primeiro e inicializá-las posteriormente. No entanto, esta forma é raramente usada, pois pode levar ao uso de variáveis não inicializadas.

```rust
fn main() {
    // Declare uma ligação de variável
    let a_binding;

    {
        let x = 2;

        // Inicialize a ligação
        a_binding = x * x;
    }

    println!("a binding: {}", a_binding);

    let another_binding;

    // Erro! Uso de ligação não inicializada
    println!("another binding: {}", another_binding);
    // FIXME ^ Comente esta linha

    another_binding = 1;

    println!("another binding: {}", another_binding);
}
```

O compilador proíbe o uso de variáveis não inicializadas, pois isso levaria a um comportamento indefinido.

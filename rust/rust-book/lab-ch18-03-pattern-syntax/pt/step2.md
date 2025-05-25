# Correspondência de Literais (Matching Literals)

Como você viu no Capítulo 6, você pode corresponder padrões diretamente a literais. O código a seguir fornece alguns exemplos:

Nome do arquivo: `src/main.rs`

```rust
let x = 1;

match x {
    1 => println!("one"),
    2 => println!("two"),
    3 => println!("three"),
    _ => println!("anything"),
}
```

Este código imprime `one` porque o valor em `x` é `1`. Essa sintaxe é útil quando você deseja que seu código execute uma ação se receber um valor concreto específico.

# Sobrescrevendo um Valor

Se inserirmos uma chave e um valor em um hash map e, em seguida, inserirmos a mesma chave com um valor diferente, o valor associado a essa chave será substituído. Embora o código na Listagem 8-23 chame `insert` duas vezes, o hash map conterá apenas um par chave-valor porque estamos inserindo o valor para a chave da equipe Azul em ambas as vezes.

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Blue"), 25);

println!("{:?}", scores);
```

Listagem 8-23: Substituindo um valor armazenado com uma chave específica

Este código imprimirá `{"Blue": 25}`. O valor original de `10` foi sobrescrito.

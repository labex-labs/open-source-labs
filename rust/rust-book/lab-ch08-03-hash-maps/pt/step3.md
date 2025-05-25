# Acessando Valores em um Hash Map

Podemos obter um valor do hash map fornecendo sua chave ao método `get`, como mostrado na Listagem 8-21.

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

let team_name = String::from("Blue");
let score = scores.get(&team_name).copied().unwrap_or(0);
```

Listagem 8-21: Acessando a pontuação da equipe Azul armazenada no hash map

Aqui, `score` terá o valor que está associado à equipe Azul, e o resultado será `10`. O método `get` retorna um `Option<&V>`; se não houver valor para essa chave no hash map, `get` retornará `None`. Este programa lida com o `Option` chamando `copied` para obter um `Option<i32>` em vez de um `Option<&i32>`, e então `unwrap_or` para definir `score` como zero se `scores` não tiver uma entrada para a chave.

Podemos iterar sobre cada par chave-valor em um hash map de maneira semelhante à que fazemos com vetores, usando um loop `for`:

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

for (key, value) in &scores {
    println!("{key}: {value}");
}
```

Este código imprimirá cada par em uma ordem arbitrária:

```rust
Yellow: 50
Blue: 10
```

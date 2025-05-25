# Atualizando um Vetor

Para criar um vetor e, em seguida, adicionar elementos a ele, podemos usar o método `push`, como mostrado na Listagem 8-3.

```rust
let mut v = Vec::new();

v.push(5);
v.push(6);
v.push(7);
v.push(8);
```

Listagem 8-3: Usando o método `push` para adicionar valores a um vetor

Como com qualquer variável, se quisermos ser capazes de alterar seu valor, precisamos torná-la mutável usando a palavra-chave `mut`, como discutido no Capítulo 3. Os números que colocamos dentro são todos do tipo `i32`, e o Rust infere isso dos dados, então não precisamos da anotação `Vec<i32>`.

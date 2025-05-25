# Desestruturando Structs e Tuplas

Podemos misturar, combinar e aninhar padrões de desestruturação de maneiras ainda mais complexas. O exemplo a seguir mostra uma desestruturação complicada onde aninhamos structs e tuplas dentro de uma tupla e desestruturamos todos os valores primitivos:

```rust
let ((feet, inches), Point { x, y }) =
    ((3, 10), Point { x: 3, y: -10 });
```

Este código nos permite quebrar tipos complexos em suas partes componentes para que possamos usar os valores nos quais estamos interessados separadamente.

Desestruturar com padrões é uma maneira conveniente de usar partes de valores, como o valor de cada campo em uma struct, separadamente um do outro.

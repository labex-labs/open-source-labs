# Literales de Cadena como Rebanadas

Recuerda que hablamos de que los literales de cadena se almacenan dentro del binario. Ahora que sabemos sobre las rebanadas, podemos entender adecuadamente los literales de cadena:

```rust
let s = "Hello, world!";
```

El tipo de `s` aquí es `&str`: es una rebanada que apunta a ese punto específico del binario. Esto también es por lo que los literales de cadena son inmutables; `&str` es una referencia inmutable.

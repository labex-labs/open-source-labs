# Literais de String como _Slices_

Lembre-se de que falamos sobre literais de string sendo armazenados dentro do binário. Agora que sabemos sobre _slices_, podemos entender corretamente os literais de string:

```rust
let s = "Hello, world!";
```

O tipo de `s` aqui é `&str`: é um _slice_ apontando para aquele ponto específico do binário. É também por isso que os literais de string são imutáveis; `&str` é uma referência imutável.

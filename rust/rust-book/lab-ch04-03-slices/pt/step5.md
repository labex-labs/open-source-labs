# Outros _Slices_

_String slices_, como você pode imaginar, são específicos para strings. Mas também existe um tipo de _slice_ mais geral. Considere este _array_:

```rust
let a = [1, 2, 3, 4, 5];
```

Assim como podemos querer nos referir a parte de uma string, podemos querer nos referir a parte de um _array_. Faríamos isso assim:

```rust
let a = [1, 2, 3, 4, 5];

let slice = &a[1..3];

assert_eq!(slice, &[2, 3]);
```

Este _slice_ tem o tipo `&[i32]`. Ele funciona da mesma forma que os _string slices_, armazenando uma referência ao primeiro elemento e um comprimento. Você usará esse tipo de _slice_ para todos os tipos de outras coleções. Discutiremos essas coleções em detalhes quando falarmos sobre vetores no Capítulo 8.

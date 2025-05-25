# Descartando um Vetor Descarta Seus Elementos

Como qualquer outra `struct`, um vetor é liberado quando sai do escopo, conforme anotado na Listagem 8-10.

```rust
{
    let v = vec![1, 2, 3, 4];

    // do stuff with v
} // <- v goes out of scope and is freed here
```

Listagem 8-10: Mostrando onde o vetor e seus elementos são descartados

Quando o vetor é descartado, todo o seu conteúdo também é descartado, o que significa que os inteiros que ele contém serão limpos. O verificador de empréstimo (borrow checker) garante que quaisquer referências ao conteúdo de um vetor sejam usadas apenas enquanto o próprio vetor for válido.

Vamos passar para o próximo tipo de coleção: `String`!

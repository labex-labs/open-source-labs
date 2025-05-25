# Iterando pelas Linhas com o Método lines

Rust tem um método útil para lidar com a iteração linha por linha de strings, convenientemente chamado `lines`, que funciona como mostrado na Listagem 12-17. Observe que isso ainda não compilará.

Nome do arquivo: `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    for line in contents.lines() {
        // do something with line
    }
}
```

Listagem 12-17: Iterando por cada linha em `contents`

O método `lines` retorna um iterador. Falaremos sobre iteradores em profundidade no Capítulo 13, mas lembre-se de que você viu essa maneira de usar um iterador na Listagem 3-5, onde usamos um loop `for` com um iterador para executar algum código em cada item de uma coleção.

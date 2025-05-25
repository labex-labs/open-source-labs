# Adicionando um Teste a um Workspace

Para outra melhoria, vamos adicionar um teste da função `add_one::add_one` dentro do crate `add_one`:

Nome do arquivo: `add_one/src/lib.rs`

```rust
pub fn add_one(x: i32) -> i32 {
    x + 1
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        assert_eq!(3, add_one(2));
    }
}
```

Agora execute `cargo test` no diretório `add` de nível superior. Executar `cargo test` em um workspace estruturado como este executará os testes para todos os crates no workspace:

```bash
[object Object]
```

A primeira seção da saída mostra que o teste `it_works` no crate `add_one` passou. A próxima seção mostra que zero testes foram encontrados no crate `adder`, e então a última seção mostra que zero testes de documentação foram encontrados no crate `add_one`.

Também podemos executar testes para um crate específico em um workspace a partir do diretório de nível superior usando a flag `-p` e especificando o nome do crate que queremos testar:

```bash
[object Object]
```

Esta saída mostra que `cargo test` executou apenas os testes para o crate `add_one` e não executou os testes do crate `adder`.

Se você publicar os crates no workspace em *https://crates.io*, cada crate no workspace precisará ser publicado separadamente. Como `cargo test`, podemos publicar um crate específico em nosso workspace usando a flag `-p` e especificando o nome do crate que queremos publicar.

Para prática adicional, adicione um crate `add_two` a este workspace de maneira semelhante ao crate `add_one`!

À medida que seu projeto cresce, considere usar um workspace: ele fornece componentes individuais menores e mais fáceis de entender do que um grande bloco de código. Além disso, manter os crates em um workspace pode facilitar a coordenação entre os crates se eles forem frequentemente alterados ao mesmo tempo.

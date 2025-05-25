# Executando um Subconjunto de Testes por Nome

Às vezes, executar um conjunto completo de testes pode levar muito tempo. Se você estiver trabalhando em código em uma área específica, pode querer executar apenas os testes relacionados a esse código. Você pode escolher quais testes executar passando para `cargo test` o nome ou nomes do(s) teste(s) que deseja executar como um argumento.

Para demonstrar como executar um subconjunto de testes, primeiro criaremos três testes para nossa função `add_two`, conforme mostrado na Listagem 11-11, e escolheremos quais executar.

Nome do arquivo: `src/lib.rs`

```rust
pub fn add_two(a: i32) -> i32 {
    a + 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn add_two_and_two() {
        assert_eq!(4, add_two(2));
    }

    #[test]
    fn add_three_and_two() {
        assert_eq!(5, add_two(3));
    }

    #[test]
    fn one_hundred() {
        assert_eq!(102, add_two(100));
    }
}
```

Listagem 11-11: Três testes com três nomes diferentes

Se executarmos os testes sem passar nenhum argumento, como vimos anteriormente, todos os testes serão executados em paralelo:

    running 3 tests
    test tests::add_three_and_two ... ok
    test tests::add_two_and_two ... ok
    test tests::one_hundred ... ok

    test result: ok. 3 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

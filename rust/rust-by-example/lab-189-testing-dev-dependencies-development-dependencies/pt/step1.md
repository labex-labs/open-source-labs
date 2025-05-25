# Dependências de Desenvolvimento

Às vezes, é necessário ter dependências apenas para testes (ou exemplos, ou benchmarks). Essas dependências são adicionadas ao `Cargo.toml` na seção `[dev-dependencies]`. Essas dependências não são propagadas para outros pacotes que dependem deste pacote.

Um exemplo é a biblioteca [`pretty_assertions`](https://docs.rs/pretty_assertions/1.0.0/pretty_assertions/index.html), que estende as macros padrão `assert_eq!` e `assert_ne!` para fornecer um diff colorido.
Arquivo `Cargo.toml`:

```toml
# Os dados padrão do crate são omitidos
[dev-dependencies]
pretty_assertions = "1"
```

Arquivo `src/lib.rs`:

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;
    use pretty_assertions::assert_eq; // biblioteca para uso apenas em testes. Não pode ser usada em código que não seja de teste.

    #[test]
    fn test_add() {
        assert_eq!(add(2, 3), 5);
    }
}
```

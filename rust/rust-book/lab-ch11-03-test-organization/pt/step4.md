# Testando Funções Privadas

Há debate dentro da comunidade de testes sobre se as funções privadas devem ou não ser testadas diretamente, e outras linguagens tornam difícil ou impossível testar funções privadas. Independentemente da ideologia de teste que você segue, as regras de privacidade do Rust permitem que você teste funções privadas. Considere o código na Listagem 11-12 com a função privada `internal_adder`.

Nome do arquivo: `src/lib.rs`

```rust
pub fn add_two(a: i32) -> i32 {
    internal_adder(a, 2)
}

fn internal_adder(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn internal() {
        assert_eq!(4, internal_adder(2, 2));
    }
}
```

Listagem 11-12: Testando uma função privada

Observe que a função `internal_adder` não está marcada como `pub`. Os testes são apenas código Rust, e o módulo `tests` é apenas outro módulo. Como discutimos em "Caminhos para Referenciar um Item na Árvore de Módulos", itens em módulos filhos podem usar os itens em seus módulos ancestrais. Neste teste, trazemos todos os itens do pai do módulo `test` para o escopo com `use super::*`, e então o teste pode chamar `internal_adder`. Se você não acha que as funções privadas devem ser testadas, não há nada no Rust que o obrigue a fazê-lo.

# O Módulo de Testes e #\[cfg(test)\]

A anotação `#[cfg(test)]` no módulo `tests` diz ao Rust para compilar e executar o código de teste somente quando você executa `cargo test`, e não quando você executa `cargo build`. Isso economiza tempo de compilação quando você só quer construir a biblioteca e economiza espaço no artefato compilado resultante porque os testes não são incluídos. Você verá que, como os testes de integração vão em um diretório diferente, eles não precisam da anotação `#[cfg(test)]`. No entanto, como os testes unitários vão nos mesmos arquivos que o código, você usará `#[cfg(test)]` para especificar que eles não devem ser incluídos no resultado compilado.

Lembre-se que quando geramos o novo projeto `adder` na primeira seção deste capítulo, o Cargo gerou este código para nós:

Nome do arquivo: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
}
```

Este código é o módulo `tests` gerado automaticamente. O atributo `cfg` significa _configuração_ e diz ao Rust que o seguinte item deve ser incluído apenas dada uma determinada opção de configuração. Neste caso, a opção de configuração é `test`, que é fornecida pelo Rust para compilar e executar testes. Ao usar o atributo `cfg`, o Cargo compila nosso código de teste somente se executarmos ativamente os testes com `cargo test`. Isso inclui quaisquer funções auxiliares que possam estar dentro deste módulo, além das funções anotadas com `#[test]`.

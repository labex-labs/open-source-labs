# Usando Result\<T, E\> em Testes

Nossos testes até agora entram em pânico quando falham. Também podemos escrever testes que usam `Result<T, E>`! Aqui está o teste da Listagem 11-1, reescrito para usar `Result<T, E>` e retornar um `Err` em vez de entrar em pânico:

Nome do arquivo: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() -> Result<(), String> {
        if 2 + 2 == 4 {
            Ok(())
        } else {
            Err(String::from("dois mais dois não é igual a quatro"))
        }
    }
}
```

A função `it_works` agora tem o tipo de retorno `Result<(), String>`. No corpo da função, em vez de chamar a macro `assert_eq!`, retornamos `Ok(())` quando o teste passa e um `Err` com uma `String` dentro quando o teste falha.

Escrever testes para que eles retornem um `Result<T, E>` permite que você use o operador de ponto de interrogação no corpo dos testes, o que pode ser uma maneira conveniente de escrever testes que devem falhar se qualquer operação dentro deles retornar uma variante `Err`.

Você não pode usar a anotação `#[should_panic]` em testes que usam `Result<T, E>`. Para afirmar que uma operação retorna uma variante `Err`, _não_ use o operador de ponto de interrogação no valor `Result<T, E>`. Em vez disso, use `assert!(value.is_err())`.

Agora que você conhece várias maneiras de escrever testes, vamos ver o que está acontecendo quando executamos nossos testes e explorar as diferentes opções que podemos usar com `cargo test`.

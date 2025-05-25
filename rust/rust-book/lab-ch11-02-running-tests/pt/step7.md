# Ignorando Alguns Testes, a Menos que Especificamente Solicitado

Às vezes, alguns testes específicos podem ser muito demorados para executar, então você pode querer excluí-los durante a maioria das execuções de `cargo test`. Em vez de listar como argumentos todos os testes que você deseja executar, você pode, em vez disso, anotar os testes demorados usando o atributo `ignore` para excluí-los, conforme mostrado aqui:

Nome do arquivo: `src/lib.rs`

```rust
#[test]
fn it_works() {
    let result = 2 + 2;
    assert_eq!(result, 4);
}

#[test]
#[ignore]
fn expensive_test() {
    // código que leva uma hora para ser executado
}
```

Após `#[test]`, adicionamos a linha `#[ignore]` ao teste que queremos excluir. Agora, quando executamos nossos testes, `it_works` é executado, mas `expensive_test` não:

```bash
[object Object]
```

A função `expensive_test` é listada como `ignored` (ignorada). Se quisermos executar apenas os testes ignorados, podemos usar `cargo test -- --ignored`:

```bash
[object Object]
```

Ao controlar quais testes são executados, você pode garantir que seus resultados `cargo test` sejam retornados rapidamente. Quando você estiver em um ponto em que faz sentido verificar os resultados dos testes `ignored` e tiver tempo para esperar pelos resultados, você pode executar `cargo test -- --ignored` em vez disso. Se você quiser executar todos os testes, sejam eles ignorados ou não, você pode executar `cargo test -- --include-ignored`.

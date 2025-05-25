# Comentários de Documentação como Testes

Adicionar blocos de código de exemplo em seus comentários de documentação pode ajudar a demonstrar como usar sua biblioteca, e fazê-lo tem um bônus adicional: executar `cargo test` executará os exemplos de código em sua documentação como testes! Nada é melhor do que documentação com exemplos. Mas nada é pior do que exemplos que não funcionam porque o código foi alterado desde que a documentação foi escrita. Se executarmos `cargo test` com a documentação para a função `add_one` da Listagem 14-1, veremos uma seção nos resultados do teste que se parece com isto:

```rust
   Doc-tests my_crate

running 1 test
test src/lib.rs - add_one (line 5) ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
filtered out; finished in 0.27s
```

Agora, se alterarmos a função ou o exemplo para que o `assert_eq!` no exemplo entre em pânico e executarmos `cargo test` novamente, veremos que os testes de documentação detectam que o exemplo e o código estão fora de sincronia um com o outro!

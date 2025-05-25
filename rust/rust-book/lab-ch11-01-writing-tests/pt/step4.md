# Testando a Igualdade com as Macros `assert_eq!` e `assert_ne!`

Uma forma comum de verificar a funcionalidade é testar a igualdade entre o resultado do código sob teste e o valor que você espera que o código retorne. Você pode fazer isso usando a macro `assert!` e passando a ela uma expressão usando o operador `==`. No entanto, este é um teste tão comum que a biblioteca padrão fornece um par de macros --- `assert_eq!` e `assert_ne!` --- para realizar este teste de forma mais conveniente. Essas macros comparam dois argumentos quanto à igualdade ou desigualdade, respectivamente. Elas também imprimirão os dois valores se a asserção falhar, o que torna mais fácil ver _por que_ o teste falhou; por outro lado, a macro `assert!` apenas indica que obteve um valor `false` para a expressão `==`, sem imprimir os valores que levaram ao valor `false`.

Na Listagem 11-7, escrevemos uma função chamada `add_two` que adiciona `2` ao seu parâmetro e, em seguida, testamos essa função usando a macro `assert_eq!`.

Nome do arquivo: `src/lib.rs`

```rust
pub fn add_two(a: i32) -> i32 {
    a + 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_adds_two() {
        assert_eq!(4, add_two(2));
    }
}
```

Listagem 11-7: Testando a função `add_two` usando a macro `assert_eq!`

Vamos verificar se ela passa!

    running 1 test
    test tests::it_adds_two ... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Passamos `4` como argumento para `assert_eq!`, que é igual ao resultado da chamada `add_two(2)`. A linha para este teste é `test tests::it_adds_two ... ok`, e o texto `ok` indica que nosso teste passou!

Vamos introduzir um bug em nosso código para ver como `assert_eq!` se parece quando falha. Altere a implementação da função `add_two` para, em vez disso, adicionar `3`:

```rust
pub fn add_two(a: i32) -> i32 {
    a + 3
}
```

Execute os testes novamente:

    running 1 test
    test tests::it_adds_two ... FAILED

    failures:

    ---- tests::it_adds_two stdout ----
    1 thread 'main' panicked at 'assertion failed: `(left == right)`
    2   left: `4`,
    3  right: `5`', src/lib.rs:11:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

    failures:
        tests::it_adds_two

    test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Nosso teste detectou o bug! O teste `it_adds_two` falhou, e a mensagem nos diz que a asserção que falhou foi `assertion failed:`(left == right)\``[1] e quais são os valores`left`[2] e`right`[3]. Essa mensagem nos ajuda a começar a depurar: o argumento`left`era`4`, mas o argumento`right`, onde tínhamos`add_two(2)`, era`5\`. Você pode imaginar que isso seria especialmente útil quando temos muitos testes em andamento.

Observe que em algumas linguagens e frameworks de teste, os parâmetros para funções de asserção de igualdade são chamados de `expected` e `actual`, e a ordem em que especificamos os argumentos importa. No entanto, em Rust, eles são chamados de `left` e `right`, e a ordem em que especificamos o valor que esperamos e o valor que o código produz não importa. Poderíamos escrever a asserção neste teste como `assert_eq!(add_two(2), 4)`, o que resultaria na mesma mensagem de falha que exibe `assertion failed:`(left == right)\`\`.

A macro `assert_ne!` passará se os dois valores que lhe dermos não forem iguais e falhará se forem iguais. Essa macro é mais útil para casos em que não temos certeza de qual valor _será_, mas sabemos qual valor definitivamente _não deveria_ ser. Por exemplo, se estamos testando uma função que tem garantia de alterar sua entrada de alguma forma, mas a maneira como a entrada é alterada depende do dia da semana em que executamos nossos testes, a melhor coisa a afirmar pode ser que a saída da função não é igual à entrada.

Por baixo, as macros `assert_eq!` e `assert_ne!` usam os operadores `==` e `!=`, respectivamente. Quando as asserções falham, essas macros imprimem seus argumentos usando a formatação de depuração, o que significa que os valores que estão sendo comparados devem implementar os traits `PartialEq` e `Debug`. Todos os tipos primitivos e a maioria dos tipos da biblioteca padrão implementam esses traits. Para structs e enums que você define por conta própria, você precisará implementar `PartialEq` para afirmar a igualdade desses tipos. Você também precisará implementar `Debug` para imprimir os valores quando a asserção falhar. Como ambos os traits são traits deriváveis, conforme mencionado na Listagem 5-12, isso geralmente é tão simples quanto adicionar a anotação `#[derive(PartialEq, Debug)]` à sua definição de struct ou enum. Consulte o Apêndice C para obter mais detalhes sobre esses e outros traits deriváveis.

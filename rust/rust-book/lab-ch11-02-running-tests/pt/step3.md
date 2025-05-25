# Mostrando a Saída da Função

Por padrão, se um teste passa, a biblioteca de testes do Rust captura tudo o que é impresso na saída padrão. Por exemplo, se chamarmos `println!` em um teste e o teste passar, não veremos a saída de `println!` no terminal; veremos apenas a linha que indica que o teste passou. Se um teste falhar, veremos o que foi impresso na saída padrão com o restante da mensagem de falha.

Como exemplo, a Listagem 11-10 tem uma função boba que imprime o valor de seu parâmetro e retorna 10, bem como um teste que passa e um teste que falha.

Nome do arquivo: `src/lib.rs`

```rust
fn prints_and_returns_10(a: i32) -> i32 {
    println!("I got the value {a}");
    10
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn this_test_will_pass() {
        let value = prints_and_returns_10(4);
        assert_eq!(10, value);
    }

    #[test]
    fn this_test_will_fail() {
        let value = prints_and_returns_10(8);
        assert_eq!(5, value);
    }
}
```

Listagem 11-10: Testes para uma função que chama `println!`

Quando executamos esses testes com `cargo test`, veremos a seguinte saída:

    running 2 tests
    test tests::this_test_will_pass ... ok
    test tests::this_test_will_fail ... FAILED

    failures:

    ---- tests::this_test_will_fail stdout ----
    1 I got the value 8
    thread 'main' panicked at 'assertion failed: `(left == right)`
      left: `5`,
     right: `10`', src/lib.rs:19:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

    failures:
        tests::this_test_will_fail

    test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Observe que em nenhum lugar nesta saída vemos `I got the value 4`, que é impresso quando o teste que passa é executado. Essa saída foi capturada. A saída do teste que falhou, `I got the value 8` \[1\], aparece na seção da saída do resumo do teste, que também mostra a causa da falha do teste.

Se quisermos ver os valores impressos também para os testes que passam, podemos dizer ao Rust para também mostrar a saída dos testes bem-sucedidos com `--show-output`:

```bash
cargo test -- --show-output
```

Quando executamos os testes na Listagem 11-10 novamente com a flag `--show-output`, vemos a seguinte saída:

    running 2 tests
    test tests::this_test_will_pass ... ok
    test tests::this_test_will_fail ... FAILED

    successes:

    ---- tests::this_test_will_pass stdout ----
    I got the value 4


    successes:
        tests::this_test_will_pass

    failures:

    ---- tests::this_test_will_fail stdout ----
    I got the value 8
    thread 'main' panicked at 'assertion failed: `(left == right)`
      left: `5`,
     right: `10`', src/lib.rs:19:9
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

    failures:
        tests::this_test_will_fail

    test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

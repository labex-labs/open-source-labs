# Testes Unitários

Testes são funções Rust que verificam se o código não-teste está funcionando como esperado. Os corpos das funções de teste normalmente realizam alguma configuração, executam o código que queremos testar e, em seguida, afirmam se os resultados são os esperados.

A maioria dos testes unitários vai para um módulo `tests` com o atributo `#[cfg(test)]`. As funções de teste são marcadas com o atributo `#[test]`.

Os testes falham quando algo na função de teste gera uma falha (panic). Existem algumas macros auxiliares:

- `assert!(expressão)` - gera uma falha (panic) se a expressão avaliar para `false`.
- `assert_eq!(esquerda, direita)` e `assert_ne!(esquerda, direita)` - testam as expressões esquerda e direita em busca de igualdade e desigualdade, respectivamente.

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

// Esta é uma função de adição realmente ruim, seu propósito é falhar neste
// exemplo.
#[allow(dead_code)]
fn bad_add(a: i32, b: i32) -> i32 {
    a - b
}

#[cfg(test)]
mod tests {
    // Observe este idiom útil: importando nomes do escopo externo (para testes de mod).
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(1, 2), 3);
    }

    #[test]
    fn test_bad_add() {
        // Esta afirmação dispararia e o teste falharia.
        // Observe que funções privadas também podem ser testadas!
        assert_eq!(bad_add(1, 2), 3);
    }
}
```

Os testes podem ser executados com `cargo test`.

```shell
$ cargo test

executando 2 testes
test tests::test_bad_add ... FALHOU
test tests::test_add ... ok

falhas:

---- tests::test_bad_add saída ----
thread 'tests::test_bad_add' panicked at 'assertion failed: `(left == right)`
  left: `-1`,
 right: `3`', src/lib.rs:21:8
nota: Execute com $(RUST_BACKTRACE=1) para um backtrace.

falhas:
tests::test_bad_add

resultado do teste: FALHOU. 1 passou
1 falhou
0 ignorado
0 medido
0 filtrado
```

## Testes e `?`

Nenhum dos exemplos anteriores de testes unitários tinha um tipo de retorno. Mas em Rust 2018, seus testes unitários podem retornar `Result<()>`, o que permite usar `?` neles! Isso pode torná-los muito mais concisos.

```rust
fn sqrt(number: f64) -> Result<f64, String> {
    if number >= 0.0 {
        Ok(number.powf(0.5))
    } else {
        Err("floats negativos não têm raízes quadradas".to_owned())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sqrt() -> Result<(), String> {
        let x = 4.0;
        assert_eq!(sqrt(x)?.powf(2.0), x);
        Ok(())
    }
}
```

Consulte "The Edition Guide" para mais detalhes.

## Testando falhas (panics)

Para verificar funções que devem falhar (panic) em certas circunstâncias, use o atributo `#[should_panic]`. Este atributo aceita um parâmetro opcional `expected =` com o texto da mensagem de falha. Se sua função pode falhar (panic) de várias maneiras, isso ajuda a garantir que seu teste esteja testando a falha (panic) correta.

```rust
pub fn divide_non_zero_result(a: u32, b: u32) -> u32 {
    if b == 0 {
        panic!("Erro de divisão por zero");
    } else if a < b {
        panic!("O resultado da divisão é zero");
    }
    a / b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_divide() {
        assert_eq!(divide_non_zero_result(10, 2), 5);
    }

    #[test]
    #[should_panic]
    fn test_any_panic() {
        divide_non_zero_result(1, 0);
    }

    #[test]
    #[should_panic(expected = "O resultado da divisão é zero")]
    fn test_specific_panic() {
        divide_non_zero_result(1, 10);
    }
}
```

Executando esses testes, obtemos:

```shell
$ cargo test

executando 3 testes
test tests::test_any_panic ... ok
test tests::test_divide ... ok
test tests::test_specific_panic ... ok

resultado do teste: ok. 3 passaram
0 falharam
0 ignorados
0 medidos
0 filtrados
```

## Executando testes específicos

Para executar testes específicos, pode-se especificar o nome do teste no comando `cargo test`.

```shell
$ cargo test test_any_panic
executando 1 teste
test tests::test_any_panic ... ok

resultado do teste: ok. 1 passou
0 falharam
0 ignorados
0 medidos
2 filtrados
```

Para executar vários testes, pode-se especificar parte de um nome de teste que corresponda a todos os testes que devem ser executados.

```shell
$ cargo test panic
executando 2 testes
test tests::test_any_panic ... ok
test tests::test_specific_panic ... ok

resultado do teste: ok. 2 passaram
0 falharam
0 ignorados
0 medidos
1 filtrado
```

## Ignorando testes

Os testes podem ser marcados com o atributo `#[ignore]` para excluir alguns testes. Ou para executá-los com o comando `cargo test -- --ignored`

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(2, 2), 4);
    }

    #[test]
    fn test_add_hundred() {
        assert_eq!(add(100, 2), 102);
        assert_eq!(add(2, 100), 102);
    }

    #[test]
    #[ignore]
    fn ignored_test() {
        assert_eq!(add(0, 0), 0);
    }
}
```

```shell
$ cargo test
executando 3 testes
test tests::ignored_test ... ignorado
test tests::test_add ... ok
test tests::test_add_hundred ... ok

resultado do teste: ok. 2 passaram
0 falharam
1 ignorado
0 medidos
0 filtrados

$ cargo test -- --ignored
executando 1 teste
test tests::ignored_test ... ok

resultado do teste: ok. 1 passou
0 falharam
0 ignorados
0 medidos
0 filtrados
```

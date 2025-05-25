# Verificando Panics com `should_panic`

Além de verificar os valores de retorno, é importante verificar se nosso código lida com as condições de erro como esperamos. Por exemplo, considere o tipo `Guess` que criamos na Listagem 9-13. Outro código que usa `Guess` depende da garantia de que as instâncias de `Guess` conterão apenas valores entre 1 e 100. Podemos escrever um teste que garante que tentar criar uma instância de `Guess` com um valor fora dessa faixa cause um pânico.

Fazemos isso adicionando o atributo `should_panic` à nossa função de teste. O teste passa se o código dentro da função entrar em pânico; o teste falha se o código dentro da função não entrar em pânico.

A Listagem 11-8 mostra um teste que verifica se as condições de erro de `Guess::new` acontecem quando esperamos que aconteçam.

    // src/lib.rs
    pub struct Guess {
        value: i32,
    }

    impl Guess {
        pub fn new(value: i32) -> Guess {
            if value < 1 || value > 100 {
                panic!(
                    "O valor de Guess deve estar entre 1 e 100, obteve {}.",
                    value
                );
            }

            Guess { value }
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        #[should_panic]
        fn greater_than_100() {
            Guess::new(200);
        }
    }

Listagem 11-8: Testando se uma condição causará um pânico!

Colocamos o atributo `#[should_panic]` após o atributo `#[test]` e antes da função de teste a que ele se aplica. Vamos ver o resultado quando este teste passa:

    running 1 test
    test tests::greater_than_100 - should panic ... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Parece bom! Agora, vamos introduzir um bug em nosso código removendo a condição de que a função `new` entrará em pânico se o valor for maior que 100:

    // src/lib.rs
    --snip--

    impl Guess {
        pub fn new(value: i32) -> Guess {
            if value < 1 {
                panic!(
                    "O valor de Guess deve estar entre 1 e 100, obteve {}.",
                    value
                );
            }

            Guess { value }
        }
    }

Quando executamos o teste na Listagem 11-8, ele falhará:

    running 1 test
    test tests::greater_than_100 - should panic ... FAILED

    failures:

    ---- tests::greater_than_100 stdout ----
    note: test did not panic as expected

    failures:
        tests::greater_than_100

    test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Não recebemos uma mensagem muito útil neste caso, mas quando olhamos para a função de teste, vemos que ela está anotada com `#[should_panic]`. A falha que obtivemos significa que o código na função de teste não causou um pânico.

Testes que usam `should_panic` podem ser imprecisos. Um teste `should_panic` passaria mesmo que o teste entrasse em pânico por uma razão diferente da que esperávamos. Para tornar os testes `should_panic` mais precisos, podemos adicionar um parâmetro `expected` opcional ao atributo `should_panic`. O _test harness_ garantirá que a mensagem de falha contenha o texto fornecido. Por exemplo, considere o código modificado para `Guess` na Listagem 11-9, onde a função `new` entra em pânico com mensagens diferentes, dependendo se o valor é muito pequeno ou muito grande.

    // src/lib.rs
    --snip--

    impl Guess {
        pub fn new(value: i32) -> Guess {
            if value < 1 {
                panic!(
                    "O valor de Guess deve ser maior ou igual a 1, obteve {}.",
                    value
                );
            } else if value > 100 {
                panic!(
                    "O valor de Guess deve ser menor ou igual a 100, obteve {}.",
                    value
                );
            }

            Guess { value }
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        #[should_panic(expected = "menor ou igual a 100")]
        fn greater_than_100() {
            Guess::new(200);
        }
    }

Listagem 11-9: Testando um `panic!` com uma mensagem de pânico contendo uma substring especificada

Este teste passará porque o valor que colocamos no parâmetro `expected` do atributo `should_panic` é uma substring da mensagem com a qual a função `Guess::new` entra em pânico. Poderíamos ter especificado toda a mensagem de pânico que esperamos, que neste caso seria `O valor de Guess deve ser menor ou igual a 100, obteve 200`. O que você escolher especificar depende de quanto da mensagem de pânico é exclusivo ou dinâmico e quão preciso você deseja que seu teste seja. Neste caso, uma substring da mensagem de pânico é suficiente para garantir que o código na função de teste execute o caso `else if value > 100`.

Para ver o que acontece quando um teste `should_panic` com uma mensagem `expected` falha, vamos novamente introduzir um bug em nosso código trocando os corpos dos blocos `if value < 1` e `else if value > 100`:

    // src/lib.rs
    --snip--
    if value < 1 {
        panic!(
            "O valor de Guess deve ser menor ou igual a 100, obteve {}.",
            value
        );
    } else if value > 100 {
        panic!(
            "O valor de Guess deve ser maior ou igual a 1, obteve {}.",
            value
        );
    }
    --snip--

Desta vez, quando executarmos o teste `should_panic`, ele falhará:

    running 1 test
    test tests::greater_than_100 - should panic ... FAILED

    failures:

    ---- tests::greater_than_100 stdout ----
    thread 'main' panicked at 'O valor de Guess deve ser maior ou igual a 1, obteve
    200.', src/lib.rs:13:13
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
    note: panic did not contain expected string
          panic message: `"O valor de Guess deve ser maior ou igual a 1, obteve
    200."`,
     expected substring: `"menor ou igual a 100"`

    failures:
        tests::greater_than_100

    test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out;
    finished in 0.00s

A mensagem de falha indica que este teste realmente entrou em pânico como esperávamos, mas a mensagem de pânico não incluiu a string esperada `'O valor de Guess deve ser menor ou igual a 100'`. A mensagem de pânico que obtivemos neste caso foi `O valor de Guess deve ser maior ou igual a 1, obteve 200`. Agora podemos começar a descobrir onde está nosso bug!

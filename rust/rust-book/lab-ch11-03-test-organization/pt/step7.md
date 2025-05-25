# Submódulos em Testes de Integração

À medida que você adiciona mais testes de integração, pode querer criar mais arquivos no diretório `tests` para ajudar a organizá-los; por exemplo, você pode agrupar as funções de teste pela funcionalidade que estão testando. Como mencionado anteriormente, cada arquivo no diretório `tests` é compilado como seu próprio crate separado, o que é útil para criar escopos separados para imitar mais de perto a maneira como os usuários finais usarão seu crate. No entanto, isso significa que os arquivos no diretório `tests` não compartilham o mesmo comportamento que os arquivos em `src` compartilham, como você aprendeu no Capítulo 7 sobre como separar o código em módulos e arquivos.

O comportamento diferente dos arquivos do diretório `tests` é mais perceptível quando você tem um conjunto de funções auxiliares para usar em vários arquivos de teste de integração e tenta seguir as etapas em "Separando Módulos em Arquivos Diferentes" para extraí-los em um módulo comum. Por exemplo, se criarmos `tests/common.rs` e colocarmos uma função chamada `setup` nele, podemos adicionar algum código a `setup` que queremos chamar de várias funções de teste em vários arquivos de teste:

Nome do arquivo: `tests/common.rs`

```rust
pub fn setup() {
    // setup code specific to your library's tests would go here
}
```

Quando executarmos os testes novamente, veremos uma nova seção na saída do teste para o arquivo `common.rs`, embora este arquivo não contenha nenhuma função de teste nem tenhamos chamado a função `setup` de nenhum lugar:

    running 1 test
    test tests::internal ... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

         Running tests/common.rs (target/debug/deps/common-
    92948b65e88960b4)

    running 0 tests

    test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

         Running tests/integration_test.rs
    (target/debug/deps/integration_test-92948b65e88960b4)

    running 1 test
    test it_adds_two ... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

       Doc-tests adder

    running 0 tests

    test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0
    filtered out; finished in 0.00s

Ter `common` aparecendo nos resultados do teste com `running 0 tests` exibido para ele não é o que queríamos. Queríamos apenas compartilhar algum código com os outros arquivos de teste de integração. Para evitar que `common` apareça na saída do teste, em vez de criar `tests/common.rs`, criaremos `tests/common/mod.rs`. O diretório do projeto agora se parece com isto:

    ├── Cargo.lock
    ├── Cargo.toml
    ├── src
    │   └── lib.rs
    └── tests
        ├── common
        │   └── mod.rs
        └── integration_test.rs

Esta é a convenção de nomenclatura mais antiga que o Rust também entende, que mencionamos em "Caminhos de Arquivos Alternativos". Nomear o arquivo dessa forma diz ao Rust para não tratar o módulo `common` como um arquivo de teste de integração. Quando movemos o código da função `setup` para `tests/common/mod.rs` e excluímos o arquivo `tests/common.rs`, a seção na saída do teste não aparecerá mais. Arquivos em subdiretórios do diretório `tests` não são compilados como crates separados ou têm seções na saída do teste.

Depois de criarmos `tests/common/mod.rs`, podemos usá-lo de qualquer um dos arquivos de teste de integração como um módulo. Aqui está um exemplo de como chamar a função `setup` do teste `it_adds_two` em `tests/integration_test.rs`:

Nome do arquivo: `tests/integration_test.rs`

```rust
use adder;

mod common;

#[test]
fn it_adds_two() {
    common::setup();
    assert_eq!(4, adder::add_two(2));
}
```

Observe que a declaração `mod common;` é a mesma da declaração de módulo que demonstramos na Listagem 7-21. Então, na função de teste, podemos chamar a função `common::setup()`.

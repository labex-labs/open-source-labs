# O Diretório de Testes

Criamos um diretório `tests` no nível superior do diretório do nosso projeto, ao lado de `src`. O Cargo sabe procurar arquivos de teste de integração neste diretório. Podemos então criar quantos arquivos de teste quisermos, e o Cargo compilará cada um dos arquivos como um crate individual.

Vamos criar um teste de integração. Com o código na Listagem 11-12 ainda no arquivo `src/lib.rs`, crie um diretório `tests` e crie um novo arquivo chamado `tests/integration_test.rs`. Sua estrutura de diretórios deve ser assim:

    adder
    ├── Cargo.lock
    ├── Cargo.toml
    ├── src
    │   └── lib.rs
    └── tests
        └── integration_test.rs

Insira o código na Listagem 11-13 no arquivo `tests/integration_test.rs`.

Nome do arquivo: `tests/integration_test.rs`

```rust
use adder;

#[test]
fn it_adds_two() {
    assert_eq!(4, adder::add_two(2));
}
```

Listagem 11-13: Um teste de integração de uma função no crate `adder`

Cada arquivo no diretório `tests` é um crate separado, então precisamos trazer nossa biblioteca para o escopo de cada crate de teste. Por essa razão, adicionamos `use adder;` no topo do código, o que não precisávamos nos testes unitários.

Não precisamos anotar nenhum código em `tests/integration_test.rs` com `#[cfg(test)]`. O Cargo trata o diretório `tests` de forma especial e compila arquivos neste diretório somente quando executamos `cargo test`. Execute `cargo test` agora:

```bash
[object Object]
```

As três seções da saída incluem os testes unitários, o teste de integração e os testes de documentação. Observe que se algum teste em uma seção falhar, as seções seguintes não serão executadas. Por exemplo, se um teste unitário falhar, não haverá nenhuma saída para testes de integração e documentação, porque esses testes só serão executados se todos os testes unitários passarem.

A primeira seção para os testes unitários \[1] é a mesma que temos visto: uma linha para cada teste unitário (um chamado `internal` que adicionamos na Listagem 11-12) e, em seguida, uma linha de resumo para os testes unitários.

A seção de testes de integração começa com a linha `Running tests/integration_test.rs` \[2]. Em seguida, há uma linha para cada função de teste nesse teste de integração \[3] e uma linha de resumo para os resultados do teste de integração \[4] logo antes da seção `Doc-tests adder` começar.

Cada arquivo de teste de integração tem sua própria seção, então, se adicionarmos mais arquivos no diretório `tests`, haverá mais seções de teste de integração.

Ainda podemos executar uma função de teste de integração específica especificando o nome da função de teste como um argumento para `cargo test`. Para executar todos os testes em um arquivo de teste de integração específico, use o argumento `--test` do `cargo test` seguido pelo nome do arquivo:

```bash
[object Object]
```

Este comando executa apenas os testes no arquivo `tests/integration_test.rs`.

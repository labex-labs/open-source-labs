# Teste de Integração

Os testes unitários testam um módulo isoladamente de cada vez: são pequenos e podem testar código privado. Os testes de integração são externos ao seu projeto e usam apenas a interface pública da mesma forma que qualquer outro código. Seu propósito é testar se muitas partes da sua biblioteca funcionam corretamente juntas.

O Cargo procura testes de integração no diretório `tests` ao lado do `src`.

Arquivo `src/lib.rs`:

```rust
// Defina isso em um projeto chamado `adder`.
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

Arquivo com teste: `tests/integration_test.rs`:

```rust
#[test]
fn test_add() {
    assert_eq!(adder::add(3, 2), 5);
}
```

Executando testes com o comando `cargo test`:

```shell
$ cargo test
executando 0 testes

resultado do teste: ok. 0 aprovado
0 falhou
0 ignorado
0 medido
0 filtrados

Executando target/debug/deps/integration_test-bcd60824f5fbfe19

executando 1 teste
teste test_add ... ok

resultado do teste: ok. 1 aprovado
0 falhou
0 ignorado
0 medido
0 filtrados

Testes de documentação adder

executando 0 testes

resultado do teste: ok. 0 aprovado
0 falhou
0 ignorado
0 medido
0 filtrados
```

Cada arquivo de origem Rust no diretório `tests` é compilado como um projeto separado. Para compartilhar código entre testes de integração, podemos criar um módulo com funções públicas, importando e usando-o dentro dos testes.

Arquivo `tests/common/mod.rs`:

```rust
pub fn setup() {
    // algum código de configuração, como criar arquivos/diretórios necessários, iniciar
    // servidores, etc.
}
```

Arquivo com teste: `tests/integration_test.rs`

```rust
// Importando o módulo comum.
mod common;

#[test]
fn test_add() {
    // Usando código comum.
    common::setup();
    assert_eq!(adder::add(3, 2), 5);
}
```

Criar o módulo como `tests/common.rs` também funciona, mas não é recomendado porque o executor de testes tratará o arquivo como um projeto de teste e tentará executar testes dentro dele.

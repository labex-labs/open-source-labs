# Validando o Número de Threads em new

Não estamos fazendo nada com os parâmetros para `new` e `execute`. Vamos implementar os corpos dessas funções com o comportamento que queremos. Para começar, vamos pensar em `new`. Anteriormente, escolhemos um tipo sem sinal para o parâmetro `size` porque um pool com um número negativo de threads não faz sentido. No entanto, um pool com zero threads também não faz sentido, mas zero é um `usize` perfeitamente válido. Adicionaremos código para verificar se `size` é maior que zero antes de retornar uma instância `ThreadPool` e fazer com que o programa entre em pânico se receber zero, usando a macro `assert!`, conforme mostrado na Listagem 20-13.

Nome do arquivo: `src/lib.rs`

```rust
impl ThreadPool {
    /// Cria um novo ThreadPool.
    ///
    /// O tamanho é o número de threads no pool.
    ///
  1 /// # Panics
    ///
    /// A função `new` entrará em pânico se o tamanho for zero.
    pub fn new(size: usize) -> ThreadPool {
      2 assert!(size > 0);

        ThreadPool
    }

    --snip--
}
```

Listagem 20-13: Implementando `ThreadPool::new` para entrar em pânico se `size` for zero

Também adicionamos alguma documentação para nosso `ThreadPool` com comentários de documentação. Observe que seguimos as boas práticas de documentação adicionando uma seção que destaca as situações em que nossa função pode entrar em pânico \[1], conforme discutido no Capítulo 14. Tente executar `cargo doc --open` e clicar na struct `ThreadPool` para ver como a documentação gerada para `new` se parece!

Em vez de adicionar a macro `assert!` como fizemos aqui \[2], poderíamos mudar `new` para `build` e retornar um `Result` como fizemos com `Config::build` no projeto I/O na Listagem 12-9. Mas decidimos neste caso que tentar criar um pool de threads sem nenhuma thread deve ser um erro irrecuperável. Se você estiver se sentindo ambicioso, tente escrever uma função chamada `build` com a seguinte assinatura para comparar com a função `new`:

```rust
pub fn build(
    size: usize
) -> Result<ThreadPool, PoolCreationError> {
```

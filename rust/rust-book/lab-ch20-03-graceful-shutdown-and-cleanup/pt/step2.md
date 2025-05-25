# Implementando o Trait Drop em ThreadPool

Vamos começar implementando `Drop` em nosso pool de threads. Quando o pool é descartado, todas as nossas threads devem se juntar para garantir que terminem seu trabalho. A Listagem 20-22 mostra uma primeira tentativa de implementação de `Drop`; este código ainda não funcionará totalmente.

Nome do arquivo: `src/lib.rs`

```rust
impl Drop for ThreadPool {
    fn drop(&mut self) {
      1 for worker in &mut self.workers {
          2 println!("Shutting down worker {}", worker.id);

          3 worker.thread.join().unwrap();
        }
    }
}
```

Listagem 20-22: Juntando cada thread quando o pool de threads sai do escopo

Primeiro, iteramos por cada um dos `workers` do pool de threads \[1]. Usamos `&mut` para isso porque `self` é uma referência mutável, e também precisamos ser capazes de mutar `worker`. Para cada `worker`, imprimimos uma mensagem dizendo que esta instância `Worker` em particular está sendo encerrada \[2], e então chamamos `join` na thread dessa instância `Worker` \[3]. Se a chamada para `join` falhar, usamos `unwrap` para fazer o Rust entrar em pânico e entrar em um encerramento não grácil.

Aqui está o erro que obtemos quando compilamos este código:

```bash
error[E0507]: cannot move out of `worker.thread` which is behind a mutable
reference
    --> src/lib.rs:52:13
     |
52   |             worker.thread.join().unwrap();
     |             ^^^^^^^^^^^^^ ------ `worker.thread` moved due to this
method call
     |             |
     |             move occurs because `worker.thread` has type
`JoinHandle<()>`, which does not implement the `Copy` trait
     |
note: this function takes ownership of the receiver `self`, which moves
`worker.thread`
```

O erro nos diz que não podemos chamar `join` porque só temos um empréstimo mutável de cada `worker` e `join` assume a propriedade de seu argumento. Para resolver este problema, precisamos mover a thread para fora da instância `Worker` que possui `thread` para que `join` possa consumir a thread. Fizemos isso na Listagem 17-15: se `Worker` contiver um `Option<thread::JoinHandle<()>>` em vez disso, podemos chamar o método `take` no `Option` para mover o valor para fora da variante `Some` e deixar uma variante `None` em seu lugar. Em outras palavras, um `Worker` que está em execução terá uma variante `Some` em `thread`, e quando quisermos limpar um `Worker`, substituiremos `Some` por `None` para que o `Worker` não tenha uma thread para executar.

Então, sabemos que queremos atualizar a definição de `Worker` assim:

Nome do arquivo: `src/lib.rs`

```rust
struct Worker {
    id: usize,
    thread: Option<thread::JoinHandle<()>>,
}
```

Agora, vamos nos apoiar no compilador para encontrar os outros lugares que precisam ser alterados. Verificando este código, obtemos dois erros:

```bash
error[E0599]: no method named `join` found for enum `Option` in the current
scope
  --> src/lib.rs:52:27
   |
52 |             worker.thread.join().unwrap();
   |                           ^^^^ method not found in
`Option<JoinHandle<()>>`

error[E0308]: mismatched types
  --> src/lib.rs:72:22
   |
72 |         Worker { id, thread }
   |                      ^^^^^^ expected enum `Option`, found struct
`JoinHandle`
   |
   = note: expected enum `Option<JoinHandle<()>>`
            found struct `JoinHandle<_>`
help: try wrapping the expression in `Some`
   |
72 |         Worker { id, thread: Some(thread) }
   |                      +++++++++++++      +
```

Vamos abordar o segundo erro, que aponta para o código no final de `Worker::new`; precisamos envolver o valor `thread` em `Some` quando criamos um novo `Worker`. Faça as seguintes alterações para corrigir este erro:

Nome do arquivo: `src/lib.rs`

```rust
impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        --snip--

        Worker {
            id,
            thread: Some(thread),
        }
    }
}
```

O primeiro erro está em nossa implementação de `Drop`. Mencionamos anteriormente que pretendíamos chamar `take` no valor `Option` para mover `thread` para fora de `worker`. As seguintes alterações farão isso:

Nome do arquivo: `src/lib.rs`

```rust
impl Drop for ThreadPool {
    fn drop(&mut self) {
        for worker in &mut self.workers {
            println!("Shutting down worker {}", worker.id);

          1 if let Some(thread) = worker.thread.take() {
              2 thread.join().unwrap();
            }
        }
    }
}
```

Como discutido no Capítulo 17, o método `take` em `Option` retira a variante `Some` e deixa `None` em seu lugar. Estamos usando `if let` para desestruturar o `Some` e obter a thread \[1]; então chamamos `join` na thread \[2]. Se a thread de uma instância `Worker` já for `None`, sabemos que o `Worker` já teve sua thread limpa, então nada acontece nesse caso.

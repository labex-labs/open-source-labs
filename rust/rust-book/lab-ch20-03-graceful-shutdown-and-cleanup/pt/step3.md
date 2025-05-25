# Sinalizando às Threads para Parar de Ouvir por Jobs

Com todas as mudanças que fizemos, nosso código compila sem nenhum aviso. No entanto, a má notícia é que este código ainda não funciona da maneira que queremos. A chave é a lógica nas closures executadas pelas threads das instâncias `Worker`: no momento, chamamos `join`, mas isso não desligará as threads, porque elas fazem `loop` para sempre procurando por jobs. Se tentarmos descartar nosso `ThreadPool` com nossa implementação atual de `drop`, a thread principal bloqueará para sempre, esperando que a primeira thread termine.

Para corrigir este problema, precisaremos de uma mudança na implementação `drop` do `ThreadPool` e, em seguida, uma mudança no loop `Worker`.

Primeiro, mudaremos a implementação `drop` do `ThreadPool` para descartar explicitamente o `sender` antes de esperar que as threads terminem. A Listagem 20-23 mostra as alterações no `ThreadPool` para descartar explicitamente o `sender`. Usamos a mesma técnica `Option` e `take` que usamos com a thread para poder mover o `sender` para fora do `ThreadPool`.

Nome do arquivo: `src/lib.rs`

```rust
pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: Option<mpsc::Sender<Job>>,
}
--snip--
impl ThreadPool {
    pub fn new(size: usize) -> ThreadPool {
        --snip--

        ThreadPool {
            workers,
            sender: Some(sender),
        }
    }

    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() + Send + 'static,
    {
        let job = Box::new(f);

        self.sender
            .as_ref()
            .unwrap()
            .send(job)
            .unwrap();
    }
}

impl Drop for ThreadPool {
    fn drop(&mut self) {
      1 drop(self.sender.take());

        for worker in &mut self.workers {
            println!("Shutting down worker {}", worker.id);

            if let Some(thread) = worker.thread.take() {
                thread.join().unwrap();
            }
        }
    }
}
```

Listagem 20-23: Descartando explicitamente `sender` antes de juntar as threads `Worker`

Descartar `sender` \[1] fecha o canal, o que indica que nenhuma mensagem será enviada. Quando isso acontece, todas as chamadas para `recv` que as instâncias `Worker` fazem no loop infinito retornarão um erro. Na Listagem 20-24, mudamos o loop `Worker` para sair graciosamente do loop nesse caso, o que significa que as threads terminarão quando a implementação `drop` do `ThreadPool` chamar `join` nelas.

Nome do arquivo: `src/lib.rs`

```rust
impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        let thread = thread::spawn(move || loop {
            let message = receiver.lock().unwrap().recv();

            match message {
                Ok(job) => {
                    println!(
                        "Worker {id} got a job; executing."
                    );

                    job();
                }
                Err(_) => {
                    println!(
                        "Worker {id} shutting down."
                    );
                    break;
                }
            }
        });

        Worker {
            id,
            thread: Some(thread),
        }
    }
}
```

Listagem 20-24: Saindo explicitamente do loop quando `recv` retorna um erro

Para ver este código em ação, vamos modificar `main` para aceitar apenas duas requisições antes de desligar graciosamente o servidor, conforme mostrado na Listagem 20-25.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
    let pool = ThreadPool::new(4);

    for stream in listener.incoming().take(2) {
        let stream = stream.unwrap();

        pool.execute(|| {
            handle_connection(stream);
        });
    }

    println!("Shutting down.");
}
```

Listagem 20-25: Desligando o servidor após atender duas requisições saindo do loop

Você não gostaria que um servidor web do mundo real desligasse após atender apenas duas requisições. Este código apenas demonstra que o desligamento e a limpeza graciosos estão funcionando.

O método `take` é definido no trait `Iterator` e limita a iteração aos dois primeiros itens no máximo. O `ThreadPool` sairá do escopo no final de `main`, e a implementação `drop` será executada.

Inicie o servidor com `cargo run` e faça três requisições. A terceira requisição deve gerar um erro, e em seu terminal você deve ver uma saída semelhante a esta:

```bash
$ cargo run
   Compiling hello v0.1.0 (file:///projects/hello)
    Finished dev [unoptimized + debuginfo] target(s) in 1.0s
     Running `target/debug/hello`
Worker 0 got a job; executing.
Shutting down.
Shutting down worker 0
Worker 3 got a job; executing.
Worker 1 disconnected; shutting down.
Worker 2 disconnected; shutting down.
Worker 3 disconnected; shutting down.
Worker 0 disconnected; shutting down.
Shutting down worker 1
Shutting down worker 2
Shutting down worker 3
```

Você pode ver uma ordem diferente de IDs e mensagens `Worker` impressas. Podemos ver como este código funciona a partir das mensagens: as instâncias `Worker` 0 e 3 receberam as duas primeiras requisições. O servidor parou de aceitar conexões após a segunda conexão, e a implementação `Drop` em `ThreadPool` começa a ser executada antes mesmo do `Worker` 3 iniciar seu job. Descartar o `sender` desconecta todas as instâncias `Worker` e diz a elas para desligarem. As instâncias `Worker` imprimem uma mensagem quando se desconectam, e então o pool de threads chama `join` para esperar que cada thread `Worker` termine.

Observe um aspecto interessante desta execução em particular: o `ThreadPool` descartou o `sender`, e antes que qualquer `Worker` recebesse um erro, tentamos juntar o `Worker` 0. O `Worker` 0 ainda não havia recebido um erro de `recv`, então a thread principal bloqueou, esperando que o `Worker` 0 terminasse. Enquanto isso, o `Worker` 3 recebeu um job e então todas as threads receberam um erro. Quando o `Worker` 0 terminou, a thread principal esperou que o restante das instâncias `Worker` terminasse. Nesse ponto, todos eles haviam saído de seus loops e parado.

Parabéns! Agora concluímos nosso projeto; temos um servidor web básico que usa um pool de threads para responder de forma assíncrona. Somos capazes de realizar um desligamento grácil do servidor, que limpa todas as threads no pool. Consulte *https://www.nostarch.com/Rust2021* para baixar o código completo deste capítulo para referência.

Poderíamos fazer mais aqui! Se você quiser continuar a aprimorar este projeto, aqui estão algumas ideias:

- Adicione mais documentação ao `ThreadPool` e seus métodos públicos.
- Adicione testes da funcionalidade da biblioteca.
- Mude as chamadas para `unwrap` para um tratamento de erros mais robusto.
- Use `ThreadPool` para realizar alguma tarefa diferente de atender requisições web.
- Encontre um crate de pool de threads em *https://crates.io* e implemente um servidor web semelhante usando o crate em vez disso. Em seguida, compare sua API e robustez com o pool de threads que implementamos.

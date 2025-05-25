# Implementando o Método execute

Vamos finalmente implementar o método `execute` em `ThreadPool`. Também mudaremos `Job` de uma struct para um alias de tipo para um objeto trait que contém o tipo de closure que `execute` recebe. Como discutido em "Criando Sinônimos de Tipo com Aliases de Tipo", aliases de tipo nos permitem tornar tipos longos mais curtos para facilitar o uso. Veja a Listagem 20-19.

Nome do arquivo: `src/lib.rs`

```rust
--snip--

type Job = Box<dyn FnOnce() + Send + 'static>;

impl ThreadPool {
    --snip--

    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() + Send + 'static,
    {
      1 let job = Box::new(f);

      2 self.sender.send(job).unwrap();
    }
}

--snip--
```

Listagem 20-19: Criando um alias de tipo `Job` para um `Box` que contém cada closure e, em seguida, enviando a tarefa pelo canal

Depois de criar uma nova instância `Job` usando o closure que obtemos em `execute` \[1], enviamos essa tarefa pela extremidade de envio do canal \[2]. Estamos chamando `unwrap` em `send` para o caso de falha no envio. Isso pode acontecer se, por exemplo, pararmos todas as nossas threads de execução, o que significa que a extremidade receptora parou de receber novas mensagens. No momento, não podemos impedir que nossas threads sejam executadas: nossas threads continuam executando enquanto o pool existir. A razão pela qual usamos `unwrap` é que sabemos que o caso de falha não acontecerá, mas o compilador não sabe disso.

Mas ainda não terminamos! No `Worker`, nosso closure sendo passado para `thread::spawn` ainda apenas _referencia_ a extremidade receptora do canal. Em vez disso, precisamos que o closure faça um loop para sempre, pedindo à extremidade receptora do canal uma tarefa e executando a tarefa quando a recebe. Vamos fazer a alteração mostrada na Listagem 20-20 para `Worker::new`.

Nome do arquivo: `src/lib.rs`

```rust
--snip--

impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        let thread = thread::spawn(move || loop {
            let job = receiver
              1 .lock()
              2 .unwrap()
              3 .recv()
              4 .unwrap();

            println!("Worker {id} got a job; executing.");

            job();
        });

        Worker { id, thread }
    }
}
```

Listagem 20-20: Recebendo e executando as tarefas na thread da instância `Worker`

Aqui, primeiro chamamos `lock` no `receiver` para adquirir o mutex \[1], e então chamamos `unwrap` para entrar em pânico em quaisquer erros \[2]. Adquirir um bloqueio pode falhar se o mutex estiver em um estado _envenenado_, o que pode acontecer se alguma outra thread entrar em pânico enquanto mantém o bloqueio em vez de liberar o bloqueio. Nessa situação, chamar `unwrap` para fazer com que essa thread entre em pânico é a ação correta a ser tomada. Sinta-se à vontade para alterar este `unwrap` para um `expect` com uma mensagem de erro que seja significativa para você.

Se obtivermos o bloqueio no mutex, chamamos `recv` para receber um `Job` do canal \[3]. Um `unwrap` final também passa por quaisquer erros aqui \[4], o que pode ocorrer se a thread que mantém o remetente foi desligada, semelhante a como o método `send` retorna `Err` se o receptor for desligado.

A chamada para `recv` bloqueia, então, se ainda não houver uma tarefa, a thread atual esperará até que uma tarefa se torne disponível. O `Mutex<T>` garante que apenas uma thread `Worker` por vez esteja tentando solicitar uma tarefa.

Nosso pool de threads agora está em um estado de funcionamento! Dê um `cargo run` e faça algumas solicitações:

```bash
[object Object]
```

Sucesso! Agora temos um pool de threads que executa conexões de forma assíncrona. Nunca há mais de quatro threads criadas, então nosso sistema não ficará sobrecarregado se o servidor receber muitas solicitações. Se fizermos uma solicitação para _/sleep_, o servidor poderá atender outras solicitações fazendo com que outra thread as execute.

> Nota: Se você abrir _/sleep_ em várias janelas do navegador simultaneamente, elas poderão carregar uma de cada vez em intervalos de cinco segundos. Alguns navegadores da web executam várias instâncias da mesma solicitação sequencialmente por motivos de cache. Essa limitação não é causada pelo nosso servidor web.

Depois de aprender sobre o loop `while let` no Capítulo 18, você pode estar se perguntando por que não escrevemos o código da thread `Worker` conforme mostrado na Listagem 20-21.

Nome do arquivo: `src/lib.rs`

```rust
--snip--

impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        let thread = thread::spawn(move || {
            while let Ok(job) = receiver.lock().unwrap().recv() {
                println!("Worker {id} got a job; executing.");

                job();
            }
        });

        Worker { id, thread }
    }
}
```

Listagem 20-21: Uma implementação alternativa de `Worker::new` usando `while let`

Este código compila e executa, mas não resulta no comportamento de thread desejado: uma solicitação lenta ainda fará com que outras solicitações esperem para serem processadas. A razão é um tanto sutil: a struct `Mutex` não possui um método `unlock` público porque a propriedade do bloqueio é baseada no tempo de vida do `MutexGuard<T>` dentro do `LockResult<MutexGuard<T>>` que o método `lock` retorna. No tempo de compilação, o verificador de empréstimo pode então impor a regra de que um recurso protegido por um `Mutex` não pode ser acessado a menos que tenhamos o bloqueio. No entanto, essa implementação também pode resultar no bloqueio sendo mantido por mais tempo do que o pretendido se não estivermos atentos ao tempo de vida do `MutexGuard<T>`.

O código na Listagem 20-20 que usa `let job = receiver.lock().unwrap().recv().unwrap();` funciona porque com `let`, quaisquer valores temporários usados na expressão do lado direito do sinal de igual são descartados imediatamente quando a instrução `let` termina. No entanto, `while let` (e `if let` e `match`) não descarta valores temporários até o final do bloco associado. Na Listagem 20-21, o bloqueio permanece mantido durante a chamada para `job()`, o que significa que outras instâncias `Worker` não podem receber tarefas.

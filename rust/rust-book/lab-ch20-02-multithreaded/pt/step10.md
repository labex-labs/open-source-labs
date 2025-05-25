# Enviando Requisições para Threads via Canais

O próximo problema que abordaremos é que os closures fornecidos para `thread::spawn` não fazem absolutamente nada. Atualmente, obtemos o closure que queremos executar no método `execute`. Mas precisamos dar a `thread::spawn` um closure para executar quando criamos cada `Worker` durante a criação do `ThreadPool`.

Queremos que as structs `Worker` que acabamos de criar busquem o código a ser executado de uma fila mantida no `ThreadPool` e enviem esse código para sua thread para execução.

Os canais sobre os quais aprendemos no Capítulo 16 - uma maneira simples de se comunicar entre duas threads - seriam perfeitos para este caso de uso. Usaremos um canal para funcionar como a fila de tarefas, e `execute` enviará uma tarefa do `ThreadPool` para as instâncias `Worker`, que enviarão a tarefa para sua thread. Aqui está o plano:

1.  O `ThreadPool` criará um canal e manterá o remetente.
2.  Cada `Worker` manterá o receptor.
3.  Criaremos uma nova struct `Job` que conterá os closures que queremos enviar pelo canal.
4.  O método `execute` enviará a tarefa que deseja executar através do remetente.
5.  Em sua thread, o `Worker` fará um loop sobre seu receptor e executará os closures de quaisquer tarefas que receber.

Vamos começar criando um canal em `ThreadPool::new` e mantendo o remetente na instância `ThreadPool`, conforme mostrado na Listagem 20-16. A struct `Job` não contém nada por enquanto, mas será o tipo de item que estamos enviando pelo canal.

Nome do arquivo: `src/lib.rs`

```rust
use std::{sync::mpsc, thread};

pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: mpsc::Sender<Job>,
}

struct Job;

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

      1 let (sender, receiver) = mpsc::channel();

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(Worker::new(id));
        }

        ThreadPool { workers, 2 sender }
    }
    --snip--
}
```

Listagem 20-16: Modificando `ThreadPool` para armazenar o remetente de um canal que transmite instâncias `Job`

Em `ThreadPool::new`, criamos nosso novo canal \[1] e fazemos com que o pool mantenha o remetente \[2]. Isso compilará com sucesso.

Vamos tentar passar um receptor do canal para cada `Worker` enquanto o pool de threads cria o canal. Sabemos que queremos usar o receptor na thread que as instâncias `Worker` geram, então faremos referência ao parâmetro `receiver` no closure. O código na Listagem 20-17 ainda não compilará.

Nome do arquivo: `src/lib.rs`

```rust
impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
          1 workers.push(Worker::new(id, receiver));
        }

        ThreadPool { workers, sender }
    }
    --snip--
}

--snip--

impl Worker {
    fn new(id: usize, receiver: mpsc::Receiver<Job>) -> Worker {
        let thread = thread::spawn(|| {
          2 receiver;
        });

        Worker { id, thread }
    }
}
```

Listagem 20-17: Passando o receptor para cada `Worker`

Fizemos algumas pequenas e simples alterações: passamos o receptor para `Worker::new` \[1] e, em seguida, o usamos dentro do closure \[2].

Quando tentamos verificar este código, obtemos este erro:

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0382]: use of moved value: `receiver`
  --> src/lib.rs:26:42
   |
21 |         let (sender, receiver) = mpsc::channel();
   |                      -------- move occurs because `receiver` has type
`std::sync::mpsc::Receiver<Job>`, which does not implement the `Copy` trait
...
26 |             workers.push(Worker::new(id, receiver));
   |                                          ^^^^^^^^ value moved here, in
previous iteration of loop
```

O código está tentando passar `receiver` para várias instâncias `Worker`. Isso não funcionará, como você se lembrará do Capítulo 16: a implementação de canal que o Rust fornece é de múltiplos _produtores_, único _consumidor_. Isso significa que não podemos simplesmente clonar a extremidade consumidora do canal para corrigir este código. Também não queremos enviar uma mensagem várias vezes para vários consumidores; queremos uma lista de mensagens com várias instâncias `Worker` de modo que cada mensagem seja processada uma vez.

Além disso, tirar uma tarefa da fila do canal envolve a mutação do `receiver`, então as threads precisam de uma maneira segura de compartilhar e modificar o `receiver`; caso contrário, podemos obter condições de corrida (conforme abordado no Capítulo 16).

Lembre-se dos ponteiros inteligentes thread-safe discutidos no Capítulo 16: para compartilhar a propriedade em várias threads e permitir que as threads mutem o valor, precisamos usar `Arc<Mutex<T>>`. O tipo `Arc` permitirá que várias instâncias `Worker` possuam o receptor, e `Mutex` garantirá que apenas um `Worker` obtenha uma tarefa do receptor por vez. A Listagem 20-18 mostra as alterações que precisamos fazer.

Nome do arquivo: `src/lib.rs`

```rust
use std::{
    sync::{mpsc, Arc, Mutex},
    thread,
};
--snip--

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

      1 let receiver = Arc::new(Mutex::new(receiver));

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(
                Worker::new(id, Arc::clone(& 2 receiver))
            );
        }

        ThreadPool { workers, sender }
    }

    --snip--
}

--snip--

impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Job>>>,
    ) -> Worker {
        --snip--
    }
}
```

Listagem 20-18: Compartilhando o receptor entre as instâncias `Worker` usando `Arc` e `Mutex`

Em `ThreadPool::new`, colocamos o receptor em um `Arc` e um `Mutex` \[1]. Para cada novo `Worker`, clonamos o `Arc` para aumentar a contagem de referência para que as instâncias `Worker` possam compartilhar a propriedade do receptor \[2].

Com essas alterações, o código compila! Estamos chegando lá!

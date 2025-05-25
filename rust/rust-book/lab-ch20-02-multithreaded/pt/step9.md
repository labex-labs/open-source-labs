# Enviando Código do ThreadPool para uma Thread

Deixamos um comentário no loop `for` na Listagem 20-14 sobre a criação de threads. Aqui, veremos como realmente criamos threads. A biblioteca padrão fornece `thread::spawn` como uma maneira de criar threads, e `thread::spawn` espera receber algum código que a thread deve executar assim que a thread é criada. No entanto, em nosso caso, queremos criar as threads e fazê-las _esperar_ por código que enviaremos mais tarde. A implementação de threads da biblioteca padrão não inclui nenhuma maneira de fazer isso; temos que implementá-lo manualmente.

Implementaremos esse comportamento introduzindo uma nova estrutura de dados entre o `ThreadPool` e as threads que gerenciará esse novo comportamento. Chamaremos essa estrutura de dados de _Worker_ (Trabalhador), que é um termo comum em implementações de pooling. O `Worker` pega o código que precisa ser executado e executa o código em sua thread.

Pense nas pessoas trabalhando na cozinha de um restaurante: os trabalhadores esperam até que os pedidos cheguem dos clientes e, em seguida, são responsáveis por pegar esses pedidos e preenchê-los.

Em vez de armazenar um vetor de instâncias `JoinHandle<()>` no pool de threads, armazenaremos instâncias da struct `Worker`. Cada `Worker` armazenará uma única instância `JoinHandle<()>`. Em seguida, implementaremos um método em `Worker` que receberá um closure de código para executar e enviá-lo para a thread já em execução para execução. Também daremos a cada `Worker` um `id` para que possamos distinguir entre as diferentes instâncias de `Worker` no pool ao registrar ou depurar.

Aqui está o novo processo que acontecerá quando criarmos um `ThreadPool`. Implementaremos o código que envia o closure para a thread depois de configurarmos o `Worker` dessa maneira:

1.  Definir uma struct `Worker` que contém um `id` e um `JoinHandle<()>`.
2.  Mudar `ThreadPool` para conter um vetor de instâncias `Worker`.
3.  Definir uma função `Worker::new` que recebe um número `id` e retorna uma instância `Worker` que contém o `id` e uma thread gerada com um closure vazio.
4.  Em `ThreadPool::new`, use o contador do loop `for` para gerar um `id`, criar um novo `Worker` com esse `id` e armazenar o `Worker` no vetor.

Se você está pronto para um desafio, tente implementar essas alterações por conta própria antes de olhar o código na Listagem 20-15.

Pronto? Aqui está a Listagem 20-15 com uma maneira de fazer as modificações anteriores.

Nome do arquivo: `src/lib.rs`

```rust
use std::thread;

pub struct ThreadPool {
  1 workers: Vec<Worker>,
}

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let mut workers = Vec::with_capacity(size);

      2 for id in 0..size {
          3 workers.push(Worker::new(id));
        }

        ThreadPool { workers }
    }
    --snip--
}

4 struct Worker {
    id: usize,
    thread: thread::JoinHandle<()>,
}

impl Worker {
  5 fn new(id: usize) -> Worker {
      6 let thread = thread::spawn(|| {});

        Worker { 7 id, 8 thread }
    }
}
```

Listagem 20-15: Modificando `ThreadPool` para conter instâncias `Worker` em vez de conter threads diretamente

Mudamos o nome do campo em `ThreadPool` de `threads` para `workers` porque agora ele contém instâncias `Worker` em vez de instâncias `JoinHandle<()>` \[1]. Usamos o contador no loop `for` \[2] como um argumento para `Worker::new` e armazenamos cada novo `Worker` no vetor chamado `workers` \[3].

O código externo (como nosso servidor em `src/main.rs`) não precisa saber os detalhes da implementação sobre o uso de uma struct `Worker` dentro de `ThreadPool`, então tornamos a struct `Worker` \[4] e sua função `new` \[5] privadas. A função `Worker::new` usa o `id` que damos a ela \[7] e armazena uma instância `JoinHandle<()>` \[8] que é criada gerando uma nova thread usando um closure vazio \[6].

> Nota: Se o sistema operacional não puder criar uma thread porque não há recursos de sistema suficientes, `thread::spawn` entrará em pânico. Isso fará com que todo o nosso servidor entre em pânico, mesmo que a criação de algumas threads possa ser bem-sucedida. Para simplificar, esse comportamento é aceitável, mas em uma implementação de pool de threads de produção, você provavelmente gostaria de usar `std::thread::Builder` e seu método `spawn` que retorna `Result` em vez disso.

Este código compilará e armazenará o número de instâncias `Worker` que especificamos como um argumento para `ThreadPool::new`. Mas _ainda_ não estamos processando o closure que recebemos em `execute`. Vamos ver como fazer isso a seguir.

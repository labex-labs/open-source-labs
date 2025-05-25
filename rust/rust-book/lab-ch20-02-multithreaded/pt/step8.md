# Criando Espaço para Armazenar as Threads

Agora que temos uma maneira de saber que temos um número válido de threads para armazenar no pool, podemos criar essas threads e armazená-las na struct `ThreadPool` antes de retornar a struct. Mas como "armazenamos" uma thread? Vamos dar outra olhada na assinatura de `thread::spawn`:

```rust
pub fn spawn<F, T>(f: F) -> JoinHandle<T>
    where
        F: FnOnce() -> T,
        F: Send + 'static,
        T: Send + 'static,
```

A função `spawn` retorna um `JoinHandle<T>`, onde `T` é o tipo que o closure retorna. Vamos tentar usar `JoinHandle` também e ver o que acontece. Em nosso caso, os closures que estamos passando para o pool de threads lidarão com a conexão e não retornarão nada, então `T` será o tipo unitário `()`.

O código na Listagem 20-14 compilará, mas ainda não cria nenhuma thread. Mudamos a definição de `ThreadPool` para conter um vetor de instâncias `thread::JoinHandle<()>`, inicializamos o vetor com uma capacidade de `size`, configuramos um loop `for` que executará algum código para criar as threads e retornamos uma instância `ThreadPool` contendo-as.

Nome do arquivo: `src/lib.rs`

```rust
1 use std::thread;

pub struct ThreadPool {
  2 threads: Vec<thread::JoinHandle<()>>,
}

impl ThreadPool {
    --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

      3 let mut threads = Vec::with_capacity(size);

        for _ in 0..size {
            // create some threads and store them in the vector
        }

        ThreadPool { threads }
    }
    --snip--
}
```

Listagem 20-14: Criando um vetor para `ThreadPool` conter as threads

Trouxemos `std::thread` para o escopo no crate da biblioteca \[1] porque estamos usando `thread::JoinHandle` como o tipo dos itens no vetor em `ThreadPool` \[2].

Depois que um tamanho válido é recebido, nosso `ThreadPool` cria um novo vetor que pode conter `size` itens \[3]. A função `with_capacity` executa a mesma tarefa que `Vec::new`, mas com uma diferença importante: ela pré-aloca espaço no vetor. Como sabemos que precisamos armazenar `size` elementos no vetor, fazer essa alocação antecipadamente é um pouco mais eficiente do que usar `Vec::new`, que redimensiona a si mesmo à medida que os elementos são inseridos.

Quando você executar `cargo check` novamente, ele deverá ser bem-sucedido.

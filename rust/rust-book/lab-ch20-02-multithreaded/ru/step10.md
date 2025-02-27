# Отправка запросов в потоки через каналы

Следующая проблема, с которой мы столкнемся, заключается в том, что замыкания, передаваемые в `thread::spawn`, ничего не делают. В настоящее время мы получаем замыкание, которое хотим выполнить, в методе `execute`. Но нам нужно передать `thread::spawn` замыкание для выполнения при создании каждого `Worker` во время создания `ThreadPool`.

Мы хотим, чтобы структуры `Worker`, которые мы только создали, получали код для выполнения из очереди, хранящейся в `ThreadPool`, и отправляли этот код в свой поток для выполнения.

Каналы, о которых мы узнали в главе 16 - простой способ общения между двумя потоками - идеально подходят для этого случая использования. Мы будем использовать канал в качестве очереди задач, и `execute` будет отправлять задачу из `ThreadPool` в экземпляры `Worker`, которые отправят задачу в свой поток. Вот план:

1. `ThreadPool` создаст канал и сохранит отправителя.
2. Каждый `Worker` будет хранить получателя.
3. Мы создадим новую структуру `Job`, которая будет хранить замыкания, которые мы хотим отправить по каналу.
4. Метод `execute` отправит задачу, которую он хочет выполнить, через отправителя.
5. В своем потоке `Worker` будет перебирать свой получатель и выполнять замыкания любых задач, которые он получает.

Давайте начнем с создания канала в `ThreadPool::new` и сохранения отправителя в экземпляре `ThreadPool`, как показано в Listing 20-16. Структура `Job` для now не хранит ничего, но будет типом элемента, который мы отправляем по каналу.

Filename: `src/lib.rs`

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

Listing 20-16: Изменение `ThreadPool` для хранения отправителя канала, передающего экземпляры `Job`

В `ThreadPool::new` мы создаем наш новый канал \[1\] и заставляем пул хранить отправителя \[2\]. Это успешно скомпилируется.

Попробуем передать получателя канала в каждый `Worker` при создании канала в потоке. Мы знаем, что хотим использовать получателя в потоке, который создают экземпляры `Worker`, поэтому мы будем ссылаться на параметр `receiver` в замыкании. Код в Listing 20-17 еще не будет компилироваться.

Filename: `src/lib.rs`

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

Listing 20-17: Передача получателя каждому `Worker`

Мы внесли несколько небольших и простых изменений: мы передаем получателя в `Worker::new` \[1\], а затем используем его внутри замыкания \[2\].

Когда мы пытаемся проверить этот код, мы получаем эту ошибку:

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

Код пытается передать `receiver` в несколько экземпляров `Worker`. Это не сработает, как вы помните из главы 16: реализация канала, предоставляемая Rust, представляет собой несколько _производителей_, один _потребитель_. Это означает, что мы не можем просто скопировать потребительскую концовку канала, чтобы исправить этот код. Мы также не хотим отправлять сообщение несколько раз для нескольких потребителей; мы хотим одну список сообщений с несколькими экземплярами `Worker`, чтобы каждое сообщение обрабатывалось один раз.

此外, получение задачи из очереди канала предполагает изменение `receiver`, поэтому потоки нуждаются в безопасном способе разделения и изменения `receiver`; в противном случае мы можем получить условия гонки (как описано в главе 16).

Вспомните о потоко-безопасных умных указателях, discutанных в главе 16: чтобы разделить владение между несколькими потоками и позволить потокам изменять значение, нам нужно использовать `Arc<Mutex<T>>`. Тип `Arc` позволит нескольким экземплярам `Worker` владеть получателем, а `Mutex` обеспечит то, что только один `Worker` получит задачу из получателя за один раз. Listing 20-18 показывает изменения, которые нам нужно внести.

Filename: `src/lib.rs`

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

Listing 20-18: Общий получатель между экземплярами `Worker` с использованием `Arc` и `Mutex`

В `ThreadPool::new` мы помещаем получателя в `Arc` и `Mutex` \[1\]. Для каждого нового `Worker` мы копируем `Arc`, чтобы увеличить счетчик ссылок, так чтобы экземпляры `Worker` могли разделить владение получателем \[2\].

С этими изменениями код компилируется! Мы почти добрались!

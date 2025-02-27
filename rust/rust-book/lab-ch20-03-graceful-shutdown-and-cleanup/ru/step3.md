# Сигнализация потокам для прекращения прослушивания заданий

После всех внесенных изменений наш код компилируется без каких-либо предупреждений. Однако, плохая новость заключается в том, что этот код не работает так, как мы хотим. Ключом является логика в замыканиях, выполняемых потоками экземпляров `Worker`: в настоящее время мы вызываем `join`, но это не остановит потоки, потому что они `loop` бесконечно, ожидая заданий. Если мы попытаемся удалить наш `ThreadPool` с нашей текущей реализацией `drop`, главный поток будет заблокирован навсегда, ожидая завершения первого потока.

Чтобы исправить эту проблему, нам нужно внести изменения в реализацию `drop` для `ThreadPool`, а затем внести изменения в цикл `Worker`.

Сначала мы изменим реализацию `drop` для `ThreadPool`, чтобы явно удалить `sender` перед ожиданием завершения потоков. Листинг 20-23 показывает изменения в `ThreadPool`, чтобы явно удалить `sender`. Мы используем ту же технику с `Option` и `take`, что и с потоком, чтобы быть able переместить `sender` из `ThreadPool`.

Имя файла: `src/lib.rs`

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

Листинг 20-23: Явное удаление `sender` перед присоединением потоков `Worker`

Удаление `sender` \[1\] закрывает канал, что означает, что больше не будут отправляться сообщения. Когда это происходит, все вызовы `recv`, которые `Worker` экземпляры делают в бесконечном цикле, вернут ошибку. В Листинге 20-24 мы изменяем цикл `Worker`, чтобы gracefully выйти из цикла в этом случае, что означает, что потоки завершатся, когда реализация `drop` для `ThreadPool` вызовет `join` для них.

Имя файла: `src/lib.rs`

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

Листинг 20-24: Явное выход из цикла, когда `recv` возвращает ошибку

Чтобы увидеть этот код в действии, давайте изменим `main`, чтобы он принимал только два запроса, прежде чем gracefully выключить сервер, как показано в Листинге 20-25.

Имя файла: `src/main.rs`

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

Листинг 20-25: Выключение сервера после обработки двух запросов путем выхода из цикла

В реальном веб-сервере вы, вероятно, не захотите выключать его после обработки только двух запросов. Этот код просто демонстрирует, что graceful shutdown и очистка работают должным образом.

Метод `take` определен в трейте `Iterator` и ограничивает итерацию максимум первыми двумя элементами. `ThreadPool` выйдет из области видимости в конце `main`, и реализация `drop` будет выполняться.

Запустите сервер с помощью `cargo run` и сделайте три запроса. Третий запрос должен завершиться с ошибкой, и в вашем терминале вы должны увидеть вывод, похожий на этот:

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

Вы, возможно, увидите другой порядок вывода идентификаторов `Worker` и сообщений. Мы можем увидеть, как этот код работает по сообщениям: экземпляры `Worker` 0 и 3 получили первые два запроса. Сервер прекратил принимать соединения после второго соединения, и реализация `Drop` для `ThreadPool` начинает выполняться, даже прежде чем `Worker` 3 начнет свою работу. Удаление `sender` отключает все экземпляры `Worker` и сообщает им выключиться. Каждый экземпляр `Worker` выводит сообщение при отключении, а затем пул потоков вызывает `join`, чтобы дождаться завершения каждого потока `Worker`.

Обратите внимание на один интересный аспект этого конкретного выполнения: `ThreadPool` удалил `sender`, и перед тем, как какой-либо `Worker` получил ошибку, мы пытались присоединиться к `Worker` 0. `Worker` 0 еще не получил ошибку от `recv`, поэтому главный поток заблокировался, ожидая завершения `Worker` 0. Между тем, `Worker` 3 получил задание, а затем все потоки получили ошибку. Когда `Worker` 0 завершился, главный поток ждал завершения остальных экземпляров `Worker`. В этот момент они все вышли из своих циклов и остановились.

Поздравляем! Теперь мы завершили наш проект; у нас есть базовый веб-сервер, который использует пул потоков для асинхронного ответа. Мы можем выполнить graceful shutdown сервера, который очищает все потоки в пуле. См. *https://www.nostarch.com/Rust2021*, чтобы скачать полный код этой главы для справки.

Мы могли бы сделать здесь еще больше! Если вы хотите продолжить улучшать этот проект, здесь есть некоторые идеи:

- Добавьте больше документации для `ThreadPool` и его публичных методов.
- Добавьте тесты функциональности библиотеки.
- Замените вызовы `unwrap` на более надежное обработку ошибок.
- Используйте `ThreadPool` для выполнения какой-либо задачи, кроме обслуживания веб-запросов.
- Найдите крейт для пула потоков на *https://crates.io* и реализуйте аналогичный веб-сервер с использованием этого крейта вместо нашего. Затем сравните его API и надежность с нашим пулом потоков.

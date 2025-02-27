# Реализация трейта Drop для ThreadPool

Начнем с реализации трейта `Drop` для нашего пула потоков. Когда пул удаляется, все наши потоки должны присоединиться, чтобы убедиться, что они завершат свою работу. Листинг 20-22 показывает первый вариант реализации `Drop`; этот код еще не будет работать должным образом.

Имя файла: `src/lib.rs`

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

Листинг 20-22: Присоединение каждого потока, когда пул потоков выходит из области видимости

Сначала мы перебираем каждый `worker` в пуле потоков \[1\]. Мы используем `&mut` для этого, потому что `self` - это изменяемая ссылка, и нам также нужно быть able изменять `worker`. Для каждого `worker` мы выводим сообщение о том, что этот конкретный экземпляр `Worker` завершает свою работу \[2\], а затем мы вызываем `join` для потока этого экземпляра `Worker` \[3\]. Если вызов `join` завершается неудачно, мы используем `unwrap`, чтобы заставить Rust вызвать панику и произвести неэлегантный выход.

Вот ошибка, которую мы получаем, когда компилируем этот код:

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

Ошибка говорит нам, что мы не можем вызвать `join`, потому что у нас есть только изменяемая ссылка на каждый `worker`, а `join` получает владение своим аргументом. Чтобы решить эту проблему, мы должны переместить поток из экземпляра `Worker`, который владеет `thread`, чтобы `join` мог потребовать поток. Мы сделали это в Листинге 17-15: если `Worker` хранит `Option<thread::JoinHandle<()>>` вместо этого, мы можем вызвать метод `take` для `Option`, чтобы переместить значение из варианта `Some` и оставить вариант `None` на его месте. Другими словами, работающий `Worker` будет иметь вариант `Some` в `thread`, а когда мы хотим очистить `Worker`, мы заменим `Some` на `None`, чтобы `Worker` не имел потока для выполнения.

Таким образом, мы знаем, что хотим обновить определение `Worker` следующим образом:

Имя файла: `src/lib.rs`

```rust
struct Worker {
    id: usize,
    thread: Option<thread::JoinHandle<()>>,
}
```

Теперь давайте полагаемся на компилятор, чтобы найти другие места, которые нужно изменить. Проверив этот код, мы получаем две ошибки:

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

Давайте решим вторую ошибку, которая указывает на код в конце `Worker::new`; мы должны обернуть значение `thread` в `Some`, когда создаем новый `Worker`. Примите следующие изменения, чтобы исправить эту ошибку:

Имя файла: `src/lib.rs`

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

Первая ошибка находится в нашей реализации `Drop`. Мы упоминали ранее, что планируем вызвать `take` для значения `Option`, чтобы переместить `thread` из `worker`. Следующие изменения это сделают:

Имя файла: `src/lib.rs`

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

Как обсуждалось в главе 17, метод `take` для `Option` извлекает вариант `Some` и оставляет `None` на его месте. Мы используем `if let`, чтобы разобрать вариант `Some` и получить поток \[1\]; затем мы вызываем `join` для потока \[2\]. Если у экземпляра `Worker` поток уже `None`, мы знаем, что `Worker` уже имел свой поток очищенным, поэтому ничего не происходит в этом случае.

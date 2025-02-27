# Каналы

Rust предоставляет асинхронные `каналы` для коммуникации между потоками. Каналы позволяют осуществлять однонаправленный поток информации между двумя точками доступа: `Sender` и `Receiver`.

```rust
use std::sync::mpsc::{Sender, Receiver};
use std::sync::mpsc;
use std::thread;

static NTHREADS: i32 = 3;

fn main() {
    // Каналы имеют две точки доступа: `Sender<T>` и `Receiver<T>`,
    // где `T` - это тип передаваемого сообщения
    // (аннотация типа избыточна)
    let (tx, rx): (Sender<i32>, Receiver<i32>) = mpsc::channel();
    let mut children = Vec::new();

    for id in 0..NTHREADS {
        // Точка доступа `Sender` может быть скопирована
        let thread_tx = tx.clone();

        // Каждый поток отправит свой идентификатор через канал
        let child = thread::spawn(move || {
            // Поток получает владение над `thread_tx`
            // Каждый поток помещает сообщение в очередь в канале
            thread_tx.send(id).unwrap();

            // Отправка - это неблокирующая операция, поток продолжит работу
            // сразу же после отправки сообщения
            println!("thread {} finished", id);
        });

        children.push(child);
    }

    // Здесь собираются все сообщения
    let mut ids = Vec::with_capacity(NTHREADS as usize);
    for _ in 0..NTHREADS {
        // Метод `recv` выбирает сообщение из канала
        // `recv` заблокирует текущий поток, если нет доступных сообщений
        ids.push(rx.recv());
    }

    // Ждем завершения потоков с выполнением оставшейся работы
    for child in children {
        child.join().expect("oops! the child thread panicked");
    }

    // Показываем порядок отправки сообщений
    println!("{:?}", ids);
}
```

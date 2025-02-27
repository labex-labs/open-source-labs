# Ожидание завершения всех потоков с использованием join-объектов

Код в листинге 16-1 не только преждевременно останавливает созданный поток в большинстве случаев из-за завершения главного потока, но и потому, что не гарантируется порядок выполнения потоков, мы также не можем гарантировать, что созданный поток вообще запустится!

Мы можем исправить проблему с тем, что созданный поток не запускается или преждевременно завершается, сохранив возвращаемое значение `thread::spawn` в переменную. Тип возврата `thread::spawn` - это `JoinHandle<T>`. `JoinHandle<T>` - это владение значением, которое, когда мы вызываем метод `join` для него, будет ожидать завершения своего потока. Листинг 16-2 показывает, как использовать `JoinHandle<T>` нашего потока, созданного в листинге 16-1, и вызвать `join`, чтобы убедиться, что созданный поток завершится, прежде чем `main` выйдет.

Имя файла: `src/main.rs`

```rust
use std::thread;
use std::time::Duration;

fn main() {
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {i} from the spawned thread!");
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("hi number {i} from the main thread!");
        thread::sleep(Duration::from_millis(1));
    }

    handle.join().unwrap();
}
```

Листинг 16-2: Сохранение `JoinHandle<T>` из `thread::spawn`, чтобы гарантировать, что поток будет выполнен до конца

Вызов `join` для объекта блокирует текущий выполняющийся поток до тех пор, пока поток, представленный объектом, не завершится. _Блокировка_ потока означает, что этот поток не может выполнять работу или выходить. Поскольку мы поместили вызов `join` после цикла `for` главного потока, запуск листинга 16-2 должен произвести вывод, похожий на этот:

    hi number 1 from the main thread!
    hi number 2 from the main thread!
    hi number 1 from the spawned thread!
    hi number 3 from the main thread!
    hi number 2 from the spawned thread!
    hi number 4 from the main thread!
    hi number 3 from the spawned thread!
    hi number 4 from the spawned thread!
    hi number 5 from the spawned thread!
    hi number 6 from the spawned thread!
    hi number 7 from the spawned thread!
    hi number 8 from the spawned thread!
    hi number 9 from the spawned thread!

Два потока продолжают чередоваться, но главный поток ждет из-за вызова `handle.join()` и не завершается, пока созданный поток не закончит работу.

Но давайте посмотрим, что произойдет, если мы переместить `handle.join()` перед циклом `for` в `main`, вот так:

Имя файла: `src/main.rs`

```rust
use std::thread;
use std::time::Duration;

fn main() {
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {i} from the spawned thread!");
            thread::sleep(Duration::from_millis(1));
        }
    });

    handle.join().unwrap();

    for i in 1..5 {
        println!("hi number {i} from the main thread!");
        thread::sleep(Duration::from_millis(1));
    }
}
```

Главный поток будет ждать завершения созданного потока и затем выполнять свой цикл `for`, поэтому вывод больше не будет чередоваться, как показано здесь:

    hi number 1 from the spawned thread!
    hi number 2 from the spawned thread!
    hi number 3 from the spawned thread!
    hi number 4 from the spawned thread!
    hi number 5 from the spawned thread!
    hi number 6 from the spawned thread!
    hi number 7 from the spawned thread!
    hi number 8 from the spawned thread!
    hi number 9 from the spawned thread!
    hi number 1 from the main thread!
    hi number 2 from the main thread!
    hi number 3 from the main thread!
    hi number 4 from the main thread!

Маленькие детали, такие как то, где вызывается `join`, могут повлиять на то, будут ли ваши потоки выполняться одновременно.

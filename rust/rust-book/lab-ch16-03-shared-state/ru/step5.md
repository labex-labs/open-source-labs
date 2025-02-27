# Множественная собственность с несколькими потоками

В главе 15 мы передали значение нескольким владельцам, создав счетчик ссылок с использованием умного указателя `Rc<T>`. Давайте поступим так же здесь и посмотрим, что произойдет. Мы обернем `Mutex<T>` в `Rc<T>` в Listing 16-14 и склонируем `Rc<T>`, прежде чем передать владение в поток.

Filename: `src/main.rs`

```rust
use std::rc::Rc;
use std::sync::Mutex;
use std::thread;

fn main() {
    let counter = Rc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Rc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();

            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Result: {}", *counter.lock().unwrap());
}
```

Listing 16-14: Попытка использовать `Rc<T>` для того, чтобы несколько потоков могли владеть `Mutex<T>`

Опять же, мы компилируем и получаем... разные ошибки! Компилятор учит нас много вещей.

```bash
error[E0277]: `Rc<Mutex<i32>>` cannot be sent between threads safely 1
   --> src/main.rs:11:22
    |
11  |           let handle = thread::spawn(move || {
    |  ______________________^^^^^^^^^^^^^_-
    | |                      |
    | |                      `Rc<Mutex<i32>>` cannot be sent between threads
safely
12  | |             let mut num = counter.lock().unwrap();
13  | |
14  | |             *num += 1;
15  | |         });
    | |_________- within this `[closure@src/main.rs:11:36: 15:10]`
    |
= help: within `[closure@src/main.rs:11:36: 15:10]`, the trait `Send` is not
implemented for `Rc<Mutex<i32>>` 2
    = note: required because it appears within the type
`[closure@src/main.rs:11:36: 15:10]`
note: required by a bound in `spawn`
```

Вау, это сообщение об ошибке очень длинное! Вот что важно заметить: ``Rc<Mutex<i32>>` cannot be sent between threads safely` [1]. Компилятор также объясняет причину: `the trait `Send` is not implemented for `Rc<Mutex<i32>>`` \[2\]. Мы поговорим о `Send` в следующем разделе: это один из трейтов, которые гарантируют, что типы, которые мы используем с потоками, предназначены для использования в конкурентных ситуациях.

К сожалению, `Rc<T>` не безопасен для обмена между потоками. Когда `Rc<T>` управляет счетчиком ссылок, он увеличивает счетчик для каждого вызова `clone` и уменьшает счетчик, когда каждый клон удаляется. Но он не использует никаких примитивов многопоточности, чтобы убедиться, что изменения счетчика не могут быть прерваны другим потоком. Это может привести к неправильным счетчикам - неочевидным ошибкам, которые, в свою очередь, могут привести к утечкам памяти или тому, что значение будет удалено, пока мы его не закончим использовать. Что нам нужно, это тип, точно такой же, как `Rc<T>`, но способный изменять счетчик ссылок в потокобезопасном режиме.

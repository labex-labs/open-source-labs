# Propriedade Múltipla com Múltiplas _Threads_

No Capítulo 15, demos um valor a múltiplos proprietários usando o _smart pointer_ `Rc<T>` para criar um valor com contagem de referência. Vamos fazer o mesmo aqui e ver o que acontece. Vamos encapsular o `Mutex<T>` em `Rc<T>` na Listagem 16-14 e clonar o `Rc<T>` antes de mover a propriedade para a _thread_.

Nome do arquivo: `src/main.rs`

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

Listagem 16-14: Tentando usar `Rc<T>` para permitir que múltiplas _threads_ possuam o `Mutex<T>`

Mais uma vez, compilamos e obtemos... erros diferentes! O compilador está nos ensinando muito.

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

Uau, essa mensagem de erro é muito longa! Aqui está a parte importante para focar: ``Rc<Mutex<i32>>` não pode ser enviado entre *threads* com segurança` \[1]. O compilador também está nos dizendo o motivo: `a trait `Send` não é implementada para `Rc<Mutex<i32>>`` \[2]. Falaremos sobre `Send` na próxima seção: é uma das _traits_ que garante que os tipos que usamos com _threads_ são destinados ao uso em situações concorrentes.

Infelizmente, `Rc<T>` não é seguro para compartilhar entre _threads_. Quando `Rc<T>` gerencia a contagem de referência, ele adiciona à contagem para cada chamada para `clone` e subtrai da contagem quando cada clone é descartado. Mas ele não usa nenhuma primitiva de concorrência para garantir que as alterações na contagem não possam ser interrompidas por outra _thread_. Isso pode levar a contagens erradas - _bugs_ sutis que podem, por sua vez, levar a vazamentos de memória ou a um valor sendo descartado antes de terminarmos de usá-lo. O que precisamos é de um tipo exatamente como `Rc<T>`, mas um que faça alterações na contagem de referência de forma _thread-safe_.

# Esperando Todas as Threads Terminarem Usando Join Handles

O código na Listagem 16-1 não apenas interrompe a thread gerada prematuramente na maioria das vezes devido ao término da thread principal, mas, como não há garantia sobre a ordem em que as threads são executadas, também não podemos garantir que a thread gerada será executada!

Podemos corrigir o problema da thread gerada não ser executada ou de terminar prematuramente salvando o valor de retorno de `thread::spawn` em uma variável. O tipo de retorno de `thread::spawn` é `JoinHandle<T>`. Um `JoinHandle<T>` é um valor próprio que, quando chamamos o método `join` nele, esperará que sua thread termine. A Listagem 16-2 mostra como usar o `JoinHandle<T>` da thread que criamos na Listagem 16-1 e chamar `join` para garantir que a thread gerada termine antes que `main` saia.

Nome do arquivo: `src/main.rs`

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

Listagem 16-2: Salvando um `JoinHandle<T>` de `thread::spawn` para garantir que a thread seja executada até a conclusão

Chamar `join` no handle bloqueia a thread atualmente em execução até que a thread representada pelo handle termine. _Bloquear_ (Blocking) uma thread significa que essa thread é impedida de realizar trabalho ou sair. Como colocamos a chamada para `join` após o loop `for` da thread principal, a execução da Listagem 16-2 deve produzir uma saída semelhante a esta:

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

As duas threads continuam alternando, mas a thread principal espera por causa da chamada para `handle.join()` e não termina até que a thread gerada seja finalizada.

Mas vamos ver o que acontece quando, em vez disso, movemos `handle.join()` antes do loop `for` em `main`, assim:

Nome do arquivo: `src/main.rs`

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

A thread principal esperará que a thread gerada termine e, em seguida, executará seu loop `for`, portanto, a saída não será mais intercalada, como mostrado aqui:

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

Pequenos detalhes, como onde `join` é chamado, podem afetar se suas threads são executadas ou não ao mesmo tempo.

# Canais

O Rust fornece canais assíncronos para comunicação entre threads. Canais permitem um fluxo unidirecional de informações entre dois pontos finais: o `Sender` e o `Receiver`.

```rust
use std::sync::mpsc::{Sender, Receiver};
use std::sync::mpsc;
use std::thread;

static NTHREADS: i32 = 3;

fn main() {
    // Canais possuem dois pontos finais: o `Sender<T>` e o `Receiver<T>`,
    // onde `T` é o tipo da mensagem a ser transferida
    // (a anotação de tipo é supérflua)
    let (tx, rx): (Sender<i32>, Receiver<i32>) = mpsc::channel();
    let mut children = Vec::new();

    for id in 0..NTHREADS {
        // O ponto final do remetente pode ser copiado
        let thread_tx = tx.clone();

        // Cada thread enviará seu ID através do canal
        let child = thread::spawn(move || {
            // A thread assume a propriedade de `thread_tx`
            // Cada thread coloca uma mensagem no canal
            thread_tx.send(id).unwrap();

            // O envio é uma operação não bloqueante, a thread continuará
            // imediatamente após enviar sua mensagem
            println!("thread {} finalizada", id);
        });

        children.push(child);
    }

    // Aqui, todas as mensagens são coletadas
    let mut ids = Vec::with_capacity(NTHREADS as usize);
    for _ in 0..NTHREADS {
        // O método `recv` pega uma mensagem do canal
        // `recv` bloqueará a thread atual se não houver mensagens disponíveis
        ids.push(rx.recv());
    }

    // Aguarde as threads completarem qualquer trabalho restante
    for child in children {
        child.join().expect("oops! a thread filha teve um erro");
    }

    // Mostra a ordem em que as mensagens foram enviadas
    println!("{:?}", ids);
}
```

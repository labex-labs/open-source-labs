# Canais e Transferência de Propriedade

As regras de propriedade desempenham um papel vital no envio de mensagens porque ajudam você a escrever código concorrente seguro. Prevenir erros em programação concorrente é a vantagem de pensar sobre a propriedade em todos os seus programas Rust. Vamos fazer um experimento para mostrar como os canais e a propriedade trabalham juntos para evitar problemas: tentaremos usar um valor `val` na thread gerada _depois_ de enviá-lo pelo canal. Tente compilar o código na Listagem 16-9 para ver por que este código não é permitido.

Nome do arquivo: `src/main.rs`

```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let val = String::from("hi");
        tx.send(val).unwrap();
        println!("val is {val}");
    });

    let received = rx.recv().unwrap();
    println!("Got: {received}");
}
```

Listagem 16-9: Tentando usar `val` depois de enviá-lo pelo canal

Aqui, tentamos imprimir `val` depois de enviá-lo pelo canal via `tx.send`. Permitir isso seria uma má ideia: uma vez que o valor foi enviado para outra thread, essa thread pode modificá-lo ou descartá-lo antes de tentarmos usar o valor novamente. Potencialmente, as modificações da outra thread podem causar erros ou resultados inesperados devido a dados inconsistentes ou inexistentes. No entanto, o Rust nos dá um erro se tentarmos compilar o código na Listagem 16-9:

```bash
error[E0382]: borrow of moved value: `val`
  --> src/main.rs:10:31
   |
8  |         let val = String::from("hi");
   |             --- move occurs because `val` has type `String`, which does
not implement the `Copy` trait
9  |         tx.send(val).unwrap();
   |                 --- value moved here
10 |         println!("val is {val}");
   |                           ^^^ value borrowed here after move
```

Nosso erro de concorrência causou um erro em tempo de compilação. A função `send` assume a propriedade de seu parâmetro, e quando o valor é movido, o receptor assume a propriedade dele. Isso nos impede de usar o valor novamente acidentalmente após enviá-lo; o sistema de propriedade verifica se tudo está correto.

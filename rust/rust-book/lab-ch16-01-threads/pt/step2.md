# Criando uma Nova Thread com `spawn`

Para criar uma nova thread, chamamos a função `thread::spawn` e passamos a ela um closure (falamos sobre closures no Capítulo 13) contendo o código que queremos executar na nova thread. O exemplo na Listagem 16-1 imprime algum texto de uma thread principal e outro texto de uma nova thread.

Nome do arquivo: `src/main.rs`

```rust
use std::thread;
use std::time::Duration;

fn main() {
    thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {i} from the spawned thread!");
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("hi number {i} from the main thread!");
        thread::sleep(Duration::from_millis(1));
    }
}
```

Listagem 16-1: Criando uma nova thread para imprimir uma coisa enquanto a thread principal imprime outra

Observe que quando a thread principal de um programa Rust é concluída, todas as threads geradas são encerradas, tenham ou não terminado a execução. A saída deste programa pode ser um pouco diferente a cada vez, mas será semelhante ao seguinte:

    hi number 1 from the main thread!
    hi number 1 from the spawned thread!
    hi number 2 from the main thread!
    hi number 2 from the spawned thread!
    hi number 3 from the main thread!
    hi number 3 from the spawned thread!
    hi number 4 from the main thread!
    hi number 4 from the spawned thread!
    hi number 5 from the spawned thread!

As chamadas para `thread::sleep` forçam uma thread a interromper sua execução por uma curta duração, permitindo que uma thread diferente seja executada. As threads provavelmente se revezarão, mas isso não é garantido: depende de como seu sistema operacional agenda as threads. Nesta execução, a thread principal imprimiu primeiro, embora a instrução de impressão da thread gerada apareça primeiro no código. E, embora tenhamos dito à thread gerada para imprimir até que `i` seja 9, ela só chegou a 5 antes que a thread principal fosse encerrada.

Se você executar este código e vir apenas a saída da thread principal, ou não vir nenhuma sobreposição, tente aumentar os números nos intervalos para criar mais oportunidades para o sistema operacional alternar entre as threads.

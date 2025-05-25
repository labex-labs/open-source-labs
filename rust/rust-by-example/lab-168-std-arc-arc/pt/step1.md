# Arc

Quando é necessária a propriedade compartilhada entre threads, `Arc` (Atomically Reference Counted) pode ser usado. Esta estrutura, por meio da implementação `Clone`, pode criar um ponteiro de referência para a localização de um valor na pilha de memória, ao mesmo tempo que incrementa o contador de referência. Como compartilha a propriedade entre threads, quando o último ponteiro de referência para um valor sai de escopo, a variável é descartada.

```rust
use std::time::Duration;
use std::sync::Arc;
use std::thread;

fn main() {
    // Esta declaração de variável é onde seu valor é especificado.
    let apple = Arc::new("a mesma maçã");

    for _ in 0..10 {
        // Aqui não há especificação de valor, pois é um ponteiro para uma
        // referência na pilha de memória.
        let apple = Arc::clone(&apple);

        thread::spawn(move || {
            // Como Arc foi usado, as threads podem ser criadas usando o valor alocado
            // na localização do ponteiro da variável Arc.
            println!("{:?}", apple);
        });
    }

    // Certifique-se de que todas as instâncias de Arc sejam impressas pelas threads criadas.
    thread::sleep(Duration::from_secs(1));
}
```

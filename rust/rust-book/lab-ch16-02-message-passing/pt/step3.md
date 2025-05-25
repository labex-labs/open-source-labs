# Enviando Vários Valores e Vendo o Receptor Esperando

O código na Listagem 16-8 compilou e executou, mas não nos mostrou claramente que duas threads separadas estavam conversando entre si pelo canal. Na Listagem 16-10, fizemos algumas modificações que provarão que o código na Listagem 16-8 está sendo executado concorrentemente: a thread gerada agora enviará várias mensagens e fará uma pausa de um segundo entre cada mensagem.

Nome do arquivo: `src/main.rs`

```rust
use std::sync::mpsc;
use std::thread;
use std::time::Duration;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let vals = vec![
            String::from("hi"),
            String::from("from"),
            String::from("the"),
            String::from("thread"),
        ];

        for val in vals {
            tx.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });

    for received in rx {
        println!("Got: {received}");
    }
}
```

Listagem 16-10: Enviando várias mensagens e pausando entre cada uma

Desta vez, a thread gerada tem um vetor de strings que queremos enviar para a thread principal. Iteramos sobre elas, enviando cada uma individualmente, e pausamos entre cada uma chamando a função `thread::sleep` com um valor `Duration` de um segundo.

Na thread principal, não estamos mais chamando a função `recv` explicitamente: em vez disso, estamos tratando `rx` como um iterador. Para cada valor recebido, estamos imprimindo-o. Quando o canal é fechado, a iteração terminará.

Ao executar o código na Listagem 16-10, você deve ver a seguinte saída com uma pausa de um segundo entre cada linha:

    Got: hi
    Got: from
    Got: the
    Got: thread

Como não temos nenhum código que pausa ou atrasa no loop `for` na thread principal, podemos dizer que a thread principal está esperando para receber valores da thread gerada.

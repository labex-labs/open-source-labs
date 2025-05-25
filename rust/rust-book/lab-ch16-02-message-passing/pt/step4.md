# Criando Múltiplos Produtores Clonando o Transmissor

Anteriormente, mencionamos que `mpsc` era um acrônimo para _múltiplos produtores, consumidor único_ (multiple producer, single consumer). Vamos colocar `mpsc` em uso e expandir o código na Listagem 16-10 para criar múltiplas threads que enviam valores para o mesmo receptor. Podemos fazer isso clonando o transmissor, como mostrado na Listagem 16-11.

Nome do arquivo: `src/main.rs`

```rust
--snip--

let (tx, rx) = mpsc::channel();

let tx1 = tx.clone();
thread::spawn(move || {
    let vals = vec![
        String::from("hi"),
        String::from("from"),
        String::from("the"),
        String::from("thread"),
    ];

    for val in vals {
        tx1.send(val).unwrap();
        thread::sleep(Duration::from_secs(1));
    }
});

thread::spawn(move || {
    let vals = vec![
        String::from("more"),
        String::from("messages"),
        String::from("for"),
        String::from("you"),
    ];

    for val in vals {
        tx.send(val).unwrap();
        thread::sleep(Duration::from_secs(1));
    }
});

for received in rx {
    println!("Got: {received}");
}

--snip--
```

Listagem 16-11: Enviando múltiplas mensagens de múltiplos produtores

Desta vez, antes de criarmos a primeira thread gerada, chamamos `clone` no transmissor. Isso nos dará um novo transmissor que podemos passar para a primeira thread gerada. Passamos o transmissor original para uma segunda thread gerada. Isso nos dá duas threads, cada uma enviando mensagens diferentes para o único receptor.

Quando você executa o código, sua saída deve ser semelhante a esta:

    Got: hi
    Got: more
    Got: from
    Got: messages
    Got: for
    Got: the
    Got: thread
    Got: you

Você pode ver os valores em outra ordem, dependendo do seu sistema. É isso que torna a concorrência interessante e difícil. Se você experimentar com `thread::sleep`, dando a ele vários valores nas diferentes threads, cada execução será mais não determinística e criará uma saída diferente a cada vez.

Agora que analisamos como os canais funcionam, vamos analisar um método diferente de concorrência.

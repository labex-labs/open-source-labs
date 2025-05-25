# Usando Passagem de Mensagens para Transferir Dados Entre Threads

Uma abordagem cada vez mais popular para garantir a concorrência segura é a _passagem de mensagens_, onde threads ou atores se comunicam enviando mensagens uns aos outros contendo dados. Aqui está a ideia em um slogan da documentação da linguagem Go em *https://golang.org/doc/effective_go.html#concurrency*: "Não se comunique compartilhando memória; em vez disso, compartilhe memória comunicando."

Para realizar a concorrência de envio de mensagens, a biblioteca padrão do Rust fornece uma implementação de _canais_. Um canal é um conceito geral de programação pelo qual os dados são enviados de uma thread para outra.

Você pode imaginar um canal em programação como um canal direcional de água, como um riacho ou um rio. Se você colocar algo como um patinho de borracha em um rio, ele viajará rio abaixo até o final do curso d'água.

Um canal tem duas metades: um transmissor e um receptor. A metade do transmissor é o local a montante onde você coloca o patinho de borracha no rio, e a metade do receptor é onde o patinho de borracha acaba a jusante. Uma parte do seu código chama métodos no transmissor com os dados que você deseja enviar, e outra parte verifica a extremidade receptora em busca de mensagens recebidas. Diz-se que um canal está _fechado_ se o transmissor ou o receptor for descartado.

Aqui, vamos desenvolver um programa que tem uma thread para gerar valores e enviá-los por um canal, e outra thread que receberá os valores e os imprimirá. Estaremos enviando valores simples entre threads usando um canal para ilustrar o recurso. Depois de se familiarizar com a técnica, você pode usar canais para quaisquer threads que precisem se comunicar entre si, como um sistema de bate-papo ou um sistema onde muitas threads executam partes de um cálculo e enviam as partes para uma thread que agrega os resultados.

Primeiro, na Listagem 16-6, criaremos um canal, mas não faremos nada com ele. Observe que isso ainda não compilará porque o Rust não consegue dizer que tipo de valores queremos enviar pelo canal.

Nome do arquivo: `src/main.rs`

```rust
use std::sync::mpsc;

fn main() {
    let (tx, rx) = mpsc::channel();
}
```

Listagem 16-6: Criando um canal e atribuindo as duas metades a `tx` e `rx`

Criamos um novo canal usando a função `mpsc::channel`; `mpsc` significa _múltiplos produtores, consumidor único_. Em suma, a maneira como a biblioteca padrão do Rust implementa canais significa que um canal pode ter vários pontos de _envio_ que produzem valores, mas apenas um ponto de _recebimento_ que consome esses valores. Imagine vários riachos fluindo juntos em um grande rio: tudo o que é enviado por qualquer um dos riachos acabará em um rio no final. Começaremos com um único produtor por enquanto, mas adicionaremos vários produtores quando fizermos este exemplo funcionar.

A função `mpsc::channel` retorna uma tupla, cujo primeiro elemento é a extremidade de envio---o transmissor---e o segundo elemento é a extremidade de recebimento---o receptor. As abreviações `tx` e `rx` são tradicionalmente usadas em muitos campos para _transmissor_ e _receptor_, respectivamente, então nomeamos nossas variáveis ​​como tal para indicar cada extremidade. Estamos usando uma instrução `let` com um padrão que desestrutura as tuplas; discutiremos o uso de padrões em instruções `let` e desestruturação no Capítulo 18. Por enquanto, saiba que usar uma instrução `let` dessa maneira é uma abordagem conveniente para extrair as partes da tupla retornada por `mpsc::channel`.

Vamos mover a extremidade de transmissão para uma thread gerada e fazer com que ela envie uma string para que a thread gerada esteja se comunicando com a thread principal, conforme mostrado na Listagem 16-7. Isso é como colocar um patinho de borracha no rio a montante ou enviar uma mensagem de bate-papo de uma thread para outra.

Nome do arquivo: `src/main.rs`

```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let val = String::from("hi");
        tx.send(val).unwrap();
    });
}
```

Listagem 16-7: Movendo `tx` para uma thread gerada e enviando `"hi"`

Novamente, estamos usando `thread::spawn` para criar uma nova thread e, em seguida, usando `move` para mover `tx` para o closure para que a thread gerada possua `tx`. A thread gerada precisa possuir o transmissor para poder enviar mensagens pelo canal.

O transmissor tem um método `send` que recebe o valor que queremos enviar. O método `send` retorna um tipo `Result<T, E>`, então, se o receptor já foi descartado e não há para onde enviar um valor, a operação de envio retornará um erro. Neste exemplo, estamos chamando `unwrap` para entrar em pânico em caso de erro. Mas em uma aplicação real, nós o trataríamos adequadamente: retorne ao Capítulo 9 para revisar as estratégias para o tratamento adequado de erros.

Na Listagem 16-8, obteremos o valor do receptor na thread principal. Isso é como recuperar o patinho de borracha da água no final do rio ou receber uma mensagem de bate-papo.

Nome do arquivo: `src/main.rs`

```rust
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let val = String::from("hi");
        tx.send(val).unwrap();
    });

    let received = rx.recv().unwrap();
    println!("Got: {received}");
}
```

Listagem 16-8: Recebendo o valor `"hi"` na thread principal e imprimindo-o

O receptor tem dois métodos úteis: `recv` e `try_recv`. Estamos usando `recv`, abreviação de _receive_ (receber), que bloqueará a execução da thread principal e esperará até que um valor seja enviado pelo canal. Depois que um valor é enviado, `recv` o retornará em um `Result<T, E>`. Quando o transmissor fecha, `recv` retornará um erro para sinalizar que nenhum valor adicional virá.

O método `try_recv` não bloqueia, mas retornará um `Result<T, E>` imediatamente: um valor `Ok` contendo uma mensagem, se uma estiver disponível, e um valor `Err` se não houver mensagens desta vez. Usar `try_recv` é útil se esta thread tiver outro trabalho a fazer enquanto espera por mensagens: poderíamos escrever um loop que chama `try_recv` de vez em quando, lida com uma mensagem, se uma estiver disponível, e, caso contrário, faz outro trabalho por um tempo até verificar novamente.

Usamos `recv` neste exemplo por simplicidade; não temos nenhum outro trabalho para a thread principal fazer além de esperar por mensagens, então bloquear a thread principal é apropriado.

Quando executamos o código na Listagem 16-8, veremos o valor impresso da thread principal:

```rust
Got: hi
```

Perfeito!

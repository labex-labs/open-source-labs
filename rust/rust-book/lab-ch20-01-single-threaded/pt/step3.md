# Lendo a Requisição

Vamos implementar a funcionalidade para ler a requisição do navegador! Para separar as preocupações de primeiro obter uma conexão e, em seguida, tomar alguma ação com a conexão, iniciaremos uma nova função para processar as conexões. Nesta nova função `handle_connection`, leremos dados do fluxo TCP e os imprimiremos para que possamos ver os dados sendo enviados do navegador. Altere o código para que se pareça com a Listagem 20-2.

Nome do arquivo: `src/main.rs`

```rust
1 use std::{
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
};

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();

      2 handle_connection(stream);
    }
}

fn handle_connection(mut stream: TcpStream) {
  3 let buf_reader = BufReader::new(&mut stream);
  4 let http_request: Vec<_> = buf_reader
      5 .lines()
      6 .map(|result| result.unwrap())
      7 .take_while(|line| !line.is_empty())
        .collect();

  8 println!("Request: {:#?}", http_request);
}
```

Listagem 20-2: Lendo do `TcpStream` e imprimindo os dados

Importamos `std::io::prelude` e `std::io::BufReader` para o escopo para ter acesso a traits e tipos que nos permitem ler e escrever no fluxo \[1]. No loop `for` na função `main`, em vez de imprimir uma mensagem que diz que fizemos uma conexão, agora chamamos a nova função `handle_connection` e passamos o `stream` para ela \[2].

Na função `handle_connection`, criamos uma nova instância de `BufReader` que envolve uma referência mutável ao `stream` \[3]. `BufReader` adiciona buffering gerenciando chamadas para os métodos da trait `std::io::Read` para nós.

Criamos uma variável chamada `http_request` para coletar as linhas da requisição que o navegador envia para nosso servidor. Indicamos que queremos coletar essas linhas em um vetor adicionando a anotação de tipo `Vec<_>` \[4].

`BufReader` implementa a trait `std::io::BufRead`, que fornece o método `lines` \[5]. O método `lines` retorna um iterador de `Result<String, std::io::Error>` dividindo o fluxo de dados sempre que vê um byte de nova linha. Para obter cada `String`, mapeamos e `unwrap` cada `Result` \[6]. O `Result` pode ser um erro se os dados não forem UTF-8 válidos ou se houver um problema ao ler do fluxo. Novamente, um programa de produção deve lidar com esses erros de forma mais elegante, mas estamos optando por interromper o programa no caso de erro para simplificar.

O navegador sinaliza o fim de uma requisição HTTP enviando dois caracteres de nova linha em sequência, então, para obter uma requisição do fluxo, pegamos linhas até obter uma linha que seja a string vazia \[7]. Depois de coletarmos as linhas no vetor, estamos imprimindo-as usando a formatação de depuração bonita \[8] para que possamos dar uma olhada nas instruções que o navegador web está enviando para nosso servidor.

Vamos tentar este código! Inicie o programa e faça uma requisição em um navegador web novamente. Observe que ainda obteremos uma página de erro no navegador, mas a saída do nosso programa no terminal agora se parecerá com isto:

```bash
$ cargo run
   Compiling hello v0.1.0 (file:///projects/hello)
    Finished dev [unoptimized + debuginfo] target(s) in 0.42s
     Running `target/debug/hello`
Request: [
    "GET / HTTP/1.1",
    "Host: 127.0.0.1:7878",
    "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0)
Gecko/20100101 Firefox/99.0",
    "Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*
;q=0.8",
    "Accept-Language: en-US,en;q=0.5",
    "Accept-Encoding: gzip, deflate, br",
    "DNT: 1",
    "Connection: keep-alive",
    "Upgrade-Insecure-Requests: 1",
    "Sec-Fetch-Dest: document",
    "Sec-Fetch-Mode: navigate",
    "Sec-Fetch-Site: none",
    "Sec-Fetch-User: ?1",
    "Cache-Control: max-age=0",
]
```

Dependendo do seu navegador, você pode obter uma saída ligeiramente diferente. Agora que estamos imprimindo os dados da requisição, podemos ver por que obtemos várias conexões de uma requisição do navegador, olhando para o caminho após `GET` na primeira linha da requisição. Se as conexões repetidas estiverem todas solicitando _/_ , sabemos que o navegador está tentando buscar _/_ repetidamente porque não está recebendo uma resposta do nosso programa.

Vamos analisar esses dados de requisição para entender o que o navegador está pedindo ao nosso programa.

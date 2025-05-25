# Validando a Requisição e Respondendo Seletivamente

No momento, nosso servidor web retornará o HTML no arquivo, independentemente do que o cliente solicitou. Vamos adicionar funcionalidade para verificar se o navegador está solicitando _/_ antes de retornar o arquivo HTML e retornar um erro se o navegador solicitar qualquer outra coisa. Para isso, precisamos modificar `handle_connection`, conforme mostrado na Listagem 20-6. Este novo código verifica o conteúdo da requisição recebida em relação ao que sabemos que uma requisição para _/_ se parece e adiciona blocos `if` e `else` para tratar as requisições de forma diferente.

Nome do arquivo: `src/main.rs`

```rust
--snip--

fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
  1 let request_line = buf_reader
        .lines()
        .next()
        .unwrap()
        .unwrap();

  2 if request_line == "GET / HTTP/1.1" {
        let status_line = "HTTP/1.1 200 OK";
        let contents = fs::read_to_string("hello.html").unwrap();
        let length = contents.len();

        let response = format!(
            "{status_line}\r\n\
             Content-Length: {length}\r\n\r\n\
             {contents}"
        );

        stream.write_all(response.as_bytes()).unwrap();
  3 } else {
        // some other request
    }
}
```

Listagem 20-6: Tratando requisições para _/_ de forma diferente de outras requisições

Vamos analisar apenas a primeira linha da requisição HTTP, então, em vez de ler toda a requisição em um vetor, estamos chamando `next` para obter o primeiro item do iterador \[1]. O primeiro `unwrap` cuida do `Option` e interrompe o programa se o iterador não tiver itens. O segundo `unwrap` lida com o `Result` e tem o mesmo efeito do `unwrap` que estava no `map` adicionado na Listagem 20-2.

Em seguida, verificamos a `request_line` para ver se ela é igual à linha de requisição de uma requisição GET para o caminho _/_ \[2]. Se for, o bloco `if` retorna o conteúdo do nosso arquivo HTML.

Se a `request_line` _não_ for igual à requisição GET para o caminho _/_, significa que recebemos alguma outra requisição. Adicionaremos código ao bloco `else` \[3] em um momento para responder a todas as outras requisições.

Execute este código agora e solicite _127.0.0.1:7878_; você deve obter o HTML em _hello.html_. Se você fizer qualquer outra requisição, como _127.0.0.1:7878/something-else_, você receberá um erro de conexão como aqueles que você viu ao executar o código na Listagem 20-1 e na Listagem 20-2.

Agora, vamos adicionar o código na Listagem 20-7 ao bloco `else` para retornar uma resposta com o código de status 404, que sinaliza que o conteúdo para a requisição não foi encontrado. Também retornaremos algum HTML para uma página renderizar no navegador, indicando a resposta ao usuário final.

Nome do arquivo: `src/main.rs`

```rust
--snip--
} else {
  1 let status_line = "HTTP/1.1 404 NOT FOUND";
  2 let contents = fs::read_to_string("404.html").unwrap();
    let length = contents.len();

    let response = format!(
        "{status_line}\r\n\
         Content-Length: {length}\r\n\r\n
         {contents}"
    );

    stream.write_all(response.as_bytes()).unwrap();
}
```

Listagem 20-7: Respondendo com o código de status 404 e uma página de erro se qualquer coisa diferente de _/_ for solicitada

Aqui, nossa resposta tem uma linha de status com o código de status 404 e a frase de motivo `NOT FOUND` \[1]. O corpo da resposta será o HTML no arquivo _404.html_ \[1]. Você precisará criar um arquivo _404.html_ ao lado de _hello.html_ para a página de erro; novamente, sinta-se à vontade para usar qualquer HTML que desejar ou use o HTML de exemplo na Listagem 20-8.

Nome do arquivo: `404.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Hello!</title>
  </head>
  <body>
    <h1>Oops!</h1>
    <p>Sorry, I don't know what you're asking for.</p>
  </body>
</html>
```

Listagem 20-8: Conteúdo de exemplo para a página a ser enviada com qualquer resposta 404

Com essas alterações, execute seu servidor novamente. Solicitar _127.0.0.1:7878_ deve retornar o conteúdo de _hello.html_, e qualquer outra requisição, como _127.0.0.1:7878/foo_, deve retornar o HTML de erro de _404.html_.

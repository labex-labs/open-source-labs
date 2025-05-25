# Retornando HTML Real

Vamos implementar a funcionalidade para retornar mais do que uma página em branco. Crie o novo arquivo _hello.html_ na raiz do diretório do seu projeto, não no diretório `src`. Você pode inserir qualquer HTML que desejar; a Listagem 20-4 mostra uma possibilidade.

Nome do arquivo: `hello.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Hello!</title>
  </head>
  <body>
    <h1>Hello!</h1>
    <p>Hi from Rust</p>
  </body>
</html>
```

Listagem 20-4: Um arquivo HTML de exemplo para retornar em uma resposta

Este é um documento HTML5 mínimo com um cabeçalho e algum texto. Para retornar isso do servidor quando uma requisição for recebida, modificaremos `handle_connection` conforme mostrado na Listagem 20-5 para ler o arquivo HTML, adicioná-lo à resposta como um corpo e enviá-lo.

Nome do arquivo: `src/main.rs`

```rust
use std::{
  1 fs,
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
};
--snip--

fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
    let http_request: Vec<_> = buf_reader
        .lines()
        .map(|result| result.unwrap())
        .take_while(|line| !line.is_empty())
        .collect();

    let status_line = "HTTP/1.1 200 OK";
    let contents = fs::read_to_string("hello.html").unwrap();
    let length = contents.len();

  2 let response = format!(
        "{status_line}\r\n\
         Content-Length: {length}\r\n\r\n\
         {contents}"
    );

    stream.write_all(response.as_bytes()).unwrap();
}
```

Listagem 20-5: Enviando o conteúdo de _hello.html_ como o corpo da resposta

Adicionamos `fs` à instrução `use` para trazer o módulo do sistema de arquivos da biblioteca padrão para o escopo \[1]. O código para ler o conteúdo de um arquivo para uma string deve parecer familiar; nós o usamos quando lemos o conteúdo de um arquivo para nosso projeto de E/S na Listagem 12-4.

Em seguida, usamos `format!` para adicionar o conteúdo do arquivo como o corpo da resposta de sucesso \[2]. Para garantir uma resposta HTTP válida, adicionamos o cabeçalho `Content-Length`, que é definido como o tamanho do corpo da nossa resposta, neste caso, o tamanho de `hello.html`.

Execute este código com `cargo run` e carregue _127.0.0.1:7878_ em seu navegador; você deve ver seu HTML renderizado!

Atualmente, estamos ignorando os dados da requisição em `http_request` e apenas enviando de volta o conteúdo do arquivo HTML incondicionalmente. Isso significa que, se você tentar solicitar _127.0.0.1:7878/something-else_ em seu navegador, ainda receberá a mesma resposta HTML. No momento, nosso servidor é muito limitado e não faz o que a maioria dos servidores web faz. Queremos personalizar nossas respostas dependendo da requisição e enviar de volta o arquivo HTML apenas para uma requisição bem formada para _/_.

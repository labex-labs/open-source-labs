# Escrevendo uma Resposta

Vamos implementar o envio de dados em resposta a uma requisição do cliente. As respostas têm o seguinte formato:

    HTTP-Version Status-Code Reason-Phrase CRLF
    headers CRLF
    message-body

A primeira linha é uma _linha de status_ que contém a versão HTTP usada na resposta, um código de status numérico que resume o resultado da requisição e uma frase de motivo que fornece uma descrição textual do código de status. Após a sequência CRLF, vêm quaisquer cabeçalhos (headers), outra sequência CRLF e o corpo da resposta.

Aqui está um exemplo de resposta que usa a versão HTTP 1.1 e tem um código de status 200, uma frase de motivo OK, sem cabeçalhos e sem corpo:

```rust
HTTP/1.1 200 OK\r\n\r\n
```

O código de status 200 é a resposta de sucesso padrão. O texto é uma pequena resposta HTTP bem-sucedida. Vamos escrever isso no fluxo como nossa resposta a uma requisição bem-sucedida! Da função `handle_connection`, remova o `println!` que estava imprimindo os dados da requisição e substitua-o pelo código na Listagem 20-3.

Nome do arquivo: `src/main.rs`

```rust
fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
    let http_request: Vec<_> = buf_reader
        .lines()
        .map(|result| result.unwrap())
        .take_while(|line| !line.is_empty())
        .collect();

  1 let response = "HTTP/1.1 200 OK\r\n\r\n";

  2 stream.write_all(response.3 as_bytes()).unwrap();
}
```

Listagem 20-3: Escrevendo uma pequena resposta HTTP bem-sucedida no fluxo

A primeira linha nova define a variável `response` que contém os dados da mensagem de sucesso \[1]. Em seguida, chamamos `as_bytes` em nossa `response` para converter os dados da string em bytes \[3]. O método `write_all` em `stream` recebe um `&[u8]` e envia esses bytes diretamente pela conexão \[2]. Como a operação `write_all` pode falhar, usamos `unwrap` em qualquer resultado de erro como antes. Novamente, em uma aplicação real, você adicionaria tratamento de erros aqui.

Com essas alterações, vamos executar nosso código e fazer uma requisição. Não estamos mais imprimindo nenhum dado no terminal, então não veremos nenhuma saída além da saída do Cargo. Quando você carregar _127.0.0.1:7878_ em um navegador web, você deverá obter uma página em branco em vez de um erro. Você acabou de codificar manualmente a recepção de uma requisição HTTP e o envio de uma resposta!

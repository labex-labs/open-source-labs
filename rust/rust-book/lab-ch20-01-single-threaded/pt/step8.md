# Um Toque de Refatoração

No momento, os blocos `if` e `else` têm muita repetição: ambos estão lendo arquivos e escrevendo o conteúdo dos arquivos no fluxo. As únicas diferenças são a linha de status e o nome do arquivo. Vamos tornar o código mais conciso, extraindo essas diferenças em linhas `if` e `else` separadas que atribuirão os valores da linha de status e do nome do arquivo a variáveis; então, podemos usar essas variáveis incondicionalmente no código para ler o arquivo e escrever a resposta. A Listagem 20-9 mostra o código resultante após substituir os grandes blocos `if` e `else`.

Nome do arquivo: `src/main.rs`

```rust
--snip--

fn handle_connection(mut stream: TcpStream) {
    --snip--

    let (status_line, filename) =
        if request_line == "GET / HTTP/1.1" {
            ("HTTP/1.1 200 OK", "hello.html")
        } else {
            ("HTTP/1.1 404 NOT FOUND", "404.html")
        };

    let contents = fs::read_to_string(filename).unwrap();
    let length = contents.len();

    let response = format!(
        "{status_line}\r\n\
         Content-Length: {length}\r\n\r\n\
         {contents}"
    );

    stream.write_all(response.as_bytes()).unwrap();
}
```

Listagem 20-9: Refatorando os blocos `if` e `else` para conter apenas o código que difere entre os dois casos

Agora, os blocos `if` e `else` retornam apenas os valores apropriados para a linha de status e o nome do arquivo em uma tupla; então, usamos a desestruturação para atribuir esses dois valores a `status_line` e `filename` usando um padrão na instrução `let`, conforme discutido no Capítulo 18.

O código duplicado anteriormente agora está fora dos blocos `if` e `else` e usa as variáveis `status_line` e `filename`. Isso torna mais fácil ver a diferença entre os dois casos e significa que temos apenas um lugar para atualizar o código se quisermos alterar como a leitura do arquivo e a escrita da resposta funcionam. O comportamento do código na Listagem 20-9 será o mesmo que o da Listagem 20-8.

Incrível! Agora temos um servidor web simples em aproximadamente 40 linhas de código Rust que responde a uma requisição com uma página de conteúdo e responde a todas as outras requisições com uma resposta 404.

Atualmente, nosso servidor é executado em um único _thread_, o que significa que ele só pode atender a uma requisição por vez. Vamos examinar como isso pode ser um problema simulando algumas requisições lentas. Então, vamos corrigi-lo para que nosso servidor possa lidar com várias requisições de uma vez.

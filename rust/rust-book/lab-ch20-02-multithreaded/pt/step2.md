# Simulando uma Requisição Lenta

Analisaremos como uma requisição de processamento lento pode afetar outras requisições feitas à nossa implementação atual do servidor. A Listagem 20-10 implementa o tratamento de uma requisição para _/sleep_ com uma resposta lenta simulada que fará com que o servidor durma por cinco segundos antes de responder.

Nome do arquivo: `src/main.rs`

```rust
use std::{
    fs,
    io::{prelude::*, BufReader},
    net::{TcpListener, TcpStream},
    thread,
    time::Duration,
};
--snip--

fn handle_connection(mut stream: TcpStream) {
    --snip--

    let (status_line, filename) = 1 match &request_line[..] {
      2 "GET / HTTP/1.1" => ("HTTP/1.1 200 OK", "hello.html"),
      3 "GET /sleep HTTP/1.1" => {
            thread::sleep(Duration::from_secs(5));
            ("HTTP/1.1 200 OK", "hello.html")
        }
      4 _ => ("HTTP/1.1 404 NOT FOUND", "404.html"),
    };

    --snip--
}
```

Listagem 20-10: Simulando uma requisição lenta dormindo por cinco segundos

Mudamos de `if` para `match` agora que temos três casos \[1]. Precisamos corresponder explicitamente a uma fatia de `request_line` para fazer a correspondência de padrão com os valores literais de string; `match` não faz referência e desreferenciação automáticas, como o método de igualdade faz.

O primeiro braço \[2] é o mesmo que o bloco `if` da Listagem 20-9. O segundo braço \[3] corresponde a uma requisição para _/sleep_. Quando essa requisição é recebida, o servidor dormirá por cinco segundos antes de renderizar a página HTML de sucesso. O terceiro braço \[4] é o mesmo que o bloco `else` da Listagem 20-9.

Você pode ver como nosso servidor é primitivo: bibliotecas reais lidariam com o reconhecimento de múltiplas requisições de uma forma muito menos verbosa!

Inicie o servidor usando `cargo run`. Em seguida, abra duas janelas do navegador: uma para *http://127.0.0.1:7878* e a outra para *http://127.0.0.1:7878/sleep*. Se você inserir o URI _/_ algumas vezes, como antes, verá que ele responde rapidamente. Mas se você inserir _/sleep_ e, em seguida, carregar _/_, verá que _/_ espera até que `sleep` tenha dormido por seus cinco segundos completos antes de carregar.

Existem múltiplas técnicas que poderíamos usar para evitar que as requisições fiquem presas atrás de uma requisição lenta; a que implementaremos é um pool de threads (thread pool).

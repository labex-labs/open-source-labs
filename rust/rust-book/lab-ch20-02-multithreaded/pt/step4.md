# Gerando uma Thread para Cada Requisição

Primeiramente, vamos explorar como nosso código pode parecer se ele criasse uma nova thread para cada conexão. Como mencionado anteriormente, este não é nosso plano final devido aos problemas com a potencial geração de um número ilimitado de threads, mas é um ponto de partida para obter um servidor multithreaded funcional primeiro. Então, adicionaremos o pool de threads como uma melhoria, e contrastar as duas soluções será mais fácil.

A Listagem 20-11 mostra as alterações a serem feitas em `main` para gerar uma nova thread para lidar com cada fluxo dentro do loop `for`.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();

        thread::spawn(|| {
            handle_connection(stream);
        });
    }
}
```

Listagem 20-11: Gerando uma nova thread para cada fluxo

Como você aprendeu no Capítulo 16, `thread::spawn` criará uma nova thread e, em seguida, executará o código no closure na nova thread. Se você executar este código e carregar _/sleep_ em seu navegador, e depois _/_ em mais duas abas do navegador, você realmente verá que as requisições para _/_ não precisam esperar _/sleep_ terminar. No entanto, como mencionamos, isso acabará sobrecarregando o sistema porque você estaria criando novas threads sem nenhum limite.

# Escrevendo e Executando um Programa Rust

Em seguida, crie um novo arquivo de código-fonte e chame-o de `main.rs`. Arquivos Rust sempre terminam com a extensão `.rs`. Se você estiver usando mais de uma palavra em seu nome de arquivo, a convenção é usar um sublinhado para separá-las. Por exemplo, use `hello_world.rs` em vez de `helloworld.rs`.

Agora, abra o arquivo `main.rs` que você acabou de criar e insira o código na Listagem 1-1.

Nome do arquivo: `main.rs`

```rust
fn main() {
    println!("Hello, world!");
}
```

Listagem 1-1: Um programa que imprime `Hello, world!`

Salve o arquivo e volte para a janela do seu terminal no diretório `~/project/hello_world`. No Linux ou macOS, insira os seguintes comandos para compilar e executar o arquivo:

```bash
$ rustc main.rs
$ ./main
Hello, world!
```

Independentemente do seu sistema operacional, a string `Hello, world!` deve ser impressa no terminal. Se você não vir essa saída, consulte "Solução de problemas" para obter ajuda.

Se `Hello, world!` foi impresso, parabéns! Você oficialmente escreveu um programa Rust. Isso faz de você um programador Rust - bem-vindo!

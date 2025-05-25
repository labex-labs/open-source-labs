# Imprimindo Erros na Saída de Erro Padrão

Usaremos o código na Listagem 12-24 para alterar como as mensagens de erro são impressas. Devido à refatoração que fizemos anteriormente neste capítulo, todo o código que imprime mensagens de erro está em uma função, `main`. A biblioteca padrão fornece a macro `eprintln!` que imprime no fluxo de erro padrão, então vamos alterar os dois lugares onde estávamos chamando `println!` para imprimir erros para usar `eprintln!` em vez disso.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::build(&args).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {err}");
        process::exit(1);
    });

    if let Err(e) = minigrep::run(config) {
        eprintln!("Application error: {e}");
        process::exit(1);
    }
}
```

Listagem 12-24: Escrevendo mensagens de erro na saída de erro padrão em vez da saída padrão usando `eprintln!`

Agora, vamos executar o programa novamente da mesma forma, sem nenhum argumento e redirecionando a saída padrão com `>`:

```bash
$ cargo run > output.txt
Problem parsing arguments: not enough arguments
```

Agora vemos o erro na tela e _output.txt_ não contém nada, que é o comportamento que esperamos dos programas de linha de comando.

Vamos executar o programa novamente com argumentos que não causam um erro, mas ainda redirecionam a saída padrão para um arquivo, assim:

```bash
cargo run -- to poem.txt > output.txt
```

Não veremos nenhuma saída no terminal, e _output.txt_ conterá nossos resultados:

Nome do arquivo: output.txt

```rust
Are you nobody, too?
How dreary to be somebody!
```

Isso demonstra que agora estamos usando a saída padrão para saída bem-sucedida e a saída de erro padrão para saída de erro, conforme apropriado.

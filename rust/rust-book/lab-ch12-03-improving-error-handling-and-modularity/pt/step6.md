# Corrigindo o Tratamento de Erros

Agora, vamos trabalhar na correção do nosso tratamento de erros. Lembre-se de que tentar acessar os valores no vetor `args` no índice 1 ou no índice 2 fará com que o programa entre em pânico se o vetor contiver menos de três itens. Tente executar o programa sem nenhum argumento; ele ficará assim:

```bash
$ cargo run
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep`
thread 'main' panicked at 'index out of bounds: the len is 1 but
the index is 1', src/main.rs:27:21
note: run with `RUST_BACKTRACE=1` environment variable to display
a backtrace
```

A linha `index out of bounds: the len is 1 but the index is 1` é uma mensagem de erro destinada a programadores. Ela não ajudará nossos usuários finais a entender o que eles devem fazer. Vamos corrigir isso agora.

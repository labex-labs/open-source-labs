# Melhorando a Mensagem de Erro

Na Listagem 12-8, adicionamos uma verificação na função `new` que verificará se a fatia (slice) é longa o suficiente antes de acessar o índice 1 e o índice 2. Se a fatia não for longa o suficiente, o programa entrará em pânico e exibirá uma mensagem de erro melhor.

Nome do arquivo: `src/main.rs`

```rust
--snip--
fn new(args: &[String]) -> Config {
    if args.len() < 3 {
        panic!("not enough arguments");
    }
    --snip--
```

Listagem 12-8: Adicionando uma verificação para o número de argumentos

Este código é semelhante à função `Guess::new` que escrevemos na Listagem 9-13, onde chamamos `panic!` quando o argumento `value` estava fora do intervalo de valores válidos. Em vez de verificar um intervalo de valores aqui, estamos verificando se o comprimento de `args` é pelo menos `3` e o restante da função pode operar sob a suposição de que essa condição foi atendida. Se `args` tiver menos de três itens, essa condição será `true`, e chamamos a macro `panic!` para encerrar o programa imediatamente.

Com essas poucas linhas extras de código em `new`, vamos executar o programa sem nenhum argumento novamente para ver como o erro se parece agora:

```bash
$ cargo run
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep`
thread 'main' panicked at 'not enough arguments',
src/main.rs:26:13
note: run with `RUST_BACKTRACE=1` environment variable to display
a backtrace
```

Esta saída é melhor: agora temos uma mensagem de erro razoável. No entanto, também temos informações extrínsecas que não queremos fornecer aos nossos usuários. Talvez a técnica que usamos na Listagem 9-13 não seja a melhor para usar aqui: uma chamada para `panic!` é mais apropriada para um problema de programação do que para um problema de uso, como discutido no Capítulo 9. Em vez disso, usaremos a outra técnica que você aprendeu no Capítulo 9 --- retornar um `Result` que indica sucesso ou um erro.

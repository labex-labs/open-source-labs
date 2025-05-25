# Usando a Função `search` na Função `run`

Agora que a função `search` está funcionando e testada, precisamos chamar `search` de nossa função `run`. Precisamos passar o valor `config.query` e o `contents` que `run` lê do arquivo para a função `search`. Então, `run` imprimirá cada linha retornada de `search`:

Nome do arquivo: `src/lib.rs`

```rust
pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)?;

    for line in search(&config.query, &contents) {
        println!("{line}");
    }

    Ok(())
}
```

Ainda estamos usando um loop `for` para retornar cada linha de `search` e imprimi-la.

Agora, todo o programa deve funcionar! Vamos experimentá-lo, primeiro com uma palavra que deve retornar exatamente uma linha do poema de Emily Dickinson: _frog_ (sapo).

```bash
$ cargo run -- frog poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.38s
     Running `target/debug/minigrep frog poem.txt`
How public, like a frog
```

Legal! Agora vamos tentar uma palavra que corresponderá a várias linhas, como _body_ (corpo):

```bash
$ cargo run -- body poem.txt
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep body poem.txt`
I'm nobody! Who are you?
Are you nobody, too?
How dreary to be somebody!
```

E, finalmente, vamos garantir que não obtenhamos nenhuma linha quando procurarmos uma palavra que não esteja em nenhum lugar no poema, como _monomorphization_ (monomorfização):

```bash
$ cargo run -- monomorphization poem.txt
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep monomorphization poem.txt`
```

Excelente! Construímos nossa própria mini versão de uma ferramenta clássica e aprendemos muito sobre como estruturar aplicações. Também aprendemos um pouco sobre entrada e saída de arquivos, _lifetimes_ (tempo de vida), testes e análise de linha de comando.

Para completar este projeto, demonstraremos brevemente como trabalhar com variáveis de ambiente e como imprimir no erro padrão, ambos úteis ao escrever programas de linha de comando.

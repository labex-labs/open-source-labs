# Extraindo a Lógica de main

Agora que terminamos de refatorar a análise da configuração, vamos nos voltar para a lógica do programa. Como afirmamos em "Separação de Preocupações para Projetos Binários", extrairemos uma função chamada `run` que conterá toda a lógica atualmente na função `main` que não está envolvida na configuração ou no tratamento de erros. Quando terminarmos, `main` será concisa e fácil de verificar por inspeção, e poderemos escrever testes para toda a outra lógica.

A Listagem 12-11 mostra a função `run` extraída. Por enquanto, estamos apenas fazendo a pequena e incremental melhoria de extrair a função. Ainda estamos definindo a função em `src/main.rs`.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    --snip--

    println!("Searching for {}", config.query);
    println!("In file {}", config.file_path);

    run(config);
}

fn run(config: Config) {
    let contents = fs::read_to_string(config.file_path)
        .expect("Should have been able to read the file");

    println!("With text:\n{contents}");
}

--snip--
```

Listagem 12-11: Extraindo uma função `run` contendo o restante da lógica do programa

A função `run` agora contém toda a lógica restante de `main`, começando pela leitura do arquivo. A função `run` recebe a instância `Config` como um argumento.

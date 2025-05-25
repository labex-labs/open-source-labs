# Tratando Erros Retornados de run em main

Verificaremos se há erros e os trataremos usando uma técnica semelhante à que usamos com `Config::build` na Listagem 12-10, mas com uma pequena diferença:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    --snip--

    println!("Searching for {}", config.query);
    println!("In file {}", config.file_path);

    if let Err(e) = run(config) {
        println!("Application error: {e}");
        process::exit(1);
    }
}
```

Usamos `if let` em vez de `unwrap_or_else` para verificar se `run` retorna um valor `Err` e para chamar `process::exit(1)` se o fizer. A função `run` não retorna um valor que queremos `unwrap` da mesma forma que `Config::build` retorna a instância `Config`. Como `run` retorna `()` no caso de sucesso, só nos preocupamos em detectar um erro, então não precisamos de `unwrap_or_else` para retornar o valor desembrulhado, que seria apenas `()`.

Os corpos das funções `if let` e `unwrap_or_else` são os mesmos em ambos os casos: imprimimos o erro e saímos.

# Extraindo o Analisador de Argumentos

Vamos extrair a funcionalidade para analisar argumentos em uma função que `main` chamará para se preparar para mover a lógica de análise da linha de comando para src/lib.rs*. A Listagem 12-5 mostra o novo início de `main` que chama uma nova função `parse_config`, que definiremos em *src/main.rs\* por enquanto.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let args: Vec<String> = env::args().collect();

    let (query, file_path) = parse_config(&args);

    --snip--
}

fn parse_config(args: &[String]) -> (&str, &str) {
    let query = &args[1];
    let file_path = &args[2];

    (query, file_path)
}
```

Listagem 12-5: Extraindo uma função `parse_config` de `main`

Ainda estamos coletando os argumentos da linha de comando em um vetor, mas em vez de atribuir o valor do argumento no índice 1 à variável `query` e o valor do argumento no índice 2 à variável `file_path` dentro da função `main`, passamos todo o vetor para a função `parse_config`. A função `parse_config` então contém a lógica que determina qual argumento vai em qual variável e passa os valores de volta para `main`. Ainda criamos as variáveis `query` e `file_path` em `main`, mas `main` não tem mais a responsabilidade de determinar como os argumentos da linha de comando e as variáveis correspondem.

Esta reformulação pode parecer exagerada para nosso pequeno programa, mas estamos refatorando em pequenas etapas incrementais. Depois de fazer essa alteração, execute o programa novamente para verificar se a análise de argumentos ainda funciona. É bom verificar seu progresso com frequência, para ajudar a identificar a causa dos problemas quando eles ocorrem.

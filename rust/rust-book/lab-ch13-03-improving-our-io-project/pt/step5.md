# Tornando o Código Mais Claro com Adaptadores de Iterador

Também podemos tirar proveito de iteradores na função `search` em nosso projeto I/O, que é reproduzida aqui na Listagem 13-21 como estava na Listagem 12-19.

Nome do arquivo: `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    let mut results = Vec::new();

    for line in contents.lines() {
        if line.contains(query) {
            results.push(line);
        }
    }

    results
}
```

Listagem 13-21: A implementação da função `search` da Listagem 12-19

Podemos escrever este código de uma forma mais concisa usando métodos de adaptador de iterador. Fazer isso também nos permite evitar ter um vetor `results` mutável intermediário. O estilo de programação funcional prefere minimizar a quantidade de estado mutável para tornar o código mais claro. Remover o estado mutável pode possibilitar uma aprimoramento futuro para fazer a busca acontecer em paralelo, porque não precisaríamos gerenciar o acesso concorrente ao vetor `results`. A Listagem 13-22 mostra essa alteração.

Nome do arquivo: `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    contents
        .lines()
        .filter(|line| line.contains(query))
        .collect()
}
```

Listagem 13-22: Usando métodos de adaptador de iterador na implementação da função `search`

Lembre-se de que o objetivo da função `search` é retornar todas as linhas em `contents` que contêm o `query`. Semelhante ao exemplo `filter` na Listagem 13-16, este código usa o adaptador `filter` para manter apenas as linhas para as quais `line.contains(query)` retorna `true`. Em seguida, coletamos as linhas correspondentes em outro vetor com `collect`. Muito mais simples! Sinta-se à vontade para fazer a mesma alteração para usar métodos de iterador na função `search_case_insensitive` também.

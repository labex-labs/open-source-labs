# Procurando Cada Linha pela Consulta

Em seguida, verificaremos se a linha atual contém nossa string de consulta. Felizmente, strings têm um método útil chamado `contains` que faz isso por nós! Adicione uma chamada ao método `contains` na função `search`, como mostrado na Listagem 12-18. Observe que isso ainda não compilará.

Nome do arquivo: `src/lib.rs`

```rust
pub fn search<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    for line in contents.lines() {
        if line.contains(query) {
            // do something with line
        }
    }
}
```

Listagem 12-18: Adicionando funcionalidade para ver se a linha contém a string em `query`

No momento, estamos construindo a funcionalidade. Para fazer o código compilar, precisamos retornar um valor do corpo, como indicamos que faríamos na assinatura da função.

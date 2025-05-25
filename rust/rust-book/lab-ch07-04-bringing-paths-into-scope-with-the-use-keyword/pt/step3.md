# Fornecendo Novos Nomes com a Palavra-chave `as`

Existe outra solução para o problema de trazer dois tipos com o mesmo nome para o mesmo escopo com `use`: após o caminho, podemos especificar `as` e um novo nome local, ou _alias_ (apelido), para o tipo. A Listagem 7-16 mostra outra maneira de escrever o código na Listagem 7-15, renomeando um dos dois tipos `Result` usando `as`.

Nome do arquivo: `src/lib.rs`

```rust
use std::fmt::Result;
use std::io::Result as IoResult;

fn function1() -> Result {
    --snip--
}

fn function2() -> IoResult<()> {
    --snip--
}
```

Listagem 7-16: Renomeando um tipo quando ele é trazido para o escopo com a palavra-chave `as`

Na segunda instrução `use`, escolhemos o novo nome `IoResult` para o tipo `std::io::Result`, que não entrará em conflito com o `Result` de `std::fmt` que também trouxemos para o escopo. A Listagem 7-15 e a Listagem 7-16 são consideradas idiomáticas, então a escolha é sua!

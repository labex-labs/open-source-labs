# Comentando Itens Contidos

O comentário de documentação `//!` adiciona documentação ao item que _contém_ os comentários, em vez de aos itens _seguindo_ os comentários. Normalmente, usamos esses comentários de documentação dentro do arquivo raiz da crate (`src/lib.rs` por convenção) ou dentro de um módulo para documentar a crate ou o módulo como um todo.

Por exemplo, para adicionar documentação que descreve o propósito da crate `my_crate` que contém a função `add_one`, adicionamos comentários de documentação que começam com `//!` ao início do arquivo `src/lib.rs`, conforme mostrado na Listagem 14-2.

Nome do arquivo: `src/lib.rs`

```rust
//! # My Crate
//!
//! `my_crate` is a collection of utilities to make performing
//! certain calculations more convenient.

/// Adds one to the number given.
--snip--
```

Listagem 14-2: Documentação para a crate `my_crate` como um todo

Observe que não há nenhum código após a última linha que começa com `//!`. Como iniciamos os comentários com `//!` em vez de `///`, estamos documentando o item que contém este comentário, em vez de um item que segue este comentário. Neste caso, esse item é o arquivo `src/lib.rs`, que é a raiz da crate. Esses comentários descrevem toda a crate.

Quando executamos `cargo doc --open`, esses comentários serão exibidos na página inicial da documentação para `my_crate` acima da lista de itens públicos na crate, conforme mostrado na Figura 14-2.

Figura 14-2: Documentação renderizada para `my_crate`, incluindo o comentário que descreve a crate como um todo

Comentários de documentação dentro de itens são úteis para descrever crates e módulos, especialmente. Use-os para explicar o propósito geral do contêiner para ajudar seus usuários a entender a organização da crate.

# Introdução

Neste laboratório, exploramos o uso do operador `?` em Rust, que permite a desestruturação fácil de valores `Option` sem a necessidade de instruções `match` aninhadas. O operador `?` pode ser usado para retornar rapidamente o valor subjacente se o `Option` for `Some`, ou terminar a função e retornar `None` se o `Option` for `None`. Este operador pode ser encadeado para tornar o código mais legível e conciso.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executá-lo com `rustc main.rs && ./main`.

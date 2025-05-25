# Introdução

Neste laboratório, temos uma implementação de uma lista encadeada usando `enums` em Rust. O `enum` `List` possui duas variantes: `Cons`, que representa um nó com um elemento e um ponteiro para o próximo nó, e `Nil`, que indica o fim da lista encadeada. O enum possui métodos como `new` para criar uma lista vazia, `prepend` para adicionar um elemento no início da lista, `len` para retornar o comprimento da lista e `stringify` para retornar uma representação em string da lista. A função principal fornecida demonstra o uso desses métodos para criar e manipular uma lista encadeada.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executar com `rustc main.rs && ./main`.

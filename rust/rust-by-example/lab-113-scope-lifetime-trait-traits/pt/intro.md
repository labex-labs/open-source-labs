# Introdução

Neste laboratório, exploramos a anotação de _lifetimes_ (tempo de vida) em métodos de _traits_ (traços), o que é semelhante às funções. Isso envolve a anotação de _lifetimes_ no bloco `impl` também. O código fornecido demonstra um exemplo onde uma _struct_ `Borrowed` possui uma anotação de _lifetime_, e o _trait_ `Default` é implementado para ela usando o _lifetime_ anotado. A função principal então cria uma instância de `Borrowed` usando o método `Default::default()`, demonstrando o uso de _lifetimes_ em métodos de _trait_.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executar com `rustc main.rs && ./main`.

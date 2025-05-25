# Introdução

Neste laboratório, a função `Iterator::any` é discutida. Esta função recebe um iterador como entrada e retorna `true` se algum elemento no iterador satisfazer um predicado dado, e `false` caso contrário. A função é definida como um método de trait na biblioteca padrão do Rust e pode ser usada em qualquer tipo que implemente o trait `Iterator`. A função recebe uma closure como argumento, que determina o predicado a ser aplicado a cada elemento no iterador. A closure é definida com o trait `FnMut`, significando que pode modificar variáveis capturadas, mas não consumi-las. A função `any` retorna um valor booleano indicando se o predicado é satisfeito por algum elemento no iterador.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executar com `rustc main.rs && ./main`.

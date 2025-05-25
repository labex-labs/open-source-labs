# Introdução

Neste laboratório, exploraremos arrays e slices em Rust. Um array é uma coleção de objetos do mesmo tipo armazenados em memória contígua, e seu comprimento é conhecido em tempo de compilação. Por outro lado, um slice é semelhante a um array, mas seu comprimento não é conhecido em tempo de compilação. Slices podem ser usados para emprestar (borrow) uma seção de um array. Também abordaremos como criar arrays, acessar elementos, calcular o comprimento, alocar memória, emprestar arrays como slices e trabalhar com slices vazios. Adicionalmente, discutiremos como acessar elementos de array com segurança usando o método `.get()` e lidar com erros de "out-of-bounds".

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executar com `rustc main.rs && ./main`.

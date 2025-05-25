# Introdução

Neste laboratório, aprendemos sobre o trait `Iterator` em Rust, que é usado para implementar iteradores sobre coleções como arrays. O trait `Iterator` requer que o método `next` seja definido para o iterador, e pode ser implementado manualmente em um bloco `impl` ou definido automaticamente para arrays e ranges. A construção `for` pode ser usada para convenientemente transformar algumas coleções em iteradores usando o método `.into_iter()`. O laboratório fornece um exemplo de implementação do gerador de sequência `Fibonacci` como um iterador, demonstrando como definir o método `next` e usar o trait `Iterator`. Adicionalmente, demonstra o uso dos métodos `take` e `skip` para manipular iteradores, bem como o método `iter` para iterar sobre arrays.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executar com `rustc main.rs && ./main`.

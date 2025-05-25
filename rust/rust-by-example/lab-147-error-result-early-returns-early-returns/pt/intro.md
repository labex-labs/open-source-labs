# Introdução

Neste laboratório, exploramos o conceito de _early returns_ (retornos antecipados) como uma forma de lidar com erros em Rust. O código de exemplo demonstra como podemos usar as instruções `match` e _early returns_ para tratar erros de forma elegante, tornando o código mais fácil de ler e escrever. Também discutimos as limitações do tratamento explícito de erros e introduzimos o uso do operador `?` para casos em que precisamos desembrulhar (unwrap) valores sem arriscar um _panic_.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executá-lo com `rustc main.rs && ./main`.

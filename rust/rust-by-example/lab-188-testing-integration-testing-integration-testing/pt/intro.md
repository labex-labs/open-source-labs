# Introdução

Neste laboratório, é discutido o teste de integração, que envolve testar múltiplas partes de uma biblioteca juntas usando sua interface pública. Os testes de integração podem ser colocados no diretório `tests` ao lado do diretório `src` em um projeto Rust, e são executados usando o comando `cargo test`. Além disso, código comum pode ser compartilhado entre testes de integração criando um módulo com funções públicas e importando-o dentro dos testes.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executá-lo com `rustc main.rs && ./main`.

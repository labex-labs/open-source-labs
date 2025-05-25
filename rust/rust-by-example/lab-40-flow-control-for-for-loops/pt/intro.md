# Introdução

Neste laboratório, aprendemos sobre o uso de loops `for` e ranges em Rust. Podemos usar o loop `for` juntamente com a notação de range `a..b` para iterar através de um intervalo de valores. Por exemplo, podemos escrever o programa FizzBuzz usando um loop `for` em vez de um loop `while`. Além disso, podemos usar a notação `..=` para um intervalo inclusivo em ambas as extremidades. O loop `for` também pode interagir com iteradores de diferentes maneiras, como usar `iter` para emprestar cada elemento de uma coleção, `into_iter` para consumir a coleção ou `iter_mut` para emprestar mutávelmente cada elemento da coleção. Cada um desses métodos fornece uma visão diferente dos dados dentro da coleção, permitindo que diferentes ações sejam executadas.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executá-lo com `rustc main.rs && ./main`.

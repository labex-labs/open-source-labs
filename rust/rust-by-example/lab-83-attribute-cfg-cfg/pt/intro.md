# Introdução

Neste laboratório, você aprenderá sobre o atributo `cfg` e a macro `cfg!` em Rust, que permitem verificações condicionais em configuração e avaliação, respectivamente. O atributo `cfg` permite compilação condicional, enquanto a macro `cfg!` avalia para verdadeiro ou falso em tempo de execução. Os blocos de código que utilizam `cfg!` devem ser válidos, independentemente do resultado da avaliação, ao contrário de `#[cfg]`, que pode remover código.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executar com `rustc main.rs && ./main`.

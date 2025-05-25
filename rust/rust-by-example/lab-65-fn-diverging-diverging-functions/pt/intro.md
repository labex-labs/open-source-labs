# Introdução

Neste laboratório, aprendemos sobre funções divergentes marcadas com `!` em Rust. Funções divergentes nunca retornam e seu tipo de retorno é um tipo vazio. Isso difere do tipo `()` que possui apenas um valor possível. Funções divergentes podem ser úteis quando é necessário fazer casting para qualquer outro tipo, como em ramos `match`. Elas também são o tipo de retorno de funções que loopam para sempre ou terminam o processo.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executar com `rustc main.rs && ./main`.

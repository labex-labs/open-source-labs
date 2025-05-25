# Introdução

Neste laboratório, aprendemos que, ao escrever funções em Rust que recebem um closure como parâmetro de entrada, o tipo completo do closure deve ser anotado usando um dos `traits`: `Fn`, `FnMut` ou `FnOnce`, que determinam como o closure utiliza o valor capturado, seja por referência, referência mutável ou valor. O compilador captura as variáveis da maneira menos restritiva possível com base no trait escolhido para o closure.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executar com `rustc main.rs && ./main`.

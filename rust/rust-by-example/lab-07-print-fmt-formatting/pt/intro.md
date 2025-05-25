# Introdução

Neste laboratório, aprendemos sobre formatação em Rust e como usar a macro `format!` para formatar variáveis. Vimos que a formatação é especificada usando uma _string_ de formatação, e diferentes tipos de argumentos podem ser usados para formatar a mesma variável de maneiras diferentes. A _trait_ de formatação mais comum é `Display`, que lida com casos em que o tipo de argumento não é especificado. Vimos um exemplo de implementação da _trait_ `Display` para uma _struct_ `City`, onde formatamos os valores de latitude e longitude. Também vimos um exemplo de uma _struct_ `Color` e fomos encarregados de implementar a _trait_ `Display` para ela, a fim de exibir os valores RGB e sua representação hexadecimal.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executá-lo com `rustc main.rs && ./main`.

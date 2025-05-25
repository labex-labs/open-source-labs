# Introdução

Neste laboratório, aprendemos sobre movimentos parciais dentro da desestruturação de uma única variável, onde tanto `by-move` quanto `by-reference` pattern bindings (ligações de padrão) podem ser usados simultaneamente. Isso resulta em um movimento parcial da variável, permitindo que algumas partes sejam movidas enquanto outras ainda podem ser referenciadas. Se uma variável pai for parcialmente movida, ela não poderá ser usada como um todo posteriormente, mas as partes que são apenas referenciadas e não movidas ainda podem ser usadas.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executá-lo com `rustc main.rs && ./main`.

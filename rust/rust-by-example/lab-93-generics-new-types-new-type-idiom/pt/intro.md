# Introdução

Neste laboratório, exploramos o idiom `newtype`, que fornece garantias em tempo de compilação, permitindo-nos criar um novo tipo distinto do seu tipo subjacente. Um exemplo é mostrado onde uma estrutura `Years` é usada para representar a idade em anos, e uma estrutura `Days` é usada para representar a idade em dias. Ao usar o idiom `newtype`, podemos garantir que o tipo de valor correto é fornecido a um programa, como na função de verificação de idade `old_enough`, que requer um valor do tipo `Years`. Além disso, aprendemos como obter o valor de um `newtype` como seu tipo subjacente usando sintaxe de tupla ou desestruturação.

> **Nota:** Se o laboratório não especificar um nome de ficheiro, pode usar qualquer nome de ficheiro que desejar. Por exemplo, pode usar `main.rs`, compilá-lo e executá-lo com `rustc main.rs && ./main`.

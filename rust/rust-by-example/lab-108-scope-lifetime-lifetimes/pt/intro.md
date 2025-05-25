# Introdução

Neste laboratório, exploraremos o conceito de lifetimes em Rust e como eles são usados pelo compilador para garantir a validade de empréstimos (borrows) no código. Lifetimes são uma construção do compilador que determinam a duração de uma variável, desde sua criação até sua destruição. Embora lifetimes e escopos estejam relacionados, eles não são a mesma coisa. Ao emprestar uma variável usando o operador `&`, o empréstimo tem um lifetime determinado por sua declaração, e é válido enquanto durar antes da destruição do emprestador. No entanto, o escopo do empréstimo é determinado por onde a referência é usada. O código de exemplo fornecido demonstra como lifetimes e escopos são usados na prática, com cada variável tendo seu próprio lifetime e escopo.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executar com `rustc main.rs && ./main`.

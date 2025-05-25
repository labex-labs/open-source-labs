# Introdução

Neste laboratório, exploramos o conceito de Linguagens de Domínio Específico (DSLs - Domain Specific Languages) em Rust, que são mini "linguagens" embutidas em macros Rust. Essas macros se expandem em construções Rust normais, mas oferecem uma sintaxe concisa e intuitiva para funcionalidades específicas. Um exemplo prático é demonstrado usando uma API de calculadora, onde uma expressão é fornecida à macro, e a saída é impressa no console. Isso permite a criação de interfaces mais complexas, como as encontradas em bibliotecas como `lazy_static` ou `clap`.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executá-lo com `rustc main.rs && ./main`.

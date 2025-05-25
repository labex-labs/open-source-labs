# Introdução

Neste laboratório, aprendemos sobre _bounds_ (limites) em Rust, que são usados para restringir os _lifetimes_ (tempos de vida) ou _traits_ (características) de tipos genéricos. O caractere `:` é usado para indicar que todas as referências em um tipo devem sobreviver a um determinado _lifetime_, enquanto `+` é usado para indicar que um tipo deve implementar uma _trait_ e todas as referências nele devem sobreviver a um determinado _lifetime_. Um trecho de código de exemplo demonstra a sintaxe e o uso de _bounds_ em Rust.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executá-lo com `rustc main.rs && ./main`.

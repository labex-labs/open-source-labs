# Introdução

Neste laboratório, aprendemos sobre _borrowing_ (empréstimo) em Rust, que permite acessar dados sem tomar posse (ownership) usando referências ('&T') em vez de passar objetos por valor ('T'). O _borrow checker_ (verificador de empréstimo) garante que as referências sempre apontem para objetos válidos e impede a destruição de objetos que estão sendo emprestados.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executá-lo com `rustc main.rs && ./main`.

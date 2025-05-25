# Introdução

Bem-vindo a **Ciclos de Referência Podem Vazar Memória**. Este laboratório faz parte do [Livro do Rust](https://doc.rust-lang.org/book/). Você pode praticar suas habilidades em Rust no LabEx.

Neste laboratório, exploramos como as garantias de segurança de memória do Rust tornam difícil, mas não impossível, criar acidentalmente vazamentos de memória, especificamente ao usar `Rc<T>` e `RefCell<T>`, que podem resultar em ciclos de referência que impedem que os valores sejam descartados e, portanto, vazem memória.

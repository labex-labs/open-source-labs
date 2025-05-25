# Introdução

Neste laboratório, pode utilizar `cargo doc` para construir a documentação em `target/doc`. Também pode utilizar `cargo test` para executar todos os testes, incluindo testes de documentação, e `cargo test --doc` para executar apenas os testes de documentação. Os comentários de documentação, denotados por `///`, são compilados em documentação pelo `rustdoc` e suportam Markdown. Estes comentários são úteis para documentar código em grandes projetos. Atributos de documentação, como `inline`, `no_inline` e `hidden`, são frequentemente utilizados com `rustdoc`. O `rustdoc` é amplamente utilizado pela comunidade para gerar documentação, incluindo a documentação da biblioteca padrão.

> **Nota:** Se o laboratório não especificar um nome de ficheiro, pode utilizar qualquer nome de ficheiro que desejar. Por exemplo, pode utilizar `main.rs`, compilá-lo e executá-lo com `rustc main.rs && ./main`.

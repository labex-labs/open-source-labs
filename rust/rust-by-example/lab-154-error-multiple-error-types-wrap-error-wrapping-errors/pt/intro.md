# Introdução

Neste laboratório, é demonstrada a abordagem alternativa de encapsular erros em um tipo de erro personalizado. O exemplo de código mostra como definir um alias de tipo `Result` que usa o enum `DoubleError` como a variante de erro, que encapsula o `ParseIntError` da biblioteca padrão. Ao implementar as traits `fmt::Display`, `error::Error` e `From`, o tipo de erro personalizado pode fornecer informações adicionais e lidar com erros subjacentes.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executá-lo com `rustc main.rs && ./main`.

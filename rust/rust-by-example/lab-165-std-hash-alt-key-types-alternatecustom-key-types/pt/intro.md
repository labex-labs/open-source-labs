# Introdução

Neste laboratório, exploramos o uso de tipos de chave alternativos/personalizados no `HashMap` do Rust, que podem incluir tipos que implementam os traits `Eq` e `Hash`, como `bool`, `int`, `uint`, `String` e `&str`. Além disso, podemos implementar esses traits para tipos personalizados usando o atributo `#[derive(PartialEq, Eq, Hash)]`, permitindo que eles sejam usados como chaves em um `HashMap`.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executar com `rustc main.rs && ./main`.

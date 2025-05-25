# Introdução

Neste laboratório, exploraremos o conceito de strings em Rust. Rust possui dois tipos de strings: `String` e `&str`.

Uma `String` é uma string alocada no heap (heap-allocated), expansível, que garante ser uma sequência UTF-8 válida. Por outro lado, `&str` é uma fatia (slice) que aponta para uma sequência UTF-8 válida e pode ser usada para visualizar uma `String`.

Em Rust, literais de string podem ser escritos de diferentes maneiras, incluindo o uso de escapes para representar caracteres especiais. Por exemplo, `\x3F` representa o caractere ponto de interrogação e `\u{211D}` representa um ponto de código Unicode. Literais de string raw (raw string literals) também podem ser usados se você quiser escrever uma string exatamente como está, sem escapes.

Se você precisar trabalhar com strings de bytes, Rust fornece literais de string de bytes usando o prefixo `b`. Strings de bytes podem ter escapes de bytes, mas não escapes Unicode. Strings de bytes raw (raw byte strings) também podem ser usadas de maneira semelhante aos literais de string raw.

É importante notar que `str` e `String` devem sempre ser sequências UTF-8 válidas. Se você precisar trabalhar com strings em diferentes codificações, pode usar crates externos como `encoding` para conversões entre codificações de caracteres.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executá-lo com `rustc main.rs && ./main`.

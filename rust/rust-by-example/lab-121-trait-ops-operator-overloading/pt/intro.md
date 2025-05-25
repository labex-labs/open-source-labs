# Introdução

Neste laboratório, exploramos a sobrecarga de operadores em Rust e como ela pode ser alcançada através de traits. Operadores em Rust podem ser sobrecarregados usando traits, o que lhes permite realizar diferentes tarefas com base em seus argumentos de entrada. O operador `+`, por exemplo, é açúcar sintático (syntactic sugar) para o método `add` e pode ser usado por qualquer implementador da trait `Add`. As traits que sobrecarregam operadores, incluindo `Add`, podem ser encontradas em `core::ops`. O código Rust fornecido demonstra como sobrecarregar o operador `+` para os tipos personalizados `Foo` e `Bar`, resultando em diferentes tipos de saída `FooBar` e `BarFoo`, respectivamente.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executá-lo com `rustc main.rs && ./main`.

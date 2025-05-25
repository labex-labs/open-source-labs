# Introdução

Neste laboratório, exploraremos o tipo `Result` em Rust, que oferece uma maneira de lidar com potenciais erros em vez da possível ausência de um valor, como o tipo `Option`. O tipo `Result` pode ter dois resultados - `Ok(T)` para um resultado bem-sucedido com o elemento `T`, e `Err(E)` para um erro com o elemento `E`. Veremos como usar `Result` em exemplos de código e como ele pode ser usado como o tipo de retorno da função `main` para lidar com erros e fornecer uma mensagem de erro mais específica.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executá-lo com `rustc main.rs && ./main`.

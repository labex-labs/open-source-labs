# Introdução

Neste laboratório, aprendemos sobre o `HashMap` em Rust, que é usado para armazenar valores por chave. As chaves do `HashMap` podem ser de vários tipos, incluindo booleanos, inteiros, strings ou qualquer outro tipo que implemente os traits `Eq` e `Hash`. Os `HashMaps` podem crescer e encolher dinamicamente com base no número de elementos. Podemos criar um `HashMap` com uma capacidade específica usando `HashMap::with_capacity(uint)` ou usar `HashMap::new()` para obter um `HashMap` com uma capacidade inicial padrão. O exemplo de código fornecido demonstra o uso do `HashMap` armazenando nomes de contato e números de telefone e realizando operações como inserção, recuperação, modificação e remoção.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executar com `rustc main.rs && ./main`.

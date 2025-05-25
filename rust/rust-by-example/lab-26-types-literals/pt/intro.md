# Introdução

Neste laboratório, aprendemos sobre literais em Rust e como especificar seus tipos adicionando um sufixo. Literais com sufixo têm seus tipos conhecidos na inicialização, enquanto os literais sem sufixo dependem de como são usados. A função `size_of_val` é usada para determinar o tamanho de uma variável em bytes, e é chamada com seu caminho completo, `std::mem::size_of_val`. A função `size_of_val` é definida no módulo `mem`, que por sua vez é definido no crate `std`.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executar com `rustc main.rs && ./main`.

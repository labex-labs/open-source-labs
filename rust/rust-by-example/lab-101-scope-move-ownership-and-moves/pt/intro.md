# Introdução

Neste laboratório, explica-se que, em Rust, as variáveis possuem a propriedade (ownership) dos recursos e só podem ter um proprietário, o que impede que os recursos sejam liberados múltiplas vezes. Quando as variáveis são atribuídas ou os argumentos de função são passados por valor, a propriedade dos recursos é transferida, o que é conhecido como uma "move" (movimentação). Após a "move", o proprietário anterior não pode mais ser usado para evitar a criação de ponteiros pendentes (dangling pointers). O exemplo de código demonstra esses conceitos, mostrando como a propriedade de variáveis alocadas na pilha (stack-allocated) e no heap (heap-allocated) é transferida e como o acesso a uma variável após sua propriedade ter sido movida leva a erros.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executar com `rustc main.rs && ./main`.

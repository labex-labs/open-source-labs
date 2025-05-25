# Introdução

Neste laboratório, somos introduzidos às assinaturas de funções com _lifetimes_ (tempo de vida) em Rust, onde qualquer referência deve ter um _lifetime_ anotado e qualquer referência que está sendo retornada deve ter o mesmo _lifetime_ de uma entrada ou ser `static`. É importante notar que retornar referências sem entrada é proibido se isso resultar em retornar referências a dados inválidos. Os exemplos fornecidos demonstram formas válidas de funções com _lifetimes_, incluindo funções com uma referência de entrada, funções com referências mutáveis, funções com múltiplos elementos e diferentes _lifetimes_, e funções que retornam referências que foram passadas como parâmetros.

> **Nota:** Se o laboratório não especificar um nome de arquivo, você pode usar qualquer nome de arquivo que desejar. Por exemplo, você pode usar `main.rs`, compilar e executá-lo com `rustc main.rs && ./main`.
